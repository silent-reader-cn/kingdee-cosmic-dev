# 应付票据交易记录-note_payable

## 应付票据交易记录-多语言表 t_note_payable_l

- **表名称：** 应付票据交易记录-多语言表
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

## 应付票据交易记录-主表 t_note_payable

- **表名称：** 应付票据交易记录-主表
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
| 8 | facpflg | 承兑类型 | varchar | 2 |  | √ | ' ' | 承兑类型 |
| 9 | fcontract_obj | contract_obj | varchar | 50 |  |  | ' ' | contract_obj |
| 10 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 11 | fbankbatchcount | 银行批次数量 | int4 | 32 |  | √ | 0 | 银行批次数量 |
| 12 | fbalbizno | 保证金业务流水 | varchar | 50 |  |  | ' ' | 保证金业务流水 |
| 13 | fbak_bank_msg | bak_bank_msg | varchar | 1000 |  |  | ' ' | bak_bank_msg |
| 14 | fbank_msg | bank_msg | varchar | 255 |  |  | ' ' | bank_msg |
| 15 | fversion | version | int8 | 64 |  |  | null | version |
| 16 | ftotal_amount | total_amount | numeric | 23 | 10 |  | null | total_amount |
| 17 | fissue_date | issue_date | varchar | 50 |  |  | ' ' | issue_date |
| 18 | fsub_biz_type | sub_biz_type | varchar | 50 |  | √ | ' ' | sub_biz_type,枚举: remit_register :出票 remit_accept :提示承兑 remit_receive :提示收票 remit_cancle :撤销 remit_revocation :撤票 nonnegotiable_cancle :不可转让撤销 |
| 19 | fexplanation | explanation | varchar | 255 |  |  | ' ' | explanation |
| 20 | fquery_type | query_type | varchar | 50 |  |  | ' ' | query_type |
| 21 | fbatchtotalamount | 金额3 | numeric | 23 | 10 |  | null | 金额3 |
| 22 | fdrawer_acc_name | drawer_acc_name | varchar | 50 |  |  | ' ' | drawer_acc_name |
| 23 | fsubrange | 文本91 | varchar | 50 |  |  | ' ' | 文本91 |
| 24 | facceptor_bank_address | acceptor_bank_address | varchar | 50 |  |  | ' ' | acceptor_bank_address |
| 25 | fpayee_bank_cnaps | payee_bank_cnaps | varchar | 50 |  |  | ' ' | payee_bank_cnaps |
| 26 | fstatus_name | status_name | varchar | 50 |  |  | ' ' | status_name |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fsubmit_success_time | submit_success_time | timestamp | 0 |  |  | null | submit_success_time |
| 29 | fpackage_key | package_key | varchar | 255 |  |  | ' ' | package_key |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | fbalepayacname | 保证金付款账户名称 | varchar | 255 |  | √ | ' ' | 保证金付款账户名称 |
| 32 | fpayee_country | payee_country | varchar | 50 |  |  | ' ' | payee_country |
| 33 | fisacceptsamebank | 文本93 | varchar | 5 |  |  | ' ' | 文本93 |
| 34 | fdrawer_bank_address | drawer_bank_address | varchar | 50 |  |  | ' ' | drawer_bank_address |
| 35 | fisonlinebal | 是否在线开立保证金 | varchar | 10 |  |  | ' ' | 是否在线开立保证金 |
| 36 | fnote_status | note_status | varchar | 10 |  |  | ' ' | note_status,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 37 | fisnewecds | 文本85 | varchar | 50 |  |  | ' ' | 文本85 |
| 38 | fbank_batch_seq_id | bank_batch_seq_id | varchar | 50 |  |  | ' ' | bank_batch_seq_id |
| 39 | fdrawer_acc_province | drawer_acc_province | varchar | 50 |  |  | ' ' | drawer_acc_province |
| 40 | frqstserialno | rqstserialno | varchar | 50 |  |  | ' ' | rqstserialno |
| 41 | fdraft_type | draft_type | varchar | 8 |  |  | ' ' | draft_type |
| 42 | fbak_status_msg | bak_status_msg | varchar | 50 |  |  | ' ' | bak_status_msg |
| 43 | fdue_date | due_date | timestamp | 0 |  |  | null | due_date |
| 44 | facceptor_acc_no | acceptor_acc_no | varchar | 50 |  |  | ' ' | acceptor_acc_no |
| 45 | famount | amount | numeric | 23 | 10 |  | null | amount |
| 46 | fpayee_bank_name | payee_bank_name | varchar | 50 |  |  | ' ' | payee_bank_name |
| 47 | fauto_accept | auto_accept | varchar | 1 |  |  | ' ' | auto_accept |
| 48 | fispayeesamebank | 文本92 | varchar | 5 |  |  | ' ' | 文本92 |
| 49 | foperation_code | operation_code | varchar | 10 |  |  | ' ' | operation_code |
| 50 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 12 :交易成功 11 :交易未确认 10 :银行处理中 13 :交易失败 9 :正在提交银行 7 :打包处理中 0 :尚未处理,还未打包 |
| 51 | fcustom_id | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 52 | fsync_count | sync_count | int8 | 64 |  |  | null | sync_count |
| 53 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 55 | fkeep_flag | keep_flag | varchar | 10 |  |  | ' ' | keep_flag |
| 56 | ftotal_count | total_count | int8 | 64 |  |  | null | total_count |
| 57 | fbalterm | 保证金期限 | varchar | 10 |  |  | ' ' | 保证金期限 |
| 58 | febg_id | ebg_id | varchar | 50 |  | √ | ' ' | ebg_id |
| 59 | fbalamount | 保证金金额 | numeric | 23 | 10 |  | null | 保证金金额 |
| 60 | fother_info | other_info | varchar | 50 |  |  | ' ' | other_info |
| 61 | fdrawer_bank_cnaps | drawer_bank_cnaps | varchar | 20 |  |  | ' ' | drawer_bank_cnaps |
| 62 | fbankrefkey | 文本90 | varchar | 255 |  |  | 0 | 文本90 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fupdate_operation | update_operation | varchar | 50 |  |  | ' ' | update_operation |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fbak_status_name | bak_status_name | varchar | 50 |  |  | ' ' | bak_status_name |
| 67 | flast_sync_request_seq | last_sync_request_seq | varchar | 50 |  |  | ' ' | last_sync_request_seq |
| 68 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 69 | fisrefuse | 是否被拒签 | varchar | 50 |  |  | ' ' | 是否被拒签 |
| 70 | fcirstatus | cirstatus | varchar | 50 |  |  | ' ' | cirstatus,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 71 | fbaltermunit | 保证金期限单元 | varchar | 10 |  |  | ' ' | 保证金期限单元 |
| 72 | fobssid | obssid | varchar | 50 |  |  | ' ' | obssid |
| 73 | fstatus_msg | status_msg | varchar | 255 |  |  | ' ' | status_msg |
| 74 | ftotalsize | 整数4 | int8 | 64 |  |  | 0 | 整数4 |
| 75 | fbank_serial_no | bank_serial_no | varchar | 50 |  |  | ' ' | bank_serial_no |
| 76 | fbooking_date | booking_date | timestamp | 0 |  |  | null | booking_date |
| 77 | fbaleac | 保证金账户 | varchar | 50 |  |  | ' ' | 保证金账户 |
| 78 | fbatch_seq_id | batch_seq_id | varchar | 50 |  | √ | ' ' | batch_seq_id |
| 79 | fgrdbag | 文本86 | varchar | 50 |  |  | ' ' | 文本86 |
| 80 | fbak_bank_status | bak_bank_status | varchar | 50 |  |  | ' ' | bak_bank_status |
| 81 | fbankrefdate | 文本89 | varchar | 50 |  |  | ' ' | 文本89 |
| 82 | facceptor_bank_name | acceptor_bank_name | varchar | 50 |  |  | ' ' | acceptor_bank_name |
| 83 | fsequence | sequence | varchar | 50 |  |  | ' ' | sequence |
| 84 | fdraftamount | 金额2 | numeric | 23 | 10 |  | null | 金额2 |
| 85 | fdrawer_due_date | drawer_due_date | timestamp | 0 |  |  | null | drawer_due_date |
| 86 | fdetail_seq_id | detail_seq_id | varchar | 50 |  |  | ' ' | detail_seq_id |
| 87 | facceptor_acc_country | acceptor_acc_country | varchar | 50 |  |  | ' ' | acceptor_acc_country |
| 88 | facceptor_acc_city | acceptor_acc_city | varchar | 50 |  |  | ' ' | acceptor_acc_city |
| 89 | fbaleacname | 保证金账户名称 | varchar | 150 |  |  | ' ' | 保证金账户名称 |
| 90 | flast_sync_time | last_sync_time | timestamp | 0 |  |  | null | last_sync_time |
| 91 | ffilelist_tag | 交易附件信息_详情 | text | 0 |  |  | null | 交易附件信息_详情 |
| 92 | fdetail_biz_no | detail_biz_no | varchar | 50 |  |  | ' ' | detail_biz_no |
| 93 | fdrawer_ratings | drawer_ratings | varchar | 50 |  |  | ' ' | drawer_ratings |
| 94 | flast_submit_time | last_submit_time | timestamp | 0 |  |  | null | last_submit_time |
| 95 | fpayee_org | 收票人机构号 | varchar | 50 |  |  | ' ' | 收票人机构号 |
| 96 | fbalcurrency | 保证金货币种类 | varchar | 4 |  | √ | ' ' | 保证金货币种类 |
| 97 | freserved4 | reserved4 | varchar | 255 |  |  | '0' | reserved4 |
| 98 | freserved2 | reserved2 | varchar | 255 |  |  | '0' | reserved2 |
| 99 | freserved3 | reserved3 | varchar | 255 |  |  | '0' | reserved3 |
| 100 | fdrawer_bank_name | drawer_bank_name | varchar | 50 |  |  | ' ' | drawer_bank_name |
| 101 | fsubmit_count | submit_count | int8 | 64 |  |  | null | submit_count |
| 102 | fto_give_up | to_give_up | varchar | 50 |  |  | ' ' | to_give_up |
| 103 | freserved1 | reserved1 | varchar | 255 |  |  | '0' | reserved1 |
| 104 | fauto_receive | auto_receive | varchar | 1 |  |  | ' ' | auto_receive |
| 105 | foperation_name | operation_name | varchar | 50 |  |  | ' ' | operation_name |
| 106 | fbalepayac | 保证金付款账号 | varchar | 50 |  | √ | ' ' | 保证金付款账号 |
| 107 | facceptor_acc_name | acceptor_acc_name | varchar | 50 |  |  | ' ' | acceptor_acc_name |
| 108 | facceptor_acc_province | acceptor_acc_province | varchar | 50 |  |  | ' ' | acceptor_acc_province |
| 109 | fbalrate | 保证金利率 | varchar | 10 |  |  | ' ' | 保证金利率 |
| 110 | fpayee_bank_address | payee_bank_address | varchar | 50 |  |  | ' ' | payee_bank_address |
| 111 | facpfer | 承兑手续费% | varchar | 50 |  | √ | ' ' | 承兑手续费% |
| 112 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 113 | fbank_status | bank_status | varchar | 60 |  |  | 0 | bank_status |
| 114 | fbaltyp | 保证金类型 | varchar | 4 |  | √ | ' ' | 保证金类型 |
| 115 | fpayee_acc_no | payee_acc_no | varchar | 50 |  |  | ' ' | payee_acc_no |
| 116 | fbank_detail_seq_id | bank_detail_seq_id | varchar | 50 |  |  | ' ' | bank_detail_seq_id |
| 117 | ferror_msg | error_msg | varchar | 255 |  |  | ' ' | error_msg |
| 118 | fdrawer_acc_country | drawer_acc_country | varchar | 50 |  |  | ' ' | drawer_acc_country |
| 119 | fbiz_type | fbiz_type | varchar | 50 |  | √ | ' ' | fbiz_type |
| 120 | fquery_impl_class_name | query_impl_class_name | varchar | 255 |  | √ | ' ' | query_impl_class_name |
| 121 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 122 | frequest_seq | request_seq | varchar | 50 |  |  | ' ' | request_seq |
| 123 | frspserialno | rspserialno | varchar | 50 |  |  | ' ' | rspserialno |
| 124 | ftransfer_flag | transfer_flag | varchar | 10 |  |  | ' ' | transfer_flag |
| 125 | fpackage_time | package_time | timestamp | 0 |  |  | null | package_time |
| 126 | fpayee_city | payee_city | varchar | 50 |  |  | ' ' | payee_city |
| 127 | fcontract_no | contract_no | varchar | 50 |  |  | ' ' | contract_no |
| 128 | fstartno | 文本87 | varchar | 100 |  |  | ' ' | 文本87 |
| 129 | fpayee_province | payee_province | varchar | 50 |  |  | ' ' | payee_province |
| 130 | fpay_finish_time | pay_finish_time | timestamp | 0 |  |  | null | pay_finish_time |
| 131 | fpayee_acc_name | payee_acc_name | varchar | 50 |  |  | ' ' | payee_acc_name |
| 132 | fbak_error_msg | bak_error_msg | varchar | 255 |  |  | ' ' | bak_error_msg |
| 133 | fcurrency | currency | varchar | 10 |  |  | ' ' | currency |
| 134 | fdrawer_agency | drawer_agency | varchar | 50 |  |  | ' ' | drawer_agency |
| 135 | fendno | 文本88 | varchar | 100 |  |  | ' ' | 文本88 |
| 136 | finvoice_no | invoice_no | varchar | 50 |  |  | ' ' | invoice_no |
| 137 | flast_submit_request_seq | last_submit_request_seq | varchar | 50 |  |  | ' ' | last_submit_request_seq |
| 138 | fbak_status | bak_status | varchar | 60 |  |  | 0 | bak_status |
| 139 | finsert_batch_seq | insert_batch_seq | varchar | 50 |  |  | ' ' | insert_batch_seq |
| 140 | fdrawer_acc_no | drawer_acc_no | varchar | 50 |  |  | ' ' | drawer_acc_no |
| 141 | ffilelist | 交易附件信息 | varchar | 10 |  | √ | ' ' | 交易附件信息 |
| 142 | fbill_no | bill_no | varchar | 50 |  |  | ' ' | bill_no |
| 143 | facceptor_org | 承兑人机构号 | varchar | 50 |  |  | ' ' | 承兑人机构号 |
| 144 | fbalcontractno | 保证金协议编号 | varchar | 50 |  |  | ' ' | 保证金协议编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_schedule_payable |  | fstatus,finsert_time |
| 2 | t_note_payable_pkey |  | fid |
| 3 | idx_note_payable_batch_seq |  | fbatch_seq_id |
