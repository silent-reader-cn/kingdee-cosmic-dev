# 单据回单关系表-eafc_bill_bank_receipt

## 单据回单关系表-主表 tk_eafc_bill_bank

- **表名称：** 单据回单关系表-主表
- **表名：** tk_eafc_bill_bank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_bankreceiptno | 银行回单唯一ID | varchar | 100 |  | √ | ' ' | 银行回单唯一ID |
| 3 | fk_eafc_createdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fk_eafc_billid | 单据主键ID | int8 | 64 |  |  | null | 单据主键ID |
| 5 | fk_eafc_bill_no | 单据唯一ID | varchar | 100 |  | √ | ' ' | 单据唯一ID |
| 6 | fk_eafc_modifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 8 | fk_eafc_seq | 序号 | int8 | 64 |  |  | null | 序号 |
| 9 | fk_eafc_bank_receipt_id | 银行回单主键ID | int8 | 64 |  |  | null | 银行回单主键ID |
| 10 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_bill_bank |  | fid |
| 2 | idx_eafc_bill_bank_bid |  | fk_eafc_billid |
