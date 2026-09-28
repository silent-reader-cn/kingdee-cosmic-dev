# 并行任务运行时节点-task_partaskcurnode

## 并行任务运行时节点-主表 t_tk_partaskcurnode

- **表名称：** 并行任务运行时节点-主表
- **表名：** t_tk_partaskcurnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurnodedefid | 当前节点定义id | varchar | 100 |  | √ | ' ' | 当前节点定义id |
| 3 | fstatus | 运行状态 | int8 | 64 |  | √ | 0 | 运行状态 |
| 4 | fcurtaskid | 当前节点任务id | int8 | 64 |  | √ | 0 | 当前节点任务id |
| 5 | fnextnodedefid | 下级节点定义id | varchar | 100 |  | √ | ' ' | 下级节点定义id |
| 6 | finstid | 并行任务实例id | int8 | 64 |  | √ | 0 | 并行任务实例id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_partaskcurnode_finstid |  | finstid |
| 2 | t_tk_partaskcurnode_pkey |  | fid |
