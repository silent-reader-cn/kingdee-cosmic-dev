#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_db_from_dict —— 把金蝶云苍穹「数据字典导出」转成 Markdown 表结构文档
==========================================================================
输入：官方导出的 HTML 包（.zip）或已解压目录，结构为

    <root>/<模块>_files/<对象>.html
    <root>/index.html, cloud.js, tailwind.css, images/ ...   ← 忽略

每个 .html 的正文结构（机器生成，高度规整）：

    <h2 id='title'>凭证-gl_voucher</h2>
    <div id='main'>
      <div class="tbl …">                        ← 一张表，一个块
        <h3 class="tbl-s-h">凭证-主表 t_gl_voucher</h3>
        <dt>表名称：</dt><dd>凭证-主表</dd>
        <dt>表名：</dt><dd>t_gl_voucher</dd>
        <div …><h3 class="tbl-c-h">…- 表格列定义</h3> <table>…</table></div>
        <div …><h3 class="tbl-c-h">…- 列规则定义</h3> <table>…</table></div>
        <div …><h3 class="tbl-c-h">…- 索引定义</h3>   <table>…</table></div>
      </div>
      … 下一张表 …
    </div>

输出：<out>/<模块>_files/<对象>.md，格式与本仓库既有语料一致：

    # 凭证-gl_voucher

    ## 凭证-主表 t_gl_voucher

    - **表名称：** 凭证-主表
    - **表名：** t_gl_voucher

    ### 表格列定义
    | 序号 | 列标题 | … |
    | :--- | :--- | … |
    …

单元格里指向其它表的 `<a href="..\\base_files\\bos_org.html">业务单元 bos_org</a>`
会转成 Markdown 链接 `[业务单元 bos_org](../base_files/bos_org.md)`，方便顺藤摸瓜。

用法：
    python tools/build_db_from_dict.py <zip 或解压目录> [选项]

选项：
    --out DIR       输出目录（默认 references/db）
    --list          只统计不写文件
    --keep-stale    保留输出目录里不属于本次导出的旧 .md（默认删除）
    --limit N       只处理前 N 个文件（调试用）
"""
import argparse
import html as _html
import os
import re
import sys
import time
import zipfile
from collections import Counter
from html.parser import HTMLParser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
DEFAULT_OUT = os.path.join(ROOT, "references", "db")

SECTIONS = ("表格列定义", "列规则定义", "索引定义")
SKIP_TAGS = {"script", "style"}


# --------------------------------------------------------------------------
# 解析器
# --------------------------------------------------------------------------

class Table:
    __slots__ = ("heading", "cn", "name", "sections")

    def __init__(self):
        self.heading = ""
        self.cn = ""
        self.name = ""
        self.sections = {}      # 小节名 -> (表头 list, 数据行 list[list])


class DictParser(HTMLParser):
    """流式解析数据字典 HTML，产出 page_title 与 tables。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.page_title = ""
        self.tables = []
        self.warnings = []

        self._div_stack = []
        self._cur = None            # 当前 Table
        self._section = None        # 当前小节名
        self._skip = 0

        self._buf = []              # 通用文本缓冲
        self._h3_kind = None
        self._in_title_h2 = False
        self._pending_dt = None
        self._dd_target = None

        self._in_thead = False
        self._head = None
        self._rows = None
        self._row = None
        self._cell = None
        self._cell_href = None

    # ---------- 基础 ----------
    def _text(self):
        return re.sub(r"\s+", " ", "".join(self._buf)).strip()

    @staticmethod
    def _cls(attrs):
        d = dict(attrs)
        return (d.get("class") or "").strip()

    # ---------- 标签 ----------
    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self._skip += 1
            return
        if self._skip:
            return
        a = dict(attrs)
        cls = (a.get("class") or "").strip()

        if tag == "h2" and a.get("id") == "title":
            self._in_title_h2 = True
            self._buf = []
            return
        if tag == "div":
            self._div_stack.append(cls)
            if cls.startswith("tbl ") or cls == "tbl":
                # 新的一张表
                self._cur = Table()
                self._section = None
                self.tables.append(self._cur)
            return
        if tag == "h3":
            if "tbl-s-h" in cls:
                self._h3_kind = "s"
            elif "tbl-c-h" in cls:
                self._h3_kind = "c"
            else:
                self._h3_kind = None
            self._buf = []
            return
        if tag == "dt":
            self._buf = []
            self._pending_dt = ""
            return
        if tag == "dd":
            self._buf = []
            self._dd_target = None
            return
        if tag == "table":
            self._rows = []
            self._head = None
            return
        if tag == "thead":
            self._in_thead = True
            return
        if tag == "tbody":
            self._in_thead = False
            return
        if tag == "tr":
            self._row = []
            return
        if tag in ("td", "th"):
            self._cell = []
            self._cell_href = None
            return
        if tag == "a" and self._cell is not None:
            self._cell_href = a.get("href") or None
            return

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return

        if tag == "h2" and self._in_title_h2:
            self._in_title_h2 = False
            self.page_title = self._text()
            self._buf = []
            return
        if tag == "div":
            if not self._div_stack:
                return
            popped = self._div_stack.pop()
            if (popped.startswith("tbl ") or popped == "tbl") and self._cur:
                self._finish_table()
            return
        if tag == "h3":
            if self._h3_kind == "s" and self._cur:
                self._cur.heading = self._text()
            elif self._h3_kind == "c":
                t = self._text()
                sec = t.rsplit("-", 1)[-1].strip()
                self._section = sec if sec in SECTIONS else None
            self._h3_kind = None
            self._buf = []
            return
        if tag == "dt":
            self._pending_dt = self._text()
            self._buf = []
            return
        if tag == "dd":
            val = self._text()
            if self._cur and self._pending_dt:
                if "表名称" in self._pending_dt:
                    self._cur.cn = val
                elif "表名" in self._pending_dt:
                    self._cur.name = val
            self._pending_dt = None
            self._buf = []
            return
        if tag == "table":
            if self._cur is not None and self._section:
                self._cur.sections[self._section] = (self._head or [], self._rows or [])
            self._rows = None
            self._head = None
            return
        if tag == "thead":
            self._in_thead = False
            return
        if tag == "tr":
            if self._row is not None:
                if self._in_thead:
                    self._head = self._row
                elif self._rows is not None:
                    self._rows.append(self._row)
            self._row = None
            return
        if tag in ("td", "th"):
            if self._row is not None:
                txt = re.sub(r"\s+", " ", "".join(self._cell or [])).strip()
                if self._cell_href:
                    href = self._cell_href.replace("\\", "/")
                    if href.endswith(".html") and txt:
                        txt = "[%s](%s)" % (txt, href[:-5] + ".md")
                self._row.append(txt.replace("|", "\\|"))
            self._cell = None
            self._cell_href = None
            return

    def handle_data(self, data):
        if self._skip:
            return
        if (self._in_title_h2 or self._h3_kind or self._pending_dt is not None
                or self._cell is not None):
            self._buf.append(data)
            if self._cell is not None:
                self._cell.append(data)

    # ---------- 收尾 ----------
    def _finish_table(self):
        t = self._cur
        self._cur = None
        if not t:
            return
        if not t.name:
            m = re.search(r"(\S+)\s*$", t.heading or "")
            if m:
                t.name = m.group(1)
        if not t.cn and t.heading:
            t.cn = re.sub(r"\s+\S+$", "", t.heading).strip()
        if not t.name:
            self.warnings.append("表块缺少表名：%r" % (t.heading or "?"))
        missing = [s for s in SECTIONS if s not in t.sections]
        if missing:
            self.warnings.append("%s 缺少小节：%s" % (t.name or t.heading, ",".join(missing)))


def parse_html(text):
    p = DictParser()
    p.feed(text)
    p.close()
    if p._cur:                 # 容错：HTML 未闭合时也要收尾
        p._finish_table()
    return p


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------

def render(page_title, tables):
    out = ["# %s" % (page_title or "").strip(), ""]
    for i, t in enumerate(tables):
        if i:
            out += ["---", ""]
        head_line = ("%s %s" % (t.cn, t.name)).strip()
        out.append("## %s" % head_line)
        out.append("")
        out.append("- **表名称：** %s" % (t.cn or "-"))
        out.append("- **表名：** %s" % (t.name or "-"))
        out.append("")
        for sec in SECTIONS:
            got = t.sections.get(sec)
            if not got:
                continue
            head, rows = got
            if not head:
                continue
            out.append("### %s" % sec)
            out.append("")
            out.append("| " + " | ".join(head) + " |")
            out.append("| " + " | ".join([":---"] * len(head)) + " |")
            for r in rows:
                cells = list(r) + [""] * (len(head) - len(r))
                out.append("| " + " | ".join(cells[:len(head)]) + " |")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------
# 输入源
# --------------------------------------------------------------------------

def iter_source(src, limit=None):
    """产出 (相对路径, 读文本的函数)。src 为 zip 或解压目录。"""
    if os.path.isdir(src):
        root = src
        subs = [d for d in os.listdir(root) if d.endswith("_files")
                and os.path.isdir(os.path.join(root, d))]
        if not subs:                     # 传进来的可能就是 <root>
            items = []
            for dirpath, _, files in os.walk(root):
                for f in files:
                    if f.endswith(".html"):
                        full = os.path.join(dirpath, f)
                        items.append((os.path.relpath(full, root).replace("\\", "/"), full))
            items.sort()
            for i, (rel, full) in enumerate(items):
                if limit and i >= limit:
                    break
                yield rel, (lambda p: lambda: open(p, encoding="utf-8", errors="replace").read())(full)
            return
        items = []
        for d in sorted(subs):
            for f in sorted(os.listdir(os.path.join(root, d))):
                if f.endswith(".html"):
                    rel = "%s/%s" % (d, f)
                    items.append((rel, os.path.join(root, d, f)))
        for i, (rel, full) in enumerate(items):
            if limit and i >= limit:
                break
            yield rel, (lambda p: lambda: open(p, encoding="utf-8", errors="replace").read())(full)
        return

    z = zipfile.ZipFile(src)
    names = [n for n in z.namelist()
             if n.lower().endswith(".html") and "/" in n.rstrip("/")]
    # 找公共根目录：取第一层目录名
    roots = {n.split("/")[0] for n in names}
    if len(roots) == 1:
        root = roots.pop() + "/"
        names = [n for n in names if n.startswith(root)]
    else:
        root = ""
    rels = sorted(n[len(root):] for n in names)
    for i, rel in enumerate(rels):
        if limit and i >= limit:
            break
        yield rel, (lambda n: lambda: z.read(n).decode("utf-8", "replace"))(root + rel)


# --------------------------------------------------------------------------
# 主流程
# --------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("source", help="数据字典导出的 .zip 或解压后的目录")
    ap.add_argument("--out", default=DEFAULT_OUT, help="输出目录（默认 references/db）")
    ap.add_argument("--list", action="store_true", help="只统计，不写文件")
    ap.add_argument("--keep-stale", action="store_true", help="保留旧文件")
    ap.add_argument("--limit", type=int, default=None, help="只处理前 N 个文件")
    args = ap.parse_args(argv)

    if not os.path.exists(args.source):
        print("!! 找不到输入：%s" % args.source)
        return 1
    out_dir = os.path.abspath(args.out)

    t0 = time.time()
    written = []
    n_tables = 0
    n_placeholder = 0
    warnings = []
    mods = Counter()
    rels_seen = []
    for rel, read in iter_source(args.source, args.limit):
        if not rel.endswith(".html"):
            continue
        parts = rel.split("/")
        if len(parts) < 2:
            continue                       # 根目录下的 index.html / 模块概览页，跳过
        mod, fname = parts[-2], parts[-1]
        if not mod.endswith("_files"):
            continue
        rels_seen.append(rel)
        p = parse_html(read())
        if p.warnings:
            warnings.extend("%s: %s" % (rel, w) for w in p.warnings[:3])
        md = render(p.page_title, p.tables)
        n_tables += len(p.tables)
        if not p.tables:
            n_placeholder += 1
        mods[mod] += len(p.tables)
        if args.list:
            continue
        dest = os.path.join(out_dir, mod, fname[:-5] + ".md")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8", newline="\n").write(md)
        written.append(os.path.relpath(dest, out_dir).replace("\\", "/"))

    print("解析完成：%d 个文件 / %d 张表 / %d 个模块（%.1fs）"
          % (len(rels_seen), n_tables, len(mods), time.time() - t0))
    print("  其中 %d 个文件在导出里就没有表（仅标题的占位页）" % n_placeholder)
    if args.list:
        print("\n各模块表数 Top 15：")
        for m, c in mods.most_common(15):
            print("  %-28s %5d" % (m, c))
        if warnings:
            print("\n⚠️ 解析告警 %d 条，前 10 条：" % len(warnings))
            for w in warnings[:10]:
                print("   ", w)
        return 0

    # 清理不在本次导出里的旧文件
    removed = 0
    if not args.keep_stale and not args.limit:
        keep = set(written)
        for dirpath, dirnames, files in os.walk(out_dir, topdown=False):
            for f in files:
                if not f.endswith(".md") or f.upper() == "_INDEX.MD":
                    continue
                rel = os.path.relpath(os.path.join(dirpath, f), out_dir).replace("\\", "/")
                if rel not in keep:
                    os.remove(os.path.join(dirpath, f))
                    removed += 1
            if dirpath != out_dir and not os.listdir(dirpath):
                os.rmdir(dirpath)
    print("  写入 %d 个 .md，清理过期 %d 个" % (len(written), removed))

    if warnings:
        print("\n⚠️ 解析告警 %d 条，前 10 条：" % len(warnings))
        for w in warnings[:10]:
            print("   ", w)
    print("\n接下来请运行：python scripts/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
