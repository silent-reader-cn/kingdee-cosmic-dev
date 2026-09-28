# 购买/赎回理财存储表-aqap_bd_financing

## 购买/赎回理财存储表-主表 t_aqap_bd_financing

- **表名称：** 购买/赎回理财存储表-主表
- **表名：** t_aqap_bd_financing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbatch_seq_id | 业务批次流水号 | varchar | 50 |  | √ | ' ' | 业务批次流水号 |
| 3 | farea_code | 地区码 | varchar | 50 |  | √ | ' ' | 地区码 |
| 4 | fbank_version_id | 银行版本号 | varchar | 50 |  | √ | ' ' | 银行版本号 |
| 5 | fproduct_code | 理财产品代码 | varchar | 50 |  | √ | ' ' | 理财产品代码 |
| 6 | fredeem_rate | 赎回费率 | varchar | 50 |  | √ | ' ' | 赎回费率 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftextfield | 赎回方式（农行） | varchar | 50 |  | √ | ' ' | 赎回方式（农行） |
| 9 | facc_name | 账号名称 | varchar | 50 |  | √ | ' ' | 账号名称 |
| 10 | fdetail_seq_id | 明细号 | varchar | 50 |  | √ | ' ' | 明细号 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fversion | 数据库锁版本号 | int8 | 64 |  |  | null | 数据库锁版本号 |
| 13 | fresponse_serial_no | 银企响应流水号, 银企的id | varchar | 50 |  | √ | ' ' | 银企响应流水号, 银企的id |
| 14 | fback_bank_status | 返回银行状态 | varchar | 50 |  | √ | ' ' | 返回银行状态 |
| 15 | flast_sync_time | 最后同步时间 | timestamp | 0 |  |  | null | 最后同步时间 |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fdetail_biz_no | 业务明细号 | varchar | 50 |  | √ | ' ' | 业务明细号 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fexpire_date | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 20 | fbank_status_msg | 银行返回状态消息 | varchar | 255 |  | √ | ' ' | 银行返回状态消息 |
| 21 | fcsh_dra_flag | 认购/赎回炒汇 | varchar | 50 |  | √ | ' ' | 认购/赎回炒汇 |
| 22 | freserved4 | 备用字段4 | varchar | 50 |  | √ | ' ' | 备用字段4 |
| 23 | fbuy_biz_no | 购买理财明细号（赎回关联购买） | varchar | 50 |  | √ | ' ' | 购买理财明细号（赎回关联购买） |
| 24 | freserved5 | 备用字段5 | varchar | 50 |  | √ | ' ' | 备用字段5 |
| 25 | freserved2 | 备用字段2 | varchar | 50 |  | √ | ' ' | 备用字段2 |
| 26 | freserved3 | 备用字段3 | varchar | 50 |  | √ | ' ' | 备用字段3 |
| 27 | freserved1 | 备用字段1 | varchar | 50 |  | √ | ' ' | 备用字段1 |
| 28 | fsubmit_success_time | 提交成功时间 | timestamp | 0 |  |  | null | 提交成功时间 |
| 29 | fnumber | 购买/赎回份数 | varchar | 50 |  | √ | ' ' | 购买/赎回份数 |
| 30 | ffoll_flag | 到期是否续存(1、续存，2、不续存)(工行) | varchar | 50 |  | √ | ' ' | 到期是否续存(1、续存，2、不续存)(工行) |
| 31 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | froll_date | 投资天数（工行） | varchar | 50 |  | √ | ' ' | 投资天数（工行） |
| 33 | fvalue_date | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 34 | fbank_status | 银行返回状态码 | varchar | 50 |  | √ | ' ' | 银行返回状态码 |
| 35 | fbank_batch_seq_id | 提交银行批次号 | varchar | 50 |  | √ | ' ' | 提交银行批次号 |
| 36 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 37 | ferror_msg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 38 | freversed_sys_field | 系统参数字段 | varchar | 500 |  | √ | ' ' | 系统参数字段 |
| 39 | famount | 购买/赎回金额 | numeric | 23 | 10 |  | null | 购买/赎回金额 |
| 40 | fprice | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 41 | ffinancing_type | 理财交易类型（购买B/赎回R） | varchar | 50 |  | √ | ' ' | 理财交易类型（购买B/赎回R） |
| 42 | fstatus | 交易状态 | varchar | 50 |  | √ | ' ' | 交易状态 |
| 43 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 44 | fsync_count | 同步次数 | int8 | 64 |  |  | null | 同步次数 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fsecurities_accno | 证券账户（招行） | varchar | 50 |  | √ | ' ' | 证券账户（招行） |
| 47 | frolldate | frolldate | varchar | 50 |  | √ | ' ' |  |
| 48 | febg_id | 所属节点 | varchar | 50 |  | √ | ' ' | 所属节点 |
| 49 | freversed_biz_field | 业务参数字段 | varchar | 500 |  | √ | ' ' | 业务参数字段 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fredeem_flag | 赎回标记（招行） | varchar | 50 |  | √ | ' ' | 赎回标记（招行） |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 54 | fprofit_amt | 收益金额 | numeric | 23 | 10 |  | null | 收益金额 |
| 55 | fbank_financing_seq_id | 银行业务参考号，传给银行的唯一码 | varchar | 50 |  | √ | ' ' | 银行业务参考号，传给银行的唯一码 |
| 56 | fproduct_name | 理财产品简称 | varchar | 50 |  | √ | ' ' | 理财产品简称 |
| 57 | fprofit_rate | 收益率 | varchar | 50 |  | √ | ' ' | 收益率 |
| 58 | fbank_login_id | 银行前置机编号 | varchar | 50 |  | √ | ' ' | 银行前置机编号 |
| 59 | fback_amount | 银行返回金额 | numeric | 23 | 10 |  | null | 银行返回金额 |
| 60 | fback_error_msg | 返回异常信息 | varchar | 255 |  | √ | ' ' | 返回异常信息 |
| 61 | fstatus_msg | 交易状态描述 | varchar | 50 |  | √ | ' ' | 交易状态描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_fin_batch_seq |  | fbatch_seq_id |
| 2 | idx_aqap_fin_createtime_index |  | fcreatetime |
| 3 | idx_aqap_fin_uindex |  | fdetail_biz_no,fstatus |
| 4 | t_aqap_bd_financing_pkey |  | fid |
| 5 | idx_aqap_fin_acc_index |  | facc_no |
