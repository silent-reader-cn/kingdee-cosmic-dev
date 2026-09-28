# 运行日志-sch_task

## 运行日志-主表 t_sch_task

- **表名称：** 运行日志-主表
- **表名：** t_sch_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fjobtype | 任务类型 | varchar | 50 |  |  | null | 任务类型,枚举: BIZ :业务 WORKFLOW :工作流 REALTIME :实时 DETECT :探测 |
| 3 | fgroupid | 分片id | int8 | 64 |  | √ | 0 | 分片id |
| 4 | ftraceid | traceId | varchar | 75 |  |  | null | traceId |
| 5 | fcosttime | 耗时（s） | int4 | 32 |  | √ | 0 | 耗时（s） |
| 6 | fscheduletime | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |
| 7 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 8 | fcanstop | fcanstop | bpchar | 1 |  | √ | '0' |  |
| 9 | fstatusdesc | 状态说明 | varchar | 50 |  |  | null | 状态说明,枚举: SKIP_BY_USER :用户跳过 SKIP_BY_SCH_DEL :计划被删除 SKIP_BY_SCH_DISABLE :计划被禁用 SKIP_BY_JOB_DEL :作业被删除 SKIP_BY_JOB_DISABLE :作业被禁用 SKIP_RUNORDER_SERIAL :作业执行顺序为串行，已存在任务正在运行中 ABORTED_BY_USER :用户手工终止 ABORTED_BY_REBOOT :服务节点重启 SCH_APP_NOTDEPLOY :应用未部署，任务无法执行 SCH_IN_LINE :排队等待执行 |
| 10 | fprogress | 进度 | int8 | 64 |  |  | null | 进度 |
| 11 | fappid | 所属应用id | varchar | 50 |  |  | null | 所属应用id |
| 12 | fstatus | 状态 | varchar | 10 |  |  | null | 状态,枚举: SCHEDULED :计划 READY :就绪 BEGIN :运行中 COMPLETED :完成 FAILED :失败 ABORTED :终止 SKIP :跳过 TIMEOUT :超时 |
| 13 | fmessageid | 消息id | varchar | 36 |  |  | null | 消息id |
| 14 | frunat | 执行服务器名称 | varchar | 100 |  |  | null | 执行服务器名称 |
| 15 | fscheduleid | 调度计划 | varchar | 36 |  |  | null | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 16 | fdispatchtime | 分发时间 | timestamp | 0 |  |  | null | 分发时间 |
| 17 | finstanceid | 执行服务器实例 | varchar | 75 |  |  | null | 执行服务器实例 |
| 18 | fruntime | 开始运行时间 | timestamp | 0 |  |  | null | 开始运行时间 |
| 19 | fendtime | 结束运行时间 | timestamp | 0 |  |  | null | 结束运行时间 |
| 20 | fnumber | 编号 | varchar | 80 |  |  | null | 编号 |
| 21 | fdata | 任务反馈数据 | text | 0 |  |  | null | 任务反馈数据 |
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
