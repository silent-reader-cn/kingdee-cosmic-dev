# 任务执行历史-aicc_task_history

## 任务执行历史-主表 t_aicc_task_history

- **表名称：** 任务执行历史-主表
- **表名：** t_aicc_task_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: create :新增 enq :进入队列 running :执行中 failed :执行失败 success :执行成功 |
| 3 | ferrmsg | 错误信息 | varchar | 1024 |  | √ | ' ' | 错误信息 |
| 4 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | 任务 |
| 5 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_task_history_ftaskid |  | ftaskid |
| 2 | pk_t_aicc_task_history |  | fid |
