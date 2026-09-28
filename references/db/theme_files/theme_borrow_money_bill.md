# 借款分析表-theme_borrow_money_bill

## 借款分析表-主表 t_theme_borrow_money

- **表名称：** 借款分析表-主表
- **表名：** t_theme_borrow_money

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcurrentliabilities | 流动负债 | numeric | 23 | 10 |  | null | 流动负债 |
| 4 | fnoncurrentliabilities | 非流动负债 | numeric | 23 | 10 |  | null | 非流动负债 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fshortgrowthratio | 短期借款占流动负债比例 | numeric | 23 | 10 |  | null | 短期借款占流动负债比例 |
| 7 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 8 | flonggrowthratio | 长期借款占非流动负债比例 | numeric | 23 | 10 |  | null | 长期借款占非流动负债比例 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fshortgrowthrate | 短期借款余额增长率 | numeric | 23 | 10 |  | null | 短期借款余额增长率 |
| 13 | flonggrowthrate | 长期借款余额增长率 | numeric | 23 | 10 |  | null | 长期借款余额增长率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_borrow_money |  | fid |
| 2 | idx_borrow_money_report |  | freportdate,fipoorgld |

---

## 借款单据体-子表 t_theme_bm_entryentity

- **表名称：** 借款单据体-子表
- **表名：** t_theme_bm_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 3 | floantype | 分类 | varchar | 50 |  | √ | ' ' | 分类,枚举: 1 :短期借款 2 :长期借款 |
| 4 | fratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fitemname | 项目名 | varchar | 50 |  | √ | ' ' | 项目名 |
| 7 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_bm_entryentity |  | fentryid |
| 2 | idx_bm_entryentity_item |  | fitemname |
