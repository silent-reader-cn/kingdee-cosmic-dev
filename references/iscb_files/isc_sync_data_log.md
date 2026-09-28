# 操作数据日志-isc_sync_data_log

## 操作数据日志-主表 t_isc_sync_data_log

- **表名称：** 操作数据日志-主表
- **表名：** t_isc_sync_data_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodify_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 3 | fstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 0 :未执行 1 :执行中 2 :执行成功 3 :执行失败 |
| 4 | fmessage | 日志内容 | varchar | 510 |  | √ | ' ' | 日志内容 |
| 5 | fbase_schema | 基础资料模型 | int8 | 64 |  | √ | 0 | 参照数据方案 isc_base_schema |
| 6 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftotal_count | 总数 | varchar | 100 |  | √ | ' ' | 总数 |
| 8 | fexec_count | 已执行数 | varchar | 100 |  | √ | ' ' | 已执行数 |
| 9 | fmapping_rule | 值映射方案 | int8 | 64 |  | √ | 0 | 值转换规则 isc_value_conver_rule |
| 10 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_sync_dlog_fsta |  | fstatus |
| 2 | t_isc_sync_data_log_pkey |  | fid |
| 3 | idx_isc_sync_dlog_rule |  | fmapping_rule |
| 4 | idx_isc_sync_dlog_base |  | fbase_schema |
