#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kingdee-cosmic-dev 索引构建工具
===============================
从 Markdown 反向生成人类可读的 `_INDEX.md` 索引。

设计原则：**Markdown 是唯一真相源**。索引只由本脚本从 Markdown 派生，
不手工维护，因此永远不会与正文脱节。修改任何文档后重跑本脚本即可。

生成的索引：
  references/_INDEX.md                        总索引（两块概览 + 入口）
  references/db/_INDEX.md                     数据库：224 个模块统计概览
  references/db/<模块>_files/_INDEX.md        数据库：各模块表清单
  references/openapi/_INDEX.md                OpenAPI 手册：分类目录

用法:
    python scripts/build_index.py                 # 全量重建
    python scripts/build_index.py gl som          # 只重建指定数据库模块
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import search  # noqa: E402

ROOT = search.ROOT
REFS = search.REFS
DB_DIR = search.DB_DIR
API_DIR = search.API_DIR


def write(path, lines):
    open(path, "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
    print("  已生成 %s" % os.path.relpath(path, ROOT).replace("\\", "/"))


def _count_files(folder):
    return len([f for f in os.listdir(folder)
                if f.lower().endswith(".md") and f.upper() != "_INDEX.MD"])


# ------------------------------------------------------------ 块一 数据库

def collect_db(mods):
    buckets = {m: [] for m in mods}
    for rec in search.iter_db(mods):
        buckets[rec["module"]].append(rec)
    for m in buckets:
        buckets[m].sort(key=lambda r: (r["title"], r["file"]))
    return buckets


def build_module_index(mod, folder, recs):
    L = ["# %s 模块表清单" % mod, "",
         "> 本模块共收录 **%d** 张表定义，来自 `%s/`。" % (len(recs), folder), "",
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。",
         "> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：",
         "> ```bash",
         "> python scripts/search.py <关键词> --scope db --category %s" % mod,
         "> ```",
         "",
         "| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |",
         "| :---: | :--- | :--- | :---: | :--- |"]
    for i, r in enumerate(recs, 1):
        L.append("| %d | `%s` | %s | %s | [%s](./%s) |"
                 % (i, r["title"] or "-", r["sub"] or "-",
                    r["meta"].split("字段数: ")[-1], os.path.basename(r["file"]),
                    os.path.basename(r["file"])))
    write(os.path.join(DB_DIR, folder, "_INDEX.md"), L)


def build_db_index(buckets, mods):
    total = sum(len(v) for v in buckets.values())
    nfile = sum(_count_files(os.path.join(DB_DIR, mods[m])) for m in mods)
    rows = sorted(((m, len(buckets[m]), _count_files(os.path.join(DB_DIR, mods[m])))
                   for m in mods), key=lambda x: (-x[1], x[0]))
    L = ["# 金蝶云苍穹库表总索引", "",
         "> 共收录 **%d** 张表定义，分布在 **%d** 个模块 / **%d** 个 Markdown 文件中。"
         % (total, len(mods), nfile),
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。", "",
         "> 检索表结构请优先用统一检索脚本（比翻本文件快得多）：",
         "> ```bash",
         "> python scripts/search.py 销售订单                        # 全库关键词检索",
         "> python scripts/search.py t_sm_salorder --table --full    # 按表名精确定位",
         "> python scripts/search.py 凭证 --scope db --category gl   # 只看总账模块",
         "> python scripts/search.py --list                          # 列出全部模块",
         "> ```", "",
         "> [!TIP]",
         "> 写 SQL 前留意金蝶约定：多语言表以 `_l` 结尾（关联时需过滤 `flocaleid`）；",
         "> 主子表通过 `fid` / `fentryid` 关联；备注列常含枚举值定义（如 `A: 暂存, B: 已提交`）。",
         "> 目标库为 **PostgreSQL 12**。",
         "",
         "## 模块统计概览", "",
         "| 序号 | 模块 | 表数量 | 文件数 | 模块索引 |",
         "| :---: | :--- | ---: | ---: | :--- |"]
    for i, (m, nt, nf) in enumerate(rows, 1):
        L.append("| %d | `%s` | **%d** | %d | [%s/_INDEX.md](./%s/_INDEX.md) |"
                 % (i, m, nt, nf, mods[m], mods[m]))
    L.append("| **合计** | **%d 个模块** | **%d** | **%d** | - |"
             % (len(mods), total, nfile))
    L.append("")
    write(os.path.join(DB_DIR, "_INDEX.md"), L)
    return total, nfile, len(mods)


# -------------------------------------------------------- 块二 OpenAPI 手册

def collect_api():
    rows = []
    for rec in search.iter_openapi():
        rows.append(rec)
    return rows


def build_api_index(rows):
    groups = {}
    for r in rows:
        top = r["file"].split("/")[0] if "/" in r["file"] else "未分类"
        groups.setdefault(top, []).append(r)
    total = len(rows)
    L = ["# 金蝶云苍穹 OpenAPI（开放平台）手册总索引", "",
         "> 共 **%d** 篇，覆盖 **%d** 个一级分类。内容抓取自金蝶云社区专题"
         "「OpenAPI（开放平台）」。" % (total, len(groups)),
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。", "",
         "> 检索请用统一检索脚本（比翻本文件快）：",
         "> ```bash",
         "> python scripts/search.py 自定义API --scope openapi",
         "> python scripts/search.py 认证 --scope openapi --brief",
         "> python scripts/search.py 回调 --scope openapi --category 开放事件",
         "> ```", "",
         "## 分类统计", "",
         "| 序号 | 一级分类 | 篇数 |", "| :---: | :--- | ---: |"]
    order = sorted(groups, key=lambda k: (-len(groups[k]), k))
    for i, top in enumerate(order, 1):
        L.append("| %d | [%s](#%s) | **%d** |" % (i, top, top, len(groups[top])))
    L.append("| **合计** | **%d 个分类** | **%d** |" % (len(groups), total))
    L.append("")
    L.append("---")
    L.append("")
    for top in order:
        L.append("## %s" % top)
        L.append("")
        L.append("> 共 `%d` 篇。" % len(groups[top]))
        L.append("")
        L.append("| 序号 | 标题 | 二级分类 | 更新日期 | 文件 |")
        L.append("| :---: | :--- | :--- | :--- | :--- |")
        for i, r in enumerate(sorted(groups[top], key=lambda x: x["file"]), 1):
            parts = r["file"].split("/")
            sub = parts[1] if len(parts) > 2 else "-"
            upd = ""
            if "更新: " in r["meta"]:
                upd = r["meta"].split("更新: ")[-1]
            L.append("| %d | %s | %s | %s | [%s](./%s) |"
                     % (i, r["title"], sub, upd, os.path.basename(r["file"]), r["file"]))
        L.append("")
    write(os.path.join(API_DIR, "_INDEX.md"), L)
    return total, len(groups)


# ------------------------------------------------------------------ 总索引

def build_root_index(db_stats, api_stats):
    n_tab, n_dbfile, n_mod = db_stats
    n_art, n_cat = api_stats
    L = ["# 金蝶云苍穹开发知识库 · 总索引", "",
         "本知识库由两大块构成，**全部内容可用同一个检索脚本定位**：", "",
         "| 块 | 内容 | 规模 | 入口 |",
         "| :--- | :--- | :--- | :--- |",
         "| **块一 数据库** | 全量物理表结构（字段/列规则/索引） | %d 张表 / %d 模块 | [db/_INDEX.md](./db/_INDEX.md) |"
         % (n_tab, n_mod),
         "| **块二 OpenAPI 手册** | 金蝶云社区开放平台官方手册 | %d 篇 / %d 分类 | [openapi/_INDEX.md](./openapi/_INDEX.md) |"
         % (n_art, n_cat), "",
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。", "",
         "## 检索", "",
         "```bash",
         "python scripts/search.py 销售订单                            # 全库检索",
         "python scripts/search.py t_sm_salorder --table --full        # 精确取表字段",
         "python scripts/search.py 自定义API --scope openapi           # 只搜开发手册",
         "python scripts/search.py 回调 --scope openapi --category 开放事件",
         "python scripts/search.py --list                              # 列出模块与分类",
         "```", "",
         "## 块一 数据库 · 模块概览", "",
         "| 序号 | 模块 | 表数量 | 模块索引 |", "| :---: | :--- | ---: | :--- |"]
    db = search.list_db_modules()
    buckets = {m: 0 for m in db}
    for rec in search.iter_db(db):
        buckets[rec["module"]] += 1
    for i, m in enumerate(sorted(db, key=lambda x: (-buckets[x], x))[:40], 1):
        L.append("| %d | `%s` | %d | [%s/_INDEX.md](./db/%s/_INDEX.md) |"
                 % (i, m, buckets[m], db[m], db[m]))
    L.append("| … | 其余 %d 个模块 | | 见 [db/_INDEX.md](./db/_INDEX.md) |"
             % max(0, len(db) - 40))
    L.append("")
    L.append("## 块二 OpenAPI 手册 · 分类概览")
    L.append("")
    L.append("| 序号 | 一级分类 | 篇数 |")
    L.append("| :---: | :--- | ---: |")
    cats = search.list_api_categories()
    for i, c in enumerate(sorted(cats, key=lambda x: (-cats[x], x)), 1):
        L.append("| %d | [%s](./openapi/_INDEX.md#%s) | %d |" % (i, c, c, cats[c]))
    L.append("")
    write(os.path.join(REFS, "_INDEX.md"), L)


def main(argv):
    if not os.path.isdir(REFS):
        print("!! 找不到 references 目录: %s" % REFS)
        return 1
    all_mods = search.list_db_modules()
    if argv:
        want = [search._norm_module(a) for a in argv]
        bad = [m for m in want if m not in all_mods]
        if bad:
            print("!! 未知模块: %s" % ", ".join(bad))
            return 1
        mods = {m: all_mods[m] for m in want}
        print("开始重建 %d 个模块的索引（源: Markdown）..." % len(mods))
    else:
        mods = all_mods
        print("开始重建全部索引（源: Markdown，%d 个数据库模块）..." % len(mods))

    buckets = collect_db(mods)
    for m, folder in mods.items():
        build_module_index(m, folder, buckets[m])
    db_stats = build_db_index(buckets, mods)
    print("     块一 数据库: %d 张表 / %d 个模块 / %d 个文件"
          % (db_stats[0], db_stats[2], db_stats[1]))

    if not argv:
        api_rows = collect_api()
        api_stats = build_api_index(api_rows)
        print("     块二 OpenAPI 手册: %d 篇 / %d 个分类" % api_stats)
        build_root_index(db_stats, api_stats)
    print("完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
