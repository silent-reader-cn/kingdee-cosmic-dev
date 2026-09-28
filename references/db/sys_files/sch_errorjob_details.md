# 异常日志详情-sch_errorjob_details

## 异常日志详情-主表 t_sch_errorjob

- **表名称：** 异常日志详情-主表
- **表名：** t_sch_errorjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frunat | frunat | varchar | 50 |  | √ | ' ' |  |
| 2 | fjobid | fjobid | varchar | 36 |  | √ | ' ' |  |
| 3 | fexecutetime | fexecutetime | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 4 | ferrorreason | ferrorreason | text | 0 |  |  | null |  |
| 5 | ftaskid | ftaskid | varchar | 36 |  | √ | ' ' | id |

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
