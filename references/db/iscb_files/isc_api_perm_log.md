# 集成云API权限调用日志-isc_api_perm_log

## 集成云API权限调用日志-主表 t_isc_api_perm_log

- **表名称：** 集成云API权限调用日志-主表
- **表名：** t_isc_api_perm_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 调用者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreated_time | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 4 | ftype | API类型 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fpermitemid | 权限项 | varchar | 50 |  | √ | ' ' | 权限项,枚举: 4TAR7QONT/3J :集成云API调用 4TASW06SC8=5 :集成云内部访问 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_isc_api_perm_log |  | fcreator |
| 2 | pk_t_isc_api_perm_log |  | fid |
