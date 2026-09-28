# 银企账户_前置机连接监控-aqap_bank_monitor_acnt

## 银企账户_前置机连接监控-多语言表 t_aqap_bank_acnt_l

- **表名称：** 银企账户_前置机连接监控-多语言表
- **表名：** t_aqap_bank_acnt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 户名 | varchar | 500 |  | √ | ' ' | 户名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_acnt_l_pkey |  | fpkid |
| 2 | idx_aqap_bank_acnt_l_0 |  | fid,flocaleid |

---

## 银企账户_前置机连接监控-主表 t_aqap_bank_acnt

- **表名称：** 银企账户_前置机连接监控-主表
- **表名：** t_aqap_bank_acnt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fgroupid | 银行 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 3 | fbank_version_id | bank_version_id | varchar | 50 |  | √ | ' ' | bank_version_id |
| 4 | fbranch_name | 运营机构名称 | varchar | 255 |  |  | ' ' | 运营机构名称 |
| 5 | fbranch_no | 运营机构编码 | varchar | 30 |  |  | ' ' | 运营机构编码 |
| 6 | favailable_balance | favailable_balance | numeric | 23 | 10 |  | null |  |
| 7 | fbank_short_name | bank_short_name | varchar | 50 |  | √ | ' ' | bank_short_name |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | facnt_has_receipt | facnt_has_receipt | varchar | 50 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fcity | city | varchar | 50 |  | √ | ' ' | city |
| 15 | faddr | 开户地区 | varchar | 50 |  | √ | ' ' | 开户地区 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 17 | fsel_bal_time | fsel_bal_time | timestamp | 0 |  |  | null |  |
| 18 | fbank_login | 编号 | int8 | 64 |  |  | null | 银企连接通道配置 aqap_bank_login |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fcurrency | 币种 | int8 | 64 |  |  | null | 银行币种映射 aqap_bank_currency |
| 21 | fiso_currency | iso_currency | varchar | 50 |  | √ | ' ' | iso_currency |
| 22 | fbank_login_id | bank_login_id | varchar | 50 |  | √ | ' ' | bank_login_id |
| 23 | fbank_name | bank_name | varchar | 50 |  | √ | ' ' | bank_name |
| 24 | fbalance | fbalance | numeric | 23 | 10 |  | null |  |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fhas_receipt | 是否电子回单账号 | varchar | 50 |  | √ | ' ' | 是否电子回单账号,枚举: 0 :否 1 :是 |
| 27 | fbank_address | bank_address | varchar | 50 |  | √ | ' ' | bank_address |
| 28 | fnumber | 账号 | varchar | 30 |  | √ | ' ' | 账号 |
| 29 | fhas_note | 是否电票账号 | varchar | 50 |  |  | ' ' | 是否电票账号,枚举: 0 :否 1 :是 |
| 30 | fprovince | province | varchar | 50 |  | √ | ' ' | province |
| 31 | fcountry | country | varchar | 50 |  | √ | ' ' | country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_acnt_pkey |  | fid |
