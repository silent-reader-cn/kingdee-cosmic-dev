# 用户组角色隔离维度差异-perm_log_ugroledim

## 用户组角色隔离维度差异-主表 t_perm_log_diff_ugroledim

- **表名称：** 用户组角色隔离维度差异-主表
- **表名：** t_perm_log_diff_ugroledim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fusrgrp_name | 用户组名 | varchar | 255 |  | √ | ' ' | 用户组名 |
| 3 | fdim_id | 权限控制对象id | int8 | 64 |  | √ | 0 | 权限控制对象id |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 6 | fusrgrp_number | 用户组编码 | varchar | 80 |  | √ | ' ' | 用户组编码 |
| 7 | frole_name | 角色名称 | varchar | 255 |  | √ | ' ' | 角色名称 |
| 8 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 9 | fdim_number | 权限控制对象编码 | varchar | 255 |  | √ | ' ' | 权限控制对象编码 |
| 10 | finclude_sub | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 11 | finclude_sub_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 12 | fusrgrp_id | 用户组id | int8 | 64 |  | √ | 0 | 用户组id |
| 13 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型 |
| 14 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | frole_id | 角色id | varchar | 18 |  | √ | ' ' | 角色id |
| 16 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 17 | frole_number | 角色编码 | varchar | 255 |  | √ | ' ' | 角色编码 |
| 18 | fdimtypedesc | 权限控制类型描述 | varchar | 30 |  | √ | ' ' | 权限控制类型描述 |
| 19 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 20 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 21 | fdim_name | 权限控制对象名称 | varchar | 255 |  | √ | ' ' | 权限控制对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_ugroledim |  | fperm_logid |
| 2 | pk_perm_log_diff_ugroledim |  | fid |
