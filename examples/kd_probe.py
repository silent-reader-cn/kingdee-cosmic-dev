#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kd_probe —— 金蝶云苍穹「探路 + 查配置」统一 CLI
=================================================
把「要对接某个业务对象时，怎么最快摸清它的 API」这一整套动作收进一个入口。

解决的问题
----------
苍穹的 OpenAPI 路径是 `/ierp/kapi/v2/{appId}/{formId}/{serviceName}`：

  * `appId` 不能从 `formId` 前缀猜（客户是 `bd_customer` / `basedata`，不是 `bd`）；
  * `serviceName` 到底是 `query` / `batchQuery` / `batchSave` / 大小写？只能猜；
  * 猜错和「未发布」的表现一模一样 —— 都是 404。

于是有了两条互补的路子：

  ┌─ HTTP 探路 ─────────────────────────────────────────────┐
  │ 把候选路径挨个 POST，用错误码反推：                          │
  │   403 = 路径存在（只是认证方式不合规）                        │
  │   404 = 路径不存在（appId/formId/serviceName 组合错）        │
  │ ⚠️ 前提：必须已认证。未认证时一律 401，存在与否返回一致，        │
  │    据此判断会把不存在的路径误判成「存在」。                     │
  └────────────────────────────────────────────────────────┘

  ┌─ 配置表直读（更快、更准，推荐先跑）──────────────────────────┐
  │ 直连 ERP 库读三张表，直接给出答案，不用猜：                    │
  │   t_open_apiservice   服务清单（服务名/业务对象/启用/是否需第三方授权）│
  │   t_open_apibodyentry 入参模板（参数名/类型/是否必填/层级）      │
  │   t_open_apirespentry 返回结构                              │
  └────────────────────────────────────────────────────────┘

用法
----
  PY=python
  # —— 先摸清「这个对象发布了哪些服务、每个服务要传什么」（读配置表，最推荐）——
  $PY examples/kd_probe.py services                    # 列出全部已发布服务
  $PY examples/kd_probe.py services sm_salorder        # 某对象的服务
  $PY examples/kd_probe.py body sm_salorder query      # 某服务的入参模板 + 返回结构
  $PY examples/kd_probe.py search 发货                 # 按中文名/表名模糊找对象

  # —— HTTP 侧（需要 --base-url；凭据可选）——
  $PY examples/kd_probe.py accounts                    # 列账套（匿名接口，不需要凭据）
  $PY examples/kd_probe.py token                       # 只验认证：能否取到 access_token
  $PY examples/kd_probe.py paths                       # 探测一批常见路径（内置默认清单）
  $PY examples/kd_probe.py paths /ierp/kapi/v2/sm/sm_salorder/query,/ierp/kapi/v2/sm/sm_salorder/list
  $PY examples/kd_probe.py ref                         # 从真实单据里取参考数据（组织/单据类型/物料…）
  $PY examples/kd_probe.py doc sm_salorder query --filter "billno like 'SO%'"
  $PY examples/kd_probe.py doc sm_salorder query --billno SO-20250303-0296

配置
----
沿用本 skill 其它示例的约定（kd.json + KD_* 环境变量），另加数据库相关变量：

  export KD_BASE_URL=http://host:port
  export KD_CLIENT_ID=...  KD_CLIENT_SECRET=...  KD_ACCOUNT_ID=...  KD_USERNAME=admin

  # services / body / search 子命令需要（直连 ERP 库）
  export KD_DB_HOST=...  KD_DB_PORT=5432  KD_DB_NAME=...  KD_DB_USER=...  KD_DB_PASSWORD=...

数据库连接为什么不用 psycopg2：本机 PyPI 不可达，装不了第三方包。
改用 `psql -c` 子进程执行 SQL —— 纯标准库，且金蝶环境通常自带 PostgreSQL 客户端。
Windows 上 `psql` 往往不在 PATH 里（本机实测装在 `C:\\Program Files\\PostgreSQL\\<版本>\\bin`），
所以脚本会自动去常见安装目录找，也可以用 `--psql <路径>` 显式指定。
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from salorder_query import (  # noqa: E402
    Client, KingdeeError, list_datacenters, login_web, get_openapi_token,
    query_salorder, rows_of, print_table, TOKEN_PATH, QUERY_PATH,
    SALORDER_APP_ID, SALORDER_FORM_ID, DEFAULT_QUERY_API,
)

# 探测默认清单：覆盖销售订单的常见服务名（save? batchSave? batchAdd? 大小写？）
DEFAULT_PATHS = [
    "/ierp/kapi/v2/sm/sm_salorder/query",
    "/ierp/kapi/v2/sm/sm_salorder/batchQuery",
    "/ierp/kapi/v2/sm/sm_salorder/save",
    "/ierp/kapi/v2/sm/sm_salorder/batchSave",
    "/ierp/kapi/v2/sm/sm_salorder/batchAdd",
    "/ierp/kapi/v2/sm/sm_salorder/batchSubmit",
    "/ierp/kapi/v2/sm/sm_salorder/batchAudit",
    "/ierp/kapi/v2/sm/sm_delivernotice/query",
    "/ierp/kapi/v2/sm/sm_delivernotice/batchQuery",
    "/ierp/kapi/v2/im/im_saloutbill/query",
    "/ierp/kapi/v2/im/im_saloutbill/batchsave",
]

# 参考数据样本：从真实单据里把「能用的枚举值」捞出来，省得去猜
REF_KEYS = ["org_number", "billtype_number", "biztype_number",
            "settlecurrency_number", "paymode", "status"]

LEVEL_LABEL = {1: "单据级", 2: "分录级", 3: "子分录级"}

DB_KEYS = ["db_host", "db_port", "db_name", "db_user", "db_password"]


# ==========================================================================
# psql 通道
# ==========================================================================

def find_psql(explicit=None):
    """定位 psql 可执行文件。

    不直接依赖 PATH —— 实测 Windows 上 PostgreSQL 装好后 `psql` 往往不在 PATH 里
    （本机 `which psql` 找不到，实际在 C:\\Program Files\\PostgreSQL\\18\\bin）。
    所以按「显式指定 → PATH → 常见安装目录」的顺序找。
    """
    if explicit:
        return explicit if os.path.exists(explicit) else None
    found = shutil.which("psql")
    if found:
        return found
    patterns = [
        r"C:\Program Files\PostgreSQL\*\bin\psql.exe",
        r"C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe",
        "/usr/lib/postgresql/*/bin/psql",
        "/opt/homebrew/opt/postgresql*/bin/psql",
        "/usr/local/opt/postgresql*/bin/psql",
        "/Applications/Postgres.app/Contents/Versions/*/bin/psql",
    ]
    candidates = []
    for p in patterns:
        candidates.extend(glob.glob(p))
    # 版本号大的优先（PostgreSQL\18 优于 PostgreSQL\9.6）
    def ver(path):
        part = path.replace("\\", "/").split("/")
        for seg in part[1:]:
            if seg and seg[0].isdigit():
                try:
                    return tuple(int(x) for x in seg.split(".")[:2])
                except ValueError:
                    return (0, 0)
        return (0, 0)
    candidates.sort(key=ver, reverse=True)
    return candidates[0] if candidates else None


def psql_query(sql, cfg, psql_bin=None, timeout=60):
    """执行一条 SQL，返回字典列表。

    用 `--csv` 让 psql 直接吐 CSV —— 比解析 psql 的表格对齐输出可靠得多
    （表格输出里 '-' 分隔线、折行、列宽都会干扰解析）。
    参数用 `-v key=value` 传并写成 :'key'，让 psql 自己做字面量转义，
    避免手工拼 SQL 带来的注入与转义问题。
    """
    exe = find_psql(psql_bin)
    if not exe:
        raise KingdeeError(
            "找不到 psql 可执行文件。\n"
            "  这个子命令要直连 ERP 数据库读配置表，需要 PostgreSQL 客户端。\n"
            "  处理方式（任选其一）：\n"
            "    1) 用 --psql <psql.exe 的完整路径> 指定；\n"
            "    2) 把 psql 所在目录加进 PATH；\n"
            "    3) 没有客户端时，用 --print-sql 拿 SQL 去别的工具里跑。"
            + NO_PSQL + ASK_DB
        )
    host = cfg.get("db_host")
    name = cfg.get("db_name")
    user = cfg.get("db_user")
    missing = [k for k, v in (("KD_DB_HOST", host), ("KD_DB_NAME", name),
                              ("KD_DB_USER", user)) if not v]
    if missing:
        raise KingdeeError("缺少数据库连接参数：%s" % " / ".join(missing) + "\n" + ASK_DB)

    cmd = [exe, "-h", str(host), "-p", str(cfg.get("db_port") or "5432"),
           "-U", str(user), "-d", str(name), "-X", "-A", "--csv",
           "-v", "ON_ERROR_STOP=1"]
    for k in ("bizobject", "service", "keyword"):
        if cfg.get(k) is not None:
            cmd += ["-v", "%s=%s" % (k, cfg[k])]
    cmd += ["-c", sql]

    env = dict(os.environ)
    if cfg.get("db_password"):
        env["PGPASSWORD"] = str(cfg["db_password"])
    env["PGCLIENTENCODING"] = "UTF8"

    try:
        # 必须设 encoding="utf-8"：Windows 默认按 GBK 解码，中文列名/描述会乱码
        out = subprocess.run(cmd, capture_output=True, timeout=timeout, env=env)
    except FileNotFoundError:
        raise KingdeeError("无法执行 %s（路径不对或没有执行权限）" % exe)
    except subprocess.TimeoutExpired:
        raise KingdeeError("SQL 执行超时（%ds）—— 检查网络/防火墙能否连到 %s:%s"
                           % (timeout, host, cfg.get("db_port")))

    err = out.stderr.decode("utf-8", "replace").strip()
    if out.returncode != 0:
        raise KingdeeError("psql 执行失败：\n%s" % err[:600])

    text = out.stdout.decode("utf-8", "replace")
    if not text.strip():
        return []

    import csv
    import io
    rows = list(csv.DictReader(io.StringIO(text)))
    # psql --csv 对空值输出空串，统一成 None 便于判断
    return [{k: (v if v != "" else None) for k, v in r.items()} for r in rows]


# ==========================================================================
# 配置
# ==========================================================================

HTTP_KEYS = ["base_url", "auth", "client_id", "client_secret", "username",
             "password", "account_id", "app", "form", "service"]
ALL_KEYS = HTTP_KEYS + DB_KEYS + ["psql"]


def load_config(args):
    """按 配置文件 → 环境变量 → 命令行 的顺序叠加（后者覆盖前者）。"""
    cfg = {}
    if getattr(args, "config", None) and os.path.exists(args.config):
        cfg = json.load(open(args.config, encoding="utf-8"))
    for k in ALL_KEYS:
        env = os.environ.get("KD_" + k.upper())
        if env:
            cfg[k] = env
    for k in ALL_KEYS:
        v = getattr(args, k, None)
        if v:
            cfg[k] = v
    return cfg


def need_base_url(cfg):
    if not cfg.get("base_url"):
        print("!! 需要 --base-url（或环境变量 KD_BASE_URL），形如 http://host:port")
        return False
    return True


# 缺凭据时给「向用户索要」的完整清单 —— 比只说「缺少 X」有用得多：
# 使用者（尤其是 agent）需要知道要哪几项、去哪拿、哪些可以不给。
ASK_HTTP = """
需要向使用者索取以下信息（任选一种认证方式）：

  【A】第三方应用（推荐，官方唯一稳定方式）—— 4 项全要
    1. 环境地址        → --base-url     形如 http://host:port
    2. 账套 accountId  → --account-id   可用 `kd_probe.py accounts --base-url <地址>` 匿名列出
    3. 系统编码        → --client-id    【开放服务云】→【OpenAPI】→【第三方应用】里的「系统编码」
    4. 认证密钥        → --client-secret 同上界面的「AccessToken 认证密钥」
    另需一个有效用户名 → --username（默认 admin）。若该应用开了「启用代理用户控制」，
    这个用户必须在其「代理用户」列表里，否则报 603（见 SKILL.md 5.7/4.7）。

  【B】网页账号密码（应急，仅当目标 API 未开「第三方应用授权」）
    1. 环境地址 2. 用户名 3. 密码 4. 账套 accountId，加 --auth web

  也可以直接把已拿到的令牌给我：--session-token <token>

⚠️ 凭据不要写进命令行历史，用环境变量（KD_BASE_URL / KD_CLIENT_ID / ...）
   或 `--save-config kd.json` 存成本地文件（kd.json 已在 .gitignore 中）。
"""

ASK_DB = """
需要向使用者索取 ERP 数据库连接信息（用于直读 API 配置表）：

    1. 数据库主机    → KD_DB_HOST
    2. 端口          → KD_DB_PORT     （默认 5432）
    3. 库名          → KD_DB_NAME     （金蝶苍穹所在的 ERPDB）
    4. 用户名        → KD_DB_USER
    5. 密码          → KD_DB_PASSWORD

  这些是苍穹**后台数据库**的直连信息，不是 OpenAPI 的应用凭据，两者不要搞混。
  拿不到时用 `--print-sql` 只打印 SQL，交给使用者在自己的数据库工具里跑。
"""

NO_PSQL = """
  ⚠️ 本机没找到 psql（PostgreSQL 客户端）。除了上面的 --psql/PATH 方案，
     也可以直接 `--print-sql` 把 SQL 拿到别的数据库工具里跑。
"""


def make_client(cfg, insecure=False):
    return Client(cfg["base_url"], insecure=insecure)


def authenticate(client, cfg, purpose=""):
    """按配置完成认证，返回是否成功。

    优先 OpenAPI（官方唯一稳定方式）；`--auth web` 走网页会话（应急，见 README）。
    """
    auth = cfg.get("auth") or "openapi"
    if cfg.get("session_token"):
        tok = cfg["session_token"]
        client.cookies["KERPSESSIONID"] = tok
        client.cookies["access_token"] = tok
        client.access_token = tok
        print("已复用现有网页会话令牌")
        return True
    if auth == "web":
        if not cfg.get("username"):
            print("!! web 认证需要 --username")
            print(ASK_HTTP)
            return False
        import getpass
        pwd = cfg.get("password") or getpass.getpass("密码：")
        login_web(client, cfg["username"], pwd, cfg.get("account_id"))
        print("网页登录成功（会话已建立）")
        return True
    missing = [k for k in ("client_id", "client_secret", "username", "account_id")
               if not cfg.get(k)]
    if missing:
        print("!! OpenAPI 认证缺少：%s"
              % ", ".join("--" + m.replace("_", "-") for m in missing))
        print("   第三方应用在【开放服务云】→【OpenAPI】→【第三方应用】里创建。")
        print(ASK_HTTP)
        return False
    get_openapi_token(client, cfg["client_id"], cfg["client_secret"],
                      cfg["username"], cfg["account_id"])
    print("已获取 access_token（有效期默认 2 小时）%s" % purpose)
    return True


def call_api(client, app, form, service, body):
    """POST 一个操作API，自动带上 access_token 头。"""
    path = QUERY_PATH.format(app=app, form=form, service=service)
    headers = {"access_token": client.access_token} if client.access_token else None
    return path, client.request(path, body, headers=headers)


def classify(resp, authenticated):
    """把一次路径探测的结果翻译成「存在 / 不存在 / 无法判定」。

    ⚠️ 核心前提：**只有已认证时** 403/404 才有判别力。
    未认证时服务端在鉴权阶段就返回 401，存在的和不存在的路径返回完全一样。
    """
    code = str(resp.get("errorCode"))
    msg = str(resp.get("message") or "")
    if code == "401" or "未经授权" in msg:
        if authenticated:
            return "已认证仍 401", "会话无效或已过期"
        return "无法判定", "未认证 —— 存在与否都返回 401，需先登录再探"
    if code == "404" or "Cannot found OpenAPI" in msg:
        return "不存在", "appId/formId/serviceName 组合错，或该 API 未发布"
    if code == "403" or "第三方应用授权" in msg:
        return "存在", "需第三方应用授权（cookie 认证会被拒，须用 client_id/secret 取 token）"
    if code == "400":
        return "存在", "已进入业务逻辑层（报的是请求体问题：%s）" % msg[:30]
    if code in ("0", "200") or resp.get("status") is True:
        return "可用", "调用成功"
    return "其它", "errorCode=%s %s" % (code, msg[:40])


# ==========================================================================
# 子命令：HTTP
# ==========================================================================

def cmd_accounts(args, cfg):
    """列账套（数据中心）。这个接口不需要登录，凭据不对时也该能用。"""
    if not need_base_url(cfg):
        return 2
    client = make_client(cfg, args.insecure)
    dcs = list_datacenters(client)
    cur = str(cfg.get("account_id") or "")
    if args.json:
        print(json.dumps(dcs, ensure_ascii=False, indent=1))
        return 0
    if not dcs:
        print("（未返回数据中心列表）")
        return 1
    for d in dcs:
        mark = "   ← 当前配置" if cur and str(d.get("accountId")) == cur else ""
        print("accountId=%-24s number=%-14s %s%s"
              % (d.get("accountId"), d.get("accountNumber"), d.get("accountName"), mark))
    print("\n提示：accountId 就是 getToken 要传的那个。「账套」= 数据中心 = accountId。")
    return 0


def cmd_token(args, cfg):
    """只验认证 —— 换应用/换账套时，先确认 token 拿得到。"""
    if not need_base_url(cfg):
        return 2
    client = make_client(cfg, args.insecure)
    if not authenticate(client, cfg):
        return 2
    if args.json:
        print(json.dumps({"status": True,
                          "token_length": len(client.access_token or "")},
                         ensure_ascii=False))
    else:
        print("access_token 获取成功（长度 %d）" % len(client.access_token or ""))
    return 0


def cmd_paths(args, cfg):
    """探测服务路径是否存在 —— 403=存在、404=不存在（必须先认证）。"""
    if not need_base_url(cfg):
        return 2
    client = make_client(cfg, args.insecure)
    authenticated = authenticate(client, cfg)

    paths = []
    for a in (args.paths or []):
        paths.extend(p.strip() for p in a.split(",") if p.strip())
    if not paths:
        paths = DEFAULT_PATHS

    results = []
    for p in paths:
        try:
            r = client.request(p, {"data": {}, "pageNo": 1, "pageSize": 1},
                               headers=({"access_token": client.access_token}
                                        if client.access_token else None))
        except KingdeeError as e:
            results.append((p, "请求失败", str(e).split("\n")[0][:70]))
            continue
        tag, note = classify(r, authenticated)
        results.append((p, tag, note))

    if args.json:
        print(json.dumps([{"path": p, "verdict": t, "detail": d}
                          for p, t, d in results], ensure_ascii=False, indent=1))
        return 0

    if not authenticated:
        print("⚠️ 未认证：下面所有路径都返回 401，无法区分存在与否。")
        print("   带上 --client-id/--client-secret（推荐）或 --auth web 再跑一次。\n")
    for p, tag, note in results:
        print("%-10s %s%s" % (tag, p, ("  ← " + note) if note else ""))
    if authenticated:
        print("\n判定依据：403/400 = 路径存在；404 = 路径不存在。")
    return 0


def cmd_ref(args, cfg):
    """取账套参考数据 —— 从真实单据里捞出能用的组织/单据类型/业务类型/物料。"""
    if not need_base_url(cfg):
        return 2
    client = make_client(cfg, args.insecure)
    if not authenticate(client, cfg):
        return 2

    app = cfg.get("app") or SALORDER_APP_ID
    form = cfg.get("form") or SALORDER_FORM_ID
    service = cfg.get("service") or DEFAULT_QUERY_API
    _, resp = call_api(client, app, form, service,
                       {"data": {}, "pageNo": 1, "pageSize": args.limit})
    if not resp.get("status", True) or str(resp.get("errorCode")) not in ("None", "", "0"):
        print("查询失败：errorCode=%s %s" % (resp.get("errorCode"), resp.get("message")))
        return 1

    rows = rows_of(resp)
    if not rows:
        print("没有查到单据，取不到参考数据（先确认账套里有数据）。")
        return 1

    info = {}
    for k in REF_KEYS:
        vals = sorted({str(r[k]) for r in rows if r.get(k) not in (None, "")})
        if vals:
            info[k] = vals
    if args.json:
        print(json.dumps({"fields": info, "sample": rows[0]}, ensure_ascii=False, indent=1))
        return 0

    print("从 %d 张单据里取到的参考值（可直接用于 filter）：\n" % len(rows))
    for k, vals in info.items():
        print("  %-26s %s" % (k + ":", " | ".join(vals[:12])))
    e = (rows[0].get("billentry") or [{}])[0]
    if e:
        print("\n分录样本：")
        for k in ("material_masterid_number", "material_masterid_modelnum",
                  "unit_number", "linetype_number", "e_stockorg_number",
                  "qty", "price", "amount"):
            if e.get(k) not in (None, ""):
                print("  %-26s %s" % (k + ":", e[k]))
    return 0


def cmd_doc(args, cfg):
    """查单据 —— 比 salesorder_query 更通用：对象/服务名可指定。"""
    if not need_base_url(cfg):
        return 2
    client = make_client(cfg, args.insecure)
    if not authenticate(client, cfg):
        return 2

    app = cfg.get("app") or args.app
    form = cfg.get("form") or args.form
    service = cfg.get("service") or args.service
    if not (app and form and service):
        print("!! 需要指定业务对象与服务名：--app sm --form sm_salorder --service query")
        return 2

    data = {}
    if args.billno:
        data["billno"] = args.billno
    body = {"data": data, "pageNo": args.page, "pageSize": args.limit}
    if args.filter:
        body["filter"] = args.filter
    if args.fields:
        body["selectFields"] = args.fields

    path, resp = call_api(client, app, form, service, body)
    if args.json:
        print(json.dumps(resp, ensure_ascii=False, indent=2))
        return 0
    if not resp.get("status", True) or str(resp.get("errorCode")) not in ("None", "", "0"):
        print("查询失败：errorCode=%s  %s\n路径=%s"
              % (resp.get("errorCode"), resp.get("message"), path))
        return 1

    rows = rows_of(resp)
    if not rows:
        print("未查到数据（请求体：%s）" % json.dumps(body, ensure_ascii=False))
        return 1
    print("路径=%s\n共 %d 条（请求体：%s）\n"
          % (path, len(rows), json.dumps(body, ensure_ascii=False)))
    fields = args.fields.split(",") if args.fields else None
    if not fields and len(rows[0]) > 10:
        fields = list(rows[0].keys())[:10]
        print("（该单据返回 %d 个字段，默认只展示前 10 列；加 --fields 指定，--json 看全部）\n"
              % len(rows[0]))
    print_table(rows, fields)
    return 0


# ==========================================================================
# 子命令：配置表直读（psql）
# ==========================================================================

SQL_SERVICES_ALL = """
SELECT fbizobject, fnumber, foperation, fenable, fis_only_thirdapp_auth
FROM t_open_apiservice
WHERE fenable = '1' AND fbizobject <> ' '
GROUP BY 1,2,3,4,5
ORDER BY fbizobject, fnumber;
"""

SQL_SERVICES_ONE = """
SELECT DISTINCT fnumber, foperation, fenable, fis_only_thirdapp_auth
FROM t_open_apiservice
WHERE fbizobject = :'bizobject'
ORDER BY fnumber;
"""

SQL_BODY = """
SELECT b.fseq, b.fparamname, b.fparamtype, b.fmust, b.fbodyparamdes,
       b.fbody_level, b.fexample
FROM t_open_apiservice s JOIN t_open_apibodyentry b ON b.fid = s.fid
WHERE s.fbizobject = :'bizobject' AND s.fnumber = :'service'
ORDER BY b.fbody_level, b.fseq;
"""

SQL_RESP = """
SELECT r.fparamname, r.fparamtype, r.fbodyparamdes, r.fbody_level
FROM t_open_apiservice s JOIN t_open_apirespentry r ON r.fid = s.fid
WHERE s.fbizobject = :'bizobject' AND s.fnumber = :'service'
LIMIT 60;
"""

SQL_SEARCH = """
SELECT DISTINCT fbizobject, fnumber
FROM t_open_apiservice
WHERE fenable = '1'
  AND (fbizobject ILIKE :'keyword' OR fnumber ILIKE :'keyword')
ORDER BY fbizobject, fnumber
LIMIT 60;
"""

OBJECT_MAP_SQL = """
SELECT fbizobject, MAX(objname) AS objname FROM (
  SELECT fbizobject, fname AS objname FROM t_open_apiservice WHERE fname IS NOT NULL
) t GROUP BY fbizobject;
"""


def cmd_services(args, cfg):
    """列出已发布的 OpenAPI 服务。

    比猜服务名快得多 —— 而且能直接看出哪些 API 开了「第三方应用授权」
    （这类必须用 client_id/client_secret 取 token，cookie 认证一律 403）。
    """
    if args.print_sql:
        print(SQL_SERVICES_ONE if args.object else SQL_SERVICES_ALL)
        return 0

    if args.object:
        cfg = dict(cfg, bizobject=args.object)
        rows = psql_query(SQL_SERVICES_ONE, cfg, cfg.get("psql"))
        if not rows:
            print("没有找到业务对象 %s。用 `kd_probe.py search <关键字>` 按中文名/表名找一下。"
                  % args.object)
            return 1
        if args.json:
            print(json.dumps(rows, ensure_ascii=False, indent=1))
            return 0
        print("业务对象 %s 发布的服务：\n" % args.object)
        for x in rows:
            print("  %-24s 操作=%-12s 启用=%s  需第三方授权=%s"
                  % (x["fnumber"], x.get("foperation") or "-",
                     x.get("fenable"), x.get("fis_only_thirdapp_auth")))
        print("\n查某个服务的入参模板：  kd_probe.py body %s <服务名>" % args.object)
        return 0

    rows = psql_query(SQL_SERVICES_ALL, cfg, cfg.get("psql"))
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    by_obj = {}
    for x in rows:
        by_obj.setdefault(x["fbizobject"], [])
        if not any(i["fnumber"] == x["fnumber"] for i in by_obj[x["fbizobject"]]):
            by_obj[x["fbizobject"]].append(x)
    for obj in sorted(by_obj):
        names = []
        for i in by_obj[obj]:
            op = i.get("foperation")
            tag = "(%s)" % op if op and op != i["fnumber"] else ""
            names.append("%s%s%s" % (i["fnumber"], tag,
                                     "*" if i.get("fis_only_thirdapp_auth") == "1" else ""))
        print("%s: %s" % (obj, ", ".join(names)))
    print("\n共 %d 个业务对象，%d 条服务配置。"
          "\n* = 需要第三方应用授权（用 client_id/client_secret 取令牌即可）。"
          "\n查某对象的入参模板：  kd_probe.py body <对象> <服务名>"
          % (len(by_obj), len(rows)))
    return 0


def cmd_body(args, cfg):
    """查某个服务的入参模板 + 返回结构 —— 回答「这个 API 到底要传什么」。

    这是猜服务名/猜参数名这件事的终点：
      t_open_apibodyentry 直接给出参数名、类型、是否必填、层级。
    ⚠️ 服务名区分大小写（`query` ≠ `Query`）。
    """
    if args.print_sql:
        print(SQL_BODY)
        return 0
    if not args.service:
        print("!! 需要服务名：kd_probe.py body %s <服务名>" % args.object)
        return 2

    cfg = dict(cfg, bizobject=args.object, service=args.service)
    rows = psql_query(SQL_BODY, cfg, cfg.get("psql"))
    if not rows:
        print("没有 %s/%s 的入参模板。\n  → 服务名区分大小写，先跑 "
              "`kd_probe.py services %s` 看可用的服务名。"
              % (args.object, args.service, args.object))
        return 1
    resp = psql_query(SQL_RESP, cfg, cfg.get("psql"))

    if args.json:
        print(json.dumps({"body": rows, "response": resp}, ensure_ascii=False, indent=1))
        return 0

    print("%s/%s 入参模板：\n" % (args.object, args.service))
    seen = set()
    for x in rows:
        key = (x.get("fbody_level"), x["fparamname"], x.get("fmust"))
        if key in seen:      # 同一服务可能有多条重复配置行
            continue
        seen.add(key)
        must = "必填" if x.get("fmust") == "1" else "可选"
        lv = LEVEL_LABEL.get(_as_int(x.get("fbody_level")), x.get("fbody_level"))
        print("  [%s] %-30s %-10s %s  %s%s"
              % (lv, x["fparamname"], x.get("fparamtype") or "", must,
                 x.get("fbodyparamdes") or "",
                 ("  eg=%s" % x["fexample"]) if x.get("fexample") else ""))
    if resp:
        print("\n返回结构：")
        seen2 = set()
        for x in resp:
            if x["fparamname"] in seen2:
                continue
            seen2.add(x["fparamname"])
            lv = LEVEL_LABEL.get(_as_int(x.get("fbody_level")), x.get("fbody_level"))
            print("  [%s] %-30s %-10s %s"
                  % (lv, x["fparamname"], x.get("fparamtype") or "",
                     x.get("fbodyparamdes") or ""))
    print("\n提示：请求体分内外两层 —— 业务参数放 `data` 里，"
          "pageNo/pageSize/filter 平铺在顶层（见 SKILL.md 第 4.6 节）。")
    return 0


def cmd_search(args, cfg):
    """按关键字模糊找业务对象 —— 中文名不好猜表名时用。"""
    if not args.keyword:
        print("!! 需要关键字：kd_probe.py search <关键字>")
        return 2
    if args.print_sql:
        print(SQL_SEARCH)
        return 0
    cfg = dict(cfg, keyword="%%%s%%" % args.keyword)
    rows = psql_query(SQL_SEARCH, cfg, cfg.get("psql"))
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    if not rows:
        print("没有匹配 %r 的服务配置。" % args.keyword)
        print("  提示：这里搜的是 t_open_apiservice 里**已发布**的业务对象编码，")
        print("  不是数据字典。要找物理表请用 scripts/search.py。")
        return 1
    for x in rows:
        print("%s.%s" % (x["fbizobject"], x["fnumber"]))
    return 0


def _as_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return v


# ==========================================================================
# main
# ==========================================================================

def add_common(p):
    p.add_argument("--config", default="kd.json", help="本地配置文件（默认 kd.json）")
    p.add_argument("--json", action="store_true", help="以 JSON 输出，便于脚本消费")
    p.add_argument("--insecure", action="store_true", help="https 时跳过证书校验")


def add_http(p):
    p.add_argument("--base-url", help="形如 http://host:port")
    p.add_argument("--auth", choices=["openapi", "web"], help="认证方式（默认 openapi）")
    p.add_argument("--client-id", help="第三方应用系统编码")
    p.add_argument("--client-secret", help="第三方应用 AccessToken 认证密钥")
    p.add_argument("--username")
    p.add_argument("--password")
    p.add_argument("--account-id", help="数据中心ID（账套）")
    p.add_argument("--session-token", help="复用已有网页会话令牌")


def add_db(p):
    p.add_argument("--db-host", help="ERP 数据库主机")
    p.add_argument("--db-port", help="ERP 数据库端口（默认 5432）")
    p.add_argument("--db-name", help="ERP 数据库名")
    p.add_argument("--db-user", help="ERP 数据库用户")
    p.add_argument("--db-password", help="ERP 数据库密码（建议用 KD_DB_PASSWORD 环境变量）")
    p.add_argument("--psql", help="psql 可执行文件路径（自动探测失败时指定）")
    p.add_argument("--print-sql", action="store_true",
                   help="只打印 SQL 不执行（没有 psql 客户端时用）")


def build_parser():
    ap = argparse.ArgumentParser(
        prog="kd_probe",
        description="金蝶云苍穹 探路 + 查配置 CLI（只读）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
常用组合
  kd_probe.py services sm_salorder          先看对象发布了哪些服务（准确、不用猜）
  kd_probe.py body sm_salorder query        再看这个服务要传什么参数
  kd_probe.py accounts                      列账套拿 accountId
  kd_probe.py paths                         再用错误码复核路径是否存在（需认证）
  kd_probe.py ref                           从真实单据取可用的过滤值
""")
    sub = ap.add_subparsers(dest="command", metavar="<子命令>")

    # —— HTTP 侧 ——
    p = sub.add_parser("accounts", help="列账套（数据中心）—— 匿名接口，不需要凭据")
    add_common(p)
    add_http(p)

    p = sub.add_parser("token", help="只验认证：能否取到 access_token")
    add_common(p)
    add_http(p)

    p = sub.add_parser("paths", help="探测服务路径是否存在（403=存在 / 404=不存在）")
    p.add_argument("paths", nargs="*", help="候选路径，逗号分隔；不传用内置清单")
    add_common(p)
    add_http(p)

    p = sub.add_parser("ref", help="取账套参考数据（组织/单据类型/业务类型/物料）")
    p.add_argument("--limit", type=int, default=20, help="取样条数（默认 20）")
    p.add_argument("--app", default=SALORDER_APP_ID)
    p.add_argument("--form", default=SALORDER_FORM_ID)
    p.add_argument("--service", default=DEFAULT_QUERY_API)
    add_common(p)
    add_http(p)

    p = sub.add_parser("doc", help="查单据（对象/服务名可指定）")
    p.add_argument("--app", default=SALORDER_APP_ID, help="应用编码（默认 sm）")
    p.add_argument("--form", default=SALORDER_FORM_ID, help="业务对象编码")
    p.add_argument("--service", default=DEFAULT_QUERY_API, help="服务名（区分大小写）")
    p.add_argument("--billno", help="单号（放进请求体的 data 里）")
    p.add_argument("--filter", help='过滤表达式，如 "billno like \'SO%%\'"')
    p.add_argument("--fields", help="只取这些字段，逗号分隔")
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--limit", type=int, default=20)
    add_common(p)
    add_http(p)

    # —— 配置表直读（psql）——
    p = sub.add_parser("services", help="列出已发布的 OpenAPI 服务（读 t_open_apiservice）")
    p.add_argument("object", nargs="?", help="业务对象编码，如 sm_salorder；不传列出全部")
    add_common(p)
    add_db(p)

    p = sub.add_parser("body", help="查某服务的入参模板 + 返回结构（读配置表）")
    p.add_argument("object", help="业务对象编码，如 sm_salorder")
    p.add_argument("service", nargs="?", help="服务名，如 query（区分大小写）")
    add_common(p)
    add_db(p)

    p = sub.add_parser("search", help="按关键字模糊找业务对象")
    p.add_argument("keyword", nargs="?", help="关键字")
    add_common(p)
    add_db(p)

    return ap


DISPATCH = {
    "accounts": cmd_accounts,
    "token": cmd_token,
    "paths": cmd_paths,
    "ref": cmd_ref,
    "doc": cmd_doc,
    "services": cmd_services,
    "body": cmd_body,
    "search": cmd_search,
}


def main(argv):
    ap = build_parser()
    if not argv:
        ap.print_help()
        return 2
    args = ap.parse_args(argv)
    if not args.command:
        ap.print_help()
        return 2

    cfg = load_config(args)
    try:
        return DISPATCH[args.command](args, cfg)
    except KingdeeError as e:
        print("ERR %s" % e)
        return 1
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
