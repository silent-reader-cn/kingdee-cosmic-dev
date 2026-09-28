# 隔离维度字段权限差异-perm_log_diff_dimfield

## 隔离维度字段权限差异-主表 t_perm_log_diff_dimfield

- **表名称：** 隔离维度字段权限差异-主表
- **表名：** t_perm_log_diff_dimfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | ffield_comment | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 3 | fdim_id | 权限控制对象id | int8 | 64 |  | √ | 0 | 权限控制对象id |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 6 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 7 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 8 | ffield_name | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 9 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 10 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 11 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 12 | fdim_number | 权限控制对象编码 | varchar | 50 |  | √ | ' ' | 权限控制对象编码 |
| 13 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 14 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 15 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型 |
| 16 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 18 | fdimtypedesc | 权限控制类型描述 | varchar | 30 |  | √ | ' ' | 权限控制类型描述 |
| 19 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 20 | fcontrol_modedesc | 控制模式描述 | varchar | 30 |  | √ | ' ' | 控制模式描述 |
| 21 | fdim_name | 权限控制对象名称 | varchar | 255 |  | √ | ' ' | 权限控制对象名称 |
| 22 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 23 | fcontrol_mode | 控制模式 | varchar | 20 |  | √ | ' ' | 控制模式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_dimfield |  | fid |
| 2 | idx_logid_dimfield |  | fperm_logid,fentity_name |
