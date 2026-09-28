# 任务监控-tctb_task_monitor

## 任务监控-主表 t_tctb_task_monitor

- **表名称：** 任务监控-主表
- **表名：** t_tctb_task_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutedetail | 执行详情 | varchar | 1000 |  | √ | ' ' | 执行详情 |
| 3 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 4 | fstarttime | 开始运行时间 | timestamp | 0 |  |  | null | 开始运行时间 |
| 5 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: SCHEDULED :计划 BEGIN :运行中 COMPLETED :完成 FAILED :失败 ABORTED :终止 SKIP :跳过 TIMEOUT :超时 |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fdispatchtime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | foperater | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fendtime | 结束运行时间 | timestamp | 0 |  |  | null | 结束运行时间 |
| 11 | ftaskdefine | 任务 | varchar | 36 |  | √ | ' ' | 调度执行程序 sch_taskdefine |
| 12 | ftaskid | 任务id | varchar | 50 |  | √ | ' ' | 任务id |
| 13 | fexecutetype | 执行类型 | varchar | 50 |  | √ | ' ' | 执行类型,枚举: 1 :自动执行 2 :手工执行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_task_taskid |  | ftaskid |
| 2 | pk_tctb_task_monitor |  | fid |
