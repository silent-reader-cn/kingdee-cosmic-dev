# 集成云服务器实例-isc_server_instance

## 集成云服务器实例-主表 t_iscb_server_instance

- **表名称：** 集成云服务器实例-主表
- **表名：** t_iscb_server_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeploy_info | 运行环境信息 | varchar | 500 |  | √ | ' ' | 运行环境信息 |
| 3 | finstance_id | 服务器ID | varchar | 140 |  | √ | ' ' | 服务器ID |
| 4 | fis_online | 是否在线 | bpchar | 1 |  | √ | '0' | 是否在线 |
| 5 | fstart_time | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 6 | fip | 服务器IP | varchar | 160 |  | √ | ' ' | 服务器IP |
| 7 | flast_modified_time | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_server_instance_pkey |  | fid |
| 2 | idx_iscb_serv_online |  | fis_online |
| 3 | idx_finstance_iscb_server |  | finstance_id |
| 4 | idx_fip_iscb_server |  | fip |
