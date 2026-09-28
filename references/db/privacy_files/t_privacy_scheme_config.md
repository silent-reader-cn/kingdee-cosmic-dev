# 隐私方案配置-t_privacy_scheme_config

## 隐私方案配置-主表 t_privacy_scheme_config

- **表名称：** 隐私方案配置-主表
- **表名：** t_privacy_scheme_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fscheme_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :发布中 1 :已发布 |
| 3 | fscheme_name | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | ftemplateid | 隐私模板 | int8 | 64 |  | √ | 0 | [隐私方案配置_模板 t_privacy_config_temp](../privacy_files/t_privacy_config_temp.md) |
| 5 | fmodifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fcreater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmessagechannel | 消息渠道 | varchar | 50 |  | √ | ' ' | 消息渠道,枚举: CLOUDHUB :云之家 EMAIL :邮件 MESSAGE :短信 |
| 11 | fscheme_code | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fscheme_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 13 | fdatalabelid | 数据安全标签 | int8 | 64 |  |  | null | [数据安全标签 privacy_data_tags](../privacy_files/privacy_data_tags.md) |
| 14 | ftemplate | 消息模板 | varchar | 500 |  |  | ' ' | 消息模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_config |  | fid |
| 2 | idx_t_privacy_scheme_config_fname |  | fscheme_name |
| 3 | idx_t_privacy_scheme_config_fnumber |  | fscheme_code |

---

## 隐私方案配置-多语言表 t_privacy_scheme_config_l

- **表名称：** 隐私方案配置-多语言表
- **表名：** t_privacy_scheme_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fscheme_name | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fscheme_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ivacy_scheme_config_l |  | fpkid |

---

## 脱敏权限设置-多语言表 t_privacy_desen_authority_l

- **表名称：** 脱敏权限设置-多语言表
- **表名：** t_privacy_desen_authority_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentityname | fentityname | varchar | 200 |  | √ | ' ' |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_desen_authority_l |  | fpkid |
| 2 | idx_privacy_desenauth_l_fid |  | fentryid,flocaleid |

---

## 加密规则-多语言表 t_privacy_scheme_encrypt_l

- **表名称：** 加密规则-多语言表
- **表名：** t_privacy_scheme_encrypt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fencrypt_cloud_name | fencrypt_cloud_name | varchar | 100 |  | √ | ' ' |  |
| 2 | fencrypt_app_name | fencrypt_app_name | varchar | 100 |  | √ | ' ' |  |
| 3 | fencrypt_entity_name | fencrypt_entity_name | varchar | 200 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fencrypt_field_desc | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_encrypt_l |  | fpkid |
| 2 | idx_privacy_seme_enc_l_fid |  | fentryid,flocaleid |

---

## 消息接收人-多选基础资料表 t_privacy_decrypt_receive

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_privacy_decrypt_receive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_decrypt_receive |  | fpkid |

---

## 角色-多选基础资料表 t_privacy_scheme_permrole

- **表名称：** 角色-多选基础资料表
- **表名：** t_privacy_scheme_permrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [通用角色 perm_role](../base_files/perm_role.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_permrole |  | fentryid |

---

## 字段解密控制-子表 t_privacy_decrypt_control

- **表名称：** 字段解密控制-子表
- **表名：** t_privacy_decrypt_control

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | frule | 处理规则 | varchar | 50 |  |  | ' ' | 处理规则,枚举: NOTALLOW :不允许超过上限 EARLYWARN :超过最大次数预警 |
| 3 | fentityname | 所属实体 | varchar | 50 |  |  | null | 所属实体 |
| 4 | ffieldname | 字段名称 | varchar | 50 |  |  | null | 字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentitynumber | 所属实体标识 | varchar | 50 |  | √ | ' ' | 所属实体标识 |
| 7 | ffieldident | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 8 | flabelid | 标签id | int8 | 64 |  | √ | null | 标签id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 10 | fdailylimit | 每日解密上限 | int4 | 32 |  | √ | 0 | 每日解密上限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_decrypt_control |  | fentryid |

---

## 脱敏规则-多语言表 t_privacy_scheme_desen_l

- **表名称：** 脱敏规则-多语言表
- **表名：** t_privacy_scheme_desen_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdense_cloud_name | fdense_cloud_name | varchar | 100 |  | √ | ' ' |  |
| 2 | fdense_entity_name | fdense_entity_name | varchar | 200 |  | √ | ' ' |  |
| 3 | fdense_app_name | fdense_app_name | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fdense_field_desc | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_desen_l |  | fpkid |
| 2 | idx_privacy_seme_des_l_fid |  | fentryid,flocaleid |

---

## 脱敏权限设置-子表 t_privacy_desen_authority

- **表名称：** 脱敏权限设置-子表
- **表名：** t_privacy_desen_authority

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fentityname | fentityname | varchar | 50 |  |  | null |  |
| 3 | fprintpolicy | 打印控制策略 | varchar | 50 |  |  | ' ' | 打印控制策略,枚举: DESENSITIZE :脱敏显示 PLAINTEXT :明文显示 |
| 4 | fformpolicy | 表单控制策略 | varchar | 50 |  |  | ' ' | 表单控制策略,枚举: CLICKVIEW :点击查看明文 DESENSITIZE :脱敏显示 PLAINTEXT :明文显示 |
| 5 | ffieldname | 字段名称 | varchar | 50 |  |  | null | 字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentitynumber | 所属实体编码 | varchar | 50 |  | √ | ' ' | 所属实体编码 |
| 8 | ffieldident | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 9 | flabelid | 标签id | int8 | 64 |  | √ | null | 标签id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | fexportpolicy | 导出控制策略 | varchar | 50 |  |  | ' ' | 导出控制策略,枚举: DESENSITIZE :脱敏显示 PLAINTEXT :明文显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_desen_authority |  | fentryid |

---

## 脱敏规则-子表 t_privacy_scheme_desen

- **表名称：** 脱敏规则-子表
- **表名：** t_privacy_scheme_desen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fdense_field_name | 物理字段名 | varchar | 50 |  |  | null | 物理字段名 |
| 3 | fdensefieldlocale | 所属语言 | varchar | 50 |  |  | ' ' | 所属语言,枚举: zh_CN :中文 |
| 4 | fdense_entity_number | 所属实体编码 | varchar | 50 |  | √ | ' ' | 所属实体编码 |
| 5 | fdense_app_number | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 6 | fdense_app_name | fdense_app_name | varchar | 50 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdense_table_name | 物理表名 | varchar | 50 |  | √ | ' ' | 物理表名 |
| 9 | fdense_field_ident | 字段标识 | varchar | 50 |  |  | null | 字段标识 |
| 10 | fdesensitize_rule | 脱敏规则 | varchar | 50 |  | √ | ' ' | [脱敏规则 privacy_desen_rules](../privacy_files/privacy_desen_rules.md) |
| 11 | fdense_field_desc | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 12 | fdense_field_locale | fdense_field_locale | varchar | 50 |  | √ | ' ' |  |
| 13 | fdesensitize_type | 脱敏类型 | varchar | 50 |  | √ | ' ' | 脱敏类型,枚举: SYSTEM :系统预置 CUSTOM :自定义 |
| 14 | fdense_cloud_name | fdense_cloud_name | varchar | 50 |  | √ | ' ' |  |
| 15 | fdense_entity_name | fdense_entity_name | varchar | 50 |  | √ | ' ' |  |
| 16 | fdesensitiz_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :已生效 0 :生效中 |
| 17 | fdense_cloud_number | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 18 | fplugin | 插件地址 | varchar | 50 |  | √ | ' ' | 插件地址 |
| 19 | flabelid | 标签id | int8 | 64 |  | √ | null | 标签id |
| 20 | fdense_field_type | 字段类型 | varchar | 50 |  |  | null | 字段类型,枚举: 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_desen |  | fentryid |

---

## 加密规则-子表 t_privacy_scheme_encrypt

- **表名称：** 加密规则-子表
- **表名：** t_privacy_scheme_encrypt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fencrypt_field_name | 物理字段名 | varchar | 50 |  |  | null | 物理字段名 |
| 3 | fapp_route | 所属库 | varchar | 50 |  | √ | ' ' | 所属库 |
| 4 | fencrypt_app_name | fencrypt_app_name | varchar | 50 |  | √ | ' ' |  |
| 5 | fencrypt_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :已生效 0 :生效中 |
| 6 | fencrypt_app_number | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 7 | fencrypt_algorithm | 加密方案 | varchar | 50 |  | √ | ' ' | 加密方案,枚举: NO :不加密 AES :AES加密 SM4 :SM4加密 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fencrypt_field_type | 字段类型 | varchar | 50 |  |  | null | 字段类型,枚举: 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 10 | fencrypt_cloud_name | fencrypt_cloud_name | varchar | 50 |  | √ | ' ' |  |
| 11 | fencrypt_entity_name | fencrypt_entity_name | varchar | 50 |  | √ | ' ' |  |
| 12 | fencrypt_cloud_number | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 13 | fencrypt_field_ident | 字段标识 | varchar | 50 |  |  | null | 字段标识 |
| 14 | flabelid | 标签id | int8 | 64 |  | √ | null | 标签id |
| 15 | fencrypt_schemeid | fencrypt_schemeid | int8 | 64 |  |  | null |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 17 | fencrypt_field_desc | 字段名称 | varchar | 60 |  |  | null | 字段名称 |
| 18 | fencrypt_entity_number | 所属实体编码 | varchar | 50 |  | √ | ' ' | 所属实体编码 |
| 19 | fversion | 版本 | int8 | 64 |  |  | null | 版本 |
| 20 | fencrypt_table_name | 物理表名 | varchar | 50 |  |  | null | 物理表名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_encrypt |  | fentryid |

---

## 用户-多选基础资料表 t_privacy_scheme_permuser

- **表名称：** 用户-多选基础资料表
- **表名：** t_privacy_scheme_permuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_scheme_permuser |  | fpkid |
