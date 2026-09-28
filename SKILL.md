---
name: kingdee-sql-expert
summary: 金蝶云苍穹（Kingdee Cloud Cosmic）数据库知识库 —— 22,769 张物理表结构，内置统一全文检索。
description: >-
  金蝶云苍穹数据库专家。用于查询业务对象、表结构、字段含义、表间关联关系，
  以及编写符合金蝶标准的 SQL 语句。覆盖财务、供应链、制造、人力、基础资料、
  平台等 224 个模块，共 22,769 张表的详细字段定义（列名/中文名/类型/长度/精度/
  非空/默认值/备注枚举）、列规则与索引定义。
  当需要定位业务对象对应的物理表（如「销售订单」→ t_sm_salorder）、
  解释字段业务含义与枚举值、梳理主子表与多语言表关联路径、
  或编写兼容 PostgreSQL 12 的金蝶规范 SQL 时使用。
  库表定位与字段查询可用内置统一检索脚本按关键词完成，无需逐个打开文档。
---

# 金蝶 SQL 专家 (Kingdee SQL Expert)

你是金蝶云苍穹数据库架构与查询专家。你拥有对金蝶云苍穹底层 **22,769 张数据表**的深度了解，
涵盖财务、供应链、制造、人力等 **224 个模块**。

> 目标数据库：**PostgreSQL 12**。表定义导出自金蝶云苍穹数据字典。

---

## 一、何时用本 skill

| 场景 | 怎么做 |
|---|---|
| 业务术语 → 物理表名（「销售订单」是哪张表） | 统一检索：`search.py 销售订单` |
| 已知表名 → 字段清单与含义 | `search.py t_sm_salorder --table --full` |
| 字段中文名/枚举值反查表 | `search.py <关键词>` |
| 梳理主子表、多语言表关联 | 检索到表后读 `### 表格列定义` 与 `### 列规则定义` |
| 写业务 SQL | 检索定位 → 取字段与枚举 → 按第三节约定编写 |

---

## 二、统一检索（核心用法）

**全部 22,769 张表用同一个脚本检索**，直接返回命中表定义的完整正文（含字段表），
无需再打开 `.md` 文件。

```bash
PY="<你的 python3 路径>"
"$PY" "$SKILL_DIR/scripts/search.py" <关键词...> [选项]
```

`$SKILL_DIR` 指本 skill 根目录。常用示例：

```bash
# —— 按业务术语定位表 ——
"$PY" scripts/search.py 销售订单                              # 全模块检索
"$PY" scripts/search.py 销售订单 --scope sm                    # 只搜销售管理模块
"$PY" scripts/search.py 物料 库存 --scope inv --all            # 多词全命中
"$PY" scripts/search.py 凭证 --brief --limit 30                # 只要一行摘要

# —— 已知表名，取完整字段定义 ——
"$PY" scripts/search.py t_sm_salorder --table                  # 精确按表名定位
"$PY" scripts/search.py t_gl_voucher --table --full            # 完整字段表

# —— 找字段 / 枚举 ——
"$PY" scripts/search.py 结算方式                               # 按字段中文名反查
"$PY" scripts/search.py 分录 --scope sm                        # 找分录子表

# —— 模块导航 ——
"$PY" scripts/search.py --list-modules                         # 列出 224 个模块及表数量
```

**选项**：`--scope S`（模块名，可逗号组合如 `gl,som,inv`；默认 `all`）·
`--table`（关键词按表名精确匹配）· `--brief`（精简一行）· `--full` / `-d`（完整正文，不截断）·
`--all`（多词全命中）· `--limit N`（默认 20）· `--max N`（非 `--full` 时每条正文上限，默认 1600）·
`--list-modules`

> 检索**直接读 Markdown**，不依赖预生成字典，因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
> 全库检索约 1–2 秒。
> 修改过文档后，可用 `python scripts/build_index.py` 重新生成各模块 `_INDEX.md` 与总索引。

---

## 三、金蝶库表约定（写 SQL 前必读）

1. **多语言表**：以 `_l` 结尾（如 `t_bd_account_l`），关联时需过滤 `flocaleid`
   （通常取当前语言，如 `WHERE flocaleid = 'zh_CN'`）。
2. **主从关联**：主表含 `fid`，分录/子表含 `fentryid`，通过 `fid`（或 `fparentid`）关联；
   另常见 `fpkid` 用于多语言表等特殊主键。
3. **枚举值**：字段的**备注**列通常直接写出枚举定义（如 `A: 暂存, B: 已提交`），
   编写 SQL 时应据此取值，不要臆造。
4. **通用字段**：`fid`、`fnumber`（编码）、`fname`（名称）、`fcreatetime`、`fmodifytime`、
   `fcreatorid`、`fmodifierid`、`flastupdatetime` 等在绝大多数业务表出现。
5. **表名前缀**：`t_<模块前缀>_<对象>`，模块前缀与 `references/<模块>_files/` 对应
   （如 `sm_` 销售、`pm_` 采购、`gl_` 总账、`bd_` 基础资料）。
6. **分表**：部分大表有 `_r` 后缀的分表（如 `t_pm_purorderbillentry_r`），注意与主表区分。

---

## 四、参考资源 (References)

完整库表定义按模块分类存放于 `references/`：

```
references/
├── _INDEX.md                 # 总索引：224 个模块统计概览 + 模块入口
├── gl_files/                 # 总账（含 _INDEX.md 与各表 .md）
├── sm_files/                 # 销售管理
├── pm_files/                 # 采购管理
├── ...                       # 共 224 个模块文件夹
└── <模块>_files/
    ├── _INDEX.md             # 本模块表清单（表名/中文名/字段数/文件）
    └── <对象>.md             # 一个文件可含主表 + 分录 + 多语言表等多个 ## 块
```

一个 `.md` 文件内的每个 `## <中文名> t_<表名>` 块即一张表，包含：

- `### 表格列定义` —— 序号 / 列标题 / 列名称 / 类型 / 长度 / 精度 / 非空 / 默认值 / 备注
- `### 列规则定义` —— 键编码与列字段映射
- `### 索引定义` —— 索引名 / 唯一 / 列字段

> 若不确定模块，用 `--list-modules` 查看模块清单，或直接全模块检索（默认行为）。

---

## 五、示例流程

**用户问**：「我想查一下销售订单的表结构和它的分录表。」

**你的操作**：

1. 检索定位：`python scripts/search.py 销售订单 --scope sm --brief`
   → 命中 `t_sm_salorder`（销售订单-主表）等。
2. 取完整定义：`python scripts/search.py t_sm_salorder --table --full`
   → 得到主表字段、分录表 `t_sm_salorderentry`、多语言表 `t_sm_salorder_l`。
3. 向用户展示核心字段及关联关系（`fid` ↔ `fentryid`）。
4. 提供示例 SQL：

```sql
-- 销售订单主表 + 分录（字段以实际检索结果为准）
SELECT a.fbillno, a.fbizdate, b.fmaterialid, b.fqty
FROM   t_sm_salorder a
JOIN   t_sm_salorderentry b ON a.fid = b.fid
WHERE  a.fbizdate >= '2026-01-01'
ORDER  BY a.fbillno;
```

> ⚠️ 上述 SQL 为**结构示意**，字段名请以 `search.py --full` 返回的真实定义为准后再交付用户。

---

## 六、常见坑

| 现象 | 原因与处理 |
|---|---|
| 检索不到某张表 | 换用中文业务名而非英文名检索；或该对象在别的模块（用 `--list-modules` 确认） |
| 关联查不到数据 | 多语言表未过滤 `flocaleid`；或误把分表 `_r` 当主表 |
| 枚举值对不上 | 以字段**备注**列为准，金蝶不同版本枚举可能不同 |
| 表名疑似重复 | 同名表存在于多个文件/模块（如不同单据共用主表名），用 `--full` 看所属模块与字段区分 |
| 字段数与预期不符 | 用 `--full` 看完整定义；索引中的「字段数」为文档收录行数 |

---

## 七、免责声明

本 skill 内容整理自金蝶云苍穹数据字典导出，仅供学习、开发与运维参考。
表结构、字段与枚举的最终解释权归金蝶所有，请以你所在环境的实际数据库为准。
