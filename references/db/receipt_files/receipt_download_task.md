# 回单任务-receipt_download_task

## 回单任务-主表 t_receipt_download_task

- **表名称：** 回单任务-主表
- **表名：** t_receipt_download_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbatch_no | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 3 | facc_no | 账号 | int8 | 64 |  |  | null | 银企账户 aqap_bank_acnt |
| 4 | fmatch_num | 回单匹配数量 | int8 | 64 |  | √ | 0 | 回单匹配数量 |
| 5 | fcomplete_time | 下载完成时间 | timestamp | 0 |  |  | null | 下载完成时间 |
| 6 | fzip_names_tag | 压缩包文件名_详情 | text | 0 |  |  | null | 压缩包文件名_详情 |
| 7 | fupload_num | 回单上传数量 | int8 | 64 |  | √ | 0 | 回单上传数量 |
| 8 | fzip_names | 压缩包文件名 | varchar | 255 |  | √ | ' ' | 压缩包文件名 |
| 9 | ftrans_date | 回单日期 | timestamp | 0 |  |  | null | 回单日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexp_msg | 异常提示信息 | varchar | 512 |  | √ | ' ' | 异常提示信息 |
| 12 | fstatus | 回单下载任务状态 | varchar | 50 |  | √ | ' ' | 回单下载任务状态,枚举: 1 :已创建 2 :预处理中 3 :预处理完成 4 :下载中 5 :下载完成 6 :失败待重试 7 :完整度检查中 8 :完整度检查完成 9 :回单码匹配中 10 :完成 11 :失败 |
| 13 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fexp_msg_tag | 异常提示信息_详情 | text | 0 |  |  | null | 异常提示信息_详情 |
| 16 | ffile_num | 回单文件数量 | int8 | 64 |  |  | null | 回单文件数量 |
| 17 | freceipt_num | 回单下载数量 | int8 | 64 |  | √ | 0 | 回单下载数量 |
| 18 | ftodays_flag | 是否当日回单 | varchar | 50 |  |  | '0' | 是否当日回单,枚举: 1 :是 0 :否 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fdetail_num | 明细下载数量 | int8 | 64 |  | √ | 0 | 明细下载数量 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fbank_login | 前置机 | int8 | 64 |  |  | null | 银企连接通道配置 aqap_bank_login |
| 24 | fdetail_flag | 明细下载状态 | varchar | 50 |  | √ | ' ' | 明细下载状态,枚举: 1 :未下载 2 :下载失败 3 :下载完成 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fsuggestion | 处理建议 | varchar | 50 |  | √ | ' ' | 处理建议,枚举: 1 :联系银行先推送回单 2 :请联系银行推送回单文件后再重新下载 3 :HTTP服务异常，请先检查回单前置机配置的前置机代理IP和端口是否正确 4 :检查远程SFTP服务是否正常登陆，可通过测试连接工验证，连接正常后重新下载 5 :联系银行开通权限或取消该账号的回单账号标识 6 :提单到金蝶银企技术支持部分析 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 29 | fredo | 重新下载次数 | int8 | 64 |  |  | null | 重新下载次数 |
| 30 | fupload_flag | 回单上传任务状态 | varchar | 50 |  | √ | ' ' | 回单上传任务状态,枚举: 1 :未上传 2 :部分上传 3 :全部上传 4 :全部失败 |
| 31 | fdefect_type | 回单缺失类型 | varchar | 50 |  | √ | ' ' | 回单缺失类型,枚举: 1 :银行未推送回单 2 :银行推送回单不全 3 :HTTP服务异常 4 :SFTP服务异常 5 :银行账户无权限 6 :其他异常 |
| 32 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_receipt_t_bd_index |  | fbank_version,ftrans_date |
| 2 | idx_receipt_task_index |  | facc_no,fstatus,ftrans_date |
| 3 | t_receipt_download_task_pk |  | facc_no,ftrans_date,fbank_login,fbank_version |
| 4 | t_receipt_download_task_pkey |  | fid |
| 5 | idx_receipt_t_t_index |  | ftrans_date |
