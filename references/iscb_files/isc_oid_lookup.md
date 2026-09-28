# 单据ID映射表-isc_oid_lookup

## 单据ID映射表-主表 t_iscb_oid_lookup

- **表名称：** 单据ID映射表-主表
- **表名：** t_iscb_oid_lookup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 22 |  | √ | ' ' | id |
| 2 | fcreated_time | 时间戳（服务器时间） | int8 | 64 |  | √ | 0 | 时间戳（服务器时间） |
| 3 | ftarget_system | 目标系统 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 4 | fsource_type | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 5 | fentry_mapping | 分录ID映射关系 | varchar | 2000 |  | √ | ' ' | 分录ID映射关系 |
| 6 | fentry_mapping_tag | 分录ID映射关系_详情 | text | 0 |  |  | null | 分录ID映射关系_详情 |
| 7 | ftarget_oid | 目标单ID | varchar | 100 |  | √ | ' ' | 目标单ID |
| 8 | fsource_system | 源系统 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 9 | fsource_oid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 10 | ftarget_type | 目标单类型 | varchar | 50 |  | √ | ' ' | 目标单类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_lookup_tid |  | ftarget_oid |
| 2 | idx_iscb_oid_loaed25b |  | fcreated_time |
| 3 | idx_iscb_lookup_soid |  | fsource_oid |
| 4 | t_iscb_oid_lookup_pkey |  | fid |
