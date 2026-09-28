# 第三方回款分析表-theme_tparty_return_bill

## 第三方回款分析表-主表 t_theme_tparty_return

- **表名称：** 第三方回款分析表-主表
- **表名：** t_theme_tparty_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | foperatingrevenue | 营业收入 | numeric | 23 | 10 |  | null | 营业收入 |
| 6 | fratio | 第三方回款比例（%） | numeric | 23 | 10 |  | null | 第三方回款比例（%） |
| 7 | ftotal | 合计 | numeric | 23 | 10 |  | null | 合计 |
| 8 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_tparty_return |  | fid |
| 2 | idx_tparty_return_report |  | freportdate,fipoorgld |

---

## 单据体-子表 t_theme_tpr_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_tpr_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fthirdparty | 实际回款第三方 | varchar | 50 |  | √ | ' ' | 实际回款第三方 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tpr_entryentity_customer |  | fcustomer |
| 2 | pk_theme_tpr_entryentity |  | fentryid |
