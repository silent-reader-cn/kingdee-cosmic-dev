# 数据表复制日志-dbc_table_copy_log

## 单据体-子表 t_dbc_tc_log_items

- **表名称：** 单据体-子表
- **表名：** t_dbc_tc_log_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomplete_count | 完成行数 | int8 | 64 |  | √ | 0 | 完成行数 |
| 3 | fbytes_count | 字节数 | int8 | 64 |  | √ | 0 | 字节数 |
| 4 | ftable_remark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftable_start_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | felapsed_time | 耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 耗时（秒） |
| 8 | frow_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 9 | fdefine_condition | 自定义条件 | varchar | 2000 |  | √ | ' ' | 自定义条件 |
| 10 | ftable_end_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | flink | 逻辑连接符 | varchar | 10 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 12 | ftable_name | 数据表 | varchar | 150 |  | √ | ' ' | 数据表 |
| 13 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: SUCCESS :成功 FAILED :失败 OMITTED :忽略 READY :就绪 ABORTED :撤销 RUNNING :执行中 |
| 14 | fexe_count | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 15 | ffilter | where条件 | varchar | 2000 |  | √ | ' ' | where条件 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ftable_remark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dbc_tc_log_items |  | fentryid |
| 2 | idx_dbc_tc_log_items_0 |  | fid |

---

## 数据表复制日志-主表 t_dbc_table_copy_log

- **表名称：** 数据表复制日志-主表
- **表名：** t_dbc_table_copy_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 执行服务器 | varchar | 50 |  | √ | ' ' | 执行服务器 |
| 3 | ftotal_elapsed_time | 总耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 总耗时（秒） |
| 4 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 5 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fexe_count | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 9 | ftar_db_id | 目标数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 10 | ftotal_bytes_count | 总字节数 | int8 | 64 |  | √ | 0 | 总字节数 |
| 11 | ffailed_count | 失败数据表个数 | int4 | 32 |  | √ | 0 | 失败数据表个数 |
| 12 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 13 | fsrc_db_id | 来源数据库 | int8 | 64 |  | √ | 0 | [数据库 dbc_database](../dbc_files/dbc_database.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fomitted_count | 忽略数据表个数 | int4 | 32 |  | √ | 0 | 忽略数据表个数 |
| 17 | fretry_count | 最大重试次数 | int4 | 32 |  | √ | 0 | 最大重试次数 |
| 18 | fbatch_size | 批处理大小 | int4 | 32 |  | √ | 0 | 批处理大小 |
| 19 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 20 | fauto_create_table | 自动创建数据表 | bpchar | 1 |  | √ | '0' | 自动创建数据表 |
| 21 | fretry_interval | 重试间隔(分钟) | varchar | 50 |  | √ | ' ' | 重试间隔(分钟) |
| 22 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: READY :创建 RUNNING :执行中 SUCCESS :完成 FAILED :失败 ABORTED :已撤销 |
| 23 | fsuccess_count | 完成数据表个数 | int4 | 32 |  | √ | 0 | 完成数据表个数 |
| 24 | ftable_copy_id | 数据表复制 | int8 | 64 |  | √ | 0 | [数据表复制 dbc_table_copy](../dbc_files/dbc_table_copy.md) |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | ftable_count | 数据表总数 | int4 | 32 |  | √ | 0 | 数据表总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dbc_table_copy_log_0 |  | fnumber |
| 2 | pk_t_dbc_table_copy_log |  | fid |
| 3 | idx_dbc_table_copy_log_1 |  | fcreatetime |
| 4 | idx_dbc_table_copy_log_2 |  | ftable_copy_id |
