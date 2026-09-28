# 隔离维度功能权限差异-perm_log_diff_dimfun

## 隔离维度功能权限差异-主表 t_perm_log_diff_dimfunc

- **表名称：** 隔离维度功能权限差异-主表
- **表名：** t_perm_log_diff_dimfunc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdim_id | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 6 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 7 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 8 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 9 | fperm_item_name | 权限项名 | varchar | 50 |  | √ | ' ' | 权限项名 |
| 10 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 11 | fperm_item_id | 权限项ID | varchar | 36 |  | √ | ' ' | 权限项ID |
| 12 | fdim_number | 隔离维度编码 | varchar | 50 |  | √ | ' ' | 隔离维度编码 |
| 13 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 14 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 15 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型 |
| 16 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 18 | fdimtypedesc | 隔离维度类型描述 | varchar | 30 |  | √ | ' ' | 隔离维度类型描述 |
| 19 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 20 | fdim_name | 隔离维度名称 | varchar | 255 |  | √ | ' ' | 隔离维度名称 |
| 21 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_dimfunc |  | fid |
| 2 | idx_logid_dimfunc |  | fperm_logid,fentity_name |
