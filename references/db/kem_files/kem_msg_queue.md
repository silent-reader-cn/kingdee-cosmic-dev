# 事件消息监控-kem_msg_queue

## 事件消息监控-主表 t_kem_queue

- **表名称：** 事件消息监控-主表
- **表名：** t_kem_queue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 200 |  |  | ' ' | 备注 |
| 3 | fdeliveryhost | 投递机器 | varchar | 50 |  | √ | ' ' | 投递机器 |
| 4 | fscheduletime | 调度时间 | timestamp | 0 |  |  | null | 调度时间 |
| 5 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpriority | 优先级 | bpchar | 1 |  | √ | ' ' | 优先级,枚举: 1 :高 2 :普通 3 :低 |
| 8 | fsubid | 事件订阅 | int8 | 64 |  | √ | 0 | [订阅详情 kem_subscribe_inh](../kem_files/kem_subscribe_inh.md) |
| 9 | fctx | 用户上下文 | varchar | 400 |  |  | ' ' | 用户上下文 |
| 10 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 11 | fmodifytime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 12 | fstatus | 状态 | bpchar | 2 |  | √ | ' ' | 状态,枚举: C1 :排队中 R1 :执行中 F1 :完成 E1 :错误 T1 :丢弃 |
| 13 | fsubinstanceid | 订阅实例ID | int8 | 64 |  | √ | 0 | 订阅实例ID |
| 14 | fdeliverycount | 调度次数 | int8 | 64 |  | √ | 0 | 调度次数 |
| 15 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :其他 1 :事件消息 2 :定时消息 3 :目标消息 |
| 16 | ferrmsg | 错误原因 | varchar | 400 |  |  | ' ' | 错误原因 |
| 17 | fqueuetag | 队列标志 | varchar | 20 |  | √ | ' ' | 队列标志 |
| 18 | fqueue | 事件编码 | varchar | 100 |  | √ | ' ' | 事件编码 |
| 19 | frequestid | 事件跟踪ID | varchar | 50 |  | √ | ' ' | 事件跟踪ID |
| 20 | fdata | fdata | text | 0 |  |  | '' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_queue |  | fid |
| 2 | idx_kem_queue_schtime |  | fscheduletime,fstatus |
| 3 | idx_kem_queue_fstatus |  | fstatus,fstarttime |
| 4 | idx_kem_queue_subid |  | fsubid |
| 5 | idx_kem_queue_frequestid |  | frequestid |
