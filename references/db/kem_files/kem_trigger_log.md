# 其它事件日志-kem_trigger_log

## 其它事件日志-主表 t_kem_trigger_log

- **表名称：** 其它事件日志-主表
- **表名：** t_kem_trigger_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevent | 事件 | int8 | 64 |  | √ | 0 | [事件 kem_event](../kem_files/kem_event.md) |
| 3 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 4 | fcreatetime | 触发时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 触发时间 |
| 5 | fdata_tag | 推送数据_详情 | text | 0 |  |  | null | 推送数据_详情 |
| 6 | frepushcnt | 重推次数 | int4 | 32 |  | √ | 0 | 重推次数 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 8 | ferror | 错误日志 | varchar | 255 |  | √ | ' ' | 错误日志 |
| 9 | ferror_tag | 错误日志_详情 | text | 0 |  |  | null | 错误日志_详情 |
| 10 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: S :成功 F :失败 I :忽略 |
| 11 | fmessageid | 消息标识 | varchar | 100 |  | √ | ' ' | 消息标识 |
| 12 | fext | 扩展信息 | varchar | 255 |  | √ | ' ' | 扩展信息 |
| 13 | fext_tag | 扩展信息_详情 | text | 0 |  |  | null | 扩展信息_详情 |
| 14 | fgroup | 连接系统 | int8 | 64 |  | √ | 0 | [连接器配置 isc_database_link](../iscb_files/isc_database_link.md) |
| 15 | frequestid | 事件跟踪ID | varchar | 50 |  | √ | ' ' | 事件跟踪ID |
| 16 | fdata | 推送数据 | varchar | 255 |  | √ | ' ' | 推送数据 |
| 17 | fcanretry | 可重推 | bpchar | 1 |  | √ | '0' | 可重推 |
| 18 | feventtype | 事件类型 | bpchar | 1 |  | √ | ' ' | 事件类型,枚举: 1 :自定义事件 2 :Webhook事件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_trigger_log_ct |  | fcreatetime |
| 2 | idx_kem_trigger_log_traceid |  | ftraceid |
| 3 | pk_kem_trigger_log |  | fid |
| 4 | idx_kem_trigger_log_requestid |  | frequestid |
