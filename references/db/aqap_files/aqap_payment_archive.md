# 付款记录归档表-aqap_payment_archive

## 付款记录归档表-主表 t_aqap_payment_archive

- **表名称：** 付款记录归档表-主表
- **表名：** t_aqap_payment_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequest_time | request_time | timestamp | 0 |  |  | null | request_time |
| 3 | fbank_version_id | bank_version_id | varchar | 50 |  | √ | ' ' | bank_version_id |
| 4 | fcheque_type | cheque_type | varchar | 255 |  | √ | ' ' | cheque_type |
| 5 | fabstract | abstract | varchar | 100 |  | √ | ' ' | abstract |
| 6 | fincome_bank_name | income_bank_name | varchar | 255 |  | √ | ' ' | income_bank_name |
| 7 | fupdate_batch_seq | update_batch_seq | varchar | 50 |  | √ | ' ' | update_batch_seq |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | facc_name | acc_name | varchar | 255 |  | √ | ' ' | acc_name |
| 10 | fclearing_branch_code | clearing_branch_code | varchar | 255 |  | √ | ' ' | clearing_branch_code |
| 11 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 12 | fbooking_time | booking_time | timestamp | 0 |  |  | null | booking_time |
| 13 | flinkpay_type | linkpay_type | varchar | 50 |  | √ | ' ' | linkpay_type |
| 14 | fincome_city | income_city | varchar | 50 |  | √ | ' ' | income_city |
| 15 | fbank_msg | bank_msg | text | 0 |  |  | null | bank_msg |
| 16 | fversion | version | int8 | 64 |  | √ | 0 | version |
| 17 | fincome_province | income_province | varchar | 50 |  | √ | ' ' | income_province |
| 18 | fproxy_acc_no | proxy_acc_no | varchar | 50 |  | √ | ' ' | proxy_acc_no |
| 19 | ftotal_amount | total_amount | numeric | 23 | 10 | √ | 0 | total_amount |
| 20 | fback_bank_status | back_bank_status | varchar | 80 |  | √ | ' ' | back_bank_status |
| 21 | fclearing_branch_sub_code | clearing_branch_sub_code | varchar | 255 |  | √ | ' ' | clearing_branch_sub_code |
| 22 | fincome_bank_address | income_bank_address | varchar | 255 |  | √ | ' ' | income_bank_address |
| 23 | fback_bank_msg | back_bank_msg | varchar | 255 |  | √ | ' ' | back_bank_msg |
| 24 | ffee_type | fee_type | varchar | 50 |  | √ | ' ' | fee_type |
| 25 | fsub_biz_type | sub_biz_type | varchar | 50 |  | √ | ' ' | sub_biz_type |
| 26 | freason | reason | varchar | 255 |  | √ | ' ' | reason |
| 27 | fexplanation | explanation | varchar | 800 |  | √ | ' ' | explanation |
| 28 | fpayment_method | payment_method | varchar | 50 |  | √ | ' ' | payment_method |
| 29 | fproxy_bank_name | proxy_bank_name | varchar | 255 |  | √ | ' ' | proxy_bank_name |
| 30 | fbochk_message_bank | bochk_message_bank | varchar | 255 |  | √ | ' ' | bochk_message_bank |
| 31 | fstatus_name | status_name | varchar | 50 |  | √ | ' ' | status_name |
| 32 | fincome_swift_code | income_swift_code | varchar | 50 |  | √ | ' ' | income_swift_code |
| 33 | facc_city | acc_city | varchar | 50 |  | √ | ' ' | acc_city |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fsubmit_success_time | submit_success_time | timestamp | 0 |  |  | null | submit_success_time |
| 36 | fproxy_bank_area | proxy_bank_area | varchar | 50 |  | √ | ' ' | proxy_bank_area |
| 37 | fpackage_key | package_key | text | 0 |  |  | null | package_key |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fthird_bank_name | third_bank_name | varchar | 255 |  | √ | ' ' | third_bank_name |
| 40 | fstatus_id | status_id | int8 | 64 |  | √ | 0 | status_id |
| 41 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  | √ | ' ' | bank_batch_seq_id |
| 42 | farchive_time | archive_time | timestamp | 0 |  |  | null | archive_time |
| 43 | fincome_branch_no | income_branch_no | varchar | 30 |  | √ | ' ' | income_branch_no |
| 44 | facc_country | acc_country | varchar | 50 |  | √ | ' ' | acc_country |
| 45 | famount | amount | numeric | 23 | 10 | √ | 0 | amount |
| 46 | fstatus | 数据状态 | varchar | 20 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 47 | facc_dept | acc_dept | varchar | 50 |  | √ | ' ' | acc_dept |
| 48 | fsync_count | sync_count | int8 | 64 |  | √ | 0 | sync_count |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 51 | fmobiles | mobiles | varchar | 50 |  | √ | ' ' | mobiles |
| 52 | fproxy_fee_currency | proxy_fee_currency | varchar | 50 |  | √ | ' ' | proxy_fee_currency |
| 53 | fuse_code | use_code | varchar | 50 |  | √ | ' ' | use_code |
| 54 | fk_ebc_textfield | clearing_code | varchar | 50 |  | √ | ' ' | clearing_code |
| 55 | ftotal_count | total_count | int8 | 64 |  | √ | 0 | total_count |
| 56 | fback_status_msg | back_status_msg | varchar | 255 |  | √ | ' ' | back_status_msg |
| 57 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 58 | fpayer_fee_type | payer_fee_type | varchar | 50 |  | √ | ' ' | payer_fee_type |
| 59 | freversed_biz_field | reversed_biz_field | varchar | 600 |  | √ | ' ' | reversed_biz_field |
| 60 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fexchange_rate | exchange_rate | varchar | 10 |  | √ | ' ' | exchange_rate |
| 62 | fupdate_operation | update_operation | varchar | 50 |  | √ | ' ' | update_operation |
| 63 | ftrans_up | trans_up | varchar | 50 |  | √ | ' ' | trans_up |
| 64 | foperator | operator | varchar | 255 |  | √ | ' ' | operator |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fthird_bank_address | third_bank_address | varchar | 255 |  | √ | ' ' | third_bank_address |
| 67 | ferror_stack | error_stack | varchar | 255 |  | √ | ' ' | error_stack |
| 68 | fthird_area_code | third_area_code | varchar | 50 |  | √ | ' ' | third_area_code |
| 69 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 70 | facc_province | acc_province | varchar | 50 |  | √ | ' ' | acc_province |
| 71 | ftransaction_remarks | transaction_remarks | varchar | 100 |  | √ | ' ' | transaction_remarks |
| 72 | fback_error_msg | back_error_msg | varchar | 255 |  | √ | ' ' | back_error_msg |
| 73 | fstatus_msg | status_msg | varchar | 50 |  | √ | ' ' | status_msg |
| 74 | fincome_branch_name | income_branch_name | varchar | 255 |  | √ | ' ' | income_branch_name |
| 75 | fbank_serial_no | bank_serial_no | varchar | 50 |  | √ | ' ' | bank_serial_no |
| 76 | fbank_address | bank_address | varchar | 255 |  | √ | ' ' | bank_address |
| 77 | fpayer_fee_acc_no | payer_fee_acc_no | varchar | 50 |  | √ | ' ' | payer_fee_acc_no |
| 78 | fincome_acc_dept | income_acc_dept | varchar | 50 |  | √ | ' ' | income_acc_dept |
| 79 | factual_amount | actual_amount | numeric | 23 | 10 | √ | 0 | actual_amount |
| 80 | femails | emails | varchar | 100 |  | √ | ' ' | emails |
| 81 | fbatch_seq_id | batch_seq_id | varchar | 50 |  | √ | ' ' | batch_seq_id |
| 82 | freversed1 | reversed1 | varchar | 255 |  | √ | ' ' | reversed1 |
| 83 | farea_code | area_code | varchar | 50 |  | √ | ' ' | area_code |
| 84 | freversed2 | reversed2 | varchar | 255 |  | √ | ' ' | reversed2 |
| 85 | freversed3 | reversed3 | varchar | 255 |  | √ | ' ' | reversed3 |
| 86 | freversed4 | reversed4 | varchar | 255 |  | √ | ' ' | reversed4 |
| 87 | fproxy_fee_type | proxy_fee_type | varchar | 50 |  | √ | ' ' | proxy_fee_type |
| 88 | fbbc_code_words | bbc_code_words | varchar | 255 |  | √ | ' ' | bbc_code_words |
| 89 | fverify_field | verify_field | varchar | 255 |  | √ | ' ' | verify_field |
| 90 | fdetail_seq_id | detail_seq_id | varchar | 50 |  | √ | ' ' | detail_seq_id |
| 91 | fforce | force | varchar | 50 |  | √ | ' ' | force |
| 92 | fpayer_fee_currency | payer_fee_currency | varchar | 50 |  | √ | ' ' | payer_fee_currency |
| 93 | fincome_country | income_country | varchar | 50 |  | √ | ' ' | income_country |
| 94 | fdelivery_method | delivery_method | varchar | 255 |  | √ | ' ' | delivery_method |
| 95 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 96 | fiso_currency_code | iso_currency_code | varchar | 10 |  | √ | ' ' | iso_currency_code |
| 97 | fproxy_bank_swift_code | proxy_bank_swift_code | varchar | 50 |  | √ | ' ' | proxy_bank_swift_code |
| 98 | individual | individual | varchar | 50 |  | √ | ' ' | individual |
| 99 | fincome_acc_no | income_acc_no | varchar | 50 |  | √ | ' ' | income_acc_no |
| 100 | fthird_acc_dept | third_acc_dept | varchar | 50 |  | √ | ' ' | third_acc_dept |
| 101 | fdetail_biz_no | detail_biz_no | varchar | 50 |  | √ | ' ' | detail_biz_no |
| 102 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 103 | flast_submit_request_req | last_submit_request_req | varchar | 50 |  | √ | ' ' | last_submit_request_req |
| 104 | fincome_acc_name | income_acc_name | varchar | 255 |  | √ | ' ' | income_acc_name |
| 105 | fpayee_bank_code | payee_bank_code | varchar | 50 |  | √ | ' ' | payee_bank_code |
| 106 | fmerge | merge | varchar | 50 |  | √ | ' ' | merge |
| 107 | flast_sync_request_req | last_sync_request_req | varchar | 50 |  | √ | ' ' | last_sync_request_req |
| 108 | fto_ground | to_ground | varchar | 50 |  | √ | ' ' | to_ground |
| 109 | fbank_name | bank_name | varchar | 255 |  | √ | ' ' | bank_name |
| 110 | fsubmit_count | submit_count | int8 | 64 |  | √ | 0 | submit_count |
| 111 | fto_give_up | to_give_up | varchar | 50 |  | √ | ' ' | to_give_up |
| 112 | fthird_acc_no | third_acc_no | varchar | 100 |  | √ | ' ' | third_acc_no |
| 113 | frelative_id | relative_id | varchar | 50 |  | √ | ' ' | relative_id |
| 114 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 115 | fbank_status | bank_status | varchar | 80 |  | √ | ' ' | bank_status |
| 116 | facc_no | acc_no | varchar | 50 |  | √ | ' ' | acc_no |
| 117 | fiso_currency_name | iso_currency_name | varchar | 50 |  | √ | ' ' | iso_currency_name |
| 118 | flinkpay_detail_seq_id | linkpay_detail_seq_id | varchar | 100 |  | √ | ' ' | linkpay_detail_seq_id |
| 119 | fincome_cnaps | income_cnaps | varchar | 50 |  | √ | ' ' | income_cnaps |
| 120 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  | √ | ' ' | bank_detail_seq_id |
| 121 | ferror_msg | error_msg | text | 0 |  |  | null | error_msg |
| 122 | fback_error_stack | back_error_stack | varchar | 255 |  | √ | ' ' | back_error_stack |
| 123 | fbiz_type | biz_type | varchar | 50 |  | √ | ' ' | biz_type |
| 124 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 125 | fproxy_bank_country | proxy_bank_country | varchar | 50 |  | √ | ' ' | proxy_bank_country |
| 126 | freversed_sys_field | reversed_sys_field | varchar | 600 |  | √ | ' ' | reversed_sys_field |
| 127 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 128 | fpay_finish_date | pay_finish_date | timestamp | 0 |  |  | null | pay_finish_date |
| 129 | frequest_seq | request_seq | varchar | 50 |  | √ | ' ' | request_seq |
| 130 | fpay_currency | pay_currency | varchar | 10 |  | √ | ' ' | pay_currency |
| 131 | fsame_bank | same_bank | varchar | 50 |  | √ | ' ' | same_bank |
| 132 | fcustomid | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 133 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 134 | fincome_area_code | income_area_code | varchar | 50 |  | √ | ' ' | income_area_code |
| 135 | fback_status | back_status | varchar | 80 |  | √ | ' ' | back_status |
| 136 | fbank_ref_id | bank_ref_id | varchar | 255 |  | √ | ' ' | bank_ref_id |
| 137 | fsame_city | same_city | varchar | 50 |  | √ | ' ' | same_city |
| 138 | fcurrency | currency | varchar | 10 |  | √ | ' ' | currency |
| 139 | fproxy_bank_address | proxy_bank_address | varchar | 255 |  | √ | ' ' | proxy_bank_address |
| 140 | fthird_acc_name | third_acc_name | varchar | 255 |  | √ | ' ' | third_acc_name |
| 141 | fuse_cn | use_cn | varchar | 50 |  | √ | ' ' | use_cn |
| 142 | fservice_level | service_level | varchar | 50 |  | √ | ' ' | service_level |
| 143 | fex_contract | ex_contract | varchar | 200 |  | √ | ' ' | ex_contract |
| 144 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  | √ | ' ' | insert_batch_seq |
| 145 | fproxy_acc_name | proxy_acc_name | varchar | 255 |  | √ | ' ' | proxy_acc_name |
| 146 | furgent | urgent | varchar | 50 |  | √ | ' ' | urgent |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_payment_bkdt_seq |  | fbank_detail_seq_id |
| 2 | idx_payment_seq_status |  | fbank_batch_seq_id,fstatus_id |
| 3 | pk_aqap_payment_archive |  | fid |
| 4 | idx_aqap_paymentinfo_0 |  | fbatch_seq_id |
| 5 | idx_payment_statusid_bank |  | fstatus_id,fbank_version_id |

---

## 付款记录归档表-多语言表 t_aqap_payment_archive_l

- **表名称：** 付款记录归档表-多语言表
- **表名：** t_aqap_payment_archive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_payment_archive_l |  | fpkid |
