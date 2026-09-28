# 优先级改变日志-task_prioritychangerecord

## 优先级改变日志-主表 t_tk_prioritychangerecord

- **表名称：** 优先级改变日志-主表
- **表名：** t_tk_prioritychangerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 3 | fchangetime | 更改时间 | timestamp | 0 |  |  | null | 更改时间 |
| 4 | flimittime | 任务期限 | numeric | 23 | 10 | √ | 0.0000000000 | 任务期限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_prioritychangerecord_pkey |  | fid |
| 2 | index_ssc_prioritychangercord |  | fjobid |
