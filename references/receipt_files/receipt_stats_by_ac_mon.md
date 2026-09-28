# 按月和账户统计-receipt_stats_by_ac_mon

## 按月和账户统计-主表 t_receipt_statistics

- **表名称：** 按月和账户统计-主表
- **表名：** t_receipt_statistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | trans_date | trans_date | timestamp | 0 |  |  | null |  |
| 3 | facc_no | 账号 | int8 | 64 |  |  | null | 银企账户 aqap_bank_acnt |
| 4 | fmatch_num | 回单匹配数量 | int8 | 64 |  |  | null | 回单匹配数量 |
| 5 | fzip_names_tag | fzip_names_tag | text | 0 |  |  | null |  |
| 6 | fupload_num | 回单上传数量 | int8 | 64 |  |  | null | 回单上传数量 |
| 7 | fzip_names | fzip_names | varchar | 255 |  | √ | ' ' |  |
| 8 | ftrans_month | 年月 | varchar | 50 |  | √ | ' ' | 年月 |
| 9 | ftrans_date | 回单日期 | timestamp | 0 |  |  | null | 回单日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | faccno | 银行账号（展示） | varchar | 50 |  | √ | ' ' | 银行账号（展示） |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 13 | fupload_pc | 回单上传率 | varchar | 50 |  | √ | ' ' | 回单上传率 |
| 14 | fcomplete_pc | 回单下载率 | varchar | 50 |  | √ | ' ' | 回单下载率 |
| 15 | ffile_num | ffile_num | int8 | 64 |  |  | null |  |
| 16 | freceipt_num | 回单下载数量 | int8 | 64 |  |  | null | 回单下载数量 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 19 | fdetail_num | 明细下载数量 | int8 | 64 |  |  | null | 明细下载数量 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fbank_login | 前置机 | int8 | 64 |  |  | null | 银企连接通道配置 aqap_bank_login |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fmatch_pc | 回单匹配率 | varchar | 50 |  | √ | ' ' | 回单匹配率 |
| 24 | fbank_version_name | 银行版本名称 | varchar | 50 |  | √ | ' ' | 银行版本名称 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 27 | fbank_login_name | 前置机编号 | varchar | 50 |  | √ | ' ' | 前置机编号 |
| 28 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_statistics_pkey |  | fid |
