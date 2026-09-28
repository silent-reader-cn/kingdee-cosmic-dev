# 对账单任务-reconcilia_download_task

## 对账单任务-主表 t_receipt_reconcilia_task

- **表名称：** 对账单任务-主表
- **表名：** t_receipt_reconcilia_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbank_login | 前置机 | int8 | 64 |  |  | null | 银企连接通道配置 aqap_bank_login |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | facc_no | 账号 | int8 | 64 |  |  | null | 银企账户 aqap_bank_acnt |
| 7 | fcomplete_time | 下载完成时间 | timestamp | 0 |  |  | null | 下载完成时间 |
| 8 | fupload_num | 对账单上传数量 | int8 | 64 |  |  | null | 对账单上传数量 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | freconcilia_num | 对账单下载数量 | int8 | 64 |  |  | null | 对账单下载数量 |
| 11 | ftrans_date | 对账单日期 | timestamp | 0 |  |  | null | 对账单日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 14 | fexp_msg | 异常提示信息 | varchar | 512 |  | √ | ' ' | 异常提示信息 |
| 15 | fstatus | 对账单下载任务状态 | varchar | 50 |  | √ | ' ' | 对账单下载任务状态,枚举: 1 :已创建 2 :预处理中 3 :预处理完成 4 :下载中 5 :下载完成 6 :失败待重试 10 :完成 11 :失败 |
| 16 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 18 | fredo | 重新下载次数 | int8 | 64 |  |  | null | 重新下载次数 |
| 19 | fexp_msg_tag | 异常提示信息_详情 | text | 0 |  |  | null | 异常提示信息_详情 |
| 20 | fupload_flag | 对账单上传任务状态 | varchar | 50 |  | √ | ' ' | 对账单上传任务状态,枚举: 1 :未上传 2 :部分上传 3 :全部上传 4 :全部失败 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_reconcilia_task_pkey |  | fid |
| 2 | idx_reconcili_t_bd_index |  | fbank_version,ftrans_date |
| 3 | idx_reconcili_task_index |  | facc_no,fstatus,ftrans_date |
| 4 | idx_reconcili_t_t_index |  | ftrans_date |
