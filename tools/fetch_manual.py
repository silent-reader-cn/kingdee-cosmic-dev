#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_manual —— 抓取金蝶云社区「专题」知识手册，落地为可索引的 Markdown
========================================================================
数据源（vip.kingdee.com 的 Nuxt SPA 背后的 JSON 接口，无需登录）：

  目录  GET /knowledgeapi/knowledge-specials/{specialId}
  正文  GET /knowledgeapi/special-knowledges/{entityId}

正文是 UEditor 富文本 HTML，用同目录的 `html2md.py`（零依赖）转成 Markdown。

产物：
  references/openapi/<一级分类>/…/<标题>.md     Markdown 正文（含 YAML frontmatter）
  references/openapi/_source/<entityId>.json    原始 JSON 存档（便于复核/重建）
  references/openapi/_INDEX.md                  手册总目录

用法：
  python tools/fetch_manual.py                      # 全量抓取（已存在的跳过）
  python tools/fetch_manual.py --force              # 全部重抓
  python tools/fetch_manual.py --only 226337046514476288
  python tools/fetch_manual.py --list               # 只打印目录树
"""
import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
from html2md import html_to_markdown  # noqa: E402

SITE = "https://vip.kingdee.com"
API = SITE + "/knowledgeapi"
SPECIAL_ID = "226337046514476288"
PRODUCT_LINE_ID = 29
OUT_DIR = os.path.join(ROOT, "references", "openapi")
SOURCE_DIR = os.path.join(OUT_DIR, "_source")
TOC_CACHE = os.path.join(SOURCE_DIR, "_toc.json")

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "application/json, text/plain, */*",
    "Referer": "%s/knowledge/specialDetail/%s?productLineId=%d&lang=zh-CN"
               % (SITE, SPECIAL_ID, PRODUCT_LINE_ID),
}

ILLEGAL = re.compile(r'[\\/:*?"<>|\r\n\t]')


def fetch_json(url, retries=4, timeout=30):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
            return json.loads(raw.decode("utf-8"))
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError("请求失败 %s：%s" % (url, last))


def safe_name(text, limit=90):
    s = ILLEGAL.sub("_", (text or "").strip())
    s = re.sub(r"\s+", " ", s).strip(" .")
    if len(s) > limit:
        s = s[:limit].rstrip()
    return s or "untitled"


def load_toc():
    """返回 [{entityId, title, path[]}]，path 为从一级分类到父分类的名称列表。

    结果会缓存到 `_source/_toc.json`，供 `--render` 离线复用（避免依赖
    每篇存档里 knowledgeSpecial 的分类树——它与专题目录并不总是一致）。
    """
    data = fetch_json("%s/knowledge-specials/%s" % (API, SPECIAL_ID))
    if data.get("errorCode"):
        raise RuntimeError("目录接口返回错误：%s" % data.get("errorCode"))
    leaves = []

    def walk(nodes, path):
        for c in nodes or []:
            name = (c.get("name") or "").strip()
            kids = c.get("childCategory") or []
            if kids:
                walk(kids, path + [name])
            elif c.get("entityId") and (c.get("entityType") or "") == "Knowledge":
                leaves.append({"entityId": str(c["entityId"]),
                               "title": name or safe_name(str(c["entityId"])),
                               "path": path})

    walk(data.get("categoryList") or [], [])
    os.makedirs(SOURCE_DIR, exist_ok=True)
    json.dump({"specialId": SPECIAL_ID, "items": leaves},
              open(TOC_CACHE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return leaves


def _ts(value):
    """把接口返回的毫秒时间戳转成可读时间；非法值原样返回。"""
    try:
        n = int(str(value)[:13])
        if n < 10 ** 11:
            return str(value)
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n / 1000))
    except (TypeError, ValueError):
        return str(value)


def render_frontmatter(item, art):
    lines = ["---",
             'title: "%s"' % (art.get("title") or item["title"]).replace('"', '\\"'),
             'entityId: "%s"' % item["entityId"],
             'category: "%s"' % " / ".join(item["path"]),
             "productLineId: %d" % PRODUCT_LINE_ID,
             'source: "%s/knowledge/specialDetail/%s?productLineId=%d&lang=zh-CN"'
             % (SITE, SPECIAL_ID, PRODUCT_LINE_ID),
             'knowledgeUrl: "%s/knowledge/%s?productLineId=%d&lang=zh-CN"'
             % (SITE, item["entityId"], PRODUCT_LINE_ID)]
    if art.get("knowledgeCreatedAt"):
        lines.append('createdAt: "%s"' % _ts(art["knowledgeCreatedAt"]))
    if art.get("updatedAt"):
        lines.append('updatedAt: "%s"' % _ts(art["updatedAt"]))
    if art.get("views") is not None:
        lines.append("views: %s" % art["views"])
    lines.append("---")
    return "\n".join(lines)


def load_toc_from_source():
    """不联网：优先读 `_source/_toc.json` 缓存的权威目录。"""
    if os.path.exists(TOC_CACHE):
        data = json.load(open(TOC_CACHE, encoding="utf-8"))
        items = []
        for it in data.get("items") or []:
            items.append({"entityId": str(it["entityId"]),
                          "title": it.get("title") or str(it["entityId"]),
                          "path": it.get("path") or []})
        return items
    return []


def fetch_all(items, force=False, delay=0.35, offline=False):
    os.makedirs(SOURCE_DIR, exist_ok=True)
    stats = {"ok": 0, "skip": 0, "fail": 0, "empty": 0}
    failures = []
    written = []
    used_paths = {}
    for i, item in enumerate(items, 1):
        eid = item["entityId"]
        raw_path = os.path.join(SOURCE_DIR, "%s.json" % eid)
        if os.path.exists(raw_path) and not force:
            art = json.load(open(raw_path, encoding="utf-8"))
            stats["skip"] += 1
        elif offline:
            stats["fail"] += 1
            failures.append((eid, item["title"], "本地无存档（_source/%s.json）" % eid))
            continue
        else:
            try:
                art = fetch_json("%s/special-knowledges/%s" % (API, eid))
            except Exception as exc:  # noqa: BLE001
                stats["fail"] += 1
                failures.append((eid, item["title"], str(exc)))
                print("  [%3d/%d] ✗ %s — %s" % (i, len(items), item["title"], exc))
                continue
            if art.get("errorCode"):
                stats["fail"] += 1
                failures.append((eid, item["title"], "errorCode=%s" % art["errorCode"]))
                print("  [%3d/%d] ✗ %s — errorCode=%s"
                      % (i, len(items), item["title"], art["errorCode"]))
                continue
            json.dump(art, open(raw_path, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            time.sleep(delay)

        title = (art.get("title") or item["title"]).strip()
        body = html_to_markdown(art.get("content") or "",
                                base_url=SITE, image_base=SITE)
        if not body.strip():
            stats["empty"] += 1
            body = "> ⚠️ 原文正文为空或仅含附件，请前往原文查看：%s\n" % (
                "%s/knowledge/%s?productLineId=%d&lang=zh-CN"
                % (SITE, eid, PRODUCT_LINE_ID))

        # 目录：openapi/<分类路径>/<标题>.md；重名时补 entityId 后缀
        sub = [safe_name(p, 40) for p in item["path"]]
        rel_dir = os.path.join(*sub) if sub else ""
        fname = safe_name(title) + ".md"
        rel = os.path.join(rel_dir, fname).replace("\\", "/")
        if rel in used_paths and used_paths[rel] != eid:
            fname = "%s-%s.md" % (safe_name(title), eid)
            rel = os.path.join(rel_dir, fname).replace("\\", "/")
        used_paths[rel] = eid

        out_path = os.path.join(OUT_DIR, *rel.split("/"))
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        doc = "%s\n\n# %s\n\n%s\n" % (render_frontmatter(item, art), title, body)
        open(out_path, "w", encoding="utf-8").write(doc)
        written.append(rel)
        stats["ok"] += 1
        print("  [%3d/%d] ✓ %s  (%d 字符)"
              % (i, len(items), rel, len(body)))

    return stats, failures, written


def prune_stale(keep_rels):
    """删掉不再属于本手册的 .md（目录调整后遗留的旧文件）。"""
    keep = set(os.path.normpath(p) for p in keep_rels)
    removed = 0
    for fp in glob.glob(os.path.join(OUT_DIR, "**", "*.md"), recursive=True):
        rel = os.path.relpath(fp, OUT_DIR).replace("\\", "/")
        if rel.startswith("_source/") or os.path.basename(rel).upper() == "_INDEX.MD":
            continue
        if os.path.normpath(rel) not in keep:
            os.remove(fp)
            removed += 1
    # 清掉空目录
    for root, dirs, files in os.walk(OUT_DIR, topdown=False):
        if root == OUT_DIR or os.path.basename(root) == "_source":
            continue
        if not os.listdir(root):
            os.rmdir(root)
    return removed


def main(argv):
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--force", action="store_true", help="忽略本地存档，全部重抓")
    ap.add_argument("--render", action="store_true",
                    help="不联网，只用 _source/ 里的存档重新渲染 Markdown")
    ap.add_argument("--list", action="store_true", help="只打印目录树，不抓取")
    ap.add_argument("--only", metavar="ENTITY_ID", help="只抓取指定 entityId")
    args = ap.parse_args(argv)

    if args.render:
        items = load_toc_from_source()
        if not items:
            print("!! 找不到目录缓存 %s，请先联网跑一次完整抓取。"
                  % os.path.relpath(TOC_CACHE, ROOT))
            return 1
        print("从本地存档渲染 %d 篇 ..." % len(items))
        stats, failures, written = fetch_all(items, force=False, offline=True)
        gone = prune_stale(written)
        print("\n渲染完成：成功 %d / 失败 %d / 清理过期文件 %d"
              % (stats["ok"], stats["fail"], gone))
        print("接下来请运行：python scripts/build_index.py")
        return 0 if not failures else 1

    print("拉取目录 ...")
    items = load_toc()
    print("共 %d 篇。" % len(items))
    if args.only:
        items = [i for i in items if i["entityId"] == args.only]
        if not items:
            print("!! 目录中没有 entityId=%s" % args.only)
            return 1
    if args.list:
        for it in items:
            print("  %s  %s  %s" % (it["entityId"], " > ".join(it["path"]), it["title"]))
        return 0

    stats, failures, written = fetch_all(items, force=args.force)
    gone = 0 if args.only else prune_stale(written)
    print("\n抓取完成：成功 %d / 跳过(已存在) %d / 空正文 %d / 失败 %d / 清理过期 %d"
          % (stats["ok"], stats["skip"], stats["empty"], stats["fail"], gone))
    print("接下来请运行：python scripts/build_index.py")

    if failures:
        print("\n以下条目抓取失败，请重跑：")
        for eid, title, err in failures:
            print("  %s  %s  — %s" % (eid, title, err))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
