# 流转日志(旧)-wf_eventlogentry

## 流转日志(旧)-主表 t_wf_evtlog

- **表名称：** 流转日志(旧)-主表
- **表名：** t_wf_evtlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtype | job类型 | varchar | 100 |  | √ | ' ' | job类型 |
| 3 | fjobid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 4 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | felementid | 节点id | varchar | 200 |  | √ | ' ' | 节点id |
| 9 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftype | 类型 | varchar | 255 |  | √ | ' ' | 类型 |
| 12 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 13 | fbusinesskey | 业务Id | varchar | 50 |  | √ | ' ' | 业务Id |
| 14 | ftraceno | 跟踪编码 | varchar | 100 |  | √ | ' ' | 跟踪编码 |
| 15 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 16 | ftimestamp | 时间 | timestamp | 0 |  |  | null | 时间 |
| 17 | fdata | 相关数据 | text | 0 |  |  | null | 相关数据 |
| 18 | fbillno | 单据编码 | varchar | 255 |  |  | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_evtlog_buskeyjobtype |  | fbusinesskey,fjobtype |
| 2 | t_wf_evtlog_pkey |  | fid |
| 3 | idx_wf_evtlog_datetimestamp |  | fcreatedate,ftimestamp |
| 4 | idx_wf_evtlog_timestamp |  | ftimestamp |
| 5 | idx_wf_evtlog_proc |  | fprocinstid |
| 6 | idx_wf_evtlog_billno |  | fbillno |
