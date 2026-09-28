# 平台级证书存储表-aqap_platform_cert

## 平台级证书存储表-主表 t_aqap_platform_cert

- **表名称：** 平台级证书存储表-主表
- **表名：** t_aqap_platform_cert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ffile_name | 文件名称 | varchar | 50 |  | √ | ' ' | 文件名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbank_version_id | 银行版本编号 | varchar | 50 |  | √ | ' ' | 银行版本编号 |
| 6 | fbank_config_name | 证书字段名称 | varchar | 50 |  | √ | ' ' | 证书字段名称 |
| 7 | fbank_config_id | 证书字段标识 | varchar | 50 |  | √ | ' ' | 证书字段标识 |
| 8 | fbank_config_value | 证书字段值 | varchar | 255 |  | √ | ' ' | 证书字段值 |
| 9 | fexpire_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 10 | fbank_login_id | 前置机编号 | varchar | 50 |  | √ | ' ' | 前置机编号 |
| 11 | falert_day | 预警天数 | int8 | 64 |  |  | null | 预警天数 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 17 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | facnt_no | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fbank_config_value_tag | 证书字段值_详情 | text | 0 |  |  | null | 证书字段值_详情 |
| 22 | fcert_password | 证书密码 | varchar | 50 |  | √ | ' ' | 证书密码 |
| 23 | fis_alert | 是否预警 | varchar | 50 |  | √ | ' ' | 是否预警 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_platform_cert_pkey |  | fid |

---

## 平台级证书存储表-多语言表 t_aqap_platform_cert_l

- **表名称：** 平台级证书存储表-多语言表
- **表名：** t_aqap_platform_cert_l

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
| 1 | idx_aqap_platform_cert_l_0 |  | fid,flocaleid |
| 2 | t_aqap_platform_cert_l_pkey |  | fpkid |
