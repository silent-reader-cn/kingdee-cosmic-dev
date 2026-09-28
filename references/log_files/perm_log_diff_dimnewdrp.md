# 隔离维度基础资料数据范围差异表-perm_log_diff_dimnewdrp

## 隔离维度基础资料数据范围差异表-主表 t_perm_log_diff_dimnewdrp

- **表名称：** 隔离维度基础资料数据范围差异表-主表
- **表名：** t_perm_log_diff_dimnewdrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdim_id | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 5 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 6 | fdim_number | 隔离维度编码 | varchar | 50 |  | √ | ' ' | 隔离维度编码 |
| 7 | finclude_suborg | 是否包含下级 | bpchar | 1 |  | √ | '0' | 是否包含下级 |
| 8 | fpre_data_rulename | 变更前数据规则方案名 | varchar | 100 |  | √ | ' ' | 变更前数据规则方案名 |
| 9 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 10 | fpre_data_ruleid | 变更前数据规则方案id | int8 | 64 |  | √ | 0 | 变更前数据规则方案id |
| 11 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型 |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fprop_name | 属性名称 | varchar | 60 |  | √ | ' ' | 属性名称 |
| 14 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 15 | fdim_name | 隔离维度名称 | varchar | 255 |  | √ | ' ' | 隔离维度名称 |
| 16 | fafter_data_ruleid | 变更后数据规则方案id | int8 | 64 |  | √ | 0 | 变更后数据规则方案id |
| 17 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 18 | fprop_key | 属性标识 | varchar | 60 |  | √ | ' ' | 属性标识 |
| 19 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 20 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 21 | finclude_suborg_desc | 是否包含下级描述 | varchar | 20 |  | √ | ' ' | 是否包含下级描述 |
| 22 | fafter_data_rulename | 变更后数据规则方案名 | varchar | 100 |  | √ | ' ' | 变更后数据规则方案名 |
| 23 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 24 | fprop_entnum | 业务对象标识 | varchar | 60 |  | √ | ' ' | 业务对象标识 |
| 25 | fdimtypedesc | 隔离维度类型描述 | varchar | 30 |  | √ | ' ' | 隔离维度类型描述 |
| 26 | fprop_entname | 业务对象名称 | varchar | 60 |  | √ | ' ' | 业务对象名称 |
| 27 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_dimnewdrp |  | fperm_logid,fentity_name |
| 2 | pk_perm_log_diff_dimnewdrp |  | fid |
