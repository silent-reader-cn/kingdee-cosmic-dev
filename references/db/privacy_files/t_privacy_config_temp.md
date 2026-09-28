# 隐私方案配置_模板-t_privacy_config_temp

## 加密规则模板-子表 t_privacy_encrypt_tpl

- **表名称：** 加密规则模板-子表
- **表名：** t_privacy_encrypt_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fencrypt_field_name | 物理字段名 | varchar | 50 |  | √ | ' ' | 物理字段名 |
| 3 | fapp_route | 所属库 | varchar | 50 |  | √ | ' ' | 所属库 |
| 4 | fencrypt_app_name | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 5 | fencrypt_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :已生效 0 :生效中 |
| 6 | fencrypt_app_number | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 7 | fencrypt_algorithm | 加密方案 | varchar | 50 |  | √ | ' ' | 加密方案,枚举: NO :不加密 AES :AES加密 SM4 :SM4加密 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fencrypt_field_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 10 | fencrypt_cloud_name | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 11 | fencrypt_entity_name | 所属实体 | varchar | 50 |  | √ | ' ' | 所属实体 |
| 12 | fencrypt_cloud_number | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 13 | fencrypt_field_ident | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 14 | flabelid | 标签id | int8 | 64 |  |  | null | 标签id |
| 15 | fencrypt_schemeid | fencrypt_schemeid | int8 | 64 |  |  | null |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 17 | fencrypt_field_desc | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 18 | fencrypt_entity_number | 所属实体 | varchar | 50 |  | √ | ' ' | 所属实体 |
| 19 | fversion | 版本 | int8 | 64 |  |  | null | 版本 |
| 20 | fencrypt_table_name | 物理表名 | varchar | 50 |  | √ | ' ' | 物理表名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_privacy_encrypt_tpl |  | fentryid |

---

## 隐私方案配置_模板-主表 t_privacy_config_tpl

- **表名称：** 隐私方案配置_模板-主表
- **表名：** t_privacy_config_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fscheme_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :发布中 1 :已发布 |
| 3 | fscheme_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifier | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fcreater | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fmessagechannel | 消息渠道 | varchar | 50 |  | √ | ' ' | 消息渠道,枚举: CLOUDHUB :云之家 EMAIL :邮件 MESSAGE :短信 |
| 10 | fscheme_code | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fscheme_desc | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 12 | fdatalabelid | 数据安全标签 | int8 | 64 |  |  | null | 数据安全标签模板 privacy_data_tags_temp |
| 13 | ftemplate | 消息模板 | varchar | 255 |  | √ | ' ' | 消息模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_privacy_config_tpl |  | fid |

---

## 脱敏规则模板-子表 t_privacy_desen_tpl

- **表名称：** 脱敏规则模板-子表
- **表名：** t_privacy_desen_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fdense_field_name | 物理字段名 | varchar | 50 |  | √ | ' ' | 物理字段名 |
| 3 | fdensefieldlocale | 所属语言 | varchar | 50 |  | √ | ' ' | 所属语言,枚举: zh_CN :中文 |
| 4 | fdense_entity_number | 所属实体 | varchar | 50 |  | √ | ' ' | 所属实体 |
| 5 | fdense_app_number | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 6 | fdense_app_name | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdense_table_name | 物理表名 | varchar | 50 |  | √ | ' ' | 物理表名 |
| 9 | fdense_field_ident | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 10 | fdesensitize_rule | 脱敏规则 | varchar | 50 |  | √ | ' ' | 脱敏规则,枚举: NO :不脱敏 QT :全部显示为* FL :只显示前后各1位明文 GD :固定6位显示* ZD :自定义 FOLLOW :跟随默认 TP :手机号码 NM :姓名 IDCARD :身份证 BC :银行卡 |
| 11 | fdense_field_desc | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 12 | fdense_field_locale | fdense_field_locale | varchar | 50 |  | √ | ' ' |  |
| 13 | fdesensitize_type | 脱敏类型 | varchar | 50 |  | √ | ' ' | 脱敏类型,枚举: SYSTEM :系统预置 CUSTOM :自定义 |
| 14 | fdense_cloud_name | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 15 | fdense_entity_name | 所属实体 | varchar | 50 |  | √ | ' ' | 所属实体 |
| 16 | fdesensitiz_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :已生效 0 :生效中 |
| 17 | fdense_cloud_number | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 18 | fplugin | 插件地址 | varchar | 50 |  | √ | ' ' | 插件地址 |
| 19 | flabelid | 标签id | int8 | 64 |  |  | null | 标签id |
| 20 | fdense_field_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_desen_tpl |  | fentryid |

---

## 隐私方案配置_模板-多语言表 t_privacy_config_tpl_l

- **表名称：** 隐私方案配置_模板-多语言表
- **表名：** t_privacy_config_tpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscheme_name | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_privacy_config_tpl_l |  | fpkid |
| 2 | idx_privacy_config_tpl_l_fid |  | fid,flocaleid |
