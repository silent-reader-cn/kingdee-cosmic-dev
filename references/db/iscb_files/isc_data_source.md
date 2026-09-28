# 数据源管理-isc_data_source

## 数据源管理-主表 t_isc_datasource

- **表名称：** 数据源管理-主表
- **表名：** t_isc_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmqlink | MQ连接 | int8 | 64 |  | √ | 0 | [MQ消息服务Old isc_mq](../iscb_files/isc_mq.md) |
| 6 | fsourceapp | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 7 | fconnection_type | 连接类型 | varchar | 50 |  | √ | ' ' | 连接类型,枚举: CurrentDB :当前数据库 oracle :Oracle sqlserver :SQL Service mysql :MySQL PostgreSQL :PostgreSQL self :当前账套 db_proxy :数据库代理 DM :达梦数据库 eas :EAS系统 k3cloud :金蝶云·星空 ierp :金蝶云·苍穹 CloudHub :云之家 DummyConnector :哑连接 isc_hub :集成云HUB |
| 8 | fdblink | 系统连接 | int8 | 64 |  | √ | 0 | [连接器配置 isc_database_link](../iscb_files/isc_database_link.md) |
| 9 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 10 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: jdbc :JDBC数据源 |
| 14 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 15 | flast_modifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 18 | flast_modified_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_datasource_pkey |  | fid |
| 2 | idx_isc_datasource_0 |  | ftype |

---

## 数据源管理-多语言表 t_isc_datasource_l

- **表名称：** 数据源管理-多语言表
- **表名：** t_isc_datasource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_datasource_l_pkey |  | fpkid |
| 2 | idx_isc_datasource_l_0 |  | flocaleid,fid |
