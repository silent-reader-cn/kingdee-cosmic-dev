# 回单结果列表-receipt_result

## 回单结果列表-主表 t_receipt_detail

- **表名称：** 回单结果列表-主表
- **表名：** t_receipt_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ffile_name | 本地存储文件名 | varchar | 400 |  | √ | ' ' | 本地存储文件名 |
| 3 | fbank_file_path | 银行返回文件名及路径 | varchar | 400 |  | √ | ' ' | 银行返回文件名及路径 |
| 4 | facc_no | 账号 | int8 | 64 |  |  | null | [银企账户 aqap_bank_acnt](../aqap_files/aqap_bank_acnt.md) |
| 5 | fcomplete_time | 下载完成时间 | timestamp | 0 |  |  | null | 下载完成时间 |
| 6 | fmd5_tag | 文件md5值_详情 | text | 0 |  |  | null | 文件md5值_详情 |
| 7 | fmatch_flag | 是否匹配到明细 | varchar | 50 |  | √ | ' ' | 是否匹配到明细,枚举: 0 :未开始匹配 1 :匹配成功 2 :匹配失败 |
| 8 | fdetail_id | 匹配到的明细编号 | varchar | 50 |  | √ | ' ' | 匹配到的明细编号 |
| 9 | frefid | 回单任务id | varchar | 50 |  | √ | ' ' | 回单任务id |
| 10 | ftrans_date | 回单日期 | timestamp | 0 |  |  | null | 回单日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fupload_exp_msg | 上传错误提示信息 | varchar | 255 |  | √ | ' ' | 上传错误提示信息 |
| 13 | fexp_msg | 下载异常信息 | varchar | 512 |  | √ | ' ' | 下载异常信息 |
| 14 | fstatus | 回单任务状态 | varchar | 50 |  | √ | ' ' | 回单任务状态,枚举: 1 :已创建 2 :预处理中 3 :预处理完成 4 :下载中 5 :下载完成 6 :失败待重试 7 :完整度检查中 8 :完整度检查完成 9 :回单码匹配中 10 :完成 11 :失败 |
| 15 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fofd_json | 光大ofd相关字段 | varchar | 2000 |  | √ | ' ' | 光大ofd相关字段 |
| 18 | fupload_exp_msg_tag | 上传错误提示信息_详情 | text | 0 |  |  | null | 上传错误提示信息_详情 |
| 19 | fupload_redo | 上传重试次数 | int8 | 64 |  |  | null | 上传重试次数 |
| 20 | fmatch_is_defect | 回单码是否缺失 | varchar | 255 |  | √ | '1' | 回单码是否缺失,枚举: 0 :是 1 :否 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fmatch_defect_desc | 回单码缺失描述 | varchar | 512 |  | √ | ' ' | 回单码缺失描述 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdetail_no | 交易明细匹配码 | varchar | 400 |  | √ | ' ' | 交易明细匹配码 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fbank_login | 前置机 | int8 | 64 |  |  | null | [银企连接通道配置 aqap_bank_login](../aqap_files/aqap_bank_login.md) |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fupload_time | 上传完成时间 | timestamp | 0 |  |  | null | 上传完成时间 |
| 29 | fmd5 | 文件md5值 | varchar | 255 |  | √ | ' ' | 文件md5值 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fbank_version | 银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 32 | fupload_file_name | 上传到苍穹返回的文件名及路径 | varchar | 400 |  | √ | ' ' | 上传到苍穹返回的文件名及路径 |
| 33 | fupload_flag | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态,枚举: 0 :未上传 1 :上传中 2 :上传完成 3 :上传失败 |
| 34 | fquery_flag | 文件是否删除 | varchar | 50 |  | √ | ' ' | 文件是否删除 |
| 35 | ffile_link | fetch返回的参数 | varchar | 400 |  | √ | ' ' | fetch返回的参数 |
| 36 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_receipt_t_d_u_index |  | fupload_flag |
| 2 | idx_receipt_t_d_s_index |  | fstatus |
| 3 | idx_receipt_task_d_index |  | frefid,fstatus |
| 4 | t_receipt_detail_pkey |  | fid |
| 5 | idx_receipt_task_d_pk |  | fdetail_no |
| 6 | idx_receipt_task_t_index |  | ftrans_date |
