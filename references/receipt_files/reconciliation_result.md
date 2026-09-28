# 对账单结果列表-reconciliation_result

## 对账单结果列表-主表 t_reconciliation_detail

- **表名称：** 对账单结果列表-主表
- **表名：** t_reconciliation_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ffile_name | 本地存储文件名 | varchar | 400 |  | √ | ' ' | 本地存储文件名 |
| 3 | fbank_file_path | 银行返回文件名及路径 | varchar | 400 |  | √ | ' ' | 银行返回文件名及路径 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | facc_no | 账号 | int8 | 64 |  |  | null | 银企账户 aqap_bank_acnt |
| 6 | fcomplete_time | 下载完成时间 | timestamp | 0 |  |  | null | 下载完成时间 |
| 7 | frefid | 对账单任务id | varchar | 50 |  | √ | ' ' | 对账单任务id |
| 8 | ftrans_date | 对账单日期 | timestamp | 0 |  |  | null | 对账单日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fupload_exp_msg | 上传错误提示信息 | varchar | 255 |  | √ | ' ' | 上传错误提示信息 |
| 11 | fexp_msg | 下载异常信息 | varchar | 512 |  | √ | ' ' | 下载异常信息 |
| 12 | fstatus | 对账单任务状态 | varchar | 50 |  | √ | ' ' | 对账单任务状态,枚举: 1 :已创建 2 :预处理中 3 :预处理完成 4 :下载中 5 :下载完成 6 :失败待重试 10 :完成 11 :失败 |
| 13 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fupload_exp_msg_tag | 上传错误提示信息_详情 | text | 0 |  |  | null | 上传错误提示信息_详情 |
| 16 | fupload_redo | 上传重试次数 | int8 | 64 |  |  | null | 上传重试次数 |
| 17 | fyear_month | 对账年月 | varchar | 50 |  | √ | ' ' | 对账年月 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fbank_login | 前置机 | int8 | 64 |  |  | null | 前置机管理_父类（供查询支付、电子回单继承） aqap_bank_login_parent |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | freconciliation_no | 对账单号 | varchar | 255 |  | √ | ' ' | 对账单号 |
| 24 | fupload_time | 上传完成时间 | timestamp | 0 |  |  | null | 上传完成时间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | ffeed_result | 反馈结果 | varchar | 50 |  | √ | ' ' | 反馈结果,枚举: success :反馈成功 fail :反馈失败 processing :反馈处理中 un_feed :未反馈 |
| 27 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 28 | fupload_file_name | 上传到苍穹返回的文件名及路径 | varchar | 400 |  | √ | ' ' | 上传到苍穹返回的文件名及路径 |
| 29 | fprotocol_no | 对账协议号 | varchar | 255 |  | √ | ' ' | 对账协议号 |
| 30 | fupload_flag | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态,枚举: 0 :未上传 1 :上传中 2 :上传完成 3 :上传失败 |
| 31 | ffile_link | fetch返回的参数 | varchar | 400 |  | √ | ' ' | fetch返回的参数 |
| 32 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reconcili_r_t_index |  | ftrans_date |
| 2 | idx_reconcili_r_d_u_index |  | fupload_flag |
| 3 | t_reconciliation_detail_pkey |  | fid |
| 4 | idx_reconcili_r_d_index |  | frefid,fstatus |
