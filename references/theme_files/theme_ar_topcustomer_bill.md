# 前五大客户应收分析表-theme_ar_topcustomer_bill

## 前五大客户应收分析表-主表 t_theme_ar_topcustomer

- **表名称：** 前五大客户应收分析表-主表
- **表名：** t_theme_ar_topcustomer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomerfield | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fbaddebt | 坏账准备 | numeric | 23 | 10 |  | null | 坏账准备 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbookbalance | 账面余额 | numeric | 23 | 10 |  | null | 账面余额 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | farratio | 占应收款比例 | numeric | 23 | 10 |  | null | 占应收款比例 |
| 10 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_ar_topcustomer |  | fid |
| 2 | idx_ar_topcustomer_report |  | fipoorgld,freportdate |
