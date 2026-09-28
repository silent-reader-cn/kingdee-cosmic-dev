# （废弃）CA证书存储表-aqap_auth

## （废弃）CA证书存储表-多语言表 t_aqap_auth_l

- **表名称：** （废弃）CA证书存储表-多语言表
- **表名：** t_aqap_auth_l

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
| 1 | idx_aqap_auth_l_0 |  | fid,flocaleid |
| 2 | t_aqap_auth_l_pkey |  | fpkid |

---

## （废弃）CA证书存储表-主表 t_aqap_auth

- **表名称：** （废弃）CA证书存储表-主表
- **表名：** t_aqap_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forganization | 公司组织 | varchar | 50 |  | √ | ' ' | 公司组织 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpublic_key | 证书公钥 | varchar | 255 |  | √ | ' ' | 证书公钥 |
| 6 | fpublic_key_tag | 证书公钥_详情 | text | 0 |  |  | null | 证书公钥_详情 |
| 7 | fexpire_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 8 | falert_day | 预警天数 | int8 | 64 |  |  | null | 预警天数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | ftype | 证书类型 | varchar | 50 |  | √ | ' ' | 证书类型 |
| 15 | fcert_name | 证书名称 | varchar | 50 |  | √ | ' ' | 证书名称 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fis_alert | 是否预警 | varchar | 50 |  | √ | ' ' | 是否预警 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_auth_pkey |  | fid |
