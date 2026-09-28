# 数据表复制-dbc_table_copy

## 数据表复制-多语言表 t_dbc_table_copy_l

- **表名称：** 数据表复制-多语言表
- **表名：** t_dbc_table_copy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dbc_table_copy_l |  | fpkid |
| 2 | idx_dbc_table_copy_l_0 |  | fid,flocaleid |

---

## 数据表复制-主表 t_dbc_table_copy

- **表名称：** 数据表复制-主表
- **表名：** t_dbc_table_copy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrc_db_id | 来源数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fretry_count | 最大重试次数 | int4 | 32 |  | √ | 0 | 最大重试次数 |
| 7 | fbatch_size | 批处理大小 | int4 | 32 |  | √ | 0 | 批处理大小 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fauto_create_table | 自动创建数据表 | bpchar | 1 |  | √ | '0' | 自动创建数据表 |
| 11 | finterval | 执行频率 | varchar | 50 |  | √ | ' ' | 执行频率,枚举: 1 :执行频率 - 1次/小时 2 :执行频率 - 2次/小时 3 :执行频率 - 3次/小时 5 :执行频率 - 5次/小时 10 :执行频率 - 10次/小时 20 :执行频率 - 20次/小时 30 :执行频率 - 30次/小时 60 :执行频率 - 60次/小时 d :每天 w :每周 m :每月 d1 :每天凌晨一点 0 :自定义 |
| 12 | fexpired_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 13 | ftrigged_count | 触发次数 | int8 | 64 |  | √ | 0 | 触发次数 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fretry_interval | 重试间隔(分钟) | varchar | 50 |  | √ | ' ' | 重试间隔(分钟) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | ftar_db_id | 目标数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 19 | fschedule | 触发间隔 | varchar | 50 |  | √ | ' ' | 触发间隔 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 21 | fvalidated_time | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | ftrigger_type | 启动类型 | varchar | 50 |  | √ | ' ' | 启动类型,枚举: auto :定时启动 manual :人工启动 |
| 24 | ftrigged_time | 最近触发时间 | timestamp | 0 |  |  | null | 最近触发时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_table_copy_0 |  | fnumber |
| 2 | pk_t_dbc_table_copy |  | fid |
| 3 | idx_dbc_table_copy_1 |  | fcreatetime |

---

## 过滤条件-子表 t_dbc_table_copy_items

- **表名称：** 过滤条件-子表
- **表名：** t_dbc_table_copy_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flink | 逻辑连接符 | varchar | 10 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 3 | fschema_id | 数据表名 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffilter | where条件 | varchar | 2000 |  | √ | ' ' | where条件 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdefine_condition | 自定义条件 | varchar | 2000 |  | √ | ' ' | 自定义条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dbc_table_copy_items |  | fentryid |
| 2 | idx_dbc_table_copy_items_0 |  | fid |
