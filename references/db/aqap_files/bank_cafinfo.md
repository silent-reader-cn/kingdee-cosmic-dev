# 活期定期业务-bank_cafinfo

## 活期定期业务-多语言表 t_aqap_bank_cafinfo_l

- **表名称：** 活期定期业务-多语言表
- **表名：** t_aqap_bank_cafinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_cafinfo_l_pkey |  | fpkid |
| 2 | idx_aqap_bank_cafinfo_l_0 |  | fid,flocaleid |

---

## 活期定期业务-主表 t_aqap_bank_cafinfo

- **表名称：** 活期定期业务-主表
- **表名：** t_aqap_bank_cafinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbatch_seq_id | 业务批次流水号 | varchar | 50 |  | √ | ' ' | 业务批次流水号 |
| 3 | fratedate | 起息日 | varchar | 50 |  | √ | ' ' | 起息日 |
| 4 | fexpireop | 到期处理方式 | varchar | 50 |  | √ | ' ' | 到期处理方式 |
| 5 | fcur_acc | 活期账号 | varchar | 50 |  | √ | ' ' | 活期账号 |
| 6 | fdetail_seq | 业务流转号 | varchar | 50 |  | √ | ' ' | 业务流转号 |
| 7 | fclosedate | 销户日 | varchar | 50 |  | √ | ' ' | 销户日 |
| 8 | fnotify_id | 通知ID | varchar | 50 |  | √ | ' ' | 通知ID |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 到期日 | varchar | 50 |  | √ | ' ' | 到期日 |
| 11 | frate | 利率 | varchar | 50 |  | √ | ' ' | 利率 |
| 12 | fcur_name | 活期账户名 | varchar | 50 |  | √ | ' ' | 活期账户名 |
| 13 | fdetail_seq_id | 明细号 | varchar | 50 |  | √ | ' ' | 明细号 |
| 14 | fbank_msg | 银行信息 | varchar | 750 |  | √ | ' ' | 银行信息 |
| 15 | fversion | 版本控制 | int8 | 64 |  |  | null | 版本控制 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fback_bank_status | 返回银行状态 | varchar | 50 |  | √ | ' ' | 返回银行状态 |
| 18 | fdetail_biz_no | 业务明细号 | varchar | 50 |  | √ | ' ' | 业务明细号 |
| 19 | ftrandate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 20 | fdraw_type | 支取方式 | varchar | 50 |  | √ | ' ' | 支取方式 |
| 21 | fexplanation | 摘要 | varchar | 100 |  | √ | ' ' | 摘要 |
| 22 | fbank_status_msg | 银行返回状态消息 | varchar | 255 |  | √ | ' ' | 银行返回状态消息 |
| 23 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 24 | fbank_name | 支行名称 | varchar | 50 |  | √ | ' ' | 支行名称 |
| 25 | faccbal | 账户余额 | varchar | 50 |  | √ | ' ' | 账户余额 |
| 26 | ffixactint | 实际利息 | varchar | 50 |  | √ | ' ' | 实际利息 |
| 27 | fstatus_name | 交易状态名 | varchar | 50 |  | √ | ' ' | 交易状态名 |
| 28 | ffixed_name | 定期账户名 | varchar | 50 |  | √ | ' ' | 定期账户名 |
| 29 | fimpl_class | 实现类 | varchar | 100 |  | √ | ' ' | 实现类 |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fsubmit_success_time | 成功提交时间 | timestamp | 0 |  |  | null | 成功提交时间 |
| 32 | fcloseint | 销户利息 | varchar | 50 |  | √ | ' ' | 销户利息 |
| 33 | freserve1 | 备用字段1 | varchar | 750 |  | √ | ' ' | 备用字段1 |
| 34 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 35 | freserve2 | 备用字段2 | varchar | 750 |  | √ | ' ' | 备用字段2 |
| 36 | fprice_no | 定价单号 | varchar | 50 |  | √ | ' ' | 定价单号 |
| 37 | fnext_term | 转存存期 | varchar | 50 |  | √ | ' ' | 转存存期 |
| 38 | ftrantime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 39 | fbank_status | 银行返回状态码 | varchar | 50 |  | √ | ' ' | 银行返回状态码 |
| 40 | fupdate_time | 数据更新时间 | timestamp | 0 |  |  | null | 数据更新时间 |
| 41 | ffixed_acc | 定期账号 | varchar | 50 |  | √ | ' ' | 定期账号 |
| 42 | ferror_msg | 错误信息 | varchar | 750 |  | √ | ' ' | 错误信息 |
| 43 | fbiz_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 44 | fdeposit_term | 存期 | varchar | 50 |  | √ | ' ' | 存期 |
| 45 | famount | 金额 | varchar | 50 |  | √ | ' ' | 金额 |
| 46 | finsert_time | 数据插入时间 | timestamp | 0 |  |  | null | 数据插入时间 |
| 47 | freqnbr | 流程流转号 | varchar | 50 |  | √ | ' ' | 流程流转号 |
| 48 | fstatus | 交易状态 | varchar | 50 |  | √ | ' ' | 交易状态,枚举: A :暂存 B :已提交 C :已审核 |
| 49 | fnext_deposit | 转存标识 | varchar | 50 |  | √ | ' ' | 转存标识 |
| 50 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 52 | finftyp | 通知类型 | varchar | 50 |  | √ | ' ' | 通知类型 |
| 53 | fcustomid | 租户id | varchar | 50 |  | √ | ' ' | 租户id |
| 54 | ffixtaxint | 扣利息税 | varchar | 50 |  | √ | ' ' | 扣利息税 |
| 55 | fbank_no | 支行行号 | varchar | 50 |  | √ | ' ' | 支行行号 |
| 56 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 57 | ffixed_bank_no | 定期支行行号 | varchar | 50 |  | √ | ' ' | 定期支行行号 |
| 58 | fendintdate | 止息日 | varchar | 50 |  | √ | ' ' | 止息日 |
| 59 | fbank_login | 前置机编号 | varchar | 50 |  | √ | ' ' | 前置机编号 |
| 60 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 61 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 62 | fopendate | 开户日 | varchar | 50 |  | √ | ' ' | 开户日 |
| 63 | ffixint | 应付利息 | varchar | 50 |  | √ | ' ' | 应付利息 |
| 64 | ffixed_bank_name | 定期支行名称 | varchar | 50 |  | √ | ' ' | 定期支行名称 |
| 65 | fback_error_msg | 返回错误信息 | varchar | 750 |  | √ | ' ' | 返回错误信息 |
| 66 | fstatus_msg | 交易状态描述 | varchar | 255 |  | √ | ' ' | 交易状态描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_caf_batch_seq |  | fbatch_seq_id |
| 2 | idx_aqap_biz_no_status_uindex |  | fdetail_biz_no,fstatus |
| 3 | idx_aqap_cur_acc_index |  | fcur_acc |
| 4 | t_aqap_bank_cafinfo_pkey |  | fid |
| 5 | idx_aqap_fixed_acc_index |  | ffixed_acc |
| 6 | idx_aqap_notify_id_index |  | fnotify_id |
