# 异常日志-sch_errorjob

## 异常日志-主表 t_sch_errorjob

- **表名称：** 异常日志-主表
- **表名：** t_sch_errorjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frunat | 执行服务器名称 | varchar | 50 |  | √ | ' ' | 执行服务器名称 |
| 2 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 3 | fexecutetime | 执行时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 执行时间 |
| 4 | ferrorreason | 错误原因 | text | 0 |  |  | null | 错误原因 |
| 5 | ftaskid | 任务id | varchar | 36 |  | √ | ' ' | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ftaskid | ftaskid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_errorjob_fjobid |  | fjobid |
| 2 | idx_sch_errorjob_fexecutetime |  | fexecutetime |
| 3 | t_sch_errorjob_pkey |  | ftaskid |
