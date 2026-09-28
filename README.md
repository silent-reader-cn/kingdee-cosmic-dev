# kingdee-sql-expert

**金蝶云苍穹（Kingdee Cloud Cosmic）数据库知识库与 AI Skill** —— 22,769 张物理表结构，覆盖 224 个模块，用一套全文检索脚本统一检索。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Kingdee](https://img.shields.io/badge/Kingdee-Cloud%20Cosmic-green.svg)
![Tables](https://img.shields.io/badge/DB%20tables-22%2C769-orange.svg)
![Modules](https://img.shields.io/badge/modules-224-orange.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB.svg)

---

## 这是什么

金蝶云苍穹二开 / 运维时最常查的东西——**某张表有哪些字段、字段什么含义、主子表怎么关联**——
全部收在一处，**并且能用同一个命令搜出来**：

| 内容 | 规模 | 入口 |
| :--- | :--- | :--- |
| 全量物理表结构（列名/中文名/类型/长度/精度/非空/默认值/备注枚举） | 22,769 张表 | [`references/`](./references/) |
| 列规则定义 + 索引定义 | 每表附带 | 同上 |
| 模块总索引与分模块清单 | 224 个模块 | [`references/_INDEX.md`](./references/_INDEX.md) |

数据导出自金蝶云苍穹数据字典，目标数据库为 **PostgreSQL 12**。

---

## 30 秒上手

```bash
git clone https://github.com/silent-reader-cn/kingdee-sql-expert.git
cd kingdee-sql-expert

# 不知道「销售订单」是哪张表？直接搜
python scripts/search.py 销售订单

# 已知表名，要完整字段定义？精确匹配 + 全量输出
python scripts/search.py t_sm_salorder --table --full

# 只想看总账模块里带「凭证」的表，一行摘要
python scripts/search.py 凭证 --scope gl --brief

# 有哪些模块？
python scripts/search.py --list-modules
```

只依赖 Python 3（标准库），无需安装任何第三方包。

---

## 检索脚本用法

```bash
python scripts/search.py <关键词...> [选项]
```

| 选项 | 说明 |
| :--- | :--- |
| `--scope S` | 检索范围，模块名可逗号组合（如 `gl,som,inv`），默认 `all` 全模块 |
| `--table` | 关键词按**表名**精确匹配（忽略大小写与首尾空格） |
| `--brief` | 精简输出：仅一行 `[模块] 表名 \| 中文名 \| 文件` |
| `--full` / `-d` | 输出命中条目的完整正文（不截断） |
| `--all` | 多个关键词需**全部**命中（默认任一命中即可） |
| `--limit N` | 最多返回结果数（默认 20） |
| `--max N` | 非 `--full` 时每条正文最多展示字符数（默认 1600） |
| `--list-modules` | 列出全部模块及各自的表数量 |

**设计要点**

- **Markdown 是唯一真相源**：脚本直接读 Markdown，不依赖任何预生成字典，
  不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- **精确到「表」而非「文件」**：一张表 = 一个 `## <中文名> t_<表名>` 块，
  多语言表（`_l`）、分录子表会被拆成独立条目。
- **全字段参与匹配**：表名、中文名、字段名、字段中文标题、备注（含枚举值定义）。
- 全库检索约 1–2 秒。

---

## 索引重建

`references/**/_INDEX.md` 全部由脚本从 Markdown 派生，**请勿手工编辑**：

```bash
python scripts/build_index.py          # 全量重建（224 个模块 + 总索引）
python scripts/build_index.py gl som   # 只重建指定模块
```

---

## 安装为 Skill

```bash
git clone https://github.com/silent-reader-cn/kingdee-sql-expert.git
mkdir -p ~/.workbuddy-ai/skills/kingdee-sql-expert
cp -r kingdee-sql-expert/. ~/.workbuddy-ai/skills/kingdee-sql-expert/
```

安装后，AI 助手在遇到金蝶库表问题时会自动加载本 skill，并用 `scripts/search.py` 定位表结构。

---

## 目录结构

```
kingdee-sql-expert/
├── SKILL.md                    # Skill 定义：检索用法 + 金蝶库表约定 + 示例流程
├── README.md
├── LICENSE
├── scripts/
│   ├── search.py               # 统一检索（22,769 张表）
│   └── build_index.py          # 从 Markdown 生成 _INDEX.md
└── references/
    ├── _INDEX.md               # 总索引：224 个模块统计概览
    └── <模块>_files/
        ├── _INDEX.md           # 本模块表清单
        └── <对象>.md           # 表定义（可含主表/分录/多语言表多个 ## 块）
```

---

## 免责声明

本仓库内容整理自金蝶云苍穹数据字典导出，仅供学习、开发与运维参考。
表结构、字段与枚举的最终解释权归金蝶所有，请以你所在环境的实际数据库为准。

## License

[MIT](./LICENSE) © 2026 silent-reader-cn
