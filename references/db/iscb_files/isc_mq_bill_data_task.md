# 单据消息任务-isc_mq_bill_data_task

## 单据消息任务-主表 t_iscb_biz_execution

- **表名称：** 单据消息任务-主表
- **表名：** t_iscb_biz_execution

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisposed_time | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 3 | fsubscriber | 订阅方案 | int8 | 64 |  | √ | 0 | [单据消息订阅 isc_mq_bill_data_sub](../iscb_files/isc_mq_bill_data_sub.md) |
| 4 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 5 | fresult | 结果 | varchar | 510 |  | √ | ' ' | 结果 |
| 6 | fdata_source | 目标系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 7 | fstack_trace_tag | 错误堆栈_详情 | text | 0 |  |  | null | 错误堆栈_详情 |
| 8 | factions | 操作 | varchar | 510 |  | √ | ' ' | 操作 |
| 9 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmeta_schema | fmeta_schema | int8 | 64 |  | √ | 0 |  |
| 11 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: S :成功 F :失败 C :新建 N :忽略 |
| 12 | fjudgefields | 单据候选键 | varchar | 200 |  | √ | ' ' | 单据候选键 |
| 13 | fstack_trace | 错误堆栈 | varchar | 510 |  | √ | ' ' | 错误堆栈 |
| 14 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 15 | fdata | 数据 | varchar | 510 |  | √ | ' ' | 数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_biz_execution_pkey |  | fid |
| 2 | idx_iscb_biz_execution |  | fnumber,fsubscriber,fdata_source |
| 3 | idx_iscb_biz_execution_s |  | fstate |
| 4 | idx_iscb_biz_execution_t |  | fcreated_time |
