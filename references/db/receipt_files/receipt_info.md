# 回单信息-receipt_info

## 回单信息-主表 t_receipt_info

- **表名称：** 回单信息-主表
- **表名：** t_receipt_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftask_num | 实际任务数 | int8 | 64 |  |  | null | 实际任务数 |
| 6 | fbatch_no | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 7 | fcompeleted_flag | 是否完成 | varchar | 50 |  | √ | ' ' | 是否完成 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | ftrans_date | 回单日期 | timestamp | 0 |  |  | null | 回单日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbank_version | 银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 12 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffile_num | 回单文件数 | int8 | 64 |  |  | null | 回单文件数 |
| 15 | fneed_create_num | 待建任务数 | int8 | 64 |  |  | null | 待建任务数 |
| 16 | freceipt_acnt_num | 应建任务数 | int8 | 64 |  |  | null | 应建任务数 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_receipt_t_i_index |  | fbank_version,ftrans_date |
| 2 | t_receipt_info_pkey |  | fid |
| 3 | idx_receipt_info_pk |  | ftrans_date,fbank_version |
