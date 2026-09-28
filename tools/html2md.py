#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
html2md —— 零依赖的 HTML → Markdown 转换器
==========================================
专为金蝶云社区（vip.kingdee.com）知识库的 UEditor 富文本输出设计，
只用 Python 标准库（html.parser），不引入任何第三方包。

支持：标题 h1-h6、段落、换行、加粗/斜体/删除线、行内代码、
围栏代码块（保留 language-xxx 语言标记）、有序/无序/嵌套列表、
表格（首行作表头）、引用块、分隔线、链接、图片（可转绝对地址）。

用法：
    from html2md import html_to_markdown
    md = html_to_markdown(html, base_url="https://vip.kingdee.com")

命令行：
    python tools/html2md.py input.html            # 输出到 stdout
    python tools/html2md.py input.html out.md     # 输出到文件
"""
import html as _html
import os
import re
import sys
from html.parser import HTMLParser

VOID_TAGS = {
    "br", "img", "hr", "input", "meta", "link", "col", "area", "base",
    "source", "wbr", "embed", "param", "track",
}
# 这些标签的“块级”语义：内部换行会影响 markdown 结构
BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "main", "aside",
    "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "table", "tr",
    "blockquote", "pre", "figure", "figcaption", "hr", "dl", "dt", "dd",
}
SKIP_TAGS = {"script", "style", "noscript", "iframe"}
# 出现这些标签才认定「这是 HTML 富文本」；否则按纯文本/Markdown 直通处理。
HTML_BLOCK_TAGS = {
    "p", "div", "table", "tbody", "thead", "tfoot", "tr", "td", "th",
    "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote",
    "pre", "section", "article", "header", "footer", "figure", "figcaption",
    "dl", "dt", "dd", "colgroup", "center",
}
_TAG_RE = re.compile(r"<\s*([a-zA-Z][a-zA-Z0-9]*)")


def looks_like_html(text):
    """判断 content 是 HTML 富文本还是纯文本 / Markdown 源码。

    金蝶社区里少数文章的正文本身就是 Markdown（含 `#` 标题、`|` 表格），
    若按 HTML 解析，文本节点的空白会被折叠，整篇会塌成一行。
    """
    for m in _TAG_RE.finditer(text or ""):
        if m.group(1).lower() in HTML_BLOCK_TAGS:
            return True
    return False


def plaintext_to_markdown(text):
    """纯文本 / Markdown 直通：只做实体还原与换行规整，保留原有结构。"""
    s = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</?font\b[^>]*>", "", s)
    s = re.sub(r"(?i)</?(?:span|div|u)\b[^>]*>", "", s)
    s = _html.unescape(s)
    s = "\n".join(l.rstrip() for l in s.split("\n"))
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


class Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = []


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = Node("#root")
        self.stack = [self.root]
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if self.skip:
            return
        node = Node(tag, {k: (v if v is not None else "") for k, v in attrs})
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        if self.skip or tag in SKIP_TAGS:
            return
        self.stack[-1].children.append(
            Node(tag, {k: (v if v is not None else "") for k, v in attrs}))

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or tag in VOID_TAGS:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.skip or not data:
            return
        self.stack[-1].children.append(data)

    def handle_entityref(self, name):
        if self.skip:
            return
        self.stack[-1].children.append(_html.unescape("&%s;" % name))

    def handle_charref(self, name):
        if self.skip:
            return
        self.stack[-1].children.append(_html.unescape("&#%s;" % name))


def _collapse(text):
    """普通文本：把连续空白折叠成一个空格。"""
    return re.sub(r"\s+", " ", text.replace("\xa0", " "))


def _plain(s):
    """去掉行内标记，只留纯文本（用于标题）。"""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", s)
    s = re.sub(r"~~(.+?)~~", r"\1", s)
    s = re.sub(r"</?u>", "", s)
    s = s.replace("`", "")
    return re.sub(r"\s+", " ", s).strip()


def _attr(node, *names):
    for n in names:
        if n in node.attrs and node.attrs[n]:
            return node.attrs[n]
    return ""


class Renderer:
    def __init__(self, base_url="", image_base=None):
        self.base_url = base_url.rstrip("/")
        self.image_base = (image_base or base_url).rstrip("/")

    # ---------- 工具 ----------
    def _abs(self, url, base):
        if not url:
            return url
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("//"):
            return url
        if url.startswith("/") and base:
            return base + url
        return url

    def _inline(self, node, in_pre=False):
        """渲染行内内容，返回字符串。"""
        if isinstance(node, str):
            if in_pre:
                return node.replace("\xa0", " ")
            return _collapse(node)
        t = node.tag
        if t in ("script", "style", "noscript", "iframe"):
            return ""
        if t == "br":
            return "\n"
        if t in ("strong", "b"):
            s = self._inline_all(node, in_pre).strip()
            return "**%s**" % s if s else ""
        if t in ("em", "i"):
            s = self._inline_all(node, in_pre).strip()
            return "*%s*" % s if s else ""
        if t in ("del", "s", "strike"):
            s = self._inline_all(node, in_pre).strip()
            return "~~%s~~" % s if s else ""
        if t == "u":
            s = self._inline_all(node, in_pre).strip()
            return "<u>%s</u>" % s if s else ""
        if t == "code":
            if in_pre:
                return self._inline_all(node, True)
            s = self._inline_all(node, False).strip()
            if not s:
                return ""
            tick = "``" if "`" in s else "`"
            return "%s%s%s" % (tick, s, tick)
        if t == "img":
            src = self._abs(_attr(node, "src", "data-src"), self.image_base)
            alt = _attr(node, "alt", "title")
            if not src:
                return ""
            return "![%s](%s)" % (alt, src)
        if t == "a":
            href = self._abs(_attr(node, "href"), self.base_url)
            text = self._inline_all(node, in_pre).strip()
            if not href or href.startswith("javascript:"):
                return text
            if not text:
                return "<%s>" % href
            return "[%s](%s)" % (text, href)
        if t in ("pre",):
            return self._pre(node)
        return self._inline_all(node, in_pre)

    def _inline_all(self, node, in_pre=False):
        return "".join(self._inline(c, in_pre) for c in node.children)

    def _pre(self, node):
        """代码块：<pre><code class="language-xxx">...</code></pre>"""
        lang = ""
        code_node = next((c for c in node.children
                          if not isinstance(c, str) and c.tag == "code"), None)
        target = code_node or node
        for c in target.children:
            if not isinstance(c, str):
                cls = _attr(c, "class")
                m = re.search(r"language-([A-Za-z0-9+#_-]+)", cls)
                if m:
                    lang = m.group(1)
                    break
        if not lang:
            m = re.search(r"language-([A-Za-z0-9+#_-]+)", _attr(node, "class"))
            lang = m.group(1) if m else ""
        if lang in ("plaintext", "text", "txt", "undefined"):
            lang = ""
        text = self._inline_all(target, in_pre=True)
        text = text.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
        if not text.strip():
            return ""
        fence = "```"
        if fence in text:
            fence = "````"
        return "\n\n%s%s\n%s\n%s\n\n" % (fence, lang, text, fence)

    # ---------- 块级 ----------
    def render_children(self, node, ctx=None):
        ctx = ctx or {}
        out = []
        for c in node.children:
            out.append(self.block(c, ctx))
        return "".join(out)

    def block(self, node, ctx):
        if isinstance(node, str):
            if ctx.get("in_pre"):
                return node.replace("\xa0", " ")
            return _collapse(node)
        t = node.tag
        if t in ("script", "style", "noscript", "iframe"):
            return ""
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = _plain(self._inline_all(node))
            if not text:
                return ""          # 跳过空的锚点标题
            level = int(t[1])
            if ctx.get("in_list"):
                # 列表里的标题降级为加粗行，避免破坏列表结构
                return "  " * ctx.get("depth", 0) + "**%s**\n" % text
            return "\n%s %s\n\n" % ("#" * level, text)
        if t == "p":
            text = self._inline_all(node).strip()
            return ("%s\n\n" % text) if text else ""
        if t in ("div", "section", "article", "header", "footer", "main",
                 "aside", "figure", "figcaption", "dd", "dt", "center"):
            inner = self.render_children(node, ctx).strip()
            if not inner:
                return ""
            if t in ("center", "figure"):
                return "\n%s\n\n" % inner
            # div 若只含行内内容，当成段落；否则原样透传
            if all(isinstance(c, str) or c.tag not in BLOCK_TAGS
                   for c in node.children):
                return "%s\n\n" % inner
            return "\n%s\n" % inner
        if t == "blockquote":
            inner = self.render_children(node, ctx).strip()
            if not inner:
                return ""
            quoted = "\n".join(("> " + l) if l.strip() else ">"
                               for l in inner.split("\n"))
            return "\n%s\n\n" % quoted
        if t == "hr":
            return "\n---\n\n"
        if t in ("ul", "ol"):
            return self._list(node, ctx)
        if t == "li":
            return self._list_item(node, ctx, ordered=False, idx=1)
        if t == "table":
            return self._table(node, ctx)
        if t == "pre":
            return self._pre(node)
        if t == "br":
            return "\n"
        if t == "img":
            return self._inline(node) + "\n\n"
        if t == "a":
            return self._inline(node)
        # 兜底：行内渲染
        return self._inline_all(node)

    def _list(self, node, ctx):
        ordered = node.tag == "ol"
        depth = ctx.get("depth", 0)
        parts = []
        idx = 0
        for c in node.children:
            if isinstance(c, str):
                continue
            if c.tag == "li":
                idx += 1
                parts.append(self._list_item(c, dict(ctx, depth=depth),
                                             ordered, idx))
            elif c.tag in ("ul", "ol"):
                # UEditor 常把嵌套列表写成 <ul><li/><ul>…</ul></ul>（平级兄弟），
                # 这里把它挂到上一个 li 之后，避免整段丢失。
                sub = self._list(c, dict(ctx, depth=depth + 1)).strip("\n")
                if not sub:
                    continue
                if parts:
                    parts[-1] = parts[-1].rstrip("\n") + "\n" + sub + "\n"
                else:
                    parts.append(sub + "\n")
        if not parts:
            inner = self.render_children(node, ctx).strip()
            return ("\n%s\n\n" % inner) if inner else ""
        return "\n" + "".join(parts) + "\n"

    def _list_item(self, node, ctx, ordered, idx):
        depth = ctx.get("depth", 0)
        indent = "  " * depth
        marker = ("%d. " % idx) if ordered else "- "
        child_ctx = dict(ctx, in_list=True, depth=depth + 1)

        # 分离「行内内容」与「嵌套列表/块级内容」
        inline_parts, block_parts = [], []
        for c in node.children:
            if isinstance(c, str):
                inline_parts.append(_collapse(c))
            elif c.tag in ("ul", "ol"):
                block_parts.append(self._list(c, child_ctx))
            elif c.tag in BLOCK_TAGS and c.tag != "p":
                block_parts.append(self.block(c, child_ctx))
            else:
                inline_parts.append(self._inline(c))
        text = "".join(inline_parts).strip()
        if not text and block_parts:
            text = ""
        line = indent + marker + text + "\n"
        # 续行缩进对齐
        cont = "  " * depth + " " * len(marker)
        body = ""
        for bp in block_parts:
            bp = bp.strip("\n")
            if not bp:
                continue
            for l in bp.split("\n"):
                body += (cont + l.strip()) if l.strip() else ""
                body += "\n"
        return line + body

    def _table(self, node, ctx):
        rows = []

        def collect(n):
            for c in n.children:
                if isinstance(c, str):
                    continue
                if c.tag == "tr":
                    cells = []
                    for cell in c.children:
                        if not isinstance(cell, str) and cell.tag in ("td", "th"):
                            cells.append(self._cell(cell))
                    if cells:
                        rows.append(cells)
                elif c.tag in ("thead", "tbody", "tfoot", "table"):
                    collect(c)

        collect(node)
        if not rows:
            return ""
        ncol = max(len(r) for r in rows)
        rows = [r + [""] * (ncol - len(r)) for r in rows]
        out = ["", "| " + " | ".join(rows[0]) + " |",
               "| " + " | ".join(["---"] * ncol) + " |"]
        for r in rows[1:]:
            out.append("| " + " | ".join(r) + " |")
        out.append("")
        return "\n".join(out) + "\n"

    def _cell(self, node):
        parts = []
        for c in node.children:
            if isinstance(c, str):
                parts.append(_collapse(c))
            elif c.tag in ("ul", "ol"):
                items = [self._inline_all(li).strip()
                         for li in c.children
                         if not isinstance(li, str) and li.tag == "li"]
                parts.append("<br>".join(x for x in items if x))
            elif c.tag == "br":
                parts.append("<br>")
            elif c.tag in ("p", "div"):
                inner = self._inline_all(c).strip()
                if inner:
                    parts.append(inner)
            else:
                parts.append(self._inline(c))
        text = "".join(parts)
        text = re.sub(r"\s+", " ", text).strip()
        # 去掉首尾多余的换行标记（UEditor 常在单元格末尾塞 <br>）
        text = re.sub(r"^(?:<br>\s*)+", "", text)
        text = re.sub(r"(?:\s*<br>)+$", "", text)
        text = re.sub(r"(?:<br>\s*){2,}", "<br>", text)
        return text.replace("|", "\\|")


def html_to_markdown(html, base_url="", image_base=None):
    """把一段 HTML（或 Markdown 源码）转成 Markdown（已做空行规整）。"""
    if not html or not html.strip():
        return ""
    if not looks_like_html(html):
        # 少数文章的 content 本身就是 Markdown，直通即可，避免空白被折叠
        return plaintext_to_markdown(html)
    builder = TreeBuilder()
    builder.feed(html)
    builder.close()
    r = Renderer(base_url=base_url, image_base=image_base)
    md = r.render_children(builder.root)
    # 规整：去行尾空白、压缩 3+ 连续空行
    md = "\n".join(l.rstrip() for l in md.split("\n"))
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md.strip()


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    src = argv[0]
    html = open(src, encoding="utf-8").read()
    md = html_to_markdown(html, base_url="https://vip.kingdee.com")
    if len(argv) > 1:
        open(argv[1], "w", encoding="utf-8").write(md + "\n")
        print("已写入 %s（%d 字符）" % (argv[1], len(md)))
    else:
        sys.stdout.write(md + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
