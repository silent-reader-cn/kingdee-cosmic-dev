# 财务费用分析表-theme_finance_cost_bill

## 财务费用分析表-主表 t_theme_finance_cost

- **表名称：** 财务费用分析表-主表
- **表名：** t_theme_finance_cost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fccounttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :合计 |
| 6 | fitemname | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_finance_cost |  | fid |
| 2 | idx_finance_cost_item |  | fipoorgld,fitemname |

---

## 单据体-子表 t_theme_fc_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_fc_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostrate | 费用率 | numeric | 23 | 10 |  | null | 费用率 |
| 3 | fgrowthrate | 增长率 | numeric | 23 | 10 |  | null | 增长率 |
| 4 | fratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fc_entryentity_report |  | freportdate |
| 2 | pk_theme_fc_entryentity |  | fentryid |
