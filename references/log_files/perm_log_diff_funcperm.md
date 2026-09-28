# 功能权限差异-perm_log_diff_funcperm

## 功能权限差异-主表 t_perm_log_diff_funcperm

- **表名称：** 功能权限差异-主表
- **表名：** t_perm_log_diff_funcperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fdatachange_type_desc | 类型描述 | varchar | 20 |  | √ | ' ' | 类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | fcloud_id | 云编码 | varchar | 36 |  | √ | ' ' | 云编码 |
| 5 | fcloud_name | 云 | varchar | 100 |  | √ | ' ' | 云 |
| 6 | fentity_name | 实体名 | varchar | 200 |  | √ | ' ' | 实体名 |
| 7 | fperm_item_name | 权限项 | varchar | 50 |  | √ | ' ' | 权限项 |
| 8 | fentity_id | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fperm_item_id | 权限项编码 | varchar | 36 |  | √ | ' ' | 权限项编码 |
| 10 | fapp_name | 应用 | varchar | 100 |  | √ | ' ' | 应用 |
| 11 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 13 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 14 | fapp_id | 应用编码 | varchar | 36 |  | √ | ' ' | 应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_funcperm |  | fid |
| 2 | idx_logid_entity |  | fperm_logid,fentity_name |
