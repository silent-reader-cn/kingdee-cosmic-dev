# 数据安全标签-privacy_data_tags

## 数据安全标签-主表 t_privacy_data_tag

- **表名称：** 数据安全标签-主表
- **表名：** t_privacy_data_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftemplateid | 隐私模板 | int8 | 64 |  | √ | 0 | 数据安全标签模板 privacy_data_tags_temp |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fcreater | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 8 | fmodifier | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_privacy_data_tag_fname |  | fname |
| 2 | idx_t_privacy_data_tag_fnumber |  | fnumber |
| 3 | pk_privacy_data_tag |  | fid |

---

## 数据安全标签-多语言表 t_privacy_data_tag_l

- **表名称：** 数据安全标签-多语言表
- **表名：** t_privacy_data_tag_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_data_tag_l |  | fpkid |

---

## 单据体-子表 t_privacy_data_tag_fields

- **表名称：** 单据体-子表
- **表名：** t_privacy_data_tag_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fapp_route | 所属库 | varchar | 50 |  | √ | ' ' | 所属库 |
| 3 | fentity_number | 所属实体编码 | varchar | 100 |  |  | null | 所属实体编码 |
| 4 | ffield_ident | 字段标识 | varchar | 100 |  |  | null | 字段标识 |
| 5 | ffield_type | 字段类型 | varchar | 10 |  |  | null | 字段类型,枚举: 12 :字符串 1111 :基础资料 91 :日期 4 :整型 3 :小数 -5 :长整型 1112 :多语言 |
| 6 | ffield_desc | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 7 | ffield_name | 物理字段名 | varchar | 50 |  | √ | ' ' | 物理字段名 |
| 8 | fcloud_name | 所属云 | varchar | 50 |  | √ | ' ' | 所属云 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentity_name | 所属实体 | varchar | 50 |  | √ | ' ' | 所属实体 |
| 11 | fapp_name | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 12 | ftable_name | 物理表名 | varchar | 50 |  | √ | ' ' | 物理表名 |
| 13 | fcloud_number | 所属云编码 | varchar | 100 |  |  | null | 所属云编码 |
| 14 | fdatatagid | fdatatagid | int8 | 64 |  |  | null |  |
| 15 | fapp_number | 所属应用编码 | varchar | 100 |  |  | null | 所属应用编码 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_privacy_data_tag_fields_pkey |  | fentryid |
