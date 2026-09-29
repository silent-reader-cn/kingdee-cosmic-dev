#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kd_doctor —— 金蝶云苍穹环境接入诊断
====================================
把「刚拿到一个环境该先确认什么」做成可执行检查，避免每次都靠人肉试错。

覆盖的检查（对应实测踩过的坑）：
  1. 连通性          首页 / 登录页是否可达
  2. 账套            匿名列数据中心，拿 accountId
  3. 登录接口契约     /ierp/api/login.do 是否存在、缺参数报什么
  4. 登录            实际登录（需要凭据），并识别「限流」这种含糊报错
  5. 取令牌接口       /ierp/kapi/oauth2/getToken 是否存在、缺什么参数
  6. 业务接口路径     用 403 vs 404 反推候选路径哪个真实存在
  7. 授权开关状态     带会话再试，判断该 API 是否要求第三方应用授权
  8. 结论            给出可执行的下一步

用法：
  # 只做匿名检查（不碰账号，不会触发限流）
  python examples/kd_doctor.py --base-url http://host:port

  # 带凭据做完整检查（只登录 1 次，不重试）
  python examples/kd_doctor.py --base-url http://host:port \
      --username admin --password <密码> --account-id <数据中心ID>

  # 批量探测候选接口路径
  python examples/kd_doctor.py --base-url http://host:port \
      --probe-paths /ierp/kapi/v2/sm/sm_salorder/query,/ierp/kapi/v2/sm/sm_salorder/list

⚠️ 登录接口有限流：连续失败后会返回含糊的「无法获取云通行证AccessToken」。
   本脚本默认只登录 1 次、不重试。要重试请显式加 --retry N。
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from salorder_query import (  # noqa: E402
    Client, KingdeeError, list_datacenters, login_web, get_openapi_token,
    WEB_LOGIN_PATH, TOKEN_PATH, DATACENTER_PATH, QUERY_PATH,
    SALORDER_APP_ID, SALORDER_FORM_ID, DEFAULT_QUERY_API,
)

RESULTS = []      # (level, title, detail)
LEVEL_OK, LEVEL_WARN, LEVEL_BAD, LEVEL_INFO = "✓", "!", "✗", "·"


def record(level, title, detail=""):
    RESULTS.append((level, title, detail))
    print("  %s %-34s %s" % (level, title, detail))


def section(name):
    print("\n── %s " % name + "─" * max(0, 60 - len(name)))


# --------------------------------------------------------------------------

def check_reach(client):
    section("1. 连通性")
    for label, path in (("ierp 首页", "/ierp/"), ("登录页", "/ierp/login.html")):
        try:
            body = client.request(path, None, method="GET", raw=True)
            record(LEVEL_OK, label, "可达（%d 字节）" % len(body))
        except KingdeeError as e:
            record(LEVEL_BAD, label, str(e).split("\n")[0][:80])


def check_datacenters(client):
    section("2. 账套（数据中心）")
    try:
        dcs = list_datacenters(client)
    except KingdeeError as e:
        record(LEVEL_BAD, "列账套", str(e).split("\n")[0][:80])
        return []
    if not dcs:
        record(LEVEL_BAD, "列账套", "返回空列表")
        return []
    record(LEVEL_OK, "列账套（无需登录）", "%d 个" % len(dcs))
    for d in dcs:
        record(LEVEL_INFO, "  " + str(d.get("accountName")),
               "accountId=%s  number=%s" % (d.get("accountId"), d.get("accountNumber")))
    return dcs


def check_login_contract(client):
    section("3. 登录接口契约")
    try:
        r = client.request(WEB_LOGIN_PATH, {})
    except KingdeeError as e:
        record(LEVEL_BAD, WEB_LOGIN_PATH, str(e).split("\n")[0][:80])
        return
    msg = str(r.get("message") or r.get("errorMsg") or "")[:60]
    record(LEVEL_OK, WEB_LOGIN_PATH + " 存在", "空体返回：%s" % msg)
    record(LEVEL_INFO, "正确键名", "user / password（不是 username！用错键名只会报「参数错误」）")


def check_login(client, username, password, account_id, retry):
    section("4. 登录")
    if not username:
        record(LEVEL_INFO, "跳过", "未提供 --username")
        return None
    for i in range(retry + 1):
        try:
            tok = login_web(client, username, password, account_id)
            record(LEVEL_OK, "网页登录", "成功，token=%s…" % tok[:28])
            return tok
        except KingdeeError as e:
            text = str(e)
            if i < retry:
                time.sleep(5 * (i + 1))
                continue
            record(LEVEL_BAD, "网页登录", text.split("\n")[0][:110])
            if "云通行证" in text:
                record(LEVEL_WARN, "这个报错有歧义",
                       "既可能是密码错，也可能是被限流，还可能是环境连不上金蝶云")
                record(LEVEL_INFO, "建议",
                       "确认账号能在网页正常登录；自动化脚本务必退避重试，别无脑循环")
            return None
    return None


def check_token_endpoint(client, cfg):
    section("5. 取令牌接口")
    try:
        r = client.request(TOKEN_PATH, {})
    except KingdeeError as e:
        record(LEVEL_BAD, TOKEN_PATH, str(e).split("\n")[0][:80])
        return
    code = str(r.get("errorCode"))
    record(LEVEL_OK, TOKEN_PATH + " 存在", "errorCode=%s %s"
           % (code, str(r.get("message") or "")[:50]))
    if code == "405":
        record(LEVEL_INFO, "只支持 POST", "GET 会报 405")
    if code == "603":
        record(LEVEL_INFO, "需要 client_id",
               "第三方应用在【开放服务云】→【OpenAPI】→【第三方应用】创建")
    if cfg.get("client_id") and cfg.get("client_secret"):
        try:
            get_openapi_token(client, cfg["client_id"], cfg["client_secret"],
                              cfg.get("username", ""), cfg.get("account_id", ""))
            record(LEVEL_OK, "取 access_token", "成功")
        except KingdeeError as e:
            record(LEVEL_BAD, "取 access_token", str(e)[:120])
    else:
        record(LEVEL_INFO, "跳过实际取令牌", "未提供 --client-id/--client-secret")


def classify(resp, has_session):
    """判定一次路径探测的结果。

    ⚠️ 关键前提：**只有已认证时**才能用 403/404 区分路径是否存在。
    未认证时服务端在鉴权阶段就返回 401，三个路径（存在的、不存在的）返回一模一样，
    据此判断会把不存在的路径误判成「存在」。
    """
    code = str(resp.get("errorCode"))
    msg = str(resp.get("message") or "")
    if code == "401" or "未经授权" in msg:
        if has_session:
            return LEVEL_BAD, "已带会话仍 401：会话无效或已过期"
        return LEVEL_INFO, "未认证（无法判定路径是否存在，需先登录再探）"
    if code == "404" or "Cannot found OpenAPI" in msg:
        return LEVEL_BAD, "路径不存在（appId/formId/serviceName 组合错）"
    if code == "403" or "第三方应用授权" in msg:
        return LEVEL_WARN, "路径存在，但要求第三方应用授权（cookie 认证会被拒）"
    if code in ("0", "200") or resp.get("status") is True:
        return LEVEL_OK, "路径存在且调用成功"
    return LEVEL_INFO, "返回 errorCode=%s %s" % (code, msg[:40])


def check_paths(client, paths, has_session):
    section("6/7. 业务接口路径与授权要求")
    if not paths:
        paths = [QUERY_PATH.format(app=SALORDER_APP_ID, form=SALORDER_FORM_ID,
                                   service=DEFAULT_QUERY_API)]
    if not has_session:
        record(LEVEL_WARN, "未登录，路径探测不可靠",
               "未认证时所有 kapi 路径都返回 401，无法区分存在与否")
        record(LEVEL_INFO, "建议", "先带 --username/--password 登录，再做路径探测")
    for p in paths:
        try:
            r = client.request(p, {})
        except KingdeeError as e:
            record(LEVEL_BAD, p, str(e).split("\n")[0][:70])
            continue
        level, note = classify(r, has_session)
        record(level, p, note)
    if has_session:
        record(LEVEL_INFO, "判断技巧",
               "403 = 路径对但认证方式不合规；404 = 路径本身不存在。可据此快速筛路径。")


# --------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(add_help=True,
                                 description="金蝶云苍穹环境接入诊断（默认不重试登录）")
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--config", default="kd.json")
    ap.add_argument("--username")
    ap.add_argument("--password")
    ap.add_argument("--account-id")
    ap.add_argument("--client-id")
    ap.add_argument("--client-secret")
    ap.add_argument("--probe-paths", help="逗号分隔的候选接口路径")
    ap.add_argument("--retry", type=int, default=0,
                    help="登录失败后的重试次数（默认 0，避免触发限流）")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出结果")
    ap.add_argument("--insecure", action="store_true")
    args = ap.parse_args(argv)

    cfg = {}
    if args.config and os.path.exists(args.config):
        cfg = json.load(open(args.config, encoding="utf-8"))
    for k in ("username", "password", "account_id", "client_id", "client_secret"):
        v = getattr(args, k, None) or os.environ.get("KD_" + k.upper())
        if v:
            cfg[k] = v

    client = Client(args.base_url, insecure=args.insecure)
    print("=" * 68)
    print("金蝶云苍穹环境诊断：%s" % args.base_url)
    print("=" * 68)

    check_reach(client)
    check_datacenters(client)
    check_login_contract(client)
    tok = check_login(client, cfg.get("username"), cfg.get("password"),
                      cfg.get("account_id"), args.retry)
    check_token_endpoint(client, cfg)
    paths = [p.strip() for p in args.probe_paths.split(",")] if args.probe_paths else []
    check_paths(client, paths, bool(tok))

    print("\n" + "=" * 68)
    ok = sum(1 for lv, _, _ in RESULTS if lv == LEVEL_OK)
    warn = sum(1 for lv, _, _ in RESULTS if lv == LEVEL_WARN)
    bad = sum(1 for lv, _, _ in RESULTS if lv == LEVEL_BAD)
    print("通过 %d / 注意 %d / 失败 %d" % (ok, warn, bad))
    if bad:
        print("\n需要处理的：")
        for lv, t, d in RESULTS:
            if lv == LEVEL_BAD:
                print("  - %s：%s" % (t.strip(), d))
    if args.json:
        print(json.dumps([{"level": l, "item": t, "detail": d} for l, t, d in RESULTS],
                         ensure_ascii=False, indent=1))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
