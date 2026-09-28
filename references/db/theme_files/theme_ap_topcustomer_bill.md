# 前五大供应商应付分析表-theme_ap_topcustomer_bill

## 前五大供应商应付分析表-主表 t_theme_ap_topcustomer

- **表名称：** 前五大供应商应付分析表-主表
- **表名：** t_theme_ap_topcustomer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fapratio | 占比 | numeric | 23 | 10 |  | null | 占比 |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsupplierfield | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 9 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_topcustomer_report |  | freportdate,fipoorgld |
| 2 | pk_theme_ap_topcustomer |  | fid |
