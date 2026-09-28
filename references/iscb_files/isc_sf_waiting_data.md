# 服务流程 - 等待数据-isc_sf_waiting_data

## 服务流程 - 等待数据-主表 t_isc_sf_waiting_data

- **表名称：** 服务流程 - 等待数据-主表
- **表名：** t_isc_sf_waiting_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreated_time | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 3 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: W :就绪 F :失败 S :成功 N :忽略 |
| 4 | fmodified_time | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 5 | fnode_title | 节点标题 | varchar | 50 |  | √ | ' ' | 节点标题 |
| 6 | fservice_flow_id | 服务流程 | int8 | 64 |  | √ | 0 | 服务流程 isc_service_flow |
| 7 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 8 | fhash_code | 哈希码 | int4 | 32 |  | √ | 0 | 哈希码 |
| 9 | fdata | 数据 | varchar | 255 |  | √ | ' ' | 数据 |
| 10 | fnode_id | 节点ID | varchar | 50 |  | √ | ' ' | 节点ID |
| 11 | fsignal_identifier | 信号标识 | varchar | 500 |  | √ | ' ' | 信号标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_sf_waiting_data_h |  | fhash_code |
| 2 | idx_isc_sf_waiting_data_t |  | fcreated_time |
| 3 | pk_t_isc_sf_waiting_data |  | fid |
| 4 | idx_isc_sf_waiting_data_f |  | fservice_flow_id |
