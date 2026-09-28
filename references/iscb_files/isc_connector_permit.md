# 连接器授权-isc_connector_permit

## 连接器授权-主表 t_iscb_connector_permit

- **表名称：** 连接器授权-主表
- **表名：** t_iscb_connector_permit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpermission | 授权 | varchar | 30 |  | √ | ' ' | 授权,枚举: READ :读取 WRITE :写入 EXECUTE :执行 |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fschema | 集成对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 7 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_con_permit_1 |  | fschema |
| 2 | t_iscb_connector_permit_pkey |  | fid |
