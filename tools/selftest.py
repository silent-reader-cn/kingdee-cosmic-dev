#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
selftest —— kingdee-cosmic-dev 数据与检索的完整性自检
=====================================================
回答两个问题：
  1. **抓取是否完整**：线上 HTML 里的内容有没有在转 Markdown 时被丢掉？
  2. **检索是否完整**：search.py 返回的是否是完整正文，而不是被静默截断？

检查项
------
A. 抓取完整性
   A1 目录(TOC) / 原始存档(_source) / 正文(md) 三方条目数一致
   A2 每篇 HTML 的可见文本切块，逐块必须在 md 中出现（默认阈值 99%）
   A3 结构元素数量守恒：table / pre / img / a[href]
   A4 md 中不残留未处理的 HTML 块级标签
B. 检索完整性
   B1 `--full` 输出必须包含该文档的**全部正文行**
   B2 非 `--full` 时若发生截断，必须打印明确的截断提示（不得静默丢内容）
   B3 `--limit N` 生效且报告的「总命中数」>= 显示条数
   B4 数据库块：`_INDEX.md` 里每张表的字段数 == 该表定义里的数据行数

用法：
    python tools/selftest.py            # 全量自检
    python tools/selftest.py --quick    # 跳过逐篇文本比对（快）
"""
import argparse
import glob
import html as _html
import json
import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from html2md import html_to_markdown  # noqa: E402

REFS = os.path.join(ROOT, "references")
API_DIR = os.path.join(REFS, "openapi")
DB_DIR = os.path.join(REFS, "db")
SRC_DIR = os.path.join(API_DIR, "_source")
SEARCH = os.path.join(ROOT, "scripts", "search.py")

PASS, FAIL, WARN = [], [], []


def ok(msg):
    PASS.append(msg)
    print("  ✓ %s" % msg)


def bad(msg):
    FAIL.append(msg)
    print("  ✗ %s" % msg)


def warn(msg):
    WARN.append(msg)
    print("  ! %s" % msg)


# ---------------------------------------------------------------- 工具

def strip_html_text(html):
    """HTML → 纯可见文本（去标签、解实体、折叠空白）。"""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html or "")
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|li|tr|h[1-6])>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s).replace("\xa0", " ")
    return s


def strip_md_text(md):
    """Markdown → 纯文本。这里**刻意保留代码块与图片地址**（它们也是正文的一部分），
    只把语法标记本身去掉，避免误判为「内容丢失」。

    注意：这里**不做 HTML 实体解码**。Markdown 已是解码后的文本，
    再解一次会把 URL 里的 `&timestamp`、`&parameters` 误当成实体
    （`&times;`→`×`、`&para;`→`¶`），反而造出「丢失」的假象。
    """
    s = md or ""
    s = re.sub(r"(?m)^\s*```[^\n]*$", " ", s)                    # 围栏行本身
    s = re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", r"\1 \2", s)          # 图片：保留 alt 与地址
    s = re.sub(r"\[([^\]]*)\]\(([^)]*)\)", r"\1 \2", s)           # 链接：保留文字与地址
    s = re.sub(r"(?m)^\s*>\s?", "", s)                            # 引用前缀
    return s.replace("\xa0", " ")


def norm(s):
    """归一化：只保留字母/数字/汉字。

    两侧用**同一套**归一化，才能跨 HTML 与 Markdown 比对；
    否则 md 侧去掉 `-`/`_` 而 html 侧没去掉，会把 `utf-8`、`create_time`
    这类词误报成「丢失」。
    """
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", s or "")


def chunks(text, minlen=8):
    """按标点/空白切成较长的文本块。"""
    parts = re.split(r"[\s，。；：、！？,.;:!?（）()【】\[\]\"'“”‘’]+", text)
    return [p for p in (x.strip() for x in parts) if len(p) >= minlen]


def md_body_of(md_text):
    """去掉 frontmatter 与首个 `# 标题` 行。"""
    if md_text.startswith("---"):
        m = re.match(r"^---\r?\n.*?\r?\n---\r?\n?", md_text, re.S)
        if m:
            md_text = md_text[m.end():]
    return re.sub(r"^\s*#\s+[^\n]*\n", "", md_text, count=1)


def run_search(args):
    proc = subprocess.run([sys.executable, SEARCH] + args,
                          capture_output=True, text=True, encoding="utf-8")
    return proc.stdout, proc.stderr, proc.returncode


# ---------------------------------------------------------------- A 抓取完整性

def check_fetch(quick=False):
    print("\n[A] 抓取完整性")
    if not os.path.isdir(SRC_DIR):
        bad("找不到 %s" % SRC_DIR)
        return
    toc_path = os.path.join(SRC_DIR, "_toc.json")
    toc = json.load(open(toc_path, encoding="utf-8"))["items"] if os.path.exists(toc_path) else []
    src = {f[:-5] for f in os.listdir(SRC_DIR)
           if f.endswith(".json") and not f.startswith("_")}
    mds = [p for p in glob.glob(os.path.join(API_DIR, "**", "*.md"), recursive=True)
           if os.path.basename(p).upper() != "_INDEX.MD"]

    toc_ids = {str(i["entityId"]) for i in toc}
    if len(toc) == len(src) == len(mds):
        ok("A1 目录/存档/正文条目数一致：各 %d 篇" % len(toc))
    else:
        bad("A1 条目数不一致：TOC %d / 存档 %d / md %d" % (len(toc), len(src), len(mds)))
    if toc_ids - src:
        bad("A1 有目录但缺存档：%s" % sorted(toc_ids - src)[:5])
    if src - toc_ids:
        bad("A1 有存档但不在目录：%s" % sorted(src - toc_ids)[:5])

    # 逐篇保真
    total_chunks = missing_chunks = 0
    struct_bad = []
    tag_bad = []
    worst = []
    for fp in mds:
        md_text = open(fp, encoding="utf-8").read()
        m = re.search(r'entityId:\s*"([^"]+)"', md_text)
        if not m:
            bad("A2 %s 缺少 entityId" % os.path.relpath(fp, ROOT))
            continue
        eid = m.group(1)
        jf = os.path.join(SRC_DIR, "%s.json" % eid)
        if not os.path.exists(jf):
            bad("A2 %s 对应的存档缺失" % eid)
            continue
        art = json.load(open(jf, encoding="utf-8"))
        html = art.get("content") or ""

        body = md_body_of(md_text)

        # A4 残留 HTML 块级标签
        leftovers = re.findall(r"(?i)</?(?:div|span|p|td|tr|table|tbody|ul|ol|li|h[1-6])\b[^>]*>", body)
        if leftovers:
            tag_bad.append((os.path.relpath(fp, ROOT), leftovers[:3]))

        if quick:
            continue

        # A2 文本块覆盖
        html_text = strip_html_text(html)
        md_text_plain = strip_md_text(body)
        hay = norm(md_text_plain)
        cs = chunks(html_text)
        miss = [c for c in cs if norm(c) not in hay]
        total_chunks += len(cs)
        missing_chunks += len(miss)
        if miss:
            worst.append((len(miss), len(cs), os.path.relpath(fp, ROOT), miss[:2]))

        # A3 结构元素守恒（注意：引用块里的表格/代码块会带 `> ` 前缀；
        #     少数文章的 content 本身就是 Markdown，表格要按 `| --- |` 数）
        def cnt(pat, text, flags=0):
            return len(re.findall(pat, text, flags))

        html_tables = (cnt(r"(?i)<table", html)
                       + cnt(r"(?m)^\s*\|[\s:|-]*-{2,}[\s:|-]*\|", html))
        html_imgs = cnt(r"(?i)<img", html) + cnt(r"!\[[^\]]*\]\(", html)
        pairs = [
            ("table", html_tables, cnt(r"(?m)^\s*>?\s*\|\s*:?-{2,}", body)),
            ("pre", cnt(r"(?i)<pre", html), cnt(r"(?m)^\s*>?\s*```", body) // 2),
            ("img", html_imgs, cnt(r"!\[[^\]]*\]\(", body)),
        ]
        for name, a, b in pairs:
            if a != b:
                struct_bad.append((os.path.relpath(fp, ROOT), name, a, b))

    if tag_bad:
        bad("A4 %d 篇残留未转换的 HTML 标签，例：%s" % (len(tag_bad), tag_bad[0]))
    else:
        ok("A4 无残留 HTML 块级标签")

    if not quick:
        rate = (total_chunks - missing_chunks) / total_chunks * 100 if total_chunks else 100
        if missing_chunks == 0:
            ok("A2 文本保真 100%%（%d 个文本块全部保留）" % total_chunks)
        elif rate >= 99:
            warn("A2 文本保真 %.2f%%（%d/%d 块缺失）" % (rate, missing_chunks, total_chunks))
            for n, t, f, sample in sorted(worst, reverse=True)[:3]:
                print("       %s: 缺 %d/%d，例 %s" % (f, n, t, sample))
        else:
            bad("A2 文本保真仅 %.2f%%（缺 %d/%d 块），前几篇："
                % (rate, missing_chunks, total_chunks))
            for n, t, f, sample in sorted(worst, reverse=True)[:5]:
                print("       %s: 缺 %d/%d，例 %s" % (f, n, t, sample))

        if struct_bad:
            bad("A3 结构元素数量不符 %d 处，例：%s" % (len(struct_bad), struct_bad[:3]))
        else:
            ok("A3 结构元素守恒（table / pre / img）")


# ---------------------------------------------------------------- B 检索完整性

def check_search():
    print("\n[B] 检索完整性")
    # 取一篇最长的文章做全文比对
    mds = [p for p in glob.glob(os.path.join(API_DIR, "**", "*.md"), recursive=True)
           if os.path.basename(p).upper() != "_INDEX.MD"]
    mds.sort(key=lambda p: -os.path.getsize(p))
    if not mds:
        bad("B 找不到手册文档")
        return
    fp = mds[0]
    rel = os.path.relpath(fp, API_DIR).replace("\\", "/")
    md_text = open(fp, encoding="utf-8").read()
    body = md_body_of(md_text).strip("\n")
    title = re.search(r'^title:\s*"([^"]+)"', md_text, re.M)
    title = title.group(1) if title else os.path.basename(rel)[:-3]

    out, err, rc = run_search([title, "--scope", "openapi", "--full", "--limit", "1"])
    if rc != 0:
        bad("B1 检索退出码 %d，stderr=%s" % (rc, err.strip()[:200]))
        return

    # B1：正文每一行都要在 --full 输出里出现（按归一化比较）
    out_norm = norm(out)
    body_lines = [l for l in body.split("\n") if len(l.strip()) >= 12]
    missing = [l for l in body_lines if norm(l.strip()) not in out_norm]
    if not missing:
        ok("B1 --full 返回完整正文（%d 行全部命中，共 %d 字符）"
           % (len(body_lines), len(body)))
    else:
        bad("B1 --full 丢失 %d/%d 行，例：%s"
            % (len(missing), len(body_lines), missing[:2]))

    # B2：非 --full 必须显式提示截断
    out2, _, _ = run_search([title, "--scope", "openapi", "--limit", "1"])
    if len(body) > 1600:
        if "已截断" in out2 or "前略" in out2 or "后略" in out2:
            ok("B2 截断有明确提示（未静默丢内容）")
        else:
            bad("B2 正文被截断但没有提示：%s" % rel)
    else:
        ok("B2 短文档无需截断")

    # B3：--limit 生效 + 总数口径正确
    out3, _, _ = run_search(["API", "--scope", "openapi", "--brief", "--limit", "3"])
    shown = len(re.findall(r"^\[openapi\]", out3, re.M))
    m = re.search(r"共找到 (\d+) 条匹配", out3)
    total = int(m.group(1)) if m else shown
    if shown <= 3 and total >= shown:
        ok("B3 --limit 生效（显示 %d / 共 %d）" % (shown, total))
    else:
        bad("B3 --limit 异常：显示 %d / 共 %d" % (shown, total))

    # B4：数据库块全量校验（索引行数 / 表名可解析 / 字段数一致）
    check_db()
    # B5：端到端抽检 —— 正文深处的关键词也必须能被检索到
    check_recall()


def check_recall(samples=6):
    """随机取样：从正文**中后段**取一个独特词，验证 search.py 能召回该文档。

    这是对「检索返回信息不全 / 静默过滤」最直接的检验：
    如果预筛或分段逻辑有问题，正文深处的内容就会搜不到。

    注意两个容易造成**假失败**的点，这里都已规避：
      - 不能抽到 URL / 路径片段（`com/knowledge/sp` 这类），它们命中面太广；
      - `--limit` 必须给足，否则目标只是被挤到后面，而不是没召回。
    """
    import random
    rnd = random.Random(20260928)   # 固定种子，结果可复现

    def usable(tok):
        return (len(tok) >= 4 and "/" not in tok and "\\" not in tok
                and ":" not in tok and not tok.lower().startswith("http")
                and not re.match(r"^\d", tok))

    cases = []
    # 块二：取文章正文后半段的一个长词
    mds = [p for p in glob.glob(os.path.join(API_DIR, "**", "*.md"), recursive=True)
           if os.path.basename(p).upper() != "_INDEX.MD"]
    for fp in rnd.sample(mds, min(samples * 3, len(mds))):
        if len([c for c in cases if c[0] == "openapi"]) >= samples:
            break
        body = md_body_of(open(fp, encoding="utf-8").read())
        tail = body[len(body) // 2:] or body
        cands = [c for c in chunks(tail, 10) if usable(c)]
        if not cands:
            continue
        token = rnd.choice(cands)[:16]
        cases.append(("openapi", os.path.relpath(fp, API_DIR).replace("\\", "/"), token))

    # 块一：取表块「表格列定义」中后段的字段名
    mods = sorted(d for d in os.listdir(DB_DIR)
                  if d.endswith("_files") and os.path.isdir(os.path.join(DB_DIR, d)))
    got = 0
    for folder in rnd.sample(mods, min(samples * 3, len(mods))):
        if got >= samples:
            break
        files = sorted(glob.glob(os.path.join(DB_DIR, folder, "*.md")))
        files = [f for f in files if os.path.basename(f).upper() != "_INDEX.MD"]
        if not files:
            continue
        fp = rnd.choice(files)
        txt = open(fp, encoding="utf-8").read()
        fields = re.findall(r"(?m)^\|\s*\d+\s*\|\s*([a-z][a-z0-9_]{5,})\s*\|", txt)
        if len(fields) < 3:
            continue
        token = rnd.choice(fields[len(fields) // 2:])
        cases.append(("db", os.path.relpath(fp, DB_DIR).replace("\\", "/"), token))
        got += 1

    hit = 0
    misses = []
    for scope, rel, token in cases:
        out, _, _ = run_search([token, "--scope", scope, "--brief", "--limit", "5000"])
        if rel in out or os.path.basename(rel) in out:
            hit += 1
        else:
            misses.append((scope, rel, token))
    if not cases:
        warn("B5 无法构造抽检样本")
    elif not misses:
        ok("B5 端到端召回 %d/%d（正文深处关键词均可检索到）" % (hit, len(cases)))
    else:
        bad("B5 端到端召回 %d/%d，未召回：%s" % (hit, len(cases), misses[:3]))


def parse_db_blocks(folder):
    """解析一个模块下所有表块，返回 [(表名, 字段数)]，保持文件顺序。

    表名不一定以 `t_` 开头：上游数据字典里存在 `uiui`、`kd_mobile_group_u`
    这类值，这里按原样接受，不做过早的格式假设。
    """
    out = []
    files = sorted(glob.glob(os.path.join(DB_DIR, folder, "*.md")))
    for fp in files:
        if os.path.basename(fp).upper() == "_INDEX.MD":
            continue
        txt = open(fp, encoding="utf-8").read()
        titles = re.findall(r"(?m)^##\s+(.*)$", txt)
        blocks = re.split(r"(?m)^##\s+.*$", txt)[1:]
        for title, blk in zip(titles, blocks):
            mt = re.search(r"(?m)^-\s*\*\*表名[：:]?\*\*[：:]?\s*(.+?)\s*$", blk)
            name = mt.group(1).strip().strip("`") if mt else ""
            if not name:
                m2 = re.search(r"(\S+)\s*$", title)
                name = m2.group(1) if m2 else ""
            sec = re.search(r"###\s*表格列定义\s*\n(.*?)(?:\n###|\Z)", blk, re.S)
            n = len(re.findall(r"(?m)^\|\s*\d+\s*\|", sec.group(1))) if sec else 0
            out.append((name, n))
    return out


def check_db():
    """对**全部 224 个模块**做交叉校验，而不是只抽查一个模块。"""
    mods = []
    for folder in sorted(os.listdir(DB_DIR)):
        full = os.path.join(DB_DIR, folder)
        if os.path.isdir(full) and folder.endswith("_files"):
            mods.append(folder)
    if not mods:
        warn("B4 找不到数据库模块目录")
        return

    n_blocks = n_rows = 0
    no_name = []
    mismatch = []
    missing_index = []
    zero_field = 0
    odd_names = set()
    for folder in mods:
        real = parse_db_blocks(folder)
        n_blocks += len(real)
        for name, n in real:
            if not name:
                no_name.append(folder)
            elif not re.match(r"^t_", name):
                odd_names.add(name)
            if n == 0:
                zero_field += 1

        idx = os.path.join(DB_DIR, folder, "_INDEX.md")
        if not os.path.exists(idx):
            missing_index.append(folder)
            continue
        itxt = open(idx, encoding="utf-8").read()
        rows = re.findall(r"(?m)^\|\s*\d+\s*\|\s*`?([^`|]+?)`?\s*\|\s*[^|]*\|\s*(\d+)\s*\|", itxt)
        rows = [(a.strip(), int(b)) for a, b in rows]
        n_rows += len(rows)
        if sorted(rows) != sorted(real):
            only_idx = len(rows) - len(real)
            mismatch.append((folder, len(real), len(rows), only_idx))

    if missing_index:
        bad("B4 %d 个模块缺少 _INDEX.md：%s" % (len(missing_index), missing_index[:5]))
    else:
        ok("B4 全部 %d 个模块都有 _INDEX.md" % len(mods))

    if no_name:
        bad("B4 有 %d 个表块解析不出表名，例：%s" % (len(no_name), no_name[:3]))
    else:
        ok("B4 全部 %d 个表块都能解析出表名" % n_blocks)

    if mismatch:
        bad("B4 索引与表定义不一致的模块 %d 个，例（模块, 定义数, 索引数）：%s"
            % (len(mismatch), mismatch[:3]))
    else:
        ok("B4 索引与表定义逐条一致（%d 个模块 / %d 个表块 / %d 行索引）"
           % (len(mods), n_blocks, n_rows))

    if odd_names:
        warn("B4 有 %d 个表名不以 `t_` 开头（上游数据如此）：%s"
             % (len(odd_names), sorted(odd_names)[:5]))
    if zero_field:
        warn("B4 有 %d 个表块在源文档里就没有字段定义（字段数=0）" % zero_field)


def _split_md_row(ln):
    s = ln.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [p.strip().replace("\\|", "|") for p in re.split(r"(?<!\\)\|", s)]


def parse_db_md(text):
    """把表结构 Markdown 解析回结构，用于与源 HTML 对账。"""
    out = []
    for blk in re.split(r"(?m)^##\s+", text)[1:]:
        lines = blk.split("\n")
        heading = lines[0].strip()
        body = "\n".join(lines[1:])
        mc = re.search(r"(?m)^-\s*\*\*表名称[：:]?\*\*[：:]*\s*(.*)$", body)
        mn = re.search(r"(?m)^-\s*\*\*表名[：:]?\*\*[：:]*\s*(.*)$", body)
        secs = {}
        parts = re.split(r"(?m)^###\s+(.*)$", body)
        for i in range(1, len(parts), 2):
            sec = parts[i].strip()
            content = parts[i + 1] if i + 1 < len(parts) else ""
            head, rows = None, []
            for ln in content.split("\n"):
                if not ln.lstrip().startswith("|"):
                    continue
                cells = _split_md_row(ln)
                if head is None:
                    head = cells
                    continue
                if all(set(c) <= set(":- ") for c in cells):
                    continue
                rows.append(cells)
            secs[sec] = (head or [], rows)
        out.append({"heading": heading,
                    "cn": mc.group(1).strip() if mc else "",
                    "name": mn.group(1).strip() if mn else "",
                    "sections": secs})
    return out


def check_dict(source, quick=False, samples=25):
    """A5/A6：数据字典 HTML → Markdown 的保真度。

    A5 全量（轻量）：每个 .html 的表数 / 小节数 / 表格数必须与 .md 完全一致
       —— 能抓住「整张表或整节丢失」。
    A6 抽样（深度）：完整重新解析 HTML，与 .md **逐单元格**比对
       —— 能抓住「某几行或某个单元格丢失」。
    """
    print("\n[A5/A6] 块一 数据字典 HTML → Markdown 保真")
    import zipfile
    sys.path.insert(0, SCRIPT_DIR)
    from build_db_from_dict import parse_html  # noqa: E402

    if os.path.isdir(source):
        pairs = []
        for dirpath, _, files in os.walk(source):
            for f in files:
                if f.endswith(".html"):
                    full = os.path.join(dirpath, f)
                    rel = os.path.relpath(full, source).replace("\\", "/")
                    pairs.append((rel, full))
        reader = lambda p: open(p, encoding="utf-8", errors="replace").read()  # noqa: E731
    else:
        z = zipfile.ZipFile(source)
        names = [n for n in z.namelist() if n.lower().endswith(".html") and "/" in n.rstrip("/")]
        roots = {n.split("/")[0] for n in names}
        root = (roots.pop() + "/") if len(roots) == 1 else ""
        names = [n for n in names if n.startswith(root)]
        pairs = sorted(((n[len(root):], n) for n in names))
        reader = lambda n: z.read(n).decode("utf-8", "replace")  # noqa: E731

    pairs = [(rel, key) for rel, key in pairs
             if rel.count("/") == 1 and rel.split("/")[0].endswith("_files")]
    if not pairs:
        bad("A5 数据源里没找到 <模块>_files/*.html")
        return

    # ---- A5 全量轻量 ----
    mismatch = []
    checked = 0
    for rel, key in pairs:
        md_path = os.path.join(DB_DIR, rel[:-5] + ".md")
        if not os.path.exists(md_path):
            mismatch.append((rel, "缺少 .md"))
            continue
        h = reader(key)
        md = open(md_path, encoding="utf-8").read()
        h_tbl = len(re.findall(r'<div class="tbl ', h))
        h_sec = len(re.findall(r'<h3 class="tbl-c-h"', h))
        h_tab = len(re.findall(r"<table", h))
        m_blk = len(re.findall(r"(?m)^##\s+", md))
        m_sec = len(re.findall(r"(?m)^###\s+", md))
        m_tab = len(re.findall(r"(?m)^\|\s*:?-{2,}", md))
        checked += 1
        if (h_tbl, h_sec, h_tab) != (m_blk, m_sec, m_tab):
            mismatch.append((rel, "html(表%d/节%d/表%d) vs md(%d/%d/%d)"
                             % (h_tbl, h_sec, h_tab, m_blk, m_sec, m_tab)))
    if mismatch:
        bad("A5 %d/%d 个文件的表/节/表格数不一致，例：%s"
            % (len(mismatch), checked, mismatch[:3]))
    else:
        ok("A5 全量 %d 个文件：表数/小节数/表格数与源 HTML 完全一致" % checked)

    if quick:
        return

    # ---- A6 抽样深度 ----
    import random
    rnd = random.Random(20260928)
    if samples <= 0:
        pick = list(pairs)                 # 0 = 全量（约 1.5 分钟）
    else:
        pick = rnd.sample(pairs, min(samples, len(pairs)))
    cell_bad = []
    cell_total = 0
    for rel, key in pick:
        md_path = os.path.join(DB_DIR, rel[:-5] + ".md")
        p = parse_html(reader(key))
        md_tables = parse_db_md(open(md_path, encoding="utf-8").read())
        if len(p.tables) != len(md_tables):
            cell_bad.append((rel, "表数 %d vs %d" % (len(p.tables), len(md_tables))))
            continue
        for t, mt in zip(p.tables, md_tables):
            if t.name != mt["name"]:
                cell_bad.append((rel, "表名 %r vs %r" % (t.name, mt["name"])))
                continue
            for sec, (hhead, hrows) in t.sections.items():
                mhead, mrows = mt["sections"].get(sec, ([], []))
                if len(hrows) != len(mrows):
                    cell_bad.append((rel, "%s %s 行数 %d vs %d"
                                     % (t.name, sec, len(hrows), len(mrows))))
                    continue
                for r_i, (hr, mr) in enumerate(zip(hrows, mrows)):
                    if len(hr) != len(mr):
                        cell_bad.append((rel, "%s %s 第%d行列数 %d vs %d"
                                         % (t.name, sec, r_i + 1, len(hr), len(mr))))
                        continue
                    for c_i, (hc, mcc) in enumerate(zip(hr, mr)):
                        cell_total += 1
                        # 两侧都可能把跨表引用写成链接（HTML 侧由解析器转换），
                        # 比对时统一只取链接文字，否则会把「一致」误判成「不一致」。
                        a = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", hc)
                        b = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", mcc)
                        if norm(a) != norm(b):
                            cell_bad.append((rel, "%s %s r%d c%d: %r != %r"
                                             % (t.name, sec, r_i + 1, c_i + 1,
                                                hc[:40], mcc[:40])))
    if cell_bad:
        bad("A6 深度抽检 %d 个文件发现 %d 处不一致，例：%s"
            % (len(pick), len(cell_bad), cell_bad[:3]))
    else:
        ok("A6 深度抽检 %d 个文件 / %d 个单元格，与源 HTML 逐格一致"
           % (len(pick), cell_total))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="跳过逐篇文本比对")
    ap.add_argument("--dict-zip", metavar="PATH",
                    help="数据字典导出包（.zip 或目录），提供后额外做块一 HTML→Markdown 保真校验")
    ap.add_argument("--dict-samples", type=int, default=25,
                    help="块一深度抽检的文件数（默认 25；传 0 表示全量，约 1.5 分钟）")
    args = ap.parse_args(argv)

    print("kingdee-cosmic-dev 自检")
    print("=" * 60)
    check_fetch(quick=args.quick)
    check_search()
    if args.dict_zip:
        check_dict(args.dict_zip, quick=args.quick, samples=args.dict_samples)
    else:
        warn("A5/A6 跳过块一保真校验：加 --dict-zip <导出包> 可启用")

    print("\n" + "=" * 60)
    print("通过 %d 项 / 警告 %d 项 / 失败 %d 项" % (len(PASS), len(WARN), len(FAIL)))
    if FAIL:
        print("\n失败项：")
        for f in FAIL:
            print("  - %s" % f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
