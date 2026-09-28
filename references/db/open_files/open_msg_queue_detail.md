# 消息队列详情-open_msg_queue_detail

## 消息队列详情-主表 t_openapi_queue

- **表名称：** 消息队列详情-主表
- **表名：** t_openapi_queue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | URL | varchar | 200 |  |  | ' ' | URL |
| 3 | fdeliveryhost | 投递机器 | varchar | 50 |  | √ | ' ' | 投递机器 |
| 4 | fscheduletime | 调度时间 | timestamp | 0 |  |  | null | 调度时间 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpriority | 优先级 | bpchar | 1 |  | √ | ' ' | 优先级,枚举: 1 :高 2 :普通 3 :低 |
| 7 | fctx | 用户上下文 | varchar | 400 |  |  | ' ' | 用户上下文 |
| 8 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 9 | fmodifytime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fstatus | 状态 | bpchar | 2 |  | √ | ' ' | 状态,枚举: C1 :排队中 R1 :执行中 F1 :完成 E1 :错误 T1 :丢弃 |
| 11 | fdeliverycount | 调度次数 | int8 | 64 |  | √ | 0 | 调度次数 |
| 12 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :其他 1 :事件消息 2 :定时消息 3 :目标消息 |
| 13 | ferrmsg | 错误原因 | varchar | 400 |  |  | ' ' | 错误原因 |
| 14 | fqueuetag | 队列标志 | varchar | 20 |  | √ | ' ' | 队列标志 |
| 15 | fqueue | 队列ID | varchar | 100 |  | √ | ' ' | 队列ID |
| 16 | freqid | 异步请求ID | int8 | 64 |  | √ | 0 | 异步请求ID |
| 17 | fdata | 消息数据 | text | 0 |  |  | '' | 消息数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_queue_fstatus |  | fstatus,fstarttime |
| 2 | idx_open_queue_schtime |  | fscheduletime,fstatus |
| 3 | idx_open_queue_reqid |  | freqid |
| 4 | pk_openapi_queue |  | fid |
