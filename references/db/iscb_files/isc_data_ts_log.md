# 单据时间戳日志-isc_data_ts_log

## 单据时间戳日志-主表 t_iscb_data_ts_log

- **表名称：** 单据时间戳日志-主表
- **表名：** t_iscb_data_ts_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 集成时间 | timestamp | 0 |  |  | null | 集成时间 |
| 3 | fjudgefields | 候选键值 | varchar | 100 |  | √ | ' ' | 候选键值 |
| 4 | foid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 5 | fsystem_id | 连接配置 | int8 | 64 |  | √ | 0 | [连接器配置 isc_database_link](../iscb_files/isc_database_link.md) |
| 6 | frepository | 数据表 | varchar | 100 |  | √ | ' ' | 数据表 |
| 7 | ftask_id | 集成任务 | int8 | 64 |  | √ | 0 | [执行结果 isc_data_copy_execution](../iscb_files/isc_data_copy_execution.md) |
| 8 | ftimestamp | 修改标识 | varchar | 50 |  | √ | ' ' | 修改标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_ts_log_oid |  | foid |
| 2 | t_iscb_data_ts_log_pkey |  | fid |
| 3 | idx_iscb_ts_log_time |  | ftime |
