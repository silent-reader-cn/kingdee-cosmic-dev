# 付款记录-aqap_bd_paymentinfo

## 付款记录-主表 t_aqap_bd_paymentinfo

- **表名称：** 付款记录-主表
- **表名：** t_aqap_bd_paymentinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | frequest_time | request_time | timestamp | 0 |  |  | null | request_time |
| 3 | fbank_version_id | bank_version_id | varchar | 50 |  | √ | ' ' | bank_version_id |
| 4 | fcheque_type | cheque_type | varchar | 255 |  | √ | ' ' | cheque_type |
| 5 | fabstract | abstract | varchar | 255 |  | √ | ' ' | abstract |
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
| 16 | fversion | version | int8 | 64 |  |  | null | version |
| 17 | fincome_province | income_province | varchar | 50 |  | √ | ' ' | income_province |
| 18 | fproxy_acc_no | proxy_acc_no | varchar | 50 |  | √ | ' ' | proxy_acc_no |
| 19 | ftotal_amount | total_amount | numeric | 23 | 10 |  | null | total_amount |
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
| 40 | fstatus_id | status_id | int8 | 64 |  |  | null | status_id |
| 41 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  | √ | ' ' | bank_batch_seq_id |
| 42 | fincome_branch_no | income_branch_no | varchar | 30 |  |  | ' ' | income_branch_no |
| 43 | facc_country | acc_country | varchar | 50 |  | √ | ' ' | acc_country |
| 44 | famount | amount | numeric | 23 | 10 |  | null | amount |
| 45 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 46 | facc_dept | acc_dept | varchar | 50 |  | √ | ' ' | acc_dept |
| 47 | fsync_count | sync_count | int8 | 64 |  |  | null | sync_count |
| 48 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 50 | fmobiles | mobiles | varchar | 50 |  | √ | ' ' | mobiles |
| 51 | fproxy_fee_currency | proxy_fee_currency | varchar | 50 |  | √ | ' ' | proxy_fee_currency |
| 52 | fuse_code | use_code | varchar | 50 |  | √ | ' ' | use_code |
| 53 | fk_ebc_textfield | clearing_code | varchar | 50 |  | √ | ' ' | clearing_code |
| 54 | ftotal_count | total_count | int8 | 64 |  |  | null | total_count |
| 55 | fback_status_msg | back_status_msg | varchar | 255 |  | √ | ' ' | back_status_msg |
| 56 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 57 | fpayer_fee_type | payer_fee_type | varchar | 50 |  | √ | ' ' | payer_fee_type |
| 58 | freversed_biz_field | reversed_biz_field | varchar | 600 |  | √ | ' ' | reversed_biz_field |
| 59 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 60 | fexchange_rate | exchange_rate | varchar | 10 |  | √ | ' ' | exchange_rate |
| 61 | fupdate_operation | update_operation | varchar | 50 |  | √ | ' ' | update_operation |
| 62 | ftrans_up | trans_up | varchar | 50 |  | √ | ' ' | trans_up |
| 63 | foperator | operator | varchar | 255 |  | √ | ' ' | operator |
| 64 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 65 | fthird_bank_address | third_bank_address | varchar | 255 |  | √ | ' ' | third_bank_address |
| 66 | ferror_stack | error_stack | varchar | 255 |  | √ | ' ' | error_stack |
| 67 | fthird_area_code | third_area_code | varchar | 50 |  | √ | ' ' | third_area_code |
| 68 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 69 | facc_province | acc_province | varchar | 50 |  | √ | ' ' | acc_province |
| 70 | ftransaction_remarks | transaction_remarks | varchar | 100 |  | √ | ' ' | transaction_remarks |
| 71 | fback_error_msg | back_error_msg | varchar | 255 |  | √ | ' ' | back_error_msg |
| 72 | fstatus_msg | status_msg | varchar | 50 |  | √ | ' ' | status_msg |
| 73 | fincome_branch_name | income_branch_name | varchar | 255 |  |  | ' ' | income_branch_name |
| 74 | fbank_serial_no | bank_serial_no | varchar | 50 |  | √ | ' ' | bank_serial_no |
| 75 | fbank_address | bank_address | varchar | 255 |  | √ | ' ' | bank_address |
| 76 | fpayer_fee_acc_no | payer_fee_acc_no | varchar | 50 |  | √ | ' ' | payer_fee_acc_no |
| 77 | fincome_acc_dept | income_acc_dept | varchar | 50 |  | √ | ' ' | income_acc_dept |
| 78 | factual_amount | actual_amount | numeric | 23 | 10 |  | null | actual_amount |
| 79 | femails | emails | varchar | 100 |  | √ | ' ' | emails |
| 80 | fbatch_seq_id | batch_seq_id | varchar | 100 |  | √ | ' ' | batch_seq_id |
| 81 | freversed1 | reversed1 | varchar | 255 |  | √ | ' ' | reversed1 |
| 82 | farea_code | area_code | varchar | 50 |  | √ | ' ' | area_code |
| 83 | freversed2 | reversed2 | varchar | 255 |  | √ | ' ' | reversed2 |
| 84 | freversed3 | reversed3 | varchar | 255 |  | √ | ' ' | reversed3 |
| 85 | freversed4 | reversed4 | varchar | 255 |  | √ | ' ' | reversed4 |
| 86 | fproxy_fee_type | proxy_fee_type | varchar | 50 |  | √ | ' ' | proxy_fee_type |
| 87 | fbbc_code_words | bbc_code_words | varchar | 255 |  | √ | ' ' | bbc_code_words |
| 88 | fverify_field | verify_field | varchar | 255 |  | √ | ' ' | verify_field |
| 89 | fdetail_seq_id | detail_seq_id | varchar | 100 |  | √ | ' ' | detail_seq_id |
| 90 | fforce | force | varchar | 50 |  | √ | ' ' | force |
| 91 | fpayer_fee_currency | payer_fee_currency | varchar | 50 |  | √ | ' ' | payer_fee_currency |
| 92 | fincome_country | income_country | varchar | 50 |  | √ | ' ' | income_country |
| 93 | fdelivery_method | delivery_method | varchar | 255 |  | √ | ' ' | delivery_method |
| 94 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 95 | fiso_currency_code | iso_currency_code | varchar | 255 |  | √ | ' ' | iso_currency_code |
| 96 | fproxy_bank_swift_code | proxy_bank_swift_code | varchar | 50 |  | √ | ' ' | proxy_bank_swift_code |
| 97 | individual | individual | varchar | 50 |  | √ | ' ' | individual |
| 98 | fincome_acc_no | income_acc_no | varchar | 50 |  | √ | ' ' | income_acc_no |
| 99 | fthird_acc_dept | third_acc_dept | varchar | 50 |  | √ | ' ' | third_acc_dept |
| 100 | fdetail_biz_no | detail_biz_no | varchar | 100 |  | √ | ' ' | detail_biz_no |
| 101 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 102 | flast_submit_request_req | last_submit_request_req | varchar | 50 |  | √ | ' ' | last_submit_request_req |
| 103 | fincome_acc_name | income_acc_name | varchar | 255 |  | √ | ' ' | income_acc_name |
| 104 | fpayee_bank_code | payee_bank_code | varchar | 50 |  | √ | ' ' | payee_bank_code |
| 105 | fmerge | merge | varchar | 50 |  | √ | ' ' | merge |
| 106 | flast_sync_request_req | last_sync_request_req | varchar | 50 |  | √ | ' ' | last_sync_request_req |
| 107 | fto_ground | to_ground | varchar | 50 |  | √ | ' ' | to_ground |
| 108 | fbank_name | bank_name | varchar | 255 |  | √ | ' ' | bank_name |
| 109 | fsubmit_count | submit_count | int8 | 64 |  |  | null | submit_count |
| 110 | fto_give_up | to_give_up | varchar | 50 |  | √ | ' ' | to_give_up |
| 111 | fthird_acc_no | third_acc_no | varchar | 255 |  | √ | ' ' | third_acc_no |
| 112 | frelative_id | relative_id | varchar | 50 |  | √ | ' ' | relative_id |
| 113 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 114 | fbank_status | bank_status | varchar | 80 |  | √ | ' ' | bank_status |
| 115 | facc_no | acc_no | varchar | 50 |  | √ | ' ' | acc_no |
| 116 | fiso_currency_name | iso_currency_name | varchar | 255 |  | √ | ' ' | iso_currency_name |
| 117 | flinkpay_detail_seq_id | linkpay_detail_seq_id | varchar | 100 |  | √ | ' ' | linkpay_detail_seq_id |
| 118 | fincome_cnaps | income_cnaps | varchar | 50 |  | √ | ' ' | income_cnaps |
| 119 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  | √ | ' ' | bank_detail_seq_id |
| 120 | ferror_msg | error_msg | text | 0 |  |  | null | error_msg |
| 121 | fback_error_stack | back_error_stack | varchar | 255 |  | √ | ' ' | back_error_stack |
| 122 | fbiz_type | biz_type | varchar | 50 |  | √ | ' ' | biz_type |
| 123 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 124 | fproxy_bank_country | proxy_bank_country | varchar | 50 |  | √ | ' ' | proxy_bank_country |
| 125 | freversed_sys_field | reversed_sys_field | varchar | 600 |  | √ | ' ' | reversed_sys_field |
| 126 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 127 | fpay_finish_date | pay_finish_date | timestamp | 0 |  |  | null | pay_finish_date |
| 128 | frequest_seq | request_seq | varchar | 50 |  | √ | ' ' | request_seq |
| 129 | fpay_currency | pay_currency | varchar | 10 |  | √ | ' ' | pay_currency |
| 130 | fsame_bank | same_bank | varchar | 50 |  | √ | ' ' | same_bank |
| 131 | fcustomid | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 132 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 133 | fincome_area_code | income_area_code | varchar | 50 |  | √ | ' ' | income_area_code |
| 134 | fback_status | back_status | varchar | 80 |  | √ | ' ' | back_status |
| 135 | fbank_ref_id | bank_ref_id | varchar | 255 |  | √ | ' ' | bank_ref_id |
| 136 | fsame_city | same_city | varchar | 50 |  | √ | ' ' | same_city |
| 137 | fcurrency | currency | varchar | 10 |  | √ | ' ' | currency |
| 138 | fproxy_bank_address | proxy_bank_address | varchar | 255 |  | √ | ' ' | proxy_bank_address |
| 139 | fthird_acc_name | third_acc_name | varchar | 255 |  | √ | ' ' | third_acc_name |
| 140 | fuse_cn | use_cn | varchar | 255 |  | √ | ' ' | use_cn |
| 141 | fservice_level | service_level | varchar | 50 |  | √ | ' ' | service_level |
| 142 | fex_contract | ex_contract | varchar | 200 |  | √ | ' ' | ex_contract |
| 143 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  | √ | ' ' | insert_batch_seq |
| 144 | fproxy_acc_name | proxy_acc_name | varchar | 255 |  | √ | ' ' | proxy_acc_name |
| 145 | furgent | urgent | varchar | 50 |  | √ | ' ' | urgent |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bd_paymentinfo_pkey |  | fid |
| 2 | idx_aqap_bd_paymentinfo_0 |  | fbatch_seq_id |
| 3 | idx_aqap_paymentinfo_accno |  | facc_no |
| 4 | idx_aqap_payment_ebgid_statusid |  | febg_id,fstatus_id |
| 5 | idx_aqap_payment_relative_id |  | frelative_id |
| 6 | idx_aqap_paymentinfo_inserttime |  | finsert_time |
| 7 | idx_aqap_payment_bizno |  | fdetail_biz_no,fback_bank_status |
| 8 | idx_aqap_payment_statusid_bank |  | fstatus_id,fbank_version_id |
| 9 | idx_aqap_payment_detail_seq |  | fdetail_seq_id |
| 10 | idx_aqap_payment_seq_status |  | fbank_batch_seq_id,fstatus_id |

---

## 付款记录-多语言表 t_aqap_bd_paymentinfo_l

- **表名称：** 付款记录-多语言表
- **表名：** t_aqap_bd_paymentinfo_l

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
| 1 | t_aqap_bd_paymentinfo_l_pkey |  | fpkid |
| 2 | idx_aqap_bd_paymentinfo_l_0 |  | fid,flocaleid |
