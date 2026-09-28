# 用户组业务角色差异-perm_log_ugbusirole

## 用户组业务角色差异-主表 t_perm_log_diff_ugbizrole

- **表名称：** 用户组业务角色差异-主表
- **表名：** t_perm_log_diff_ugbizrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fusrgrp_name | 用户组名 | varchar | 255 |  | √ | ' ' | 用户组名 |
| 3 | fbusirole_number | 业务角色编码 | varchar | 255 |  | √ | ' ' | 业务角色编码 |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 6 | fusrgrp_number | 用户组编码 | varchar | 80 |  | √ | ' ' | 用户组编码 |
| 7 | fusrgrpstdid | 用户组分类id | int8 | 64 |  | √ | '1404221671421785088' | 用户组分类id |
| 8 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fbusirole_name | 业务角色名称 | varchar | 255 |  | √ | ' ' | 业务角色名称 |
| 10 | fusrgrp_id | 用户组id | int8 | 64 |  | √ | 0 | 用户组id |
| 11 | fusrgrpstd_desc | 用户组分类描述 | varchar | 255 |  | √ | ' ' | 用户组分类描述 |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 14 | fbusirole_id | 业务角色id | int8 | 64 |  | √ | 0 | 业务角色id |
| 15 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 16 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_ugbizrole |  | fid |
| 2 | idx_logid_diffugbizrole |  | fperm_logid |
