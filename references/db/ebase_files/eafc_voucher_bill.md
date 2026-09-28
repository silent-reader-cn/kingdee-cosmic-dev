# 凭证单据关系表-eafc_voucher_bill

## 凭证单据关系表-主表 tk_eafc_voucher_bill

- **表名称：** 凭证单据关系表-主表
- **表名：** tk_eafc_voucher_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_bill_no | 单据唯一ID | varchar | 100 |  | √ | ' ' | 单据唯一ID |
| 3 | fk_eafc_voucher_no | 凭证唯一ID | varchar | 100 |  | √ | ' ' | 凭证唯一ID |
| 4 | fk_eafc_createtime | 创建时间 | int4 | 32 |  |  | null | 创建时间 |
| 5 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fk_eafc_seq | 序号 | int8 | 64 |  |  | null | 序号 |
| 7 | fk_eafc_bill_id | 单据主键ID | int8 | 64 |  |  | null | 单据主键ID |
| 8 | fk_eafc_voucher_id | 凭证主键ID | int8 | 64 |  |  | null | 凭证主键ID |
| 9 | fk_eafc_updatetime | 更新时间 | int4 | 32 |  |  | null | 更新时间 |
| 10 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_voucher_bill_v |  | fk_eafc_voucher_no,fk_eafc_voucher_id |
| 2 | pk__eafc_voucher_bill |  | fid |
| 3 | idx_eafc_voucher_bill_b |  | fk_eafc_bill_no,fk_eafc_bill_id |
| 4 | idx_eafc_voucher_bill_bid |  | fk_eafc_bill_id |
| 5 | idx_eafc_voucher_bill_uid |  | fk_eafc_voucher_no,fk_eafc_bill_no |
| 6 | idx_eafc_voucher_bill_vid |  | fk_eafc_voucher_id |
| 7 | idx_eafc_voucher_bill_batch |  | fk_eafc_batchnum |
