# 集成云HUB事件触发日志-isc_res_evt_log

## 集成云HUB事件触发日志-主表 t_isc_res_evt_log

- **表名称：** 集成云HUB事件触发日志-主表
- **表名：** t_isc_res_evt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_tag | 推送数据_详情 | text | 0 |  |  | null | 推送数据_详情 |
| 3 | froot_id | 根日志id | int8 | 64 |  | √ | 0 | 根日志id |
| 4 | fsrc_data_id | 事件源数据id | int8 | 64 |  | √ | 0 | 事件源数据id |
| 5 | fevt_schema_type | 事件源类型 | varchar | 100 |  | √ | ' ' | 事件源类型,枚举: isc_data_source :数据源 isc_data_copy_trigger :启动方案 isc_service_flow :服务流程 isc_user_defined_event :集成云自定义事件 |
| 6 | ferror | 错误日志 | varchar | 255 |  | √ | ' ' | 错误日志 |
| 7 | ferror_tag | 错误日志_详情 | text | 0 |  |  | null | 错误日志_详情 |
| 8 | fsrc_data_type | 事件源数据类型 | varchar | 100 |  | √ | ' ' | 事件源数据类型,枚举: isc_data_copy_execution :执行结果 isc_sf_proc_inst :流程实例 |
| 9 | fstate | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: C :创建 F :失败 S :成功 R :重推 |
| 10 | fmodified_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fhas_license | 许可 | bpchar | 1 |  | √ | '0' | 许可 |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fttl | ttl | int8 | 64 |  | √ | 0 | ttl |
| 14 | faction | 事件 | varchar | 100 |  | √ | ' ' | 事件,枚举: end :结束 fail :失败 cancel :撤销 OnTaskSuccess :任务执行成功 OnTaskFailed :任务执行失败 OnRowSuccess :单据执行成功 OnRowFailed :单据执行失败 valid :活跃 invalid :异常 |
| 15 | ftrigger | 触发方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 16 | fprior_id | 前一个日志id | int8 | 64 |  | √ | 0 | 前一个日志id |
| 17 | ftrigger_type | 触发方案类型 | varchar | 100 |  | √ | ' ' | 触发方案类型,枚举: isc_data_copy_trigger :启动方案 isc_mq_bill_data_pub :单据消息发布 isc_service_flow :服务流程 isc_call_api_by_evt :API任务（事件触发） |
| 18 | fdata | 推送数据 | varchar | 2000 |  | √ | ' ' | 推送数据 |
| 19 | fevt_schema | 事件源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_res_log_tm |  | fmodified_time |
| 2 | idx_res_log_src |  | fsrc_data_id,fsrc_data_type |
| 3 | idx_res_log_scm |  | fevt_schema,fevt_schema_type |
| 4 | pk_t_isc_res_evt_log |  | fid |
| 5 | idx_res_log_trg |  | ftrigger,ftrigger_type |
