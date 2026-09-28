# 执行日志-isc_data_copy_exec_log

## 执行日志-主表 t_isc_data_copy_exec_log

- **表名称：** 执行日志-主表
- **表名：** t_isc_data_copy_exec_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 日志内容 | varchar | 2000 |  | √ | ' ' | 日志内容 |
| 3 | fdata_copy_execution | 执行结果对象 | int8 | 64 |  | √ | 0 | [执行结果 isc_data_copy_execution](../iscb_files/isc_data_copy_execution.md) |
| 4 | fdata_copy_schema | 数据集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 5 | fsource_data_tag | 源数据文本_详情 | text | 0 |  |  | ' ' | 源数据文本_详情 |
| 6 | fserver_id | 执行服务器 | varchar | 100 |  | √ | ' ' | 执行服务器 |
| 7 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodify_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftarget_data | 目标数据文本 | varchar | 300 |  | √ | ' ' | 目标数据文本 |
| 10 | fstate | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: S :成功 F :失败 G :失效 N :忽略 I :手动失效 R :已重做 |
| 11 | fdigest | 摘要信息 | varchar | 255 |  |  | ' ' | 摘要信息 |
| 12 | fdata_copy_trigger | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 13 | fjudgefields | 源单候选键 | varchar | 255 |  | √ | ' ' | 源单候选键 |
| 14 | fstack_trace | fstack_trace | varchar | 2000 |  | √ | ' ' |  |
| 15 | ftarget_data_tag | 目标数据文本_详情 | text | 0 |  |  | ' ' | 目标数据文本_详情 |
| 16 | fdata | fdata | varchar | 2000 |  | √ | ' ' |  |
| 17 | fsource_data | 源数据文本 | varchar | 2000 |  | √ | ' ' | 源数据文本 |
| 18 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | ' ' | 日志内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_data_copy_exec_log_e |  | fdata_copy_execution |
| 2 | idx_data_copy_exec_log_c |  | fcreated_time |
| 3 | idx_data_copy_exec_log_s |  | fdata_copy_schema |
| 4 | t_isc_data_copy_exec_log_pkey |  | fid |
| 5 | idx_data_copy_exec_log_state |  | fstate |
| 6 | idx_data_copy_exec_log_jf |  | fjudgefields |
| 7 | idx_data_copy_exec_log_z |  | fdata_copy_trigger,fcreated_time |
