# 并行任务实例节点-task_partaskinstnode

## 并行任务实例节点-主表 t_tk_partaskinstnode

- **表名称：** 并行任务实例节点-主表
- **表名：** t_tk_partaskinstnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskstate | 任务状态 | varchar | 3 |  | √ | ' ' | 任务状态,枚举: |
| 3 | fworkflowid | 工作流任务id | int8 | 64 |  | √ | 0 | 工作流任务id |
| 4 | finstantid | 并行任务实例id | int8 | 64 |  | √ | 0 | 并行任务实例id |
| 5 | fparenttaskid | 上级节点任务id | int8 | 64 |  | √ | 0 | 上级节点任务id |
| 6 | fparenttype | 上级节点任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 7 | fstate | 节点任务状态 | int8 | 64 |  | √ | 0 | 节点任务状态 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ftype | 节点任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 10 | fdealdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 11 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 12 | fpersonid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 14 | fauditmsg | 审批意见 | varchar | 1024 |  | √ | ' ' | 审批意见 |
| 15 | fnodedefid | 节点定义id | varchar | 100 |  | √ | ' ' | 节点定义id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_partaskinstnode_pkey |  | fid |
| 2 | index_partaskinstnode_instid |  | finstantid,ftaskid |
