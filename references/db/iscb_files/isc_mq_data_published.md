# 消息队列发送的数据-isc_mq_data_published

## 消息队列发送的数据-主表 t_iscb_mq_data_published

- **表名称：** 消息队列发送的数据-主表
- **表名：** t_iscb_mq_data_published

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_producer | 数据生产者 | varchar | 60 |  | √ | ' ' | 数据生产者 |
| 3 | fretry_count | 重发次数 | int8 | 64 |  | √ | 0 | 重发次数 |
| 4 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 5 | fstack_trace_tag | 错误堆栈_详情 | text | 0 |  |  | null | 错误堆栈_详情 |
| 6 | fmsg_digest | 消息摘要 | varchar | 300 |  |  | ' ' | 消息摘要 |
| 7 | fpublisher_server | 发布服务器 | varchar | 140 |  | √ | ' ' | 发布服务器 |
| 8 | fpublished_time | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 9 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: C :待发布 S :已发布 F :失败 |
| 10 | fmessage_queue | 消息发布主题 | int8 | 64 |  | √ | 0 | 消息发布主题 isc_mq_publisher |
| 11 | fstack_trace | 错误堆栈 | varchar | 510 |  | √ | ' ' | 错误堆栈 |
| 12 | fmessage_server | 消息队列服务器 | int8 | 64 |  | √ | 0 | 消息队列服务器 isc_mq_server |
| 13 | fdata | 数据 | varchar | 510 |  | √ | ' ' | 数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_data_published_pkey |  | fid |
| 2 | idx_iscb_mq_data_pub |  | fmessage_queue |
| 3 | idx_iscb_mq_data_pub_2 |  | fpublished_time |
| 4 | idx_mq_data_pub_digest |  | fmsg_digest |
