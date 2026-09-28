# 隔离维度通用角色差异-perm_log_diff_dimcomrole

## 隔离维度通用角色差异-主表 t_perm_log_diff_dimrole

- **表名称：** 隔离维度通用角色差异-主表
- **表名：** t_perm_log_diff_dimrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fdim_id | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | frole_name | 角色名称 | varchar | 255 |  | √ | ' ' | 角色名称 |
| 6 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 7 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fdim_number | 隔离维度编码 | varchar | 50 |  | √ | ' ' | 隔离维度编码 |
| 9 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 10 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型 |
| 11 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 13 | frole_number | 角色编码 | varchar | 36 |  | √ | ' ' | 角色编码 |
| 14 | fdimtypedesc | 隔离维度类型描述 | varchar | 30 |  | √ | ' ' | 隔离维度类型描述 |
| 15 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 16 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 17 | fdim_name | 隔离维度名称 | varchar | 255 |  | √ | ' ' | 隔离维度名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_dimrole |  | fid |
| 2 | idx_logid_dimrole |  | fperm_logid |
