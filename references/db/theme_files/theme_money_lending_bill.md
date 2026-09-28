# 资金拆借分析表-theme_money_lending_bill

## 单据体-子表 t_theme_money_entryentity

- **表名称：** 单据体-子表
- **表名：** t_theme_money_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopeningbalance | 期初余额 | numeric | 23 | 10 |  | null | 期初余额 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frepaybalance | 偿还余额 | numeric | 23 | 10 |  | null | 偿还余额 |
| 7 | floanamount | 借出金额 | numeric | 23 | 10 |  | null | 借出金额 |
| 8 | fclosingbalance | 期末余额 | numeric | 23 | 10 |  | null | 期末余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_money_entryentity_report |  | freportdate |
| 2 | pk_theme_money_entryentity |  | fentryid |

---

## 资金拆借分析表-主表 t_theme_money_lending

- **表名称：** 资金拆借分析表-主表
- **表名：** t_theme_money_lending

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '1' | 是否叶子节点 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | faccounttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :合计 1 :其他应收款 2 :内部往来 |
| 7 | frdetermination | 关联方 | int8 | 64 |  | √ | 0 | 关联关系认定表 theme_rdetermination_bill |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_money_lending |  | fid |
| 2 | idx_money_lending_rdete |  | fipoorgld,frdetermination |
