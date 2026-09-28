# 分表归档路由变更-bos_cbs_shard_archirt

## 分表归档路由变更-主表 t_cbs_shard_archi_route

- **表名称：** 分表归档路由变更-主表
- **表名：** t_cbs_shard_archi_route

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginal_route | 原库 | varchar | 50 |  | √ | ' ' | 原库 |
| 3 | fshardtable | 分片表 | varchar | 50 |  | √ | ' ' | 分片表 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | findex | 分片标识 | int8 | 64 |  |  | null | 分片标识 |
| 6 | fentitynumber | 表单 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | farchiconfigid | 分表归档配置id | int8 | 64 |  |  | null | 分表归档配置id |
| 8 | farchivefield | 归档属性 | varchar | 50 |  | √ | ' ' | 归档属性 |
| 9 | farchicondiid | 分表归档条件id | int8 | 64 |  |  | null | 分表归档条件id |
| 10 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 12 | ftarget_route | 目标库 | varchar | 50 |  | √ | ' ' | 目标库 |
| 13 | foriginaltable | 原表 | varchar | 50 |  | √ | ' ' | 原表 |
| 14 | fversion | 变更版本号 | int8 | 64 |  |  | null | 变更版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_shard_archi_route_fentity |  | fentitynumber |
| 2 | pk_t_cbs_shard_archi_route |  | fid |
