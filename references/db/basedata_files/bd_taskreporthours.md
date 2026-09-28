# 任务汇报工时-bd_taskreporthours

## 任务汇报工时-主表 t_bd_taskreporthours

- **表名称：** 任务汇报工时-主表
- **表名：** t_bd_taskreporthours

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanhours | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 3 | fprojecttaskid | 项目任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 4 | fcurreporthours | 本次汇报工时(小时) | numeric | 23 | 10 | √ | 0 | 本次汇报工时(小时) |
| 5 | freportdate | 汇报日期 | timestamp | 0 |  |  | null | 汇报日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_taskreporthours |  | fid |
| 2 | idx_bd_tskrpthours_task |  | fprojecttaskid |
