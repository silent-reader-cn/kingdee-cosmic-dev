# 连接器-iscx_connector

## 连接器-主表 t_iscx_connector

- **表名称：** 连接器-主表
- **表名：** t_iscx_connector

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: isc_database_link :系统连接 isc_mq_server :消息队列 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fconnection | 连接配置／消息队列 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 8 | fsourceapp | 来源应用 | varchar | 50 |  | √ | ' ' | 来源应用 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_connector |  | fid |
| 2 | idx_t_iscx_connector_i |  | fnumber |
