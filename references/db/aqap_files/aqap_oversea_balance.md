# 外资银行余额表-aqap_oversea_balance

## 外资银行余额表-多语言表 t_aqap_oversea_balance_l

- **表名称：** 外资银行余额表-多语言表
- **表名：** t_aqap_oversea_balance_l

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
| 1 | t_aqap_oversea_balance_l_pkey |  | fpkid |

---

## 外资银行余额表-主表 t_aqap_oversea_balance

- **表名称：** 外资银行余额表-主表
- **表名：** t_aqap_oversea_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbalance_date | 余额日期 | timestamp | 0 |  |  | null | 余额日期 |
| 3 | ffrozen_balance | 冻结余额 | numeric | 23 | 2 |  | null | 冻结余额 |
| 4 | favailable_balance | 可用余额 | numeric | 23 | 2 |  | null | 可用余额 |
| 5 | fext_config_field | ext_Config_Field | varchar | 300 |  |  | ' ' | ext_Config_Field |
| 6 | fext_system_field | ext_System_Field | varchar | 200 |  |  | ' ' | ext_System_Field |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fupdate_source | 来源 | varchar | 100 |  |  | ' ' | 来源 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fext_field1 | ext_Field1 | varchar | 100 |  |  | ' ' | ext_Field1 |
| 11 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | flast_day_balance | 昨日余额 | numeric | 23 | 2 |  | null | 昨日余额 |
| 15 | fext_field4 | ext_field4 | varchar | 100 |  |  | ' ' | ext_field4 |
| 16 | fext_field2 | ext_field2 | varchar | 100 |  |  | ' ' | ext_field2 |
| 17 | fext_field3 | ext_field3 | varchar | 100 |  |  | ' ' | ext_field3 |
| 18 | fcurrent_balance | 当前余额 | numeric | 23 | 2 |  | null | 当前余额 |
| 19 | fname | 户名 | varchar | 50 |  |  | ' ' | 户名 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fext_biz_field | ext_Biz_Field | varchar | 300 |  |  | ' ' | ext_Biz_Field |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fcurrency | 币别 | varchar | 10 |  |  | ' ' | 币别 |
| 24 | fbank_version | 银行版本 | varchar | 50 |  |  | ' ' | 银行版本 |
| 25 | fbank_name | 银行名称 | varchar | 100 |  |  | ' ' | 银行名称 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 账号 | varchar | 30 |  | √ | ' ' | 账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_oversea_balance_0 |  | fnumber,fbalance_date |
| 2 | t_aqap_oversea_balance_pkey |  | fid |
