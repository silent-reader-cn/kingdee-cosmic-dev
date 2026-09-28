# 单据集成日志-isc_bill_log_relation

## 单据集成日志-主表 t_iscb_bill_log_relation

- **表名称：** 单据集成日志-主表
- **表名：** t_iscb_bill_log_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 集成时间 | timestamp | 0 |  |  | null | 集成时间 |
| 3 | fsystem | 业务系统 | int8 | 64 |  | √ | 0 | [连接器配置 isc_database_link](../iscb_files/isc_database_link.md) |
| 4 | frole | 集成方向 | varchar | 30 |  | √ | ' ' | 集成方向,枚举: 1 :源单 2 :目标单 |
| 5 | fvoid | fvoid | varchar | 80 |  | √ | ' ' |  |
| 6 | flog_id | 详细日志 | varchar | 100 |  | √ | ' ' | 详细日志 |
| 7 | fstatus | 集成状态 | varchar | 30 |  | √ | ' ' | 集成状态,枚举: 9 :成功 0 :失败 5 :忽略 |
| 8 | ftable_name | 数据表 | varchar | 140 |  | √ | ' ' | 数据表 |
| 9 | foid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 10 | ftask_id | ftask_id | varchar | 100 |  | √ | ' ' |  |
| 11 | ftask | 集成任务 | int8 | 64 |  | √ | 0 | [执行结果 isc_data_copy_execution](../iscb_files/isc_data_copy_execution.md) |
| 12 | ftrigger | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 13 | fnumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 14 | fschema | 集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 15 | fvid | 单据虚拟ID | varchar | 80 |  | √ | ' ' | 单据虚拟ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_bill_log_system |  | foid,fsystem |
| 2 | t_iscb_bill_log_relation_pkey |  | fid |
| 3 | idx_iscb_bill_log_task |  | ftask,frole |
| 4 | idx_iscb_bill_log_time |  | ftime |
