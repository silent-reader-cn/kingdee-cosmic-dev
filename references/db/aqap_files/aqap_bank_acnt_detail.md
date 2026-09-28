# 银企交易明细查询-aqap_bank_acnt_detail

## 银企交易明细查询-多语言表 t_aqap_bank_detail_l

- **表名称：** 银企交易明细查询-多语言表
- **表名：** t_aqap_bank_detail_l

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
| 1 | t_aqap_bank_detail_l_pkey |  | fpkid |
| 2 | idx_aqap_bank_detail_l_0 |  | fid,flocaleid |

---

## 银企交易明细查询-主表 t_aqap_bank_detail

- **表名称：** 银企交易明细查询-主表
- **表名：** t_aqap_bank_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fopp_accno | 对方账号 | varchar | 50 |  | √ | ' ' | 对方账号 |
| 3 | fdebit_amount | 借方/付款金额 | numeric | 23 | 10 |  | null | 借方/付款金额 |
| 4 | freceipt_no | 回单匹配码 | varchar | 255 |  |  | null | 回单匹配码 |
| 5 | facc_no | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 6 | ftrans_date | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | facc_name | 户名 | varchar | 50 |  | √ | ' ' | 户名 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fbank_acnt | 账号 | int8 | 64 |  |  | null | [银企账户 aqap_bank_acnt](../aqap_files/aqap_bank_acnt.md) |
| 13 | fbank_detail_no | 交易流水号 | varchar | 128 |  |  | null | 交易流水号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fdetail_no | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 16 | funique_seq | 银行主键 | varchar | 128 |  | √ | ' ' | 银行主键 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 19 | ftrans_time | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 20 | fmatch_node | 匹配节点 | varchar | 2 |  |  | null | 匹配节点,枚举: 1 :银行主键匹配 2 :明细基本属性全量匹配 3 :深度匹配 4 :深度匹配+流水号匹配 5 :深度未匹配（新增） 6 :银行主键未匹配（新增） |
| 21 | fcredit_amount | 贷方/收款金额 | numeric | 23 | 10 |  | null | 贷方/收款金额 |
| 22 | fexplanation | 摘要 | varchar | 50 |  | √ | ' ' | 摘要 |
| 23 | fis_key_repeat | 疑似重复 | varchar | 2 |  | √ | 0 | 疑似重复,枚举: 0 :否 1 :是 |
| 24 | fbank_version | 银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 25 | fbank_currency | 银行币别 | int8 | 64 |  |  | null | [银行币种映射 aqap_bank_currency](../aqap_files/aqap_bank_currency.md) |
| 26 | fopp_bankname | 对方银行 | varchar | 50 |  | √ | ' ' | 对方银行 |
| 27 | fbank_name | 银行名称 | varchar | 50 |  | √ | ' ' | 银行名称 |
| 28 | fsort_field | 排序字段 | varchar | 500 |  |  | ' ' | 排序字段 |
| 29 | fopp_accname | 对方账户名 | varchar | 50 |  | √ | ' ' | 对方账户名 |
| 30 | fbalance | 余额 | numeric | 23 | 10 |  | null | 余额 |
| 31 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fcurrencyfield | 币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_detail_pkey |  | fid |
