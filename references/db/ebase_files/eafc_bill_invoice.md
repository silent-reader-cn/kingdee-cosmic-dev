# 单据发票关系表-eafc_bill_invoice

## 单据发票关系表-主表 tk_eafc_bill_invoice

- **表名称：** 单据发票关系表-主表
- **表名：** tk_eafc_bill_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_timefield1 | 时间1 | int4 | 32 |  |  | null | 时间1 |
| 3 | fk_eafc_textfield | 单据唯一ID | varchar | 100 |  | √ | ' ' | 单据唯一ID |
| 4 | fk_eafc_seq | 序号 | int8 | 64 |  |  | null | 序号 |
| 5 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fk_eafc_bill_id | 单据主键ID | int8 | 64 |  |  | null | 单据主键ID |
| 7 | fk_eafc_textfield1 | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 8 | fk_eafc_timefield | 时间 | int4 | 32 |  |  | null | 时间 |
| 9 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 10 | fk_eafc_invoice_id | 发票主键ID | int8 | 64 |  |  | null | 发票主键ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_bill_inv_uid |  | fk_eafc_textfield,fk_eafc_textfield1 |
| 2 | idx_eafc_bill_invoice_bid |  | fk_eafc_bill_id |
| 3 | pk__eafc_bill_invoice |  | fid |
