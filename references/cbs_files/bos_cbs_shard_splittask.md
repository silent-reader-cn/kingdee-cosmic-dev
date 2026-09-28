# 分片切分任务-bos_cbs_shard_splittask

## 分片切分任务-主表 t_cbs_shard_splittask

- **表名称：** 分片切分任务-主表
- **表名：** t_cbs_shard_splittask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 分任务标记 | varchar | 50 |  | √ | ' ' | 分任务标记 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftailpk | 页尾 | varchar | 50 |  | √ | ' ' | 页尾 |
| 5 | fentitynumber | 实体标识 | varchar | 255 |  | √ | ' ' | 实体标识 |
| 6 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnum | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | fheadpk | 页头 | varchar | 50 |  | √ | ' ' | 页头 |
| 10 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 11 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: |
| 12 | ftotalcount | 总数 | int8 | 64 |  | √ | 0 | 总数 |
| 13 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_splittask_tid |  | ftaskid |
| 2 | pk_cbs_shard_splittask |  | fid |
| 3 | idx_cbs_shard_splittask |  | fentitynumber |
