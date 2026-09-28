# 附件集成日志-isc_attachment_log

## 附件集成日志-主表 t_isc_attach_log

- **表名称：** 附件集成日志-主表
- **表名：** t_isc_attach_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fattachname | 附件名称 | varchar | 255 |  | √ | ' ' | 附件名称 |
| 3 | fattachid | 附件信息id | varchar | 50 |  | √ | ' ' | 附件信息id |
| 4 | fend_time | 同步结束时间 | timestamp | 0 |  |  | null | 同步结束时间 |
| 5 | fbytes | 附件大小(单位:字节) | varchar | 50 |  | √ | ' ' | 附件大小(单位:字节) |
| 6 | fstart_time | 同步开始时间 | timestamp | 0 |  |  | null | 同步开始时间 |
| 7 | felapsed_time | 耗时（s） | int8 | 64 |  | √ | 0 | 耗时（s） |
| 8 | fprogress | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 9 | ferror | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 10 | ferror_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 11 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: C :创建 R :同步中 S :成功 F :失败 I :忽略 K :中断 |
| 12 | fupdated_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 13 | ftask | 集成任务 | int8 | 64 |  | √ | 0 | 执行结果 isc_data_copy_execution |
| 14 | ftrigger | 启动方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 15 | fschema | 集成方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_attach_log |  | fattachid |
| 2 | idx_attach_log_state |  | fstate |
| 3 | idx_attach_log_time |  | fstart_time |
| 4 | t_isc_attach_log_pkey |  | fid |
