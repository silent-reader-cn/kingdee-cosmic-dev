# 消息队列接收的数据-isc_mq_data_received

## 消息队列接收的数据-主表 t_iscb_mq_data_received

- **表名称：** 消息队列接收的数据-主表
- **表名：** t_iscb_mq_data_received

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisposed_time | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 3 | fretry_count | 重做次数 | int8 | 64 |  | √ | 0 | 重做次数 |
| 4 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 5 | fstack_trace_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 6 | fexecution | fexecution | int8 | 64 |  | √ | 0 |  |
| 7 | fmsg_digest | 消息摘要 | varchar | 300 |  |  | ' ' | 消息摘要 |
| 8 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: R :待处理 S :已处理 N :已忽略 F :失败 |
| 9 | fmessage_queue | 消息订阅主题 | int8 | 64 |  | √ | 0 | 消息订阅主题 isc_mq_subscriber |
| 10 | fstack_trace | 详细信息 | varchar | 510 |  | √ | ' ' | 详细信息 |
| 11 | freceiver_server | 接收者服务器 | varchar | 140 |  | √ | ' ' | 接收者服务器 |
| 12 | freceived_time | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 13 | fmessage_server | 消息队列服务器 | int8 | 64 |  | √ | 0 | 消息队列服务器 isc_mq_server |
| 14 | fdata | 数据 | varchar | 510 |  | √ | ' ' | 数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mq_data_rec_2 |  | freceived_time |
| 2 | idx_iscb_mq_data_rec_1 |  | fexecution,fmessage_queue |
| 3 | idx_mq_data_rec_digest |  | fmsg_digest |
| 4 | t_iscb_mq_data_received_pkey |  | fid |
