# 前置机配置存储表-aqap_bank_login_config

## 前置机配置存储表-多语言表 t_aqap_bank_login_config_l

- **表名称：** 前置机配置存储表-多语言表
- **表名：** t_aqap_bank_login_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_login_config_l_pkey |  | fpkid |
| 2 | idx_aqap_bank_login_config_l_0 |  | fid,flocaleid |

---

## 前置机配置存储表-主表 t_aqap_bank_login_config

- **表名称：** 前置机配置存储表-主表
- **表名：** t_aqap_bank_login_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fconfig_type | 配置类型 | varchar | 50 |  | √ | ' ' | 配置类型 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbank_version_id | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 6 | fbank_config_id | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 7 | fbank_config_value | 字段值 | varchar | 1024 |  | √ | ' ' | 字段值 |
| 8 | fnullable | 是否允许为空 | varchar | 50 |  | √ | ' ' | 是否允许为空 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | freadonly | 是否只读 | varchar | 50 |  | √ | ' ' | 是否只读 |
| 12 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | finput_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 前置机编码 | varchar | 30 |  | √ | ' ' | 前置机编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_login_config_pkey |  | fid |
