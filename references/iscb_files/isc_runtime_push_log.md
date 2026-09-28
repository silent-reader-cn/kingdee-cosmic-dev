# 运行时数据推送日志-isc_runtime_push_log

## 运行时数据推送日志-主表 t_isc_runtime_push_log

- **表名称：** 运行时数据推送日志-主表
- **表名：** t_isc_runtime_push_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstate | 日志状态 | bpchar | 1 |  | √ | ' ' | 日志状态,枚举: 0 :失败 1 :成功 |
| 3 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fend_time | 推送数据范围终点 | timestamp | 0 |  |  | null | 推送数据范围终点 |
| 5 | fstart_time | 推送数据范围起点 | timestamp | 0 |  |  | null | 推送数据范围起点 |
| 6 | fend | 历史数据推送结束 | bpchar | 1 |  | √ | ' ' | 历史数据推送结束,枚举: 0 :否 1 :是 |
| 7 | fcount | 推送数量 | int4 | 32 |  | √ | 0 | 推送数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rp_log_time |  | fcreate_time |
| 2 | pk_t_isc_runtime_push_log |  | fid |
