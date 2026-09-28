# 分片主要堆栈采集-bos_cbs_shard_metric_main

## 分片主要堆栈采集-主表 t_cbs_shard_metric_main

- **表名称：** 分片主要堆栈采集-主表
- **表名：** t_cbs_shard_metric_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillnumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 3 | fmetricflag | 采集标志 | varchar | 100 |  | √ | ' ' | 采集标志 |
| 4 | ftimes | 采集次数 | int8 | 64 |  | √ | 0 | 采集次数 |
| 5 | fmetricstype | 采集类型 | bpchar | 1 |  | √ | ' ' | 采集类型,枚举: 0 :告警 1 :统计 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsql | 采集SQL | text | 0 |  |  | null | 采集SQL |
| 8 | fstack | 采集堆栈 | text | 0 |  |  | null | 采集堆栈 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmainstack | 主要堆栈 | text | 0 |  |  | null | 主要堆栈 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_shard_metric_main |  | fbillnumber |
| 2 | pk_cbs_shard_metric_main |  | fid |
