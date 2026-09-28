# 凭证回单关系日志-eafc_voucher_bank_log

## 凭证回单关系日志-主表 tk_eafc_voucher_bank_log

- **表名称：** 凭证回单关系日志-主表
- **表名：** tk_eafc_voucher_bank_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_voucher_no | 凭证唯一ID | varchar | 50 |  | √ | ' ' | 凭证唯一ID |
| 3 | fk_eafc_createtime | 创建时间 | int4 | 32 |  |  | null | 创建时间 |
| 4 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 5 | fk_eafc_seq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fk_eafc_bank_receipt_id | 银行回单主键ID | int8 | 64 |  | √ | 0 | 银行回单主键ID |
| 7 | fk_eafc_textfield1 | 银行回单唯一ID | varchar | 50 |  | √ | ' ' | 银行回单唯一ID |
| 8 | fk_eafc_updatetime | 更新时间 | int4 | 32 |  |  | null | 更新时间 |
| 9 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 10 | fk_eafc_voucherid | 凭证主键ID | int8 | 64 |  | √ | 0 | 凭证主键ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_voucher_bank_log |  | fid |
