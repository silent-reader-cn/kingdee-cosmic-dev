# 历史变量-wf_hivarinst

## 历史变量-主表 t_wf_hivarinst

- **表名称：** 历史变量-主表
- **表名：** t_wf_hivarinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 3 | ftext | 文本值 | text | 0 |  |  | null | 文本值 |
| 4 | fname | 变量名称 | varchar | 255 |  | √ | ' ' | 变量名称 |
| 5 | fvartype | 变量类型 | varchar | 100 |  | √ | ' ' | 变量类型 |
| 6 | fdouble | 双精度浮点值 | numeric | 19 | 6 | √ | 0.000000 | 双精度浮点值 |
| 7 | factinstid | 节点实例ID | int8 | 64 |  | √ | 0 | 节点实例ID |
| 8 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | flong | 长精度值 | int8 | 64 |  | √ | 0 | 长精度值 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 13 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 14 | ftext2 | 文本值2 | text | 0 |  |  | null | 文本值2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hivarinst_pkey |  | fid |
| 2 | idx_wf_hi_procvar_name_type |  | fname,fvartype |
| 3 | idx_wf_hi_procvar_inst_name |  | fprocinstid,fname |
| 4 | idx_wf_hi_procvar_exec_name |  | fexecutionid,fname |
| 5 | idx_wf_hi_procvar_task_id |  | ftaskid |
