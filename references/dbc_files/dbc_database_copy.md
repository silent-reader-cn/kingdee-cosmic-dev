# 数据库复制-dbc_database_copy

## 数据库复制-主表 t_dbc_database_copy

- **表名称：** 数据库复制-主表
- **表名：** t_dbc_database_copy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fsrc_db_id | 来源数据库 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 4 | fbytes_count | 总字节数（MB） | int8 | 64 |  | √ | 0 | 总字节数（MB） |
| 5 | fcreator_id | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fomitted_count | 忽略数据表个数 | int4 | 32 |  | √ | 0 | 忽略数据表个数 |
| 7 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 8 | fbatch_size | 批处理大小 | int4 | 32 |  | √ | 0 | 批处理大小 |
| 9 | fmax_threads | 最大并发数 | int4 | 32 |  | √ | 0 | 最大并发数 |
| 10 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | felapsed_time | 最近一次执行耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 最近一次执行耗时（秒） |
| 13 | finclusive_tab_patterns | 包含表模式 | varchar | 1000 |  | √ | ' ' | 包含表模式 |
| 14 | flog_tab_patterns | 日志表模式 | varchar | 1000 |  | √ | ' ' | 日志表模式 |
| 15 | fdescription | 任务描述 | varchar | 150 |  | √ | ' ' | 任务描述 |
| 16 | fauto_create_table | 自动创建数据表 | bpchar | 1 |  | √ | '0' | 自动创建数据表 |
| 17 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: READY :就绪 SUCCESS :完成 FAILED :失败 ABORTED :撤销 RUNNING :执行中 |
| 19 | fsuccess_count | 完成数据表个数 | int4 | 32 |  | √ | 0 | 完成数据表个数 |
| 20 | ftar_db_id | 目标数据库 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 21 | ffailed_count | 失败数据表个数 | int4 | 32 |  | √ | 0 | 失败数据表个数 |
| 22 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 23 | fexclusive_tab_patterns | 忽略表模式 | varchar | 1000 |  | √ | ' ' | 忽略表模式 |
| 24 | ftable_count | 数据表总数 | int4 | 32 |  | √ | 0 | 数据表总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_database_copy_0 |  | fnumber |
| 2 | idx_dbc_database_copy_1 |  | fcreated_time |
| 3 | pk_t_dbc_database_copy |  | fid |

---

## 数据表明细-子表 t_dbc_database_copy_items

- **表名称：** 数据表明细-子表
- **表名：** t_dbc_database_copy_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomplete_count | 完成行数 | int8 | 64 |  | √ | 0 | 完成行数 |
| 3 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 4 | fbytes_count | 字节数 | int8 | 64 |  | √ | 0 | 字节数 |
| 5 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | felapsed_time | 耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 耗时（秒） |
| 10 | frow_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 11 | ftable_name | 数据表 | varchar | 255 |  | √ | ' ' | 数据表 |
| 12 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: SUCCESS :成功 FAILED :失败 OMITTED :忽略 READY :就绪 ABORTED :撤销 RUNNING :执行中 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_database_copy_items_0 |  | fid |
| 2 | pk_t_dbc_database_copy_items |  | fentryid |
