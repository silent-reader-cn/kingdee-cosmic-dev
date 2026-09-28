# 分片指标采集-bos_cbs_shard_metric

## 分片指标采集-主表 t_cbs_shard_metric

- **表名称：** 分片指标采集-主表
- **表名：** t_cbs_shard_metric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillnumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 3 | ftraceid | 跟踪ID | varchar | 50 |  | √ | ' ' | 跟踪ID |
| 4 | fmetricstype | 采集类型 | bpchar | 1 |  | √ | ' ' | 采集类型,枚举: 0 :告警 1 :统计 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstack | 采集堆栈 | text | 0 |  |  | null | 采集堆栈 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_metric_num |  | fbillnumber |
| 2 | pk_cbs_shard_metric |  | fid |
| 3 | idx_cbs_shard_metric_tracd |  | ftraceid |
