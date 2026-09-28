# 应收票据交易记录-note_receivable

## 应收票据交易记录-多语言表 t_note_receivable_l

- **表名称：** 应收票据交易记录-多语言表
- **表名：** t_note_receivable_l

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
| 1 | idx_note_receivable_l_0 |  | fid,flocaleid |
| 2 | t_note_receivable_l_pkey |  | fpkid |

---

## 应收票据交易记录-主表 t_note_receivable

- **表名称：** 应收票据交易记录-主表
- **表名：** t_note_receivable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | facceptor_bank_cnaps | acceptor_bank_cnaps | varchar | 50 |  |  | ' ' | acceptor_bank_cnaps |
| 3 | frequest_time | request_time | timestamp | 0 |  |  | null | request_time |
| 4 | fbank_version_id | bank_version_id | varchar | 50 |  | √ | ' ' | bank_version_id |
| 5 | fdrawer_acc_city | drawer_acc_city | varchar | 50 |  |  | ' ' | drawer_acc_city |
| 6 | fincrease_rate | increase_rate | varchar | 50 |  |  | ' ' | increase_rate |
| 7 | fautoreceive | autoReceive | varchar | 2 |  | √ | ' ' | autoReceive |
| 8 | fdiscount_rate | discount_rate | varchar | 50 |  |  | ' ' | discount_rate |
| 9 | fpay_agency | pay_agency | varchar | 50 |  |  | ' ' | pay_agency |
| 10 | fupdate_batch_seq | update_batch_seq | varchar | 50 |  |  | ' ' | update_batch_seq |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbank_ref_date | bank_ref_date | varchar | 50 |  |  | ' ' | bank_ref_date |
| 13 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 14 | fbankbatchcount | 银行批次数量 | int4 | 32 |  | √ | 0 | 银行批次数量 |
| 15 | finvc_date | 发票日期 | varchar | 50 |  |  | ' ' | 发票日期 |
| 16 | fbank_msg | bank_msg | varchar | 1000 |  |  | ' ' | bank_msg |
| 17 | fbak_bank_msg | bak_bank_msg | varchar | 255 |  |  | ' ' | bak_bank_msg |
| 18 | fversion | version | int8 | 64 |  |  | null | version |
| 19 | fsettleway | 文本100 | varchar | 10 |  |  | ' ' | 文本100 |
| 20 | ftotal_amount | total_amount | numeric | 23 | 10 |  | null | total_amount |
| 21 | fissue_date | issue_date | timestamp | 0 |  |  | null | issue_date |
| 22 | fsub_biz_type | sub_biz_type | varchar | 50 |  | √ | ' ' | sub_biz_type,枚举: present_payment :提示付款 note_signin :通用签收 pledge_note :质押 note_discount :贴现 note_endorse :背书 note_cancle :撤销 nonnegotiable_cancle :不可转让撤销 |
| 23 | forgendno | orgendno | varchar | 100 |  |  | ' ' | orgendno |
| 24 | fquery_type | query_type | varchar | 50 |  |  | ' ' | query_type |
| 25 | fexplanation | explanation | varchar | 255 |  |  | ' ' | explanation |
| 26 | finvc_chk_no | 发票校验码 | varchar | 50 |  |  | ' ' | 发票校验码 |
| 27 | fbatchtotalamount | 金额5 | numeric | 23 | 10 |  | null | 金额5 |
| 28 | fdrawer_acc_name | drawer_acc_name | varchar | 50 |  |  | ' ' | drawer_acc_name |
| 29 | fsubrange | 文本102 | varchar | 50 |  |  | ' ' | 文本102 |
| 30 | facceptor_bank_address | acceptor_bank_address | varchar | 50 |  |  | ' ' | acceptor_bank_address |
| 31 | fpayee_bank_cnaps | payee_bank_cnaps | varchar | 50 |  |  | ' ' | payee_bank_cnaps |
| 32 | fstatus_name | status_name | varchar | 50 |  |  | ' ' | status_name |
| 33 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fsubmit_success_time | submit_success_time | timestamp | 0 |  |  | null | submit_success_time |
| 35 | fpackage_key | package_key | varchar | 50 |  |  | ' ' | package_key |
| 36 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 37 | fdis_red_rate | dis_red_rate | varchar | 50 |  |  | ' ' | dis_red_rate |
| 38 | fpayee_country | payee_country | varchar | 50 |  |  | ' ' | payee_country |
| 39 | fisacceptsamebank | isAcceptSameBank | varchar | 2 |  | √ | ' ' | isAcceptSameBank |
| 40 | fdrawer_bank_address | drawer_bank_address | varchar | 50 |  |  | ' ' | drawer_bank_address |
| 41 | fnote_status | note_status | varchar | 50 |  |  | ' ' | note_status,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 42 | fisnewecds | 文本97 | varchar | 50 |  |  | ' ' | 文本97 |
| 43 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  |  | ' ' | bank_batch_seq_id |
| 44 | fdrawer_acc_province | drawer_acc_province | varchar | 50 |  |  | ' ' | drawer_acc_province |
| 45 | frqstserialno | rqstserialno | varchar | 50 |  |  | ' ' | rqstserialno |
| 46 | fdraft_type | draft_type | varchar | 10 |  | √ | ' ' | draft_type |
| 47 | fbak_status_msg | bak_status_msg | varchar | 255 |  |  | ' ' | bak_status_msg |
| 48 | fdue_date | due_date | timestamp | 0 |  |  | null | due_date |
| 49 | facceptor_acc_no | acceptor_acc_no | varchar | 50 |  |  | ' ' | acceptor_acc_no |
| 50 | famount | amount | numeric | 23 | 10 | √ | null | amount |
| 51 | fpayee_bank_name | payee_bank_name | varchar | 50 |  |  | ' ' | payee_bank_name |
| 52 | fispayeesamebank | 文本94 | varchar | 5 |  |  | ' ' | 文本94 |
| 53 | foperation_code | operation_code | varchar | 50 |  |  | ' ' | operation_code |
| 54 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 12 :交易成功 11 :交易未确认 10 :银行处理中 13 :交易失败 9 :正在提交银行 7 :打包处理中 0 :尚未处理,还未打包 |
| 55 | fcustom_id | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 56 | fsync_count | sync_count | int8 | 64 |  |  | null | sync_count |
| 57 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 58 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 59 | fkeep_flag | keep_flag | varchar | 50 |  |  | ' ' | keep_flag |
| 60 | fbank_ref_key | bank_ref_key | varchar | 255 |  |  | 0 | bank_ref_key |
| 61 | ftotal_count | total_count | int8 | 64 |  |  | null | total_count |
| 62 | finvc_code | 发票代码 | varchar | 50 |  |  | ' ' | 发票代码 |
| 63 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 64 | fredemption_e_date | redemption_e_date | timestamp | 0 |  |  | null | redemption_e_date |
| 65 | fother_info | other_info | varchar | 50 |  |  | ' ' | other_info |
| 66 | fdiscount_amount | discount_amount | numeric | 23 | 10 |  | null | discount_amount |
| 67 | fdrawer_bank_cnaps | drawer_bank_cnaps | varchar | 50 |  |  | ' ' | drawer_bank_cnaps |
| 68 | fautoaccept | autoAccept | varchar | 2 |  | √ | ' ' | autoAccept |
| 69 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 70 | fupdate_operation | update_operation | varchar | 50 |  |  | ' ' | update_operation |
| 71 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 72 | fbak_status_name | bak_status_name | varchar | 50 |  |  | ' ' | bak_status_name |
| 73 | flast_sync_request_seq | last_sync_request_seq | varchar | 50 |  |  | ' ' | last_sync_request_seq |
| 74 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 75 | fisrefuse | 是否被拒签 | varchar | 50 |  |  | ' ' | 是否被拒签 |
| 76 | fcirstatus | cirstatus | varchar | 50 |  |  | ' ' | cirstatus,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 77 | fobssid | obssid | varchar | 50 |  |  | ' ' | obssid |
| 78 | fstatus_msg | status_msg | varchar | 50 |  |  | ' ' | status_msg |
| 79 | ftotalsize | 整数4 | int8 | 64 |  |  | 0 | 整数4 |
| 80 | fbank_serial_no | bank_serial_no | varchar | 50 |  |  | ' ' | bank_serial_no |
| 81 | fbooking_date | booking_date | timestamp | 0 |  |  | null | booking_date |
| 82 | fdiscount_accname | discount_accname | varchar | 50 |  |  | ' ' | discount_accname |
| 83 | fbatch_seq_id | batch_seq_id | varchar | 50 |  | √ | ' ' | batch_seq_id |
| 84 | ftextfield1 | to_give_up | varchar | 50 |  |  | ' ' | to_give_up |
| 85 | fgrdbag | 文本98 | varchar | 50 |  |  | ' ' | 文本98 |
| 86 | fdrawer_acc_countrys | drawer_acc_countrys | varchar | 50 |  |  | ' ' | drawer_acc_countrys |
| 87 | fbak_bank_status | bak_bank_status | varchar | 50 |  |  | ' ' | bak_bank_status |
| 88 | finvc_amt | 发票金额 | varchar | 50 |  |  | ' ' | 发票金额 |
| 89 | ftextfield | 文本41 | varchar | 50 |  |  | ' ' | 文本41 |
| 90 | facceptor_bank_name | acceptor_bank_name | varchar | 50 |  |  | ' ' | acceptor_bank_name |
| 91 | fsequence | sequence | varchar | 50 |  |  | ' ' | sequence |
| 92 | floan_amount | loan_amount | numeric | 23 | 10 |  | null | loan_amount |
| 93 | fdraftamount | 金额4 | numeric | 23 | 10 |  | null | 金额4 |
| 94 | fdrawer_due_date | drawer_due_date | timestamp | 0 |  |  | null | drawer_due_date |
| 95 | fdetail_seq_id | detail_seq_id | varchar | 50 |  |  | ' ' | detail_seq_id |
| 96 | facceptor_acc_country | acceptor_acc_country | varchar | 50 |  |  | ' ' | acceptor_acc_country |
| 97 | fimpa_type | impa_type | varchar | 50 |  |  | ' ' | impa_type |
| 98 | fregisterbankname | registerBankName | varchar | 255 |  | √ | ' ' | registerBankName |
| 99 | fregisteracno | registerAcno | varchar | 50 |  | √ | ' ' | registerAcno |
| 100 | facceptor_acc_city | acceptor_acc_city | varchar | 50 |  |  | ' ' | acceptor_acc_city |
| 101 | fadd_day | add_day | varchar | 50 |  |  | ' ' | add_day |
| 102 | fdiscount_type | discount_type | varchar | 50 |  |  | ' ' | discount_type |
| 103 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 104 | ffilelist_tag | 交易附件信息_详情 | text | 0 |  |  | null | 交易附件信息_详情 |
| 105 | fdetail_biz_no | detail_biz_no | varchar | 50 |  |  | ' ' | detail_biz_no |
| 106 | fredemption_s_date | redemption_s_date | timestamp | 0 |  |  | null | redemption_s_date |
| 107 | fdrawer_ratings | drawer_ratings | varchar | 50 |  |  | ' ' | drawer_ratings |
| 108 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 109 | freserved4 | reserved4 | varchar | 255 |  |  | '0' | reserved4 |
| 110 | freserved2 | reserved2 | varchar | 255 |  |  | '0' | reserved2 |
| 111 | freserved3 | reserved3 | varchar | 255 |  |  | '0' | reserved3 |
| 112 | fdrawer_bank_name | drawer_bank_name | varchar | 50 |  |  | ' ' | drawer_bank_name |
| 113 | fsubmit_count | submit_count | int8 | 64 |  |  | null | submit_count |
| 114 | fdiscount_accno | discount_accno | varchar | 50 |  |  | ' ' | discount_accno |
| 115 | freserved1 | reserved1 | varchar | 255 |  |  | '0' | reserved1 |
| 116 | foperation_name | operation_name | varchar | 50 |  |  | ' ' | operation_name |
| 117 | finvc_type | 发票类型 | varchar | 50 |  |  | ' ' | 发票类型 |
| 118 | facceptor_acc_name | acceptor_acc_name | varchar | 50 |  |  | ' ' | acceptor_acc_name |
| 119 | facceptor_acc_province | acceptor_acc_province | varchar | 50 |  |  | ' ' | acceptor_acc_province |
| 120 | frate_type | rate_type | varchar | 50 |  |  | ' ' | rate_type |
| 121 | fpayee_bank_address | payee_bank_address | varchar | 50 |  |  | ' ' | payee_bank_address |
| 122 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 123 | fbank_status | bank_status | varchar | 60 |  |  | 0 | bank_status |
| 124 | fpayee_acc_no | payee_acc_no | varchar | 50 |  |  | ' ' | payee_acc_no |
| 125 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  |  | ' ' | bank_detail_seq_id |
| 126 | ferror_msg | error_msg | varchar | 255 |  |  | ' ' | error_msg |
| 127 | fbiz_type | biz_type | varchar | 50 |  | √ | ' ' | biz_type |
| 128 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 129 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 130 | frequest_seq | request_seq | varchar | 50 |  |  | ' ' | request_seq |
| 131 | forgstartno | orgstartno | varchar | 100 |  |  | ' ' | orgstartno |
| 132 | finterest | 文本103 | varchar | 100 |  |  | ' ' | 文本103 |
| 133 | frspserialno | rspserialno | varchar | 50 |  |  | ' ' | rspserialno |
| 134 | ftransfer_flag | transfer_flag | varchar | 50 |  |  | ' ' | transfer_flag |
| 135 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 136 | fregisternmae | registerNmae | varchar | 50 |  | √ | ' ' | registerNmae |
| 137 | fpayee_city | payee_city | varchar | 50 |  |  | ' ' | payee_city |
| 138 | fcontract_no | contract_no | varchar | 50 |  |  | ' ' | contract_no |
| 139 | fstartno | 文本99 | varchar | 100 |  |  | ' ' | 文本99 |
| 140 | finvc_no | 发票号码 | varchar | 50 |  |  | ' ' | 发票号码 |
| 141 | fpayee_province | payee_province | varchar | 50 |  |  | ' ' | payee_province |
| 142 | fpay_finish_time | pay_finish_time | timestamp | 0 |  |  | null | pay_finish_time |
| 143 | fpayee_acc_name | payee_acc_name | varchar | 50 |  |  | ' ' | payee_acc_name |
| 144 | fbak_error_msg | bak_error_msg | varchar | 255 |  |  | ' ' | bak_error_msg |
| 145 | fcurrency | currency | varchar | 50 |  |  | ' ' | currency |
| 146 | fdrawer_agency | drawer_agency | varchar | 50 |  |  | ' ' | drawer_agency |
| 147 | fendno | 文本100 | varchar | 100 |  |  | ' ' | 文本100 |
| 148 | fincreaserateper | increaseRatePer | varchar | 50 |  | √ | ' ' | increaseRatePer |
| 149 | flast_submit_request_seq | last_submit_request_seq | varchar | 50 |  |  | ' ' | last_submit_request_seq |
| 150 | fbak_status | bak_status | varchar | 60 |  |  | 0 | bak_status |
| 151 | fcleartype | 文本101 | varchar | 10 |  |  | ' ' | 文本101 |
| 152 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  |  | ' ' | insert_batch_seq |
| 153 | fdrawer_acc_no | drawer_acc_no | varchar | 50 |  |  | ' ' | drawer_acc_no |
| 154 | ffilelist | 交易附件信息 | varchar | 10 |  | √ | ' ' | 交易附件信息 |
| 155 | fbill_no | bill_no | varchar | 50 |  | √ | ' ' | bill_no |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_receivable_pkey |  | fid |
| 2 | idx_schedule_receivable |  | fstatus,finsert_time |
