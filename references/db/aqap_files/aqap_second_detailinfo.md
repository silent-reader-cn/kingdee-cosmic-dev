# 交易明细第二通道存储表-aqap_second_detailinfo

## 交易明细第二通道存储表-主表 t_aqap_second_detailinfo

- **表名称：** 交易明细第二通道存储表-主表
- **表名：** t_aqap_second_detailinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | freversed1 | reversed1 | varchar | 255 |  | √ | ' ' | reversed1 |
| 3 | freversed2 | reversed2 | varchar | 50 |  | √ | ' ' | reversed2 |
| 4 | freversed3 | reversed3 | varchar | 255 |  | √ | ' ' | reversed3 |
| 5 | fagent_acc_name | agent_acc_name | varchar | 255 |  | √ | ' ' | agent_acc_name |
| 6 | freversed4 | reversed4 | varchar | 255 |  | √ | ' ' | reversed4 |
| 7 | fbank_version_id | bank_version_id | varchar | 20 |  | √ | ' ' | bank_version_id |
| 8 | favailable_balance | available_balance | numeric | 23 | 10 |  | null | available_balance |
| 9 | fdetail_id | detail_id | varchar | 50 |  | √ | ' ' | detail_id |
| 10 | ftrans_date | trans_date | timestamp | 0 |  |  | null | trans_date |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | facc_name | acc_name | varchar | 255 |  | √ | ' ' | acc_name |
| 13 | fimpl_class_name | impl_class_name | varchar | 255 |  | √ | ' ' | impl_class_name |
| 14 | fagent_acc_no | agent_acc_no | varchar | 50 |  | √ | ' ' | agent_acc_no |
| 15 | fbank_detail_no | 交易流水号 | varchar | 128 |  | √ | ' ' | 交易流水号 |
| 16 | ftrans_type | trans_type | varchar | 50 |  | √ | ' ' | trans_type |
| 17 | facc_type | acc_type | varchar | 50 |  | √ | ' ' | acc_type |
| 18 | fbus_type | bus_type | varchar | 50 |  | √ | ' ' | bus_type |
| 19 | funique_seq | unique_seq | varchar | 255 |  | √ | ' ' | unique_seq |
| 20 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 21 | ftrans_time | trans_time | timestamp | 0 |  |  | null | trans_time |
| 22 | fbiz_ref_no | biz_ref_no | varchar | 50 |  | √ | ' ' | biz_ref_no |
| 23 | funique_version | 银行主键版本 | varchar | 50 |  | √ | ' ' | 银行主键版本 |
| 24 | fexplanation | explanation | varchar | 1000 |  | √ | ' ' | explanation |
| 25 | fbank_name | bank_name | varchar | 255 |  | √ | ' ' | bank_name |
| 26 | fsort_field | 排序字段 | varchar | 500 |  |  | ' ' | 排序字段 |
| 27 | fbalance | balance | numeric | 23 | 10 |  | null | balance |
| 28 | fopp_acc_no | opp_acc_no | varchar | 50 |  | √ | ' ' | opp_acc_no |
| 29 | ftransfer_charge | transfer_charge | numeric | 23 | 10 |  | null | transfer_charge |
| 30 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fagent_acc_bank_name | agent_acc_bank_name | varchar | 255 |  | √ | ' ' | agent_acc_bank_name |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | fsort_id | sort_id | varchar | 50 |  | √ | ' ' | sort_id |
| 34 | fcreate_date | 查询日期 | int8 | 64 |  |  | null | 查询日期 |
| 35 | fdebit_amount | debit_amount | numeric | 23 | 10 |  | null | debit_amount |
| 36 | freceipt_no | receipt_no | varchar | 255 |  | √ | ' ' | receipt_no |
| 37 | fupdate_time | update_time | timestamp | 0 |  |  | null | update_time |
| 38 | facc_no | acc_no | varchar | 50 |  | √ | ' ' | acc_no |
| 39 | freversed_sys_field | reversed_sys_field | varchar | 600 |  | √ | ' ' | reversed_sys_field |
| 40 | finsert_time | insert_time | timestamp | 0 |  |  | null | insert_time |
| 41 | fvouh_no | vouh_no | varchar | 255 |  | √ | ' ' | vouh_no |
| 42 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 43 | fcustom_id | custom_id | varchar | 50 |  | √ | ' ' | custom_id |
| 44 | fserial_no | serial_no | int8 | 64 |  |  | null | serial_no |
| 45 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 47 | fopp_bank_name | opp_bank_name | varchar | 255 |  | √ | ' ' | opp_bank_name |
| 48 | fpay_detail_seq_id | pay_detail_seq_id | varchar | 50 |  | √ | ' ' | pay_detail_seq_id |
| 49 | freversed_biz_field | reversed_biz_field | varchar | 600 |  | √ | ' ' | reversed_biz_field |
| 50 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fcurrency | currency | varchar | 50 |  | √ | ' ' | currency |
| 53 | fcredit_amount | credit_amount | numeric | 23 | 10 |  | null | credit_amount |
| 54 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 55 | fkd_flag | kd_flag | varchar | 50 |  | √ | ' ' | kd_flag |
| 56 | fuse_cn | use_cn | varchar | 500 |  | √ | ' ' | use_cn |
| 57 | fopp_acc_name | opp_acc_name | varchar | 255 |  | √ | ' ' | opp_acc_name |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_second_detailinfo |  | fid |
| 2 | idx_aqap_sec_del_ac_tr |  | facc_no,ftrans_date |

---

## 交易明细第二通道存储表-多语言表 t_aqap_second_detailinfo_l

- **表名称：** 交易明细第二通道存储表-多语言表
- **表名：** t_aqap_second_detailinfo_l

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
| 1 | idx_aqap_sec_del_l_0 |  | fid,flocaleid |
| 2 | pk_t_aqap_second_detailinfo_l |  | fpkid |
