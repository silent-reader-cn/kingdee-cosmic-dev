# 应付票据-note_payable

## 应付票据-多语言表 t_note_payable_l

- **表名称：** 应付票据-多语言表
- **表名：** t_note_payable_l

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
| 1 | t_note_payable_l_pkey |  | fpkid |
| 2 | idx_note_payable_l_0 |  | fid,flocaleid |

---

## 应付票据-主表 t_note_payable

- **表名称：** 应付票据-主表
- **表名：** t_note_payable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | facceptor_bank_cnaps | acceptor_bank_cnaps | varchar | 50 |  |  | ' ' | acceptor_bank_cnaps |
| 3 | frequest_time | request_time | timestamp | 0 |  |  | null | request_time |
| 4 | fbank_version_id | bank_version_id | varchar | 50 |  | √ | ' ' | bank_version_id |
| 5 | fdrawer_acc_city | drawer_acc_city | varchar | 50 |  |  | ' ' | drawer_acc_city |
| 6 | fupdate_batch_seq | update_batch_seq | varchar | 50 |  |  | ' ' | update_batch_seq |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcontract_obj | contract_obj | varchar | 50 |  |  | ' ' | contract_obj |
| 9 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 10 | fbank_msg | bank_msg | varchar | 255 |  |  | ' ' | bank_msg |
| 11 | fbak_bank_msg | bak_bank_msg | varchar | 50 |  |  | ' ' | bak_bank_msg |
| 12 | fversion | version | int8 | 64 |  |  | null | version |
| 13 | ftotal_amount | total_amount | numeric | 23 | 10 |  | null | total_amount |
| 14 | fissue_date | issue_date | varchar | 50 |  |  | ' ' | issue_date |
| 15 | fsub_biz_type | sub_biz_type | varchar | 50 |  | √ | ' ' | sub_biz_type |
| 16 | fexplanation | explanation | varchar | 255 |  |  | ' ' | explanation |
| 17 | fquery_type | query_type | varchar | 50 |  |  | ' ' | query_type |
| 18 | fdrawer_acc_name | drawer_acc_name | varchar | 50 |  |  | ' ' | drawer_acc_name |
| 19 | facceptor_bank_address | acceptor_bank_address | varchar | 255 |  |  | ' ' | acceptor_bank_address |
| 20 | fpayee_bank_cnaps | payee_bank_cnaps | varchar | 50 |  |  | ' ' | payee_bank_cnaps |
| 21 | fstatus_name | status_name | varchar | 50 |  |  | ' ' | status_name |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fsubmit_success_time | submit_success_time | timestamp | 0 |  |  | null | submit_success_time |
| 24 | fpackage_key | package_key | varchar | 255 |  |  | ' ' | package_key |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fpayee_country | payee_country | varchar | 50 |  |  | ' ' | payee_country |
| 27 | fdrawer_bank_address | drawer_bank_address | varchar | 255 |  |  | ' ' | drawer_bank_address |
| 28 | fnote_status | note_status | varchar | 10 |  |  | ' ' | note_status |
| 29 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  |  | ' ' | bank_batch_seq_id |
| 30 | fdrawer_acc_province | drawer_acc_province | varchar | 50 |  |  | ' ' | drawer_acc_province |
| 31 | frqstserialno | rqstserialno | varchar | 50 |  |  | ' ' | rqstserialno |
| 32 | fdraft_type | draft_type | varchar | 8 |  |  | ' ' | draft_type |
| 33 | fbak_status_msg | bak_status_msg | varchar | 255 |  |  | ' ' | bak_status_msg |
| 34 | fdue_date | due_date | timestamp | 0 |  |  | null | due_date |
| 35 | facceptor_acc_no | acceptor_acc_no | varchar | 50 |  |  | ' ' | acceptor_acc_no |
| 36 | famount | amount | numeric | 23 | 10 |  | null | amount |
| 37 | fpayee_bank_name | payee_bank_name | varchar | 50 |  |  | ' ' | payee_bank_name |
| 38 | fauto_accept | auto_accept | varchar | 1 |  |  | ' ' | auto_accept |
| 39 | foperation_code | operation_code | varchar | 10 |  |  | ' ' | operation_code |
| 40 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 41 | fcustom_id | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 42 | fsync_count | sync_count | int8 | 64 |  |  | null | sync_count |
| 43 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 44 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 45 | fkeep_flag | keep_flag | varchar | 10 |  |  | ' ' | keep_flag |
| 46 | ftotal_count | total_count | int8 | 64 |  |  | null | total_count |
| 47 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 48 | fother_info | other_info | varchar | 50 |  |  | ' ' | other_info |
| 49 | fdrawer_bank_cnaps | drawer_bank_cnaps | varchar | 20 |  |  | ' ' | drawer_bank_cnaps |
| 50 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 51 | fupdate_operation | update_operation | varchar | 50 |  |  | ' ' | update_operation |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | fbak_status_name | bak_status_name | varchar | 50 |  |  | ' ' | bak_status_name |
| 54 | flast_sync_request_seq | last_sync_request_seq | varchar | 50 |  |  | ' ' | last_sync_request_seq |
| 55 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 56 | fobssid | obssid | varchar | 50 |  |  | ' ' | obssid |
| 57 | fstatus_msg | status_msg | varchar | 255 |  |  | ' ' | status_msg |
| 58 | fbank_serial_no | bank_serial_no | varchar | 50 |  |  | ' ' | bank_serial_no |
| 59 | fbooking_date | booking_date | timestamp | 0 |  |  | null | booking_date |
| 60 | fbatch_seq_id | batch_seq_id | varchar | 50 |  | √ | ' ' | batch_seq_id |
| 61 | fbak_bank_status | bak_bank_status | varchar | 50 |  |  | ' ' | bak_bank_status |
| 62 | facceptor_bank_name | acceptor_bank_name | varchar | 50 |  |  | ' ' | acceptor_bank_name |
| 63 | fsequence | sequence | varchar | 50 |  |  | ' ' | sequence |
| 64 | fdrawer_due_date | drawer_due_date | timestamp | 0 |  |  | null | drawer_due_date |
| 65 | fdetail_seq_id | detail_seq_id | varchar | 50 |  |  | ' ' | detail_seq_id |
| 66 | facceptor_acc_country | acceptor_acc_country | varchar | 50 |  |  | ' ' | acceptor_acc_country |
| 67 | facceptor_acc_city | acceptor_acc_city | varchar | 50 |  |  | ' ' | acceptor_acc_city |
| 68 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 69 | fdetail_biz_no | detail_biz_no | varchar | 50 |  |  | ' ' | detail_biz_no |
| 70 | fdrawer_ratings | drawer_ratings | varchar | 50 |  |  | ' ' | drawer_ratings |
| 71 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 72 | freserved4 | reserved4 | varchar | 255 |  |  | '0' | reserved4 |
| 73 | freserved2 | reserved2 | varchar | 255 |  |  | '0' | reserved2 |
| 74 | fdrawer_bank_name | drawer_bank_name | varchar | 255 |  |  | ' ' | drawer_bank_name |
| 75 | freserved3 | reserved3 | varchar | 255 |  |  | '0' | reserved3 |
| 76 | fsubmit_count | submit_count | int8 | 64 |  |  | null | submit_count |
| 77 | fto_give_up | to_give_up | varchar | 50 |  |  | ' ' | to_give_up |
| 78 | freserved1 | reserved1 | varchar | 255 |  |  | '0' | reserved1 |
| 79 | fauto_receive | auto_receive | varchar | 1 |  |  | ' ' | auto_receive |
| 80 | foperation_name | operation_name | varchar | 50 |  |  | ' ' | operation_name |
| 81 | facceptor_acc_name | acceptor_acc_name | varchar | 50 |  |  | ' ' | acceptor_acc_name |
| 82 | facceptor_acc_province | acceptor_acc_province | varchar | 50 |  |  | ' ' | acceptor_acc_province |
| 83 | fpayee_bank_address | payee_bank_address | varchar | 50 |  |  | ' ' | payee_bank_address |
| 84 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 85 | fbank_status | bank_status | varchar | 50 |  |  | ' ' | bank_status |
| 86 | fpayee_acc_no | payee_acc_no | varchar | 50 |  |  | ' ' | payee_acc_no |
| 87 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  |  | ' ' | bank_detail_seq_id |
| 88 | ferror_msg | error_msg | varchar | 500 |  |  | '0' | error_msg |
| 89 | fdrawer_acc_country | drawer_acc_country | varchar | 50 |  |  | ' ' | drawer_acc_country |
| 90 | fbiz_type | fbiz_type | varchar | 50 |  | √ | ' ' | fbiz_type |
| 91 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 92 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 93 | frequest_seq | request_seq | varchar | 50 |  |  | ' ' | request_seq |
| 94 | frspserialno | rspserialno | varchar | 50 |  |  | ' ' | rspserialno |
| 95 | ftransfer_flag | transfer_flag | varchar | 10 |  |  | ' ' | transfer_flag |
| 96 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 97 | fpayee_city | payee_city | varchar | 50 |  |  | ' ' | payee_city |
| 98 | fcontract_no | contract_no | varchar | 50 |  |  | ' ' | contract_no |
| 99 | fpayee_province | payee_province | varchar | 50 |  |  | ' ' | payee_province |
| 100 | fpay_finish_time | pay_finish_time | timestamp | 0 |  |  | null | pay_finish_time |
| 101 | fpayee_acc_name | payee_acc_name | varchar | 50 |  |  | ' ' | payee_acc_name |
| 102 | fbak_error_msg | bak_error_msg | varchar | 255 |  |  | ' ' | bak_error_msg |
| 103 | fcurrency | currency | varchar | 10 |  |  | ' ' | currency |
| 104 | fdrawer_agency | drawer_agency | varchar | 50 |  |  | ' ' | drawer_agency |
| 105 | finvoice_no | invoice_no | varchar | 50 |  |  | ' ' | invoice_no |
| 106 | flast_submit_request_seq | last_submit_request_seq | varchar | 50 |  |  | ' ' | last_submit_request_seq |
| 107 | fbak_status | bak_status | varchar | 50 |  |  | ' ' | bak_status |
| 108 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  |  | ' ' | insert_batch_seq |
| 109 | fdrawer_acc_no | drawer_acc_no | varchar | 50 |  |  | ' ' | drawer_acc_no |
| 110 | fbill_no | bill_no | varchar | 50 |  |  | ' ' | bill_no |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_payable_pkey |  | fid |
