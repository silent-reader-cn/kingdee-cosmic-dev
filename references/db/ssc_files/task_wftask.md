# 任务工作流关系表-task_wftask

## 任务工作流关系表-主表 t_tk_wftask

- **表名称：** 任务工作流关系表-主表
- **表名：** t_tk_wftask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskhistoryid | 共享历史任务ID | int8 | 64 |  | √ | 0 | 共享历史任务ID |
| 3 | fassignid | 工作流任务ID | int8 | 64 |  | √ | 0 | 工作流任务ID |
| 4 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 5 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 6 | fcompletetime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 7 | ftaskdefkey | 流程节点ID | varchar | 100 |  | √ | ' ' | 流程节点ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_wftask |  | fid |
| 2 | idx_ssc_wftask_date |  | fcompletetime |
