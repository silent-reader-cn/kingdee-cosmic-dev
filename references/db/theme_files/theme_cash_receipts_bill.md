# 现金收款分析表-theme_cash_receipts_bill

## 单据体-子表 t_theme_cash_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_cash_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 5 | fcount | 笔数 | int8 | 64 |  | √ | 0 | 笔数 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_cash_entryentity |  | fentryid |
| 2 | idx_cash_entryentity_customer |  | fcustomer |

---

## 现金收款分析表-主表 t_theme_cash_receipts

- **表名称：** 现金收款分析表-主表
- **表名：** t_theme_cash_receipts

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcurrenttotalreceipts | 当期总收款金额 | numeric | 23 | 10 |  | null | 当期总收款金额 |
| 6 | fratio | 现金收款占比（%） | numeric | 23 | 10 |  | null | 现金收款占比（%） |
| 7 | ftaotlcount | 总笔数 | int8 | 64 |  | √ | 0 | 总笔数 |
| 8 | ftotal | 合计 | numeric | 23 | 10 |  | null | 合计 |
| 9 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_cash_receipts |  | fid |
| 2 | idx_cash_receipts_report |  | freportdate,fipoorgld |
