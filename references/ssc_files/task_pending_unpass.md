# 任务暂挂原因-task_pending_unpass

## 任务暂挂原因-主表 t_tk_pending_unpass

- **表名称：** 任务暂挂原因-主表
- **表名：** t_tk_pending_unpass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftask | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 3 | fpending | 暂挂原因 | int8 | 64 |  | √ | 0 | 暂挂原因 task_pendingreason |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_pending_unpass |  | fid |
| 2 | index_pending_unpass |  | ftask |
