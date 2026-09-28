# 快速索引配置-bos_cbs_shard_fast_index

## 快速索引配置-主表 t_cbs_shard_fast_index

- **表名称：** 快速索引配置-主表
- **表名：** t_cbs_shard_fast_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 配置状态 | bpchar | 1 |  | √ | ' ' | 配置状态,枚举: 0 :可配置 1 :启用中 |
| 3 | flastfastindex | 上次快速索引 | varchar | 1000 |  | √ | ' ' | 上次快速索引 |
| 4 | fconfigid | 分片配置 | int8 | 64 |  | √ | 0 | 分片配置 bos_cbs_shard_config |
| 5 | ffastindex | 快速索引 | varchar | 1000 |  | √ | ' ' | 快速索引 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fentitynumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 8 | frwmark | 读写标志值 | varchar | 512 |  | √ | ' ' | 读写标志值 |
| 9 | foperationlog | 操作日志 | varchar | 2000 |  | √ | ' ' | 操作日志 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_fast_index |  | fid |
| 2 | idx_cbs_shard_fast_index_num |  | fentitynumber |
