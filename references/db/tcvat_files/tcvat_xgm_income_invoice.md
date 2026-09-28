# 小规模收入台账已开票明细-tcvat_xgm_income_invoice

## 小规模收入台账已开票明细-主表 t_tcvat_xgm_income_invoic

- **表名称：** 小规模收入台账已开票明细-主表
- **表名：** t_tcvat_xgm_income_invoic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 50 |  | √ | ' ' | 所属月份 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型 |
| 5 | ftaxrate | 税率/征收率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率/征收率 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 9 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 10 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 11 | ffiltercondition | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_xgm_income_invoic_pkey |  | fid |
| 2 | idx_tcvat_xgm_income_invoic |  | forgid,ftaxperiod |
