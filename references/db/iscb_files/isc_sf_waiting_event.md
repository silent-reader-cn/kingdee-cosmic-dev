# 服务流程 - 等待事件注册-isc_sf_waiting_event

## 服务流程 - 等待事件注册-主表 t_isc_sf_waiting_event

- **表名称：** 服务流程 - 等待事件注册-主表
- **表名：** t_isc_sf_waiting_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreated_time | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 3 | frequires | 要求的字段 | varchar | 255 |  | √ | ' ' | 要求的字段 |
| 4 | fmeta_schema | 集成对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 5 | fnode_title | 节点标题 | varchar | 50 |  | √ | ' ' | 节点标题 |
| 6 | fservice_flow_id | 服务流程 | int8 | 64 |  | √ | 0 | 服务流程 isc_service_flow |
| 7 | fsignal_fields | 信号字段 | varchar | 500 |  | √ | ' ' | 信号字段 |
| 8 | frequires_tag | 要求的字段_详情 | text | 0 |  |  | null | 要求的字段_详情 |
| 9 | fevents | 监听事件 | varchar | 1000 |  | √ | ' ' | 监听事件 |
| 10 | fenabled | 启用 | bpchar | 1 |  | √ | ' ' | 启用 |
| 11 | fnode_id | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_sf_waiting_event_f |  | fservice_flow_id |
| 2 | pk_t_isc_sf_waiting_event |  | fid |
| 3 | idx_t_isc_sf_waiting_event_t |  | fcreated_time |
