#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kingdee-sql-expert 索引构建工具
===============================
从 Markdown 反向生成人类可读的 `_INDEX.md` 索引。

设计原则：**Markdown 是唯一真相源**。索引只由本脚本从 Markdown 派生，
不手工维护，因此永远不会与正文脱节。修改任何表文档后重跑本脚本即可。

生成的索引：
  references/_INDEX.md                  模块统计概览（224 个模块）
  references/<模块>_files/_INDEX.md     该模块的表清单（表名 / 中文名 / 字段数 / 文件）

用法:
    python scripts/build_index.py            # 全量重建
    python scripts/build_index.py gl som     # 只重建指定模块（含总索引）
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import search  # noqa: E402

ROOT = search.ROOT
REFS = search.REFS


def write(path, lines):
    open(path, "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
    print("  已生成 %s" % os.path.relpath(path, ROOT).replace("\\", "/"))


def collect(mods):
    """返回 {模块名: [记录...]}，记录按表名排序。"""
    buckets = {m: [] for m in mods}
    for rec in search.iter_tables(mods):
        buckets[rec["scope"]].append(rec)
    for m in buckets:
        buckets[m].sort(key=lambda r: (r["table"], r["file"]))
    return buckets


def build_module_index(mod, folder, recs):
    L = ["# %s 模块表清单" % mod, "",
         "> 本模块共收录 **%d** 张表定义，来自 `%s/`。" % (len(recs), folder), "",
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。",
         "> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：",
         "> ```bash",
         "> python scripts/search.py <关键词> --scope %s" % mod,
         "> ```",
         "",
         "| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |",
         "| :---: | :--- | :--- | :---: | :--- |"]
    for i, r in enumerate(recs, 1):
        L.append("| %d | `%s` | %s | %d | [%s](./%s) |"
                 % (i, r["table"] or "-", r["cn"] or "-", r["ncol"],
                    os.path.basename(r["file"]), os.path.basename(r["file"])))
    write(os.path.join(REFS, folder, "_INDEX.md"), L)


def build_root_index(buckets, mods):
    total = sum(len(v) for v in buckets.values())
    nfile = sum(len([f for f in os.listdir(os.path.join(REFS, mods[m]))
                     if f.lower().endswith(".md") and f.upper() != "_INDEX.MD"])
                for m in mods)
    L = ["# 金蝶云苍穹库表总索引", "",
         "> 共收录 **%d** 张表定义，分布在 **%d** 个模块 / **%d** 个 Markdown 文件中。"
         % (total, len(mods), nfile),
         "> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。", "",
         "> 检索表结构请优先用统一检索脚本（比翻本文件快得多）：",
         "> ```bash",
         "> python scripts/search.py 销售订单                  # 全模块关键词检索",
         "> python scripts/search.py t_sm_salorder --table     # 按表名精确定位",
         "> python scripts/search.py 凭证 --scope gl --brief   # 只看总账模块摘要",
         "> python scripts/search.py --list-modules            # 列出全部模块",
         "> ```", "",
         "> [!TIP]",
         "> 写 SQL 前留意金蝶约定：多语言表以 `_l` 结尾（关联时需过滤 `flocaleid`）；",
         "> 主子表通过 `fid` / `fentryid` 关联；备注列常含枚举值定义（如 `A: 暂存, B: 已提交`）。",
         "> 目标库为 **PostgreSQL 12**。",
         "",
         "## 模块统计概览", "",
         "| 序号 | 模块 | 表数量 | 文件数 | 模块索引 |",
         "| :---: | :--- | ---: | ---: | :--- |"]
    rows = []
    for m in mods:
        nf = len([f for f in os.listdir(os.path.join(REFS, mods[m]))
                  if f.lower().endswith(".md") and f.upper() != "_INDEX.MD"])
        rows.append((m, len(buckets[m]), nf))
    rows.sort(key=lambda x: (-x[1], x[0]))
    for i, (m, nt, nf) in enumerate(rows, 1):
        L.append("| %d | `%s` | **%d** | %d | [%s/%s](./%s/_INDEX.md) |"
                 % (i, m, nt, nf, mods[m], "_INDEX.md", mods[m]))
    L.append("| **合计** | **%d 个模块** | **%d** | **%d** | - |" % (len(mods), total, nfile))
    L.append("")
    write(os.path.join(REFS, "_INDEX.md"), L)
    return total, nfile


def main(argv):
    if not os.path.isdir(REFS):
        print("!! 找不到 references 目录: %s" % REFS)
        return 1
    all_mods = search.list_modules()
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
        print("开始重建全部索引（源: Markdown，%d 个模块）..." % len(mods))

    buckets = collect(mods)
    for m, folder in mods.items():
        build_module_index(m, folder, buckets[m])
    if not argv:
        total, nfile = build_root_index(buckets, mods)
        print("     合计: %d 张表 / %d 个模块 / %d 个文件" % (total, len(mods), nfile))
    print("完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
