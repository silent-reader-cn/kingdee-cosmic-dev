#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kingdee-sql-expert 统一检索工具
===============================
在全部模块的库表文档中按关键词检索，返回命中**表定义的完整正文**（含字段表），
无需再逐个打开 .md 文件。

  数据源  references/<模块>_files/*.md
          224 个模块文件夹 / 8,606 个文件 / 22,769 张表定义

设计要点
--------
- **Markdown 是唯一真相源**：本脚本直接读 Markdown，不依赖任何预生成的字典，
  因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- 一张表 = 一个 `## <中文名> t_<表名>` 块；同名的多语言表（`_l` 后缀）、
  主子表分录会被拆成独立条目，因此检索结果精确到「表」而不是「文件」。
- 表名、中文名、字段名、字段中文标题、备注（含枚举值定义）全部纳入匹配范围。

用法
----
  python scripts/search.py <关键词...> [选项]

示例
----
  python scripts/search.py 销售订单                              # 全模块检索
  python scripts/search.py t_sal_order --table                   # 精确按表名定位
  python scripts/search.py 凭证 --scope gl                       # 只搜总账模块
  python scripts/search.py 物料 库存 --scope inv --all           # 多词全命中
  python scripts/search.py 枚举 --brief --limit 50               # 只要一行摘要
  python scripts/search.py t_sal_order --full                    # 完整字段定义
  python scripts/search.py --list-modules                        # 列出全部模块

选项
----
  --scope S      检索范围，模块名可逗号组合（如 gl,som,inv）；默认 all 全模块
                 模块名即 references/ 下的文件夹名去掉 `_files` 后缀
  --table        关键词按「表名」精确匹配（忽略大小写与首尾空格）
  --brief        精简输出：仅一行 `[模块] 表名 | 中文名 | 文件`
  --full         输出命中条目的完整正文（不截断）
  --all          多个关键词需全部命中（默认任一命中即可）
  --limit N      最多返回结果数（默认 20）
  --max N        非 --full 时每条正文最多展示字符数（默认 1600）
  -d, --detail   同 --full
  --list-modules 列出全部模块及各自的表数量后退出

说明
----
- 关键词大小写不敏感；中文按子串匹配。
- 结果按命中次数降序排列。
- 脚本通过 __file__ 自动定位 references 目录，任意 cwd 下均可运行。
"""
import os
import re
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
REFS = os.path.join(ROOT, "references")

SCOPE_SUFFIX = "_files"


# --------------------------------------------------------------------------
# 解析：每个 `## <中文名> t_<表名>` 块产出一条记录
# --------------------------------------------------------------------------

def _norm_module(folder):
    """`gl_files` -> `gl`"""
    return folder[:-len(SCOPE_SUFFIX)] if folder.endswith(SCOPE_SUFFIX) else folder


def list_modules():
    """返回 {模块名: 文件夹名}，模块名已去掉 `_files` 后缀。"""
    mods = {}
    for folder in sorted(os.listdir(REFS)):
        full = os.path.join(REFS, folder)
        if os.path.isdir(full) and folder.endswith(SCOPE_SUFFIX):
            mods[_norm_module(folder)] = folder
    return mods


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
    """抽取 `- **表名：** xxx` 形式的字段值。"""
    m = re.search(r"\*\*%s\*\*\s*[:：]\s*(.+)" % re.escape(header), body)
    return m.group(1).strip().strip("`").strip() if m else ""


def _count_cols(body):
    """统计「表格列定义」小节里的数据行数（序号列）。"""
    m = re.search(r"###\s*表格列定义\s*\n(.*?)(?:\n###|\Z)", body, re.S)
    if not m:
        return 0
    return sum(1 for ln in m.group(1).split("\n") if re.match(r"^\|\s*\d+\s*\|", ln))


def iter_tables(mods, text_filter=None):
    """遍历指定模块下的全部表定义。mods 为 {模块名: 文件夹名}。

    text_filter 为可选的**文件级预筛**：整篇文本不含关键词的文件直接跳过，
    不进入逐块正则解析。实测可把全模块检索从约 3.3s 降到 1s 量级。
    """
    for mod, folder in mods.items():
        pattern = os.path.join(REFS, folder, "*.md")
        for fp in sorted(glob.glob(pattern)):
            name = os.path.basename(fp)
            if name.upper() == "_INDEX.MD":
                continue
            text = open(fp, encoding="utf-8").read()
            if text_filter is not None and not text_filter(text):
                continue
            blocks = _split_blocks(text, r"(?m)^##\s+(.*)$")
            if not blocks:
                # 少数文件只有一行 `# 模块名` 标题、没有表定义（占位/概述文件），跳过
                continue
            for title, body in blocks:
                table = _extract(body, "表名")
                cn = _extract(body, "表名称")
                if not table:
                    mt = re.search(r"(t_[A-Za-z0-9_]+)\s*$", title)
                    table = mt.group(1) if mt else ""
                if not cn:
                    cn = re.sub(r"\s*t_[A-Za-z0-9_]+\s*$", "", title).strip()
                yield {
                    "scope": mod,
                    "folder": folder,
                    "file": "%s/%s" % (folder, name),
                    "table": table,
                    "cn": cn,
                    "title": title,
                    "ncol": _count_cols(body),
                    "body": body,
                }


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------

def render(rec, full, max_chars):
    out = []
    out.append("▪ %s" % (rec["table"] or rec["title"]))
    if rec["cn"]:
        out.append("  中文名: %s" % rec["cn"])
    out.append("  [模块: %s] %s   字段数: %d" % (rec["scope"], rec["file"], rec["ncol"]))
    body = rec["body"].strip("\n")
    if body.strip():
        if not full and len(body) > max_chars:
            view = body[:max_chars].rstrip() + \
                "\n  …(已截断，完整字段定义请加 --full 或打开 references/%s)" % rec["file"]
        else:
            view = body
        out.append("\n".join(("  " + l) if l.strip() else "" for l in view.split("\n")))
    out.append("")
    return "\n".join(out)


def main(argv):
    args = list(argv)
    terms, scopes = [], ["all"]
    brief = full = all_match = table_mode = False
    limit, max_chars = 20, 1600

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
        elif a == "--list-modules":
            mods = list_modules()
            counts = {}
            for rec in iter_tables(mods):
                counts[rec["scope"]] = counts.get(rec["scope"], 0) + 1
            print("共 %d 个模块 / %d 张表：\n" % (len(mods), sum(counts.values())))
            for mod in sorted(mods, key=lambda m: -counts.get(m, 0)):
                print("  %-14s %5d 张表   (%s)" % (mod, counts.get(mod, 0), mods[mod]))
            return 0
        elif a == "--scope":
            i += 1
            scopes = [s.strip() for s in args[i].split(",")] if i < len(args) else ["all"]
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

    all_mods = list_modules()
    if "all" in scopes:
        mods = all_mods
        scope_txt = "all(%d模块)" % len(all_mods)
    else:
        scopes = [_norm_module(s) for s in scopes]
        bad = [s for s in scopes if s not in all_mods]
        if bad:
            print("未知模块: %s" % ", ".join(bad))
            print("可用模块见 `python scripts/search.py --list-modules`。")
            return 1
        mods = {s: all_mods[s] for s in scopes}
        scope_txt = ",".join(scopes)

    results = []
    low = [t.lower() for t in terms]
    # 纯中文关键词无需 lower()，省掉对 40MB 语料的大小写折叠
    need_lower = any(any(c.isascii() and c.isalpha() for c in t) for t in terms)
    if need_lower:
        if all_match:
            def text_filter(txt):
                low_txt = txt.lower()
                return all(t in low_txt for t in low)
        else:
            def text_filter(txt):
                low_txt = txt.lower()
                return any(t in low_txt for t in low)
    else:
        if all_match:
            def text_filter(txt):
                return all(t in txt for t in terms)
        else:
            def text_filter(txt):
                return any(t in txt for t in terms)
    for rec in iter_tables(mods, text_filter):
        if table_mode:
            key = rec["table"].lower()
            if not any(t.lower().strip() == key for t in terms):
                continue
            rec["score"] = 1
            results.append(rec)
            continue
        hay = (rec["table"] + "\n" + rec["cn"] + "\n" + rec["title"] +
               "\n" + rec["body"]).lower()
        matched = [(t, hay.count(t.lower())) for t in terms if t.lower() in hay]
        if not matched:
            continue
        if all_match and len(matched) < len(terms):
            continue
        # 相关性分层：表名/中文名命中优先于正文命中，主表优先于子表，
        # 最后才按正文出现次数排序。否则「销售订单」会被大量引用该词的分录表淹没。
        name = (rec["cn"] + "\n" + rec["table"]).lower()
        score = sum(c for _, c in matched)
        # 中文名去掉「-主表/-子表」等后缀后与关键词完全相等 → 最优先
        base_cn = re.split(r"[-—–]", rec["cn"], 1)[0].strip().lower()
        if base_cn and base_cn in [t.lower() for t in terms]:
            score += 20000
        elif any(name.startswith(t.lower()) for t in terms):
            score += 5000
        elif any(t.lower() in name for t in terms):
            score += 2000
        if "主表" in rec["cn"]:
            score += 800
        rec["score"] = score
        results.append(rec)

    results.sort(key=lambda r: -r["score"])
    total = len(results)
    results = results[:limit]

    if not results:
        print("未找到匹配「%s」的表（范围: %s）。" % (" ".join(terms), scope_txt))
        return 0

    # 必须区分「总命中数」与「本次显示数」，否则用户会误以为只有这么多条
    if total > len(results):
        print("共找到 %d 条匹配（关键词: %s ；范围: %s），"
              "本次显示前 %d 条，可用 --limit N 调整：\n"
              % (total, " ".join(terms), scope_txt, len(results)))
    else:
        print("找到 %d 条匹配（关键词: %s ；范围: %s）：\n"
              % (total, " ".join(terms), scope_txt))

    print("> 表结构来自金蝶云苍穹数据字典导出，字段定义与其一致。")
    print("> 写 SQL 前请留意：多语言表以 `_l` 结尾（需过滤 flocaleid）；")
    print("> 主子表通过 `fid`/`fentryid` 关联；备注列常含枚举值定义。\n")
    for r in results:
        if brief:
            print("[%s] %s | %s | %s" % (r["scope"], r["table"] or r["title"],
                                         r["cn"] or "-", r["file"]))
        else:
            print(render(r, full, max_chars))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
