# 预留字段映射（废弃）-msmod_field_mapping

## 预留字段映射（废弃）-多语言表 t_msmod_field_mapping_l

- **表名称：** 预留字段映射（废弃）-多语言表
- **表名：** t_msmod_field_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_field_mapping_l |  | fpkid |
| 2 | idx_msmod_field_mapping_l_id |  | fid,flocaleid |

---

## 预留字段映射（废弃）-主表 t_msmod_field_mapping

- **表名称：** 预留字段映射（废弃）-主表
- **表名：** t_msmod_field_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 9 | f_target_obj | 目标业务对象实体 | varchar | 128 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | f_source_bill | 来源单据 | varchar | 128 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_field_mapping_num |  | fnumber |
| 2 | pk_t_msmod_field_mapping |  | fid |

---

## 字段映射表-子表 t_msmod_fields

- **表名称：** 字段映射表-子表
- **表名：** t_msmod_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | f_target_col | 标识 | varchar | 128 |  | √ | ' ' | 标识 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | f_source_col | 标识 | varchar | 128 |  | √ | ' ' | 标识 |
| 6 | f_target_col_name | 名称 | varchar | 128 |  | √ | ' ' | 名称 |
| 7 | f_source_col_name | 名称 | varchar | 128 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_fields_id |  | fid |
| 2 | pk_t_msmod_fields |  | fentryid |
