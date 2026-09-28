# 银行币种映射-aqap_bank_currency

## 银行币种映射-多语言表 t_aqap_bank_currency_l

- **表名称：** 银行币种映射-多语言表
- **表名：** t_aqap_bank_currency_l

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
| 1 | t_aqap_bank_currency_l_pkey |  | fpkid |
| 2 | idx_aqap_bank_currency_l_0 |  | fid,flocaleid |

---

## 银行币种映射-主表 t_aqap_bank_currency

- **表名称：** 银行币种映射-主表
- **表名：** t_aqap_bank_currency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 6 | fiso | ISO币种 | int8 | 64 |  |  | null | ISO币别管理 aqap_iso_currency |
| 7 | fbank_currency | 银行币种编号 | varchar | 50 |  | √ | ' ' | 银行币种编号 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_bank_currency_un |  | fbank_version,fiso |
| 2 | t_aqap_bank_currency_pkey |  | fid |
