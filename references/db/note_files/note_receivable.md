# 应收票据-note_receivable

## 应收票据-多语言表 t_note_receivable_l

- **表名称：** 应收票据-多语言表
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
| 1 | t_note_receivable_l_pkey |  | fpkid |
| 2 | idx_note_receivable_l_0 |  | fid,flocaleid |

---

## 应收票据-主表 t_note_receivable

- **表名称：** 应收票据-主表
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
| 7 | fdiscount_rate | discount_rate | varchar | 50 |  |  | ' ' | discount_rate |
| 8 | fpay_agency | pay_agency | varchar | 50 |  |  | ' ' | pay_agency |
| 9 | fupdate_batch_seq | update_batch_seq | varchar | 50 |  |  | ' ' | update_batch_seq |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbank_ref_date | bank_ref_date | varchar | 50 |  |  | ' ' | bank_ref_date |
| 12 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 13 | fbank_msg | bank_msg | varchar | 255 |  |  | ' ' | bank_msg |
| 14 | fbak_bank_msg | bak_bank_msg | varchar | 255 |  |  | ' ' | bak_bank_msg |
| 15 | fversion | version | int8 | 64 |  |  | null | version |
| 16 | ftotal_amount | total_amount | numeric | 23 | 10 |  | null | total_amount |
| 17 | fissue_date | issue_date | timestamp | 0 |  |  | null | issue_date |
| 18 | fsub_biz_type | sub_biz_type | varchar | 50 |  | √ | ' ' | sub_biz_type |
| 19 | fexplanation | explanation | varchar | 255 |  |  | ' ' | explanation |
| 20 | fquery_type | query_type | varchar | 50 |  |  | ' ' | query_type |
| 21 | fdrawer_acc_name | drawer_acc_name | varchar | 50 |  |  | ' ' | drawer_acc_name |
| 22 | facceptor_bank_address | acceptor_bank_address | varchar | 255 |  |  | ' ' | acceptor_bank_address |
| 23 | fpayee_bank_cnaps | payee_bank_cnaps | varchar | 50 |  |  | ' ' | payee_bank_cnaps |
| 24 | fstatus_name | status_name | varchar | 50 |  |  | ' ' | status_name |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fsubmit_success_time | submit_success_time | timestamp | 0 |  |  | null | submit_success_time |
| 27 | fpackage_key | package_key | varchar | 50 |  |  | ' ' | package_key |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fdis_red_rate | dis_red_rate | varchar | 50 |  |  | ' ' | dis_red_rate |
| 30 | fpayee_country | payee_country | varchar | 50 |  |  | ' ' | payee_country |
| 31 | fdrawer_bank_address | drawer_bank_address | varchar | 255 |  |  | ' ' | drawer_bank_address |
| 32 | fnote_status | note_status | varchar | 50 |  |  | ' ' | note_status |
| 33 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  |  | ' ' | bank_batch_seq_id |
| 34 | fdrawer_acc_province | drawer_acc_province | varchar | 50 |  |  | ' ' | drawer_acc_province |
| 35 | frqstserialno | rqstserialno | varchar | 50 |  |  | ' ' | rqstserialno |
| 36 | fdraft_type | draft_type | varchar | 10 |  | √ | ' ' | draft_type |
| 37 | fbak_status_msg | bak_status_msg | varchar | 255 |  |  | ' ' | bak_status_msg |
| 38 | fdue_date | due_date | timestamp | 0 |  |  | null | due_date |
| 39 | facceptor_acc_no | acceptor_acc_no | varchar | 50 |  |  | ' ' | acceptor_acc_no |
| 40 | famount | amount | numeric | 23 | 10 | √ | null | amount |
| 41 | fpayee_bank_name | payee_bank_name | varchar | 50 |  |  | ' ' | payee_bank_name |
| 42 | foperation_code | operation_code | varchar | 50 |  |  | ' ' | operation_code |
| 43 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 44 | fcustom_id | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 45 | fsync_count | sync_count | int8 | 64 |  |  | null | sync_count |
| 46 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 47 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 48 | fkeep_flag | keep_flag | varchar | 50 |  |  | ' ' | keep_flag |
| 49 | fbank_ref_key | bank_ref_key | varchar | 50 |  |  | ' ' | bank_ref_key |
| 50 | ftotal_count | total_count | int8 | 64 |  |  | null | total_count |
| 51 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 52 | fredemption_e_date | redemption_e_date | timestamp | 0 |  |  | null | redemption_e_date |
| 53 | fother_info | other_info | varchar | 50 |  |  | ' ' | other_info |
| 54 | fdiscount_amount | discount_amount | numeric | 23 | 10 |  | null | discount_amount |
| 55 | fdrawer_bank_cnaps | drawer_bank_cnaps | varchar | 50 |  |  | ' ' | drawer_bank_cnaps |
| 56 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 57 | fupdate_operation | update_operation | varchar | 50 |  |  | ' ' | update_operation |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fbak_status_name | bak_status_name | varchar | 50 |  |  | ' ' | bak_status_name |
| 60 | flast_sync_request_seq | last_sync_request_seq | varchar | 50 |  |  | ' ' | last_sync_request_seq |
| 61 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 62 | fobssid | obssid | varchar | 50 |  |  | ' ' | obssid |
| 63 | fstatus_msg | status_msg | varchar | 255 |  |  | ' ' | status_msg |
| 64 | fbank_serial_no | bank_serial_no | varchar | 50 |  |  | ' ' | bank_serial_no |
| 65 | fbooking_date | booking_date | timestamp | 0 |  |  | null | booking_date |
| 66 | fdiscount_accname | discount_accname | varchar | 50 |  |  | ' ' | discount_accname |
| 67 | fbatch_seq_id | batch_seq_id | varchar | 50 |  | √ | ' ' | batch_seq_id |
| 68 | ftextfield1 | to_give_up | varchar | 50 |  |  | ' ' | to_give_up |
| 69 | fdrawer_acc_countrys | drawer_acc_countrys | varchar | 50 |  |  | ' ' | drawer_acc_countrys |
| 70 | fbak_bank_status | bak_bank_status | varchar | 50 |  |  | ' ' | bak_bank_status |
| 71 | ftextfield | 文本41 | varchar | 50 |  |  | ' ' | 文本41 |
| 72 | facceptor_bank_name | acceptor_bank_name | varchar | 50 |  |  | ' ' | acceptor_bank_name |
| 73 | fsequence | sequence | varchar | 50 |  |  | ' ' | sequence |
| 74 | floan_amount | loan_amount | numeric | 23 | 10 |  | null | loan_amount |
| 75 | fdrawer_due_date | drawer_due_date | timestamp | 0 |  |  | null | drawer_due_date |
| 76 | fdetail_seq_id | detail_seq_id | varchar | 50 |  |  | ' ' | detail_seq_id |
| 77 | facceptor_acc_country | acceptor_acc_country | varchar | 50 |  |  | ' ' | acceptor_acc_country |
| 78 | fimpa_type | impa_type | varchar | 50 |  |  | ' ' | impa_type |
| 79 | facceptor_acc_city | acceptor_acc_city | varchar | 50 |  |  | ' ' | acceptor_acc_city |
| 80 | fadd_day | add_day | varchar | 50 |  |  | ' ' | add_day |
| 81 | fdiscount_type | discount_type | varchar | 50 |  |  | ' ' | discount_type |
| 82 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 83 | fdetail_biz_no | detail_biz_no | varchar | 50 |  |  | ' ' | detail_biz_no |
| 84 | fredemption_s_date | redemption_s_date | timestamp | 0 |  |  | null | redemption_s_date |
| 85 | fdrawer_ratings | drawer_ratings | varchar | 50 |  |  | ' ' | drawer_ratings |
| 86 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 87 | freserved4 | reserved4 | varchar | 255 |  |  | '0' | reserved4 |
| 88 | freserved2 | reserved2 | varchar | 255 |  |  | '0' | reserved2 |
| 89 | fdrawer_bank_name | drawer_bank_name | varchar | 50 |  |  | ' ' | drawer_bank_name |
| 90 | freserved3 | reserved3 | varchar | 255 |  |  | '0' | reserved3 |
| 91 | fsubmit_count | submit_count | int8 | 64 |  |  | null | submit_count |
| 92 | fdiscount_accno | discount_accno | varchar | 50 |  |  | ' ' | discount_accno |
| 93 | freserved1 | reserved1 | varchar | 255 |  |  | '0' | reserved1 |
| 94 | foperation_name | operation_name | varchar | 50 |  |  | ' ' | operation_name |
| 95 | facceptor_acc_name | acceptor_acc_name | varchar | 50 |  |  | ' ' | acceptor_acc_name |
| 96 | facceptor_acc_province | acceptor_acc_province | varchar | 50 |  |  | ' ' | acceptor_acc_province |
| 97 | frate_type | rate_type | varchar | 50 |  |  | ' ' | rate_type |
| 98 | fpayee_bank_address | payee_bank_address | varchar | 255 |  |  | ' ' | payee_bank_address |
| 99 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 100 | fbank_status | bank_status | varchar | 50 |  |  | ' ' | bank_status |
| 101 | fpayee_acc_no | payee_acc_no | varchar | 50 |  |  | ' ' | payee_acc_no |
| 102 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  |  | ' ' | bank_detail_seq_id |
| 103 | ferror_msg | error_msg | varchar | 500 |  |  | '0' | error_msg |
| 104 | fbiz_type | biz_type | varchar | 50 |  | √ | ' ' | biz_type |
| 105 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 106 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 107 | frequest_seq | request_seq | varchar | 50 |  |  | ' ' | request_seq |
| 108 | frspserialno | rspserialno | varchar | 50 |  |  | ' ' | rspserialno |
| 109 | ftransfer_flag | transfer_flag | varchar | 50 |  |  | ' ' | transfer_flag |
| 110 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 111 | fpayee_city | payee_city | varchar | 50 |  |  | ' ' | payee_city |
| 112 | fcontract_no | contract_no | varchar | 50 |  |  | ' ' | contract_no |
| 113 | fpayee_province | payee_province | varchar | 50 |  |  | ' ' | payee_province |
| 114 | fpay_finish_time | pay_finish_time | timestamp | 0 |  |  | null | pay_finish_time |
| 115 | fpayee_acc_name | payee_acc_name | varchar | 50 |  |  | ' ' | payee_acc_name |
| 116 | fbak_error_msg | bak_error_msg | varchar | 255 |  |  | ' ' | bak_error_msg |
| 117 | fcurrency | currency | varchar | 50 |  |  | ' ' | currency |
| 118 | fdrawer_agency | drawer_agency | varchar | 50 |  |  | ' ' | drawer_agency |
| 119 | flast_submit_request_seq | last_submit_request_seq | varchar | 50 |  |  | ' ' | last_submit_request_seq |
| 120 | fbak_status | bak_status | varchar | 50 |  |  | ' ' | bak_status |
| 121 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  |  | ' ' | insert_batch_seq |
| 122 | fdrawer_acc_no | drawer_acc_no | varchar | 50 |  |  | ' ' | drawer_acc_no |
| 123 | fbill_no | bill_no | varchar | 50 |  | √ | ' ' | bill_no |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_receivable_pkey |  | fid |
