# 任务轨迹记录-sch_tasktracerecord

## 任务轨迹记录-主表 t_sch_tasktrace

- **表名称：** 任务轨迹记录-主表
- **表名：** t_sch_tasktrace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskrecord | 轨迹记录 | text | 0 |  |  | null | 轨迹记录 |
| 3 | fstatus | 轨迹状态 | varchar | 4 |  | √ | ' ' | 轨迹状态,枚举: 100 :服务端获取执行时间点 200 :数据中心被移除，不发布新任务 300 :服务停止，不发布新任务 400 :服务端推送任务到本地队列 500 :服务端从本地队列取出任务 600 :开始将任务发送到MQ 700 :将任务发送到MQ成功 800 :发送MQ消息失败 900 :执行机从MQ获取任务成功 1000 :执行机已接收消息并将任务推送到就绪队列 1100 :执行机将任务从就绪队列取出 1101 :没有注册对应的handler,无法处理这个类型的消息 1200 :执行机开始执行任务 1300 :执行机将任务提交到线程池 1400 :执行机完成任务执行 1500 :执行机异常 1600 :任务终止 1700 :任务跳过 1800 :任务超时 |
| 4 | fgroupid | 任务分片id | int8 | 64 |  | √ | 0 | 任务分片id |
| 5 | fscheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 6 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 7 | ftaskid | 任务id | varchar | 36 |  | √ | ' ' | 任务id |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sch_tasktrace_jobid |  | fjobid |
| 2 | pk_t_sch_tasktrace |  | fid |
| 3 | idx_t_sch_tasktrace_schid |  | fscheduleid |
| 4 | idx_t_sch_tasktrace_taskid |  | ftaskid |
