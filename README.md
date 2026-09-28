# kingdee-cosmic-dev

**金蝶云苍穹（Kingdee Cloud Cosmic / 金蝶AI苍穹）开发知识库与 AI Skill** —— 22,769 张物理表结构 + 144 篇 OpenAPI 开放平台官方手册，两块钱内容用一套全文检索脚本统一检索。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Kingdee](https://img.shields.io/badge/Kingdee-Cloud%20Cosmic-green.svg)
![Tables](https://img.shields.io/badge/DB%20tables-22%2C769-orange.svg)
![Modules](https://img.shields.io/badge/modules-224-orange.svg)
![OpenAPI](https://img.shields.io/badge/OpenAPI%20docs-144-blueviolet.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB.svg)

---

## 这是什么

金蝶云苍穹二开 / 运维时最常查的两类资料，全部收在一处，**并且都能用同一个命令搜出来**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构（列名/中文名/类型/长度/精度/非空/默认值/备注枚举）+ 列规则 + 索引定义 | 22,769 张表 / 224 模块 | [`references/db/`](./references/db/) |
| **块二 OpenAPI 手册** | 开放平台官方手册：认证鉴权、操作API、自定义API、RESTful API、Webservice、开放事件、限流与排错 | 144 篇 / 8 分类 | [`references/openapi/`](./references/openapi/) |

数据库目标版本 **PostgreSQL 12**。手册抓取自金蝶云社区专题「OpenAPI（开放平台）」，每篇文档的 frontmatter 里保留了原文链接。

---

## 30 秒上手

```bash
git clone https://github.com/silent-reader-cn/kingdee-cosmic-dev.git
cd kingdee-cosmic-dev

# 不知道「销售订单」是哪张表？直接搜
python scripts/search.py 销售订单

# 已知表名，要完整字段定义？精确匹配 + 全量输出
python scripts/search.py t_sm_salorder --table --full

# 调接口报 access_token 错？搜手册
python scripts/search.py access_token --scope openapi

# 自定义API 插件怎么写？
python scripts/search.py 自定义API --scope openapi --brief

# 有哪些模块和分类？
python scripts/search.py --list
```

只依赖 Python 3（标准库），无需安装任何第三方包。

---

## 检索脚本用法

```bash
python scripts/search.py <关键词...> [选项]
```

| 选项 | 说明 |
| :--- | :--- |
| `--scope S` | 检索范围：`db`（数据库）\| `openapi`（开发手册）\| `all`（默认） |
| `--category C` | 块一按模块过滤（如 `gl`）；块二按分类过滤（如 `用户手册/常见问题`） |
| `--table` | 关键词按**表名**精确匹配（仅块一）；此时默认返回**完整字段定义**，避免上百字段的表被截断后当成完整定义 |
| `--brief` | 精简输出：仅一行摘要 |
| `--full` / `-d` | 输出命中条目的完整正文（不截断） |
| `--all` | 多个关键词需**全部**命中（默认任一命中即可） |
| `--limit N` | 最多返回结果数（默认 20） |
| `--max N` | 非 `--full` 时每条正文最多展示字符数（默认 1600） |
| `--list` | 列出全部数据库模块与手册分类 |

**设计要点**

- **Markdown 是唯一真相源**：脚本直接读 Markdown，不依赖任何预生成字典，
  不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- **块一精确到「表」**：一张表 = 一个 `## <中文名> t_<表名>` 块，多语言表（`_l`）、
  分录子表会被拆成独立条目。
- **块二截取命中位置**：正文超长时截取的是关键词附近的片段，而不是从头截断，
  答案在文末也看得到。
- 全库检索约 1–3 秒。

---

## 索引重建

`references/**/_INDEX.md` 全部由脚本从 Markdown 派生，**请勿手工编辑**：

```bash
python scripts/build_index.py          # 全量重建
python scripts/build_index.py gl som   # 只重建指定数据库模块
```

---

## 自检（内容完整性与检索完整性）

内容是从线上抓的，所以仓库自带一套审计脚本，用来回答「有没有悄悄丢内容」：

```bash
python tools/selftest.py            # 全量自检（约 20 秒）
python tools/selftest.py --quick    # 跳过逐篇文本比对
```

它检查两类问题：

| 检查 | 内容 |
| :--- | :--- |
| **A1** | 目录 / 原始存档 / 正文三方条目数一致 |
| **A2** | 每篇 HTML 的可见文本切块，逐块必须在 Markdown 中出现（**当前 100%，9,465 个文本块全保留**） |
| **A3** | 结构元素数量守恒：table / pre / img |
| **A4** | Markdown 中不残留未处理的 HTML 块级标签 |
| **B1** | `--full` 输出包含该文档**全部正文行** |
| **B2** | 非 `--full` 时若截断，必须打印明确的截断提示（不静默丢内容） |
| **B3** | `--limit` 生效，且报告的「总命中数」口径正确 |
| **B4** | 全部 224 个模块的 `_INDEX.md` 与表定义**逐条一致**（22,769 个表块 / 22,769 行索引） |
| **B5** | 端到端召回抽检：正文深处的关键词也能被检索到 |

> 已知的**上游数据特征**（非本仓库问题，自检会以警告形式列出）：
> 88 个表名不以 `t_` 开头（如 `uiui`、`community_user`）；
> 606 个表块在源文档里本身就没有字段定义。

---

## 手册更新（内容是从线上抓的）

```bash
python tools/fetch_manual.py            # 重新抓取（已存在的跳过，可增量）
python tools/fetch_manual.py --force    # 全部重抓
python tools/fetch_manual.py --render   # 不联网，用 _source/ 存档重新渲染
python tools/fetch_manual.py --list     # 只看目录树
```

- 抓取源是 vip.kingdee.com 的 JSON 接口（`/knowledgeapi/...`），**无需登录**。
- 原始 JSON 存档在 `references/openapi/_source/`，所以调整 `tools/html2md.py`
  的转换规则后可以 `--render` 离线重出，不必再联网。
- `tools/html2md.py` 是零依赖的 HTML→Markdown 转换器（只用标准库 `html.parser`），
  针对金蝶社区的 UEditor 富文本做了适配：表格、围栏代码块、嵌套列表、图片绝对路径。

---

## 安装为 Skill

```bash
git clone https://github.com/silent-reader-cn/kingdee-cosmic-dev.git
mkdir -p ~/.workbuddy-ai/skills/kingdee-cosmic-dev
cp -r kingdee-cosmic-dev/. ~/.workbuddy-ai/skills/kingdee-cosmic-dev/
```

安装后，AI 助手在遇到金蝶库表或 OpenAPI 问题时会自动加载本 skill，并用 `scripts/search.py` 定位内容。

---

## 目录结构

```
kingdee-cosmic-dev/
├── SKILL.md                    # Skill 定义：检索用法 + 库表约定 + OpenAPI 速查
├── README.md
├── LICENSE
├── scripts/
│   ├── search.py               # 统一检索（块一 + 块二）
│   └── build_index.py          # 从 Markdown 生成各级 _INDEX.md
├── tools/
│   ├── html2md.py              # HTML→Markdown 转换器（零依赖）
│   ├── fetch_manual.py         # 抓取金蝶云社区专题手册
│   └── selftest.py             # 内容/检索完整性自检
└── references/
    ├── _INDEX.md               # 总索引
    ├── db/                     # 块一：数据库
    │   ├── _INDEX.md
    │   └── <模块>_files/
    └── openapi/                # 块二：OpenAPI 手册
        ├── _INDEX.md
        ├── _source/
        └── <分类>/…/<标题>.md
```

---

## 免责声明

- **块一**：表结构整理自金蝶云苍穹数据字典导出，最终解释权归金蝶所有，请以实际数据库为准。
- **块二**：手册内容抓取自金蝶云社区公开专题，版权归金蝶所有，仅供学习与开发参考；
  文档内所有外链均指向原站，请以线上最新版本为准。

## License

[MIT](./LICENSE) © 2026 silent-reader-cn
