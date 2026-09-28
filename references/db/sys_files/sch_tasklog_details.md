# 运行日志详情-sch_tasklog_details

## 运行日志详情-主表 t_sch_task

- **表名称：** 运行日志详情-主表
- **表名：** t_sch_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fjobtype | fjobtype | varchar | 50 |  |  | null |  |
| 3 | fgroupid | 分组id | int8 | 64 |  | √ | 0 | 分组id |
| 4 | ftraceid | ftraceid | varchar | 75 |  |  | null |  |
| 5 | fcosttime | 耗时 | int4 | 32 |  | √ | 0 | 耗时 |
| 6 | fscheduletime | fscheduletime | timestamp | 0 |  |  | null |  |
| 7 | fjobid | Job | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 8 | fcanstop | 允许终止 | bpchar | 1 |  | √ | '0' | 允许终止 |
| 9 | fstatusdesc | fstatusdesc | varchar | 50 |  |  | null |  |
| 10 | fprogress | fprogress | int8 | 64 |  |  | null |  |
| 11 | fappid | fappid | varchar | 50 |  |  | null |  |
| 12 | fstatus | 状态 | varchar | 10 |  |  | null | 状态,枚举: SCHEDULED :计划 BEGIN :运行中 COMPLETED :完成 FAILED :失败 ABORTED :终止 SKIP :跳过 TIMEOUT :超时 READY :就绪 |
| 13 | fmessageid | fmessageid | varchar | 36 |  |  | null |  |
| 14 | frunat | 执行服务器 | varchar | 100 |  |  | null | 执行服务器 |
| 15 | fscheduleid | 计划id | varchar | 36 |  |  | null | 计划id |
| 16 | fdispatchtime | 分发时间 | timestamp | 0 |  |  | null | 分发时间 |
| 17 | finstanceid | finstanceid | varchar | 75 |  |  | null |  |
| 18 | fruntime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 19 | fendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 20 | fnumber | 作业内码 | varchar | 80 |  |  | null | 作业内码 |
| 21 | fdata | fdata | text | 0 |  |  | null |  |
| 22 | ftimeout | 超时时间(s) | int4 | 32 |  | √ | 0 | 超时时间(s) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_task_dispatchtime |  | fdispatchtime |
| 2 | idx_sch_task_fschid |  | fscheduleid |
| 3 | idx_sch_task_endtime |  | fendtime |
| 4 | idx_sch_task_scheduletime |  | fscheduletime |
| 5 | t_sch_task_pkey |  | fid |
| 6 | idx_sch_task_fjobid |  | fjobid |
