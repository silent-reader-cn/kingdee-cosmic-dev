# 隔离维度范围差异-perm_log_diff_dimrange

## 隔离维度范围差异-主表 t_perm_log_diff_dimrange

- **表名称：** 隔离维度范围差异-主表
- **表名：** t_perm_log_diff_dimrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fdim_id | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 6 | fdim_number | 隔离维度编码 | varchar | 50 |  | √ | ' ' | 隔离维度编码 |
| 7 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 8 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型 |
| 9 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 11 | fdimtypedesc | 隔离维度类型描述 | varchar | 30 |  | √ | ' ' | 隔离维度类型描述 |
| 12 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 13 | fdim_name | 隔离维度名称 | varchar | 255 |  | √ | ' ' | 隔离维度名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_dimrange |  | fid |
| 2 | idx_logid_dimrange |  | fperm_logid |
