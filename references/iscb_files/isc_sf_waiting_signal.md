# 服务流程 - 等待信号-isc_sf_waiting_signal

## 服务流程 - 等待信号-主表 t_isc_sf_waiting_signal

- **表名称：** 服务流程 - 等待信号-主表
- **表名：** t_isc_sf_waiting_signal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fservice_process_number | 流程实例编码 | varchar | 50 |  | √ | ' ' | 流程实例编码 |
| 3 | fhash_code | 哈希码 | int4 | 32 |  | √ | 0 | 哈希码 |
| 4 | fstack_trace_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 5 | fnode_id | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |
| 6 | fsignal_identifier | 信号标识 | varchar | 500 |  | √ | ' ' | 信号标识 |
| 7 | fcreated_time | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 8 | fservice_process_id | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 9 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: W :等待 F :失败 S :成功 N :忽略 |
| 10 | fmodified_time | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 11 | fnode_title | 节点标题 | varchar | 50 |  | √ | ' ' | 节点标题 |
| 12 | fstack_trace | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 13 | fservice_flow_id | 服务流程 | int8 | 64 |  | √ | 0 | 服务流程 isc_service_flow |
| 14 | factivity_id | 节点实例ID | varchar | 50 |  | √ | ' ' | 节点实例ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_sf_waiting_signal_h |  | fhash_code |
| 2 | idx_isc_sf_waiting_signal_f |  | fservice_process_id |
| 3 | idx_isc_sf_waiting_signal_n |  | fservice_process_number |
| 4 | idx_isc_sf_waiting_signal_t |  | fcreated_time |
| 5 | pk_t_isc_sf_waiting_signal |  | fid |
