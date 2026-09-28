# 隔离维度数据规则差异表-perm_log_diff_dimnewdr

## 隔离维度数据规则差异表-主表 t_perm_log_diff_dimnewdr

- **表名称：** 隔离维度数据规则差异表-主表
- **表名：** t_perm_log_diff_dimnewdr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fdim_id | 权限控制对象id | int8 | 64 |  | √ | 0 | 权限控制对象id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 5 | fperm_item_name | 权限项名 | varchar | 50 |  | √ | ' ' | 权限项名 |
| 6 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 7 | fdim_number | 权限控制对象编码 | varchar | 50 |  | √ | ' ' | 权限控制对象编码 |
| 8 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 9 | fpre_data_rulename | 变更前数据规则方案名 | varchar | 100 |  | √ | ' ' | 变更前数据规则方案名 |
| 10 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 11 | fpre_data_ruleid | 变更前数据规则方案id | int8 | 64 |  | √ | 0 | 变更前数据规则方案id |
| 12 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型 |
| 13 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 15 | fdim_name | 权限控制对象名称 | varchar | 255 |  | √ | ' ' | 权限控制对象名称 |
| 16 | fafter_data_ruleid | 变更后数据规则方案id | int8 | 64 |  | √ | 0 | 变更后数据规则方案id |
| 17 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 18 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 19 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 20 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 21 | fafter_data_rulename | 变更后数据规则方案名 | varchar | 100 |  | √ | ' ' | 变更后数据规则方案名 |
| 22 | fperm_item_id | 权限项ID | varchar | 36 |  | √ | ' ' | 权限项ID |
| 23 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 24 | fdimtypedesc | 权限控制类型描述 | varchar | 30 |  | √ | ' ' | 权限控制类型描述 |
| 25 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_dimnewdr |  | fperm_logid,fentity_name |
| 2 | pk_perm_log_diff_dimnewdr |  | fid |
