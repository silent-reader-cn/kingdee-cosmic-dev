#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
金蝶云苍穹 · 销售订单查询工具
==============================
只读工具：登录 → 取令牌 → 查询销售订单（t_sm_salorder）。

支持两种认证方式
----------------
1. `openapi`（推荐，也是官方唯一稳定的方式）
   走 OpenAPI 的第三方应用：POST /ierp/kapi/oauth2/getToken
   需要先在 【开放服务云】→【OpenAPI】→【第三方应用】 建一个应用，
   拿到 client_id（系统编码）与 client_secret（AccessToken 认证密钥）。

2. `web`（应急）
   走网页登录接口：POST /ierp/api/login.do，拿会话 Cookie 直接调接口。
   ⚠️ 只有当目标 API 的「第三方应用授权」开关**关闭**时才可用；
   开关打开时服务端会返回 403「该接口需要第三方应用授权」。
   本工具的 --probe 会把这个开关状态探出来。

用法
----
  # 0) 探路：不需要任何凭据，先看环境能不能通、有哪些账套、接口要不要第三方应用
  python examples/salorder_query.py --base-url http://<host>:<port> --probe

  # 1) 列账套（不需要凭据）
  python examples/salorder_query.py --base-url ... --list-datacenters

  # 2) OpenAPI 方式查询
  python examples/salorder_query.py --base-url ... \
      --client-id <系统编码> --client-secret <密钥> \
      --account-id <数据中心ID> --username admin \
      --limit 20 --filter "fbillno like '%SO%'"

  # 3) 网页会话方式查询（接口未开第三方应用授权时可用）
  python examples/salorder_query.py --base-url ... --auth web \
      --username admin --password <密码> --account-id <数据中心ID>

凭据请用环境变量或本地配置文件，不要写进命令行历史
------------------------------------------------
  export KD_BASE_URL=http://host:port
  export KD_CLIENT_ID=...  KD_CLIENT_SECRET=...  KD_ACCOUNT_ID=...
  export KD_USERNAME=...   KD_PASSWORD=...

  # 或写到本地配置文件（已在 .gitignore 中）
  python examples/salorder_query.py --save-config kd.json
"""
import argparse
import getpass
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

SALORDER_FORM_ID = "sm_salorder"      # 销售订单业务对象编码
SALORDER_APP_ID = "sm"                # 所属应用编码
DEFAULT_QUERY_API = "query"           # 标准查询操作API的编码

# 查询接口默认返回上百个字段，直接打表没法看。
# 这里挑一小组「一眼能判断单据状态」的列作为默认视图；用 --fields 可覆盖。
DEFAULT_VIEW_FIELDS = [
    ("billno", "单据编号"),
    ("billstatus", "单据状态"),
    ("orderstatus", "订单状态"),
    ("bizdate", "业务日期"),
    ("customer_name", "客户"),
    ("totalamount", "金额"),
    ("auditdate", "审核日期"),
    ("createtime", "创建时间"),
    ("modifier_name", "修改人"),
]

TOKEN_PATH = "/ierp/kapi/oauth2/getToken"
QUERY_PATH = "/ierp/kapi/v2/{app}/{form}/{service}"
WEB_LOGIN_PATH = "/ierp/api/login.do"
DATACENTER_PATH = "/ierp/auth/getAllDatacenters.do"


class KingdeeError(RuntimeError):
    pass


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

class Client:
    def __init__(self, base_url, timeout=30, insecure=False):
        self.base = base_url.rstrip("/")
        self.timeout = timeout
        self.cookies = {}
        self.access_token = None
        ctx = None
        if self.base.startswith("https") and insecure:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        self._ctx = ctx

    def request(self, path, body=None, method="POST", headers=None,
                form=False, raw=False):
        url = self.base + path
        hdrs = {"User-Agent": "kingdee-cosmic-dev/salorder-query"}
        data = None
        if body is not None:
            if form:
                data = urllib.parse.urlencode(body).encode()
                hdrs["Content-Type"] = "application/x-www-form-urlencoded;charset=utf-8"
            else:
                data = json.dumps(body, ensure_ascii=False).encode("utf-8")
                hdrs["Content-Type"] = "application/json;charset=UTF-8"
        if self.cookies:
            hdrs["Cookie"] = "; ".join("%s=%s" % kv for kv in self.cookies.items())
        if headers:
            hdrs.update(headers)

        req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as resp:
                payload = resp.read().decode("utf-8", "replace")
                for k, v in resp.headers.items():
                    if k.lower() == "set-cookie":
                        ck = v.split(";", 1)[0]
                        if "=" in ck:
                            name, val = ck.split("=", 1)
                            self.cookies[name.strip()] = val.strip()
        except urllib.error.HTTPError as e:
            payload = e.read().decode("utf-8", "replace")
            raise KingdeeError("HTTP %s %s\n%s" % (e.code, url, payload[:600]))
        except Exception as e:  # noqa: BLE001
            raise KingdeeError("请求失败 %s：%s" % (url, e))

        if raw:
            return payload
        try:
            return json.loads(payload)
        except ValueError:
            return {"_raw": payload}


# --------------------------------------------------------------------------
# 认证
# --------------------------------------------------------------------------

def list_datacenters(client):
    """列出环境里的账套（数据中心）。这个接口不需要登录。"""
    return client.request(DATACENTER_PATH, {}, form=True)


def login_web(client, username, password, account_id=None):
    """网页登录，拿会话 Cookie。

    实测契约（本工具已在本机环境验证）：
        POST /ierp/api/login.do
        {"user": "<用户名>", "password": "<密码>"}     ← 键名是 user，不是 username
    返回 data.access_token（形如 <accountId>_<...>）与 KERPSESSIONID，
    两者都作为 Cookie 回传即可访问内部接口。
    """
    body = {"user": username, "password": password}
    if account_id:
        body["accountId"] = account_id
    r = client.request(WEB_LOGIN_PATH, body)
    d = r.get("data") or {}
    if not d.get("success"):
        desc = str(d.get("error_desc") or r)
        hint = ""
        if "云通行证" in desc:
            # 这个报错有歧义，直接给出排查方向，别让人误判成密码错
            hint = ("\n  ⚠️ 这个报错有三种可能：①密码错 ②登录被限流（前面试太多次）"
                    "③环境连不上金蝶云通行证。\n"
                    "     先手工在网页上登一次确认账号正常，再回来跑；"
                    "不要连续重试。")
        raise KingdeeError("网页登录失败：%s%s" % (desc, hint))
    token = d.get("access_token") or ""
    if not token:
        raise KingdeeError("登录返回成功但没有 access_token：%s" % json.dumps(r, ensure_ascii=False)[:300])
    client.cookies["KERPSESSIONID"] = token
    client.cookies["access_token"] = token
    return token


def explain_token_error(resp):
    """把 getToken 的各种报错翻译成「下一步该干什么」。

    这些报错的字面意思都不难懂，但**排查方向**不直观，尤其是：
      - 「密钥验证失败」其实意味着 client_id 已经通过了；
      - 「代理用户为空」是应用配置问题，不是凭据问题。
    实测逐个确认过，见 examples/README.md。
    """
    msg = str(resp.get("message") or "")
    if "在系统中不存在或未启用" in msg:
        return ("client_id 无效",
                "该第三方应用不存在或未启用。注意第三方应用是**按数据中心隔离**的："
                "同一个 client_id 换一个 accountId 就会报「不存在」，先确认账套对不对。")
    if "代理用户为空或userName不在代理用户中" in msg:
        return ("代理用户未配置（凭据本身是对的！）",
                "该应用开启了「启用代理用户控制」，但传的 username 不在它的代理用户列表里。"
                "处理：【开放服务云】→【OpenAPI】→【安全策略】→【第三方应用】→ 该应用，"
                "把 username 加进「代理用户」，或关掉「启用代理用户控制」。")
    if "用户无效或不可用" in msg:
        return ("username 无效", "该用户名在系统中不存在；换一个有效用户。"
                                "（注意这条和上一条不同：上一条说明用户有效但没被授权）")
    if "username为空" in msg:
        return ("缺少 username", "getToken 必须传 username（第三方应用代理用户）")
    if "密钥验证失败" in msg:
        return ("client_secret 不对（但 client_id 已经通过了）",
                "看到这条就说明 client_id 是对的。去应用详情核对/重置 AccessToken 认证密钥。"
                "⚠️ 连续 5 次失败会锁定 180 秒，不要靠猜。")
    if "锁定" in msg or "已连续5次" in msg:
        return ("已被锁定", "密钥连续失败 5 次，等 180 秒再试")
    if "nonce" in msg and "调用过" in msg:
        return ("nonce 重复", "每次请求都要用新的随机 nonce")
    if "client_id为空" in msg:
        return ("缺少 client_id", "需要第三方应用的系统编码（appId）")
    return ("未知错误", msg[:160])


def get_openapi_token(client, client_id, client_secret, username, account_id,
                      language="zh_CN"):
    """OpenAPI 第三方应用取 access_token（有效期默认 2 小时）。

    参数名来自官方《增强型Token认证》：
        client_id / client_secret / username / accountId / nonce / timestamp
    """
    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "accountId": account_id,
        "language": language,
        "nonce": uuid.uuid4().hex[:16],     # 必须每次不同，否则会被判重放
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    r = client.request(TOKEN_PATH, body)
    data = r.get("data")
    if isinstance(data, dict) and data.get("access_token"):
        client.access_token = data["access_token"]
        return data["access_token"]
    if r.get("access_token"):
        client.access_token = r["access_token"]
        return client.access_token
    what, todo = explain_token_error(r)
    raise KingdeeError("取 access_token 失败 —— %s\n  怎么办：%s" % (what, todo))


# --------------------------------------------------------------------------
# 查询
# --------------------------------------------------------------------------

def query_salorder(client, app=SALORDER_APP_ID, form=SALORDER_FORM_ID,
                   service=DEFAULT_QUERY_API, body=None, use_token=True):
    """调用销售订单查询操作API。"""
    path = QUERY_PATH.format(app=app, form=form, service=service)
    headers = {}
    if use_token and client.access_token:
        headers["access_token"] = client.access_token
    return client.request(path, body or {"data": {}, "pageNo": 1, "pageSize": 20},
                          headers=headers)


def query_all_pages(client, base_body, app, form, service, max_rows=5000, verbose=True):
    """翻页取全量。

    响应里有 `lastPage`，据此判断是否还有下一页。
    """
    rows = []
    page = 1
    while len(rows) < max_rows:
        body = dict(base_body)
        body["pageNo"] = page
        resp = query_salorder(client, app, form, service, body)
        if not resp.get("status", True) and resp.get("errorCode") not in (None, "", "0"):
            raise KingdeeError("第 %d 页查询失败：%s" % (page, resp.get("message")))
        d = resp.get("data") or {}
        got = d.get("rows") or []
        rows.extend(got)
        if verbose:
            print("  第 %d 页：%d 条%s" % (page, len(got), "（末页）" if d.get("lastPage") else ""))
        if d.get("lastPage") or not got:
            break
        page += 1
    return rows[:max_rows]


def sort_rows(rows, spec):
    """客户端排序。

    为什么要自己做：实测发现该查询接口**静默忽略** orderBy 参数
    （试了 12 种写法，全部返回 code=0 但顺序不变），
    排序由 API 配置决定，运行时改不了。所以要在本地排。
    """
    if not spec or not rows:
        return rows
    parts = spec.split(",")
    # 依次按每个键排序（从最后一个键往前，保证稳定性）
    for part in reversed(parts):
        part = part.strip()
        desc = False
        for sep in (":", " "):
            if sep in part:
                f, _, d = part.partition(sep)
                desc = d.strip().lower() in ("desc", "descending", "-1")
                part = f.strip()
                break
        key = part

        def sort_key(r, _k=key):
            v = r.get(_k)
            if v is None:
                return (1, "")
            if isinstance(v, (int, float)):
                return (0, v)
            s = str(v)
            # 数字型字符串按数值排，否则按文本
            try:
                return (0, float(s))
            except ValueError:
                return (0, s)

        rows = sorted(rows, key=sort_key, reverse=desc)
    return rows


def build_query_body(args):
    """构造查询请求体。

    实测契约 —— 请求体分**内外两层**：

        {
          "data": { … },        ← 内层：业务入参，由每个 API 的配置决定
          "pageNo": 1,          ← 外层：通用分页/过滤参数
          "pageSize": 20,
          "filter": "...", "orderBy": "...", "selectFields": "..."
        }

    - `data` 键**必须存在**（销售订单查询传空对象即可）；
      少了它报 `400 请求参数没有 data 数据`
    - `pageNo`/`pageSize` 必须在**顶层**，塞进 `data` 里会被忽略，
      报 `400 页大小pageSize不能为空`
    - **业务必填参数要放进 `data`**：例如采购订单的查询强制要求 `billno`，
      且必须放在 `data` 里（放外层报 `603 参数【billno】必填`）。
      用 `--param billno=XXX` 传。
    - ⚠️ 同名操作在不同对象上必填参数不同 —— 操作API 是按业务对象逐个配置的。
    """
    if args.body:
        text = args.body
        if text.startswith("@"):
            text = open(text[1:], encoding="utf-8").read()
        return json.loads(text)

    data = {}
    for kv in (args.param or []):
        if "=" not in kv:
            raise KingdeeError("--param 需要 k=v 形式，收到：%s" % kv)
        k, v = kv.split("=", 1)
        data[k.strip()] = v
    if args.data_json:
        data.update(json.loads(args.data_json))

    body = {"data": data, "pageNo": args.page, "pageSize": args.limit}
    if args.filter:
        body["filter"] = args.filter
    if args.order_by:
        body["orderBy"] = args.order_by
    if args.fields:
        body["selectFields"] = args.fields
    return body


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------

def rows_of(resp):
    """从响应里尽量捞出数据行（不同版本出参结构不同）。"""
    d = resp.get("data")
    if isinstance(d, list):
        return d
    if isinstance(d, dict):
        for key in ("rows", "list", "records", "data", "items", "result"):
            v = d.get(key)
            if isinstance(v, list):
                return v
        # 单条
        if d:
            return [d]
    return []


def export_rows(rows, path):
    """导出结果。按扩展名决定格式：.json 原样，其余按 .csv 处理。

    CSV 用 utf-8-sig（带 BOM），否则 Excel 打开中文会乱码。
    """
    if not rows:
        return 0
    if path.lower().endswith(".json"):
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(rows, f, ensure_ascii=False, indent=1)
        return len(rows)

    import csv
    fields = list(rows[0].keys())
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            row = {}
            for k, v in r.items():
                if isinstance(v, (list, dict)):
                    v = json.dumps(v, ensure_ascii=False)
                row[k] = v
            w.writerow(row)
    return len(rows)


def print_table(rows, fields=None, max_col=34, headers=None):
    if not rows:
        print("（无数据）")
        return
    if not fields:
        fields = list(rows[0].keys())
    titles = [headers.get(f, f) if headers else f for f in fields]

    def cell(v):
        if isinstance(v, (list, dict)):
            v = json.dumps(v, ensure_ascii=False)
        s = "" if v is None else str(v)
        return s if len(s) <= max_col else s[:max_col - 1] + "…"

    widths = [min(max(len(t), *(len(cell(r.get(f, ""))) for r in rows)), max_col)
              for t, f in zip(titles, fields)]
    print("  ".join(t.ljust(w) for t, w in zip(titles, widths)))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print("  ".join(cell(r.get(f, "")).ljust(w) for f, w in zip(fields, widths)))


def pick_view_fields(rows, requested=None):
    """决定展示哪些列。显式指定就用指定的；否则挑默认视图里存在的列。"""
    if requested:
        return requested, None
    if not rows:
        return None, None
    keys = set(rows[0].keys())
    picked = [f for f, _ in DEFAULT_VIEW_FIELDS if f in keys]
    if len(picked) >= 3:
        return picked, dict(DEFAULT_VIEW_FIELDS)
    # 字段名对不上（别的环境/别的对象）就退回「前 10 列」
    return list(rows[0].keys())[:10], None


# --------------------------------------------------------------------------
# 探路
# --------------------------------------------------------------------------

def probe(client, cfg, app, form, service):
    """不需要凭据也能跑；带了凭据就顺带把认证链路和接口授权要求探清楚。"""
    print("=" * 66)
    print("环境探路：%s" % client.base)
    print("=" * 66)

    def step(name, fn):
        try:
            v = fn()
            print("  ✓ %-30s %s" % (name, v if isinstance(v, str) else ""))
            return v
        except Exception as e:  # noqa: BLE001
            print("  ✗ %-30s %s" % (name, str(e).split("\n")[0][:90]))
            return None

    step("网页登录接口可达", lambda: client.request(
        WEB_LOGIN_PATH, {"user": "__probe__", "password": "__probe__"})
        and "接口存在（返回 JSON）")

    dcs = list_datacenters(client)
    print("  ✓ %-30s %d 个账套" % ("列账套", len(dcs)))
    for d in dcs:
        print("      accountId=%-22s number=%-14s %s"
              % (d.get("accountId"), d.get("accountNumber"), d.get("accountName")))

    r0 = client.request(TOKEN_PATH, {})
    print("  ✓ %-30s errorCode=%s %s"
          % ("OpenAPI 取令牌接口", r0.get("errorCode"),
             str(r0.get("message") or "")[:50]))

    path = QUERY_PATH.format(app=app, form=form, service=service)
    print("\n  ── 销售订单查询接口 %s ──" % path)
    r = client.request(path, {})
    code = str(r.get("errorCode"))
    print("     未认证访问 → errorCode=%s  %s" % (code, str(r.get("message") or "")[:60]))
    if code == "404":
        print("     ✗ 路径不存在：appId / formId / serviceName 组合不对")
    elif code in ("401", "403"):
        print("     · 接口存在，但需要认证")

    # 带凭据时，进一步判断「是否允许 cookie 认证」
    if cfg.get("auth") == "web" and cfg.get("username") and cfg.get("password"):
        try:
            login_web(client, cfg["username"], cfg["password"], cfg.get("account_id"))
            print("\n     网页登录成功，用会话再试一次查询接口：")
            r2 = client.request(path, {})
            c2 = str(r2.get("errorCode"))
            print("     errorCode=%s  %s" % (c2, str(r2.get("message") or "")[:60]))
            if c2 == "403":
                print("     → 该接口的「第三方应用授权」开关是**打开**的，")
                print("       cookie 认证被拒；必须改用 OpenAPI 的 client_id/client_secret。")
            elif c2 in ("200", "0") or r2.get("status"):
                print("     → cookie 认证可用，可以 --auth web 直接查询。")
        except Exception as e:  # noqa: BLE001
            print("\n     网页登录失败：%s" % str(e).split("\n")[0][:120])
    else:
        print("\n     （带上 --auth web --username --password 可继续判断能否用 cookie 认证）")
    print()


# --------------------------------------------------------------------------
# 配置
# --------------------------------------------------------------------------

CONFIG_KEYS = ["base_url", "auth", "client_id", "client_secret", "username",
               "password", "account_id", "app", "form", "service"]


def load_config(args):
    cfg = {}
    if args.config and os.path.exists(args.config):
        cfg = json.load(open(args.config, encoding="utf-8"))
    for k in CONFIG_KEYS:
        env = os.environ.get("KD_" + k.upper())
        if env:
            cfg[k] = env
    for k in CONFIG_KEYS:
        v = getattr(args, k, None)
        if v:
            cfg[k] = v
    return cfg


def main(argv):
    ap = argparse.ArgumentParser(add_help=True,
                                 description="金蝶云苍穹 销售订单查询工具（只读）")
    ap.add_argument("--base-url", help="形如 http://host:port")
    ap.add_argument("--config", default="kd.json", help="本地配置文件（默认 kd.json）")
    ap.add_argument("--auth", choices=["openapi", "web"], help="认证方式")
    ap.add_argument("--client-id", help="第三方应用系统编码（appId）")
    ap.add_argument("--client-secret", help="第三方应用 AccessToken 认证密钥")
    ap.add_argument("--username")
    ap.add_argument("--password")
    ap.add_argument("--account-id", help="数据中心ID（账套），可用 --list-datacenters 查")
    ap.add_argument("--app", default=SALORDER_APP_ID)
    ap.add_argument("--form", default=SALORDER_FORM_ID)
    ap.add_argument("--service", default=DEFAULT_QUERY_API)
    ap.add_argument("--page", type=int, default=1)
    ap.add_argument("--limit", type=int, default=20, help="每页条数")
    ap.add_argument("--filter", help="过滤条件，如 \"fbillno like '%%SO%%'\"")
    ap.add_argument("--param", action="append", metavar="K=V",
                    help="业务入参，放进请求体的 data 里（可重复）。"
                         "例：采购订单查询必须 --param billno=XXX")
    ap.add_argument("--data-json", help="直接给定 data 对象的 JSON（与 --param 合并）")
    ap.add_argument("--order-by", help="传给接口的 orderBy —— ⚠️ 实测多数环境会**静默忽略**，"
                                       "要排序请用 --sort")
    ap.add_argument("--sort", help="客户端排序，如 totalamount:desc,billno:asc（服务端不认排序，只能本地排）")
    ap.add_argument("--all", action="store_true", help="翻页取全量（配合 --limit 作为每页大小）")
    ap.add_argument("--export", metavar="FILE", help="把结果导出为文件（.csv 或 .json）")
    ap.add_argument("--fields", help="只取这些字段，逗号分隔")
    ap.add_argument("--body", help="直接给定查询请求体（JSON 字符串或 @文件）")
    ap.add_argument("--session-token", help="已有网页会话令牌时直接复用（形如 <accountId>_<...>）")
    ap.add_argument("--json", action="store_true", help="原样输出 JSON")
    ap.add_argument("--probe", action="store_true", help="只探路，不查询")
    ap.add_argument("--list-datacenters", action="store_true", help="列出账套后退出")
    ap.add_argument("--save-config", metavar="PATH", help="把当前参数存成本地配置文件")
    ap.add_argument("--insecure", action="store_true", help="https 时跳过证书校验")
    args = ap.parse_args(argv)

    cfg = load_config(args)

    if args.save_config:
        json.dump({k: cfg[k] for k in CONFIG_KEYS if k in cfg},
                  open(args.save_config, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("已写入 %s —— 里面有凭据，注意别提交到仓库（.gitignore 已包含 kd.json）"
              % args.save_config)
        return 0

    if not cfg.get("base_url"):
        print("!! 缺少 --base-url（或环境变量 KD_BASE_URL）")
        return 2
    client = Client(cfg["base_url"], insecure=args.insecure)

    if args.probe:
        probe(client, cfg, cfg.get("app", SALORDER_APP_ID),
              cfg.get("form", SALORDER_FORM_ID), cfg.get("service", DEFAULT_QUERY_API))
        return 0

    if args.list_datacenters:
        for d in list_datacenters(client):
            print("accountId=%-22s number=%-14s default=%-5s %s"
                  % (d.get("accountId"), d.get("accountNumber"),
                     d.get("default"), d.get("accountName")))
        return 0

    auth = cfg.get("auth") or "openapi"
    if args.session_token:
        client.cookies["KERPSESSIONID"] = args.session_token
        client.cookies["access_token"] = args.session_token
        client.access_token = args.session_token
        print("已复用现有网页会话令牌")
    elif auth == "web":
        if not cfg.get("username"):
            print("!! web 认证需要 --username")
            return 2
        pwd = cfg.get("password") or getpass.getpass("密码：")
        login_web(client, cfg["username"], pwd, cfg.get("account_id"))
        print("网页登录成功（会话已建立）")
    else:
        missing = [k for k in ("client_id", "client_secret", "username", "account_id")
                   if not cfg.get(k)]
        if missing:
            print("!! OpenAPI 认证缺少：%s" % ", ".join("--" + m.replace("_", "-") for m in missing))
            print("   第三方应用在【开放服务云】→【OpenAPI】→【第三方应用】里创建。")
            return 2
        get_openapi_token(client, cfg["client_id"], cfg["client_secret"],
                          cfg["username"], cfg["account_id"])
        print("已获取 access_token（有效期默认 2 小时）")

    body = build_query_body(args)
    app = cfg.get("app", SALORDER_APP_ID)
    form = cfg.get("form", SALORDER_FORM_ID)
    service = cfg.get("service", DEFAULT_QUERY_API)

    if args.all:
        print("翻页取全量（每页 %d 条）..." % args.limit)
        rows = query_all_pages(client, body, app, form, service,
                               max_rows=max(args.limit * 100, 1000))
        resp = {"status": True, "data": {"rows": rows}}
    else:
        resp = query_salorder(client, app, form, service, body)

    if args.json and not args.export:
        print(json.dumps(resp, ensure_ascii=False, indent=2))
        return 0

    if not resp.get("status", True) or resp.get("errorCode") not in (None, "", "0"):
        print("查询失败：errorCode=%s\n%s"
              % (resp.get("errorCode"), resp.get("message")))
        return 1

    rows = rows_of(resp)
    if args.sort:
        rows = sort_rows(rows, args.sort)

    if args.export:
        n = export_rows(rows, args.export)
        print("已导出 %d 条到 %s" % (n, args.export))
        if args.json:
            return 0

    print("共返回 %d 条（请求体：%s）\n"
          % (len(rows), json.dumps(body, ensure_ascii=False)))
    requested = args.fields.split(",") if args.fields else None
    fields, headers = pick_view_fields(rows, requested)
    if not requested and rows and len(rows[0]) > len(fields or []):
        print("（共 %d 个字段，默认只展示 %d 个关键列；加 --fields 可指定，--json 看全部）\n"
              % (len(rows[0]), len(fields)))
    print_table(rows, fields, headers=headers)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
