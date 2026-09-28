# 数据流失败日志-iscx_data_stream_log

## 数据流失败日志-主表 t_iscx_data_stream_log

- **表名称：** 数据流失败日志-主表
- **表名：** t_iscx_data_stream_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 服务器 | varchar | 50 |  | √ | ' ' | 服务器 |
| 3 | ftime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 4 | ftask_context | 任务上下文 | varchar | 255 |  | √ | ' ' | 任务上下文 |
| 5 | fdata_stream | 数据流实例 | int8 | 64 |  | √ | 0 | 数据流实例 iscx_data_stream |
| 6 | ftask_type | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: FiberTask :数据线 BatchTask :批处理 StreamTask :数据查询 |
| 7 | fdata_tag | 业务数据_详情 | text | 0 |  |  | null | 业务数据_详情 |
| 8 | ftask_context_tag | 任务上下文_详情 | text | 0 |  |  | null | 任务上下文_详情 |
| 9 | fnode_id | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |
| 10 | ferror |  | varchar | 255 |  | √ | ' ' |  |
| 11 | ferror_tag | 详情 | text | 0 |  |  | null | 详情 |
| 12 | fnode_title | 节点标题 | varchar | 50 |  | √ | ' ' | 节点标题 |
| 13 | fdata | 业务数据 | varchar | 255 |  | √ | ' ' | 业务数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_data_stream_log |  | fid |
| 2 | idx_t_iscx_data_stream_log_i |  | fdata_stream |
