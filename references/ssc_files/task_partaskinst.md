# 并行任务实例表-task_partaskinst

## 并行任务实例表-主表 t_tk_partaskinst

- **表名称：** 并行任务实例表-主表
- **表名：** t_tk_partaskinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fflowcode | 流程编码 | int8 | 64 |  | √ | 0 | 多级任务流程 task_partaskflowdef |
| 4 | fptendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | fsubject | 主题 | varchar | 128 |  | √ | ' ' | 主题 |
| 6 | fptstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fptstatus | 实例运行状态 | int8 | 64 |  | √ | 0 | 实例运行状态 |
| 8 | fworkflowid | 工作流任务id | int8 | 64 |  | √ | 0 | 工作流任务id |
| 9 | fptretain | 保留字段 | varchar | 64 |  | √ | ' ' | 保留字段 |
| 10 | fbillid | 单据编号 | int8 | 64 |  | √ | 0 | 单据编号 |
| 11 | fbilltype | 业务单据类型 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_partaskinst_sscid |  | fsscid |
| 2 | t_tk_partaskinst_pkey |  | fid |
