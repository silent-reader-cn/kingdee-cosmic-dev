# 任务退回重扫原因-task_rescan_unpass

## 任务退回重扫原因-主表 t_tk_rescan_unpass

- **表名称：** 任务退回重扫原因-主表
- **表名：** t_tk_rescan_unpass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftask | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 3 | frescan | 退回重扫原因 | int8 | 64 |  | √ | 0 | 退扫原因 task_rescanreason |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_rescan_unpass |  | fid |
| 2 | index_rescan_unpass |  | ftask |
