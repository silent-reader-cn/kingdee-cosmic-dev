# 外资银行交易明细表-aqap_oversea_detail

## 外资银行交易明细表-主表 t_aqap_oversea_detail

- **表名称：** 外资银行交易明细表-主表
- **表名：** t_aqap_oversea_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbenefit_acc_no | 收款账号 | varchar | 50 |  |  | ' ' | 收款账号 |
| 3 | fbenefit_bank_name | 收款行名 | varchar | 250 |  |  | ' ' | 收款行名 |
| 4 | ftx_amt | 交易金额 | numeric | 23 | 2 |  | null | 交易金额 |
| 5 | fext_config_field | ext_Config_Field | varchar | 300 |  |  | ' ' | ext_Config_Field |
| 6 | fext_system_field | ext_System_Field | varchar | 300 |  |  | ' ' | ext_System_Field |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftextfield | ftextfield | varchar | 50 |  |  | ' ' |  |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fext_field1 | ext_Field1 | varchar | 100 |  |  | ' ' | ext_Field1 |
| 11 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fdetail_type | detail_Type | varchar | 50 |  |  | ' ' | detail_Type |
| 15 | fext_field4 | ext_Field4 | varchar | 100 |  |  | ' ' | ext_Field4 |
| 16 | fext_field2 | ext_Field2 | varchar | 100 |  |  | ' ' | ext_Field2 |
| 17 | fext_field3 | ext_Field3 | varchar | 100 |  |  | ' ' | ext_Field3 |
| 18 | fbenefit_acc_name | 收款户名 | varchar | 250 |  |  | ' ' | 收款户名 |
| 19 | fmemory | memory | varchar | 350 |  |  | ' ' | memory |
| 20 | ftx_date | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 21 | ftrans_type | trans_Type | varchar | 10 |  |  | ' ' | trans_Type |
| 22 | fpay_bank_version | 银行版本 | varchar | 50 |  |  | ' ' | 银行版本 |
| 23 | fpay_bank_name | 付款银行名 | varchar | 50 |  |  | ' ' | 付款银行名 |
| 24 | fname | 户名 | varchar | 50 |  |  | ' ' | 户名 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 26 | fdetail_no | detail_No | varchar | 250 |  |  | ' ' | detail_No |
| 27 | fext_biz_field | ext_Biz_Field | varchar | 300 |  |  | ' ' | ext_Biz_Field |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fdetail_file_name | 交易明细文件名 | varchar | 250 |  |  | ' ' | 交易明细文件名 |
| 30 | fcurrency | 币别 | varchar | 10 |  |  | ' ' | 币别 |
| 31 | fexplanation | 附言 | varchar | 500 |  |  | ' ' | 附言 |
| 32 | fbank_orderid | bank_OrderId | varchar | 50 |  |  | ' ' | bank_OrderId |
| 33 | fuse_desc | use_Desc | varchar | 500 |  |  | ' ' | use_Desc |
| 34 | fcord_flag | cord_Flag | varchar | 50 |  |  | ' ' | cord_Flag |
| 35 | fbalance | 余额 | numeric | 23 | 2 |  | null | 余额 |
| 36 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 付款账号 | varchar | 30 |  |  | ' ' | 付款账号 |
| 38 | fpayid | payId | varchar | 50 |  |  | ' ' | payId |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_oversea_detail_0 |  | fnumber,ftx_date |
| 2 | t_aqap_oversea_detail_pkey |  | fid |

---

## 外资银行交易明细表-多语言表 t_aqap_oversea_detail_l

- **表名称：** 外资银行交易明细表-多语言表
- **表名：** t_aqap_oversea_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 户名 | varchar | 50 |  | √ | ' ' | 户名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_oversea_detail_l_pkey |  | fpkid |
