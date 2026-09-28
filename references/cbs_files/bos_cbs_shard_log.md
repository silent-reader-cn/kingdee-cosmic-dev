# 分片操作日志-bos_cbs_shard_log

## 分片操作日志-主表 t_cbs_shard_log

- **表名称：** 分片操作日志-主表
- **表名：** t_cbs_shard_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprogresstype | 操作类型 | varchar | 200 |  | √ | ' ' | 操作类型 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fentitynumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 5 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 6 | foperationlog | 操作日志 | varchar | 2000 |  | √ | ' ' | 操作日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_log |  | fentitynumber |
| 2 | pk_cbs_shard_log |  | fid |
