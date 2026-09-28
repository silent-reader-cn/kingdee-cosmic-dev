# 数据库比较-dbc_database_comp

## 数据表明细-子表 t_dbc_database_comp_items

- **表名称：** 数据表明细-子表
- **表名：** t_dbc_database_comp_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fbytes_count | 比较字节数 | int8 | 64 |  | √ | 0 | 比较字节数 |
| 4 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | felapsed_time | 耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 耗时（秒） |
| 9 | fcomp_count | 比较行数 | int8 | 64 |  | √ | 0 | 比较行数 |
| 10 | frow_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 11 | ftable_name | 数据表 | varchar | 255 |  | √ | ' ' | 数据表 |
| 12 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: EQUIV :数据一致 DIFF :数据不一致 FAILED :失败 OMITTED :忽略 READY :就绪 ABORTED :撤销 RUNNING :执行中 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dbc_database_comp_items |  | fentryid |
| 2 | idx_dbc_database_comp_items_0 |  | fid |

---

## 数据库比较-主表 t_dbc_database_comp

- **表名称：** 数据库比较-主表
- **表名：** t_dbc_database_comp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fsrc_db_id | 来源数据库 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 4 | fbytes_count | 总字节数（MB） | int8 | 64 |  | √ | 0 | 总字节数（MB） |
| 5 | fcreator_id | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdiff_count | 数据不一致表个数 | int4 | 32 |  | √ | 0 | 数据不一致表个数 |
| 7 | fomitted_count | 忽略数据表个数 | int4 | 32 |  | √ | 0 | 忽略数据表个数 |
| 8 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 9 | fbatch_size | 批处理大小 | int4 | 32 |  | √ | 0 | 批处理大小 |
| 10 | fmax_threads | 最大并发数 | int4 | 32 |  | √ | 0 | 最大并发数 |
| 11 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 12 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 13 | felapsed_time | 最近一次执行耗时（秒） | numeric | 10 | 1 | √ | 0.0 | 最近一次执行耗时（秒） |
| 14 | finclusive_tab_patterns | 包含表模式 | varchar | 1000 |  | √ | ' ' | 包含表模式 |
| 15 | flog_tab_patterns | 日志表模式 | varchar | 1000 |  | √ | ' ' | 日志表模式 |
| 16 | fdescription | 任务描述 | varchar | 150 |  | √ | ' ' | 任务描述 |
| 17 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: EQUIV :数据一致 DIFF :数据不一致 FAILED :失败 ABORTED :撤销 READY :就绪 RUNNING :执行中 |
| 19 | fequiv_count | 数据一致表个数 | int4 | 32 |  | √ | 0 | 数据一致表个数 |
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
| 1 | idx_dbc_database_comp_0 |  | fnumber |
| 2 | idx_dbc_database_comp_1 |  | fcreated_time |
| 3 | pk_t_dbc_database_comp |  | fid |
