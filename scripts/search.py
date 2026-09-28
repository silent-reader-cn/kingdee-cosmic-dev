#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kingdee-cosmic-dev 统一检索工具
===============================
跨两大内容块按关键词检索，返回命中条目的**完整正文**，无需再打开 .md 文件。

  块一 数据库       references/db/<模块>_files/*.md    （22,769 张表定义）
  块二 OpenAPI 手册  references/openapi/**/*.md         （144 篇开发手册）

设计要点
--------
- **Markdown 是唯一真相源**：本脚本直接读 Markdown，不依赖任何预生成的字典，
  因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- 块一：一张表 = 一个 `## <中文名> t_<表名>` 块，检索精确到「表」而非「文件」。
- 块二：一篇文章 = 一条记录；关键词命中时正文默认**截取命中位置附近的片段**，
  而不是从头截断，避免答案在文末时看不到。
- 表名、中文名、字段名、字段中文标题、备注（含枚举值）、文章标题与分类全部纳入匹配。

用法
----
  python scripts/search.py <关键词...> [选项]

示例
----
  python scripts/search.py 销售订单                              # 全库检索
  python scripts/search.py t_sm_salorder --table --full          # 精确按表名取字段
  python scripts/search.py 凭证 --scope db --category gl         # 只搜总账模块
  python scripts/search.py 自定义API --scope openapi             # 只搜开发手册
  python scripts/search.py 回调 --scope openapi --category 开放事件
  python scripts/search.py 认证 --scope openapi --brief --limit 50
  python scripts/search.py --list                                # 列出全部模块与分类

选项
----
  --scope S      检索范围：db | openapi | all（默认 all）
  --category C   仅块一按模块过滤（如 gl）；仅块二按分类过滤（如 用户手册/常见问题）
  --table        关键词按「表名」精确匹配（忽略大小写与首尾空格，仅块一）
  --brief        精简输出：仅一行摘要
  --full         输出命中条目的完整正文（不截断）
  --all          多个关键词需全部命中（默认任一命中即可）
  --limit N      最多返回结果数（默认 20）
  --max N        非 --full 时每条正文最多展示字符数（默认 1600）
  -d, --detail   同 --full
  --list         列出全部数据库模块与手册分类后退出

说明
----
- 关键词大小写不敏感；中文按子串匹配。
- 结果按相关性分层排序（标题命中优先于正文命中），同级再按出现次数。
- 脚本通过 __file__ 自动定位 references 目录，任意 cwd 下均可运行。
"""
import os
import re
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
REFS = os.path.join(ROOT, "references")

DB_DIR = os.path.join(REFS, "db")
API_DIR = os.path.join(REFS, "openapi")
SCOPE_SUFFIX = "_files"

SCOPE_ALIAS = {
    "db": "db", "database": "db", "数据库": "db", "库表": "db",
    "openapi": "openapi", "api": "openapi", "手册": "openapi",
    "开发手册": "openapi",
}
SCOPE_LABEL = {"db": "数据库", "openapi": "OpenAPI手册"}


# --------------------------------------------------------------------------
# 公共解析
# --------------------------------------------------------------------------

def parse_frontmatter(text):
    """拆出 YAML frontmatter（只做扁平 key: value 解析）与正文。"""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def _split_blocks(text, pattern):
    """按 pattern 切块，返回 [(标题, 正文)]。pattern 需含一个标题捕获组。"""
    parts = re.split(pattern, text)
    out = []
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((title, body))
    return out


def _extract(body, header):
    """抽取 `- **表名：** t_xxx` 形式的字段值。

    注意金蝶文档的冒号在加粗标记**里面**（`**表名：**`），
    所以这里冒号与 `**` 的先后顺序都要兼容。
    """
    m = re.search(r"\*\*%s[：:]?\*\*[：:]*\s*(.+)" % re.escape(header), body)
    return m.group(1).strip().strip("`").strip() if m else ""


def _count_cols(body):
    m = re.search(r"###\s*表格列定义\s*\n(.*?)(?:\n###|\Z)", body, re.S)
    if not m:
        return 0
    return sum(1 for ln in m.group(1).split("\n") if re.match(r"^\|\s*\d+\s*\|", ln))


def _norm_module(folder):
    return folder[:-len(SCOPE_SUFFIX)] if folder.endswith(SCOPE_SUFFIX) else folder


# --------------------------------------------------------------------------
# 块一：数据库
# --------------------------------------------------------------------------

def list_db_modules():
    mods = {}
    if not os.path.isdir(DB_DIR):
        return mods
    for folder in sorted(os.listdir(DB_DIR)):
        full = os.path.join(DB_DIR, folder)
        if os.path.isdir(full) and folder.endswith(SCOPE_SUFFIX):
            mods[_norm_module(folder)] = folder
    return mods


def iter_db(mods, text_filter=None):
    for mod, folder in mods.items():
        for fp in sorted(glob.glob(os.path.join(DB_DIR, folder, "*.md"))):
            name = os.path.basename(fp)
            if name.upper() == "_INDEX.MD":
                continue
            text = open(fp, encoding="utf-8").read()
            if text_filter is not None and not text_filter(text):
                continue
            blocks = _split_blocks(text, r"(?m)^##\s+(.*)$")
            if not blocks:
                continue      # 少数文件只有一行 `# 模块名` 标题（占位文件）
            for title, body in blocks:
                table = _extract(body, "表名")
                cn = _extract(body, "表名称")
                if not table:
                    mt = re.search(r"(t_[A-Za-z0-9_]+)\s*$", title)
                    table = mt.group(1) if mt else ""
                if not cn:
                    cn = re.sub(r"\s*t_[A-Za-z0-9_]+\s*$", "", title).strip()
                yield {"scope": "db", "module": mod,
                       "file": "%s/%s" % (folder, name),
                       "name": "%s\n%s" % (cn, table),
                       "title": table or title, "sub": cn,
                       "meta": "模块: %s   字段数: %d" % (mod, _count_cols(body)),
                       "body": body}


# --------------------------------------------------------------------------
# 块二：OpenAPI 手册
# --------------------------------------------------------------------------

def list_api_categories():
    counts = {}
    if not os.path.isdir(API_DIR):
        return counts
    for fp in glob.glob(os.path.join(API_DIR, "**", "*.md"), recursive=True):
        rel = os.path.relpath(fp, API_DIR).replace("\\", "/")
        if rel.startswith("_source/") or os.path.basename(rel).upper() == "_INDEX.MD":
            continue
        top = rel.split("/")[0] if "/" in rel else "未分类"
        counts[top] = counts.get(top, 0) + 1
    return counts


def iter_openapi(text_filter=None):
    if not os.path.isdir(API_DIR):
        return
    for fp in sorted(glob.glob(os.path.join(API_DIR, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(fp, API_DIR).replace("\\", "/")
        if rel.startswith("_source/") or os.path.basename(rel).upper() == "_INDEX.MD":
            continue
        raw = open(fp, encoding="utf-8").read()
        if text_filter is not None and not text_filter(raw):
            continue
        fm, body = parse_frontmatter(raw)
        title = fm.get("title") or os.path.splitext(os.path.basename(rel))[0]
        cat = fm.get("category") or (rel.split("/")[0] if "/" in rel else "")
        meta = "分类: %s" % (cat or "-")
        if fm.get("updatedAt"):
            meta += "   更新: %s" % fm["updatedAt"][:10]
        yield {"scope": "openapi", "category": cat, "file": rel,
               "name": "%s\n%s" % (title, cat),
               "title": title, "sub": cat, "meta": meta, "body": body,
               "url": fm.get("knowledgeUrl", "")}


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------

def excerpt(body, terms, max_chars):
    """正文超长时，截取**首次命中位置附近**的片段，而不是从头截断。"""
    if len(body) <= max_chars:
        return body
    low = body.lower()
    pos = -1
    for t in terms:
        p = low.find(t.lower())
        if p >= 0 and (pos < 0 or p < pos):
            pos = p
    if pos < 0:
        return body[:max_chars].rstrip() + "\n…(已截断，完整正文请加 --full)"
    start = max(0, pos - max_chars // 3)
    nl = body.rfind("\n", 0, start)
    if nl > 0:
        start = nl + 1
    end = min(len(body), start + max_chars)
    nl2 = body.find("\n", end)
    if nl2 > 0:
        end = nl2
    head = "" if start == 0 else "…(前略)\n"
    tail = "" if end >= len(body) else "\n…(后略，完整正文请加 --full)"
    return head + body[start:end].rstrip() + tail


def render(rec, full, max_chars, terms):
    out = ["▪ %s" % rec["title"]]
    if rec["sub"]:
        out.append("  %s" % rec["sub"])
    out.append("  [%s] %s" % (SCOPE_LABEL[rec["scope"]], rec["file"]))
    if rec["meta"]:
        out.append("  %s" % rec["meta"])
    if rec.get("url"):
        out.append("  原文: %s" % rec["url"])
    body = rec["body"].strip("\n")
    if body:
        view = body if full else excerpt(body, terms, max_chars)
        out.append("\n".join(("  " + l) if l.strip() else "" for l in view.split("\n")))
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------

def main(argv):
    args = list(argv)
    terms, scopes = [], ["all"]
    brief = full = all_match = table_mode = False
    limit, max_chars, category = 20, 1600, None

    i = 0
    while i < len(args):
        a = args[i]
        if a == "--brief":
            brief = True
        elif a == "--full":
            full = True
        elif a in ("-d", "--detail"):
            full = True
        elif a == "--all":
            all_match = True
        elif a == "--table":
            table_mode = True
        elif a == "--list":
            mods = list_db_modules()
            counts = {}
            for rec in iter_db(mods):
                counts[rec["module"]] = counts.get(rec["module"], 0) + 1
            print("【块一 数据库】references/db/ —— %d 个模块 / %d 张表\n"
                  % (len(mods), sum(counts.values())))
            for m in sorted(mods, key=lambda x: -counts.get(x, 0)):
                print("  %-14s %5d 张表   (%s)" % (m, counts.get(m, 0), mods[m]))
            cats = list_api_categories()
            print("\n【块二 OpenAPI 手册】references/openapi/ —— %d 篇 / %d 个分类\n"
                  % (sum(cats.values()), len(cats)))
            for c in sorted(cats, key=lambda x: -cats[x]):
                print("  %-10s %4d 篇" % (c, cats[c]))
            return 0
        elif a == "--scope":
            i += 1
            scopes = [s.strip() for s in args[i].split(",")] if i < len(args) else ["all"]
        elif a == "--category":
            i += 1
            category = args[i].strip() if i < len(args) else None
        elif a == "--limit":
            i += 1
            limit = int(args[i]) if i < len(args) else 20
        elif a == "--max":
            i += 1
            max_chars = int(args[i]) if i < len(args) else 1600
        elif a.startswith("-"):
            pass
        else:
            terms.append(a)
        i += 1

    if not terms:
        print(__doc__)
        return 1

    # 归一化 scope
    if "all" in scopes:
        wanted = ["db", "openapi"]
        scope_txt = "all"
    else:
        wanted, bad = [], []
        for s in scopes:
            k = SCOPE_ALIAS.get(s.lower(), SCOPE_ALIAS.get(s))
            if k:
                wanted.append(k)
            else:
                bad.append(s)
        if bad:
            print("未知范围: %s（可选: db | openapi | all）" % ", ".join(bad))
            return 1
        scope_txt = ",".join(wanted)

    low = [t.lower() for t in terms]
    need_lower = any(any(c.isascii() and c.isalpha() for c in t) for t in terms)

    def make_filter():
        if need_lower:
            if all_match:
                return lambda txt: all(t in txt.lower() for t in low)
            return lambda txt: any(t in txt.lower() for t in low)
        if all_match:
            return lambda txt: all(t in txt for t in terms)
        return lambda txt: any(t in txt for t in terms)

    text_filter = make_filter()
    results = []

    def consider(rec):
        if table_mode and rec["scope"] != "db":
            return
        if category:
            hay_cat = rec.get("module") or rec.get("category") or ""
            if category.lower() not in hay_cat.lower():
                return
        hay = (rec["name"] + "\n" + rec["body"]).lower()
        matched = [(t, hay.count(t.lower())) for t in terms if t.lower() in hay]
        if not matched:
            return
        if all_match and len(matched) < len(terms):
            return
        if table_mode:
            if not any(t.lower().strip() == rec["title"].lower() for t in terms):
                return
            rec["score"] = 1
            results.append(rec)
            return
        name = rec["name"].lower()
        score = sum(c for _, c in matched)
        # 分层加权：标题完全相等 > 标题前缀命中 > 标题包含 > 正文命中
        base = re.split(r"[-—–/]", rec["sub"] or "", maxsplit=1)[0].strip().lower()
        if base and base in low:
            score += 20000
        elif any(name.startswith(t) for t in low):
            score += 5000
        elif any(t in name for t in low):
            score += 2000
        if rec["scope"] == "db" and "主表" in (rec["sub"] or ""):
            score += 800
        rec["score"] = score
        results.append(rec)

    if "db" in wanted:
        mods = list_db_modules()
        if category:
            keep = {m: f for m, f in mods.items()
                    if category.lower() in m.lower()}
            if not keep and wanted == ["db"]:
                print("数据库中没有匹配「%s」的模块。" % category)
            mods = keep
        for rec in iter_db(mods, text_filter):
            consider(rec)
    if "openapi" in wanted:
        for rec in iter_openapi(text_filter):
            consider(rec)

    results.sort(key=lambda r: -r["score"])
    total = len(results)
    results = results[:limit]

    if not results:
        print("未找到匹配「%s」的内容（范围: %s）。" % (" ".join(terms), scope_txt))
        return 0

    if total > len(results):
        print("共找到 %d 条匹配（关键词: %s ；范围: %s），"
              "本次显示前 %d 条，可用 --limit N 调整：\n"
              % (total, " ".join(terms), scope_txt, len(results)))
    else:
        print("找到 %d 条匹配（关键词: %s ；范围: %s）：\n"
              % (total, " ".join(terms), scope_txt))

    if any(r["scope"] == "db" for r in results):
        print("> 表结构来自金蝶云苍穹数据字典导出。写 SQL 前留意：")
        print("> 多语言表以 `_l` 结尾（需过滤 flocaleid）；主子表通过 `fid`/`fentryid` 关联；")
        print("> 备注列常含枚举值定义。目标库 PostgreSQL 12。\n")
    if any(r["scope"] == "openapi" for r in results):
        print("> 手册内容抓取自金蝶云社区「OpenAPI（开放平台）」专题，")
        print("> 原文链接见每条结果的「原文」行。\n")

    for r in results:
        if brief:
            print("[%s] %s | %s | %s"
                  % (r["scope"], r["title"], r["sub"] or "-", r["file"]))
        else:
            print(render(r, full, max_chars, terms))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
