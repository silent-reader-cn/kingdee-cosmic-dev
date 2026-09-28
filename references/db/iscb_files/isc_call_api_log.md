# 集成API日志（废弃）-isc_call_api_log

## 集成API日志（废弃）-主表 t_isc_call_api_log

- **表名称：** 集成API日志（废弃）-主表
- **表名：** t_isc_call_api_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 执行对象名称 | varchar | 50 |  | √ | ' ' | 执行对象名称 |
| 3 | fmessage | 日志内容 | varchar | 1000 |  | √ | ' ' | 日志内容 |
| 4 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fapi_type | API类型 | varchar | 30 |  | √ | ' ' | API类型,枚举: isc_apic_by_meta_schema :集成对象转API isc_apic_by_dc_schema :数据集成方案转API isc_apic_by_dc_trigger :启动方案转API |
| 7 | fserver_id | 执行服务器 | varchar | 50 |  | √ | ' ' | 执行服务器 |
| 8 | fdata_trigger | 启动方案转API | int8 | 64 |  | √ | 0 | 启动方案转API isc_apic_by_dc_trigger |
| 9 | fmeta_schema | 集成对象转API | int8 | 64 |  | √ | 0 | 集成对象转API isc_apic_by_meta_schema |
| 10 | fstate | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: S :成功 F :失败 E :执行中 |
| 11 | fduration | 持续时间(ms) | int8 | 64 |  | √ | 0 | 持续时间(ms) |
| 12 | fdata_copy | 数据集成方案转API | int8 | 64 |  | √ | 0 | 数据集成方案转API isc_apic_by_dc_schema |
| 13 | fnumber | 执行对象编码 | varchar | 50 |  | √ | ' ' | 执行对象编码 |
| 14 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_call_api_log_pkey |  | fid |
| 2 | idx_isc_call_api_log_m |  | fmeta_schema |
| 3 | idx_isc_call_api_log_n |  | fnumber |
| 4 | idx_isc_call_api_log_state |  | fstate |
| 5 | idx_isc_call_api_log_c |  | fdata_copy |
| 6 | idx_isc_call_api_log_t |  | fend_time |
