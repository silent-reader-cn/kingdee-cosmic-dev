# 余额对账详情表-aqap_balance_rec_detail

## 余额对账详情表-主表 t_aqap_balance_rec_detail

- **表名称：** 余额对账详情表-主表
- **表名：** t_aqap_balance_rec_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatement_no | 对账单编号 | varchar | 50 |  | √ | ' ' | 对账单编号 |
| 3 | fbank_status | 银行响应码 | varchar | 50 |  | √ | ' ' | 银行响应码 |
| 4 | fbank_version_id | 银行版本编号 | varchar | 50 |  | √ | ' ' | 银行版本编号 |
| 5 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 6 | freversed_sys_field | 系统备用字段 | varchar | 600 |  | √ | ' ' | 系统备用字段 |
| 7 | fhandle_num | 反馈次数 | int4 | 32 |  | √ | 0 | 反馈次数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: EB_PROCESSING :银企处理中 BANK_PROCESSING :银行处理中 BANK_COMPLETED :对账完成 BANK_FAIL :对账失败 BANK_EXCEPTION :对账异常 OTHER_COMPLETED :其他途径反馈 |
| 10 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fhandle_status | 反馈状态 | int4 | 32 |  | √ | 0 | 反馈状态 |
| 13 | fmonth | 月份文本字符串 | varchar | 50 |  | √ | ' ' | 月份文本字符串 |
| 14 | fsync_date | 交易月份 | timestamp | 0 |  |  | null | 交易月份 |
| 15 | facc_id | 账号基础资料 | int8 | 64 |  | √ | 0 | 银企账户 aqap_bank_acnt |
| 16 | fcurrency_id | 币别基础资料 | int8 | 64 |  | √ | 0 | ISO币别管理 aqap_iso_currency |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | freversed_biz_field | 业务备用字段 | varchar | 600 |  | √ | ' ' | 业务备用字段 |
| 19 | fback_status | fback_status | varchar | 50 |  | √ | ' ' |  |
| 20 | fversion | 数据版本号 | int4 | 32 |  | √ | 0 | 数据版本号 |
| 21 | fflag | 返回信息类型 | varchar | 50 |  | √ | ' ' | 返回信息类型,枚举: 0 :报文 1 :文件 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fbank_login | 前置机编号 | int8 | 64 |  | √ | 0 | 银企连接通道配置 aqap_bank_login |
| 25 | foperator | 操作人 | varchar | 50 |  | √ | ' ' | 操作人 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | freason | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |
| 30 | fbank_login_id | 银企连接通道编号 | varchar | 50 |  | √ | ' ' | 银企连接通道编号 |
| 31 | fbank_status_msg | 银行响应信息 | varchar | 200 |  | √ | ' ' | 银行响应信息 |
| 32 | ffile_path | 文件路径 | varchar | 255 |  | √ | ' ' | 文件路径 |
| 33 | fbank_version | 银行版本 | int8 | 64 |  | √ | 0 | 银行启用管理 aqap_bank |
| 34 | freserved2 | 备用字段2 | varchar | 100 |  | √ | ' ' | 备用字段2 |
| 35 | fcheck_status | 余额核对状态 | varchar | 50 |  | √ | ' ' | 余额核对状态,枚举: Y :相符 N :不符 |
| 36 | freserved3 | 备用字段3 | varchar | 100 |  | √ | ' ' | 备用字段3 |
| 37 | fstatus_name | 状态中文描述 | varchar | 50 |  | √ | ' ' | 状态中文描述 |
| 38 | freserved1 | 备用字段1 | varchar | 100 |  | √ | ' ' | 备用字段1 |
| 39 | fbalance | 余额 | varchar | 50 |  | √ | ' ' | 余额 |
| 40 | fsubmit_success_time | 提交银行成功时间 | timestamp | 0 |  |  | null | 提交银行成功时间 |
| 41 | fstatus_id | 状态整数 | int8 | 64 |  | √ | 0 | 状态整数 |
| 42 | fquery_num | 同步状态次数 | int4 | 32 |  | √ | 0 | 同步状态次数 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcombofield | 修改前状态 | varchar | 50 |  | √ | ' ' | 修改前状态,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rec_detail_fsyncdate |  | fsync_date |
| 2 | idx_rec_detail__fcurrency |  | fcurrency |
| 3 | unidx_balance_rec_detail |  | facc_no,fcurrency,fsync_date |
| 4 | pk_t_aqap_balance_rec_detail |  | fid |
