# 日志迁移任务-bos_log_etl_task

## 日志迁移任务-主表 t_log_etl_task

- **表名称：** 日志迁移任务-主表
- **表名：** t_log_etl_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmovecount | 计划归档记录数 | int8 | 64 |  | √ | 0 | 计划归档记录数 |
| 3 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: Finish :归档完成 Fialed :归档失败 STARTING :归档中 |
| 4 | ffinishcount | 完成归档记录数 | int8 | 64 |  | √ | 0 | 完成归档记录数 |
| 5 | fendtime | 归档完成时间 | timestamp | 0 |  |  | null | 归档完成时间 |
| 6 | ftaskid | 任务编号 | varchar | 30 |  | √ | ' ' | 任务编号 |
| 7 | fstarttime | 归档开始时间 | timestamp | 0 |  |  | null | 归档开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_etl_task_id |  | ftaskid |
| 2 | pk_log_etl_task |  | fid |
