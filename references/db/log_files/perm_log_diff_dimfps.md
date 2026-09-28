# 隔离维度字段权限方案差异-perm_log_diff_dimfps

## 隔离维度字段权限方案差异-主表 t_perm_log_diff_dimfps

- **表名称：** 隔离维度字段权限方案差异-主表
- **表名：** t_perm_log_diff_dimfps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fdim_id | 权限控制对象id | int8 | 64 |  | √ | 0 | 权限控制对象id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 6 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 7 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 8 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 9 | ffpschemeid | 字段方案id | int8 | 64 |  | √ | 0 | 字段方案id |
| 10 | fentity_num | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 11 | fdim_number | 权限控制对象编码 | varchar | 50 |  | √ | ' ' | 权限控制对象编码 |
| 12 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 13 | fsensitive | 敏感方案 | bpchar | 1 |  | √ | '0' | 敏感方案 |
| 14 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 15 | ffpschemename | 字段方案名 | varchar | 255 |  | √ | ' ' | 字段方案名 |
| 16 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型 |
| 17 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 19 | fdimtypedesc | 权限控制类型描述 | varchar | 30 |  | √ | ' ' | 权限控制类型描述 |
| 20 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 21 | fdim_name | 权限控制对象名称 | varchar | 255 |  | √ | ' ' | 权限控制对象名称 |
| 22 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dimfps_permlogid |  | fperm_logid,fentity_name |
| 2 | pk_t_perm_log_diff_dimfps |  | fid |
