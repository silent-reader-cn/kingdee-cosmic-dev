# 导入结果明细-bos_importtask

## 导入结果明细-主表 t_sch_task

- **表名称：** 导入结果明细-主表
- **表名：** t_sch_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fjobtype | fjobtype | varchar | 50 |  |  | null |  |
| 3 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 4 | ftraceid | ftraceid | varchar | 75 |  |  | null |  |
| 5 | fcosttime | fcosttime | int4 | 32 |  | √ | 0 |  |
| 6 | fscheduletime | fscheduletime | timestamp | 0 |  |  | null |  |
| 7 | fjobid | 任务 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 8 | fcanstop | fcanstop | bpchar | 1 |  | √ | '0' |  |
| 9 | fstatusdesc | fstatusdesc | varchar | 50 |  |  | null |  |
| 10 | fprogress | 进度 | int8 | 64 |  |  | null | 进度 |
| 11 | fappid | fappid | varchar | 50 |  |  | null |  |
| 12 | fstatus | 状态 | varchar | 10 |  |  | null | 状态,枚举: SCHEDULED :计划 RUNNING :运行中 COMPLETED :完成 FAILED :失败 ABORTED :终止 |
| 13 | fmessageid | fmessageid | varchar | 36 |  |  | null |  |
| 14 | frunat | 执行服务器名称 | varchar | 100 |  |  | null | 执行服务器名称 |
| 15 | fscheduleid | fscheduleid | varchar | 36 |  |  | null |  |
| 16 | fdispatchtime | 分发时间 | timestamp | 0 |  |  | null | 分发时间 |
| 17 | finstanceid | finstanceid | varchar | 75 |  |  | null |  |
| 18 | fruntime | 开始运行时间 | timestamp | 0 |  |  | null | 开始运行时间 |
| 19 | fendtime | 结束运行时间 | timestamp | 0 |  |  | null | 结束运行时间 |
| 20 | fnumber | 单据编号 | varchar | 80 |  |  | null | 单据编号 |
| 21 | fdata | 日志数据 | text | 0 |  |  | null | 日志数据 |
| 22 | ftimeout | ftimeout | int4 | 32 |  | √ | 0 |  |

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
