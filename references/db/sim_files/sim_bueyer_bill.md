# 发票购方统计单据-sim_bueyer_bill

## 发票购方统计单据-主表 t_sim_bueyer_bill

- **表名称：** 发票购方统计单据-主表
- **表名：** t_sim_bueyer_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyertaxno | 购方税号 | varchar | 50 |  | √ | ' ' | 购方税号 |
| 3 | ftotaltax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :电子普票 028 :电子专票 |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | finvoicenum | 发票数量 | int8 | 64 |  | √ | 0 | 发票数量 |
| 8 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_bueyer_bill |  | fid |
| 2 | idx_sim_buyer_bill |  | fdate |
