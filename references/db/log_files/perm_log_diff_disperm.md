# 权限禁用差异-perm_log_diff_disperm

## 权限禁用差异-主表 t_perm_log_diff_disperm

- **表名称：** 权限禁用差异-主表
- **表名：** t_perm_log_diff_disperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 5 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 6 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 7 | fperm_item_name | 权限项名 | varchar | 50 |  | √ | ' ' | 权限项名 |
| 8 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 9 | fperm_item_id | 权限项ID | varchar | 36 |  | √ | ' ' | 权限项ID |
| 10 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 11 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 13 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 14 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_disperm |  | fid |
| 2 | idx_logid_entity_c |  | fperm_logid,fentity_name |
