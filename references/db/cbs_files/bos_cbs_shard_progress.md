# 分片迁移进度表-bos_cbs_shard_progress

## 分片迁移进度表-主表 t_cbs_shard_progress

- **表名称：** 分片迁移进度表-主表
- **表名：** t_cbs_shard_progress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fentitynumber | 实体标识 | varchar | 255 |  | √ | ' ' | 实体标识 |
| 4 | fshard_progress | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 5 | fshard_table | 分片表 | varchar | 50 |  | √ | ' ' | 分片表 |
| 6 | fshard_total_record | 预估数量 | int8 | 64 |  | √ | 0 | 预估数量 |
| 7 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fshard_moving_record | 已迁移数量 | int8 | 64 |  | √ | 0 | 已迁移数量 |
| 10 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 11 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :等待 1 :执行中 2 :成功 3 :失败 4 :已终止 5 :暂停中 6 :已暂停 |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 14 | fshard_index | 分片表后缀 | int8 | 64 |  | √ | 0 | 分片表后缀 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_taskid_stb |  | ftaskid,fshard_table |
| 2 | idx_cbs_shard_progress |  | fentitynumber |
| 3 | pk_cbs_shard_progress |  | fid |
