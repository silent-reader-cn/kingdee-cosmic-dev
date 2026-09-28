# 用户角色关系差异-perm_log_urdim

## 用户角色关系差异-主表 t_perm_log_diff_urdim

- **表名称：** 用户角色关系差异-主表
- **表名：** t_perm_log_diff_urdim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 3 | fdim_id | 权限控制对象id | int8 | 64 |  | √ | 0 | 权限控制对象id |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fuser_name | 用户姓名 | varchar | 50 |  | √ | ' ' | 用户姓名 |
| 6 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 7 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 8 | frole_name | 角色名称 | varchar | 255 |  | √ | ' ' | 角色名称 |
| 9 | finclude_suborg_desc | 分配组织及下级描述 | varchar | 20 |  | √ | ' ' | 分配组织及下级描述 |
| 10 | fuser_number | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |
| 11 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 12 | fdim_number | 权限控制对象编码 | varchar | 50 |  | √ | ' ' | 权限控制对象编码 |
| 13 | finclude_suborg | 分配组织及下级 | bpchar | 1 |  | √ | '0' | 分配组织及下级 |
| 14 | fuser_username | 用户用户名 | varchar | 255 |  | √ | ' ' | 用户用户名 |
| 15 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型 |
| 16 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 18 | frole_number | 角色编码 | varchar | 36 |  | √ | ' ' | 角色编码 |
| 19 | fdimtypedesc | 权限控制类型描述 | varchar | 30 |  | √ | ' ' | 权限控制类型描述 |
| 20 | fuser_id | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 21 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 22 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 23 | fdim_name | 权限控制对象名称 | varchar | 255 |  | √ | ' ' | 权限控制对象名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_urdim |  | fperm_logid |
| 2 | pk_perm_log_diff_urdim |  | fid |
