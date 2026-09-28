# 基础资料数据范围差异-perm_log_diff_newdrprop

## 基础资料数据范围差异-主表 t_perm_log_diff_newdrprop

- **表名称：** 基础资料数据范围差异-主表
- **表名：** t_perm_log_diff_newdrprop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fafter_data_ruleid | 变更后数据规则方案id | int8 | 64 |  | √ | 0 | 变更后数据规则方案id |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fprop_key | 属性标识 | varchar | 60 |  | √ | ' ' | 属性标识 |
| 6 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 7 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 8 | fentity_name | 实体名称 | varchar | 200 |  | √ | ' ' | 实体名称 |
| 9 | fafter_data_rulename | 变更后数据规则方案名 | varchar | 100 |  | √ | ' ' | 变更后数据规则方案名 |
| 10 | fentity_id | 实体ID | varchar | 50 |  | √ | ' ' | 实体ID |
| 11 | fpre_data_rulename | 变更前数据规则方案 | varchar | 100 |  | √ | ' ' | 变更前数据规则方案 |
| 12 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 13 | fpre_data_ruleid | 变更前数据规则方案ID | int8 | 64 |  | √ | 0 | 变更前数据规则方案ID |
| 14 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 16 | fprop_entnum | 业务对象标识 | varchar | 60 |  | √ | ' ' | 业务对象标识 |
| 17 | fprop_name | 属性名称 | varchar | 60 |  | √ | ' ' | 属性名称 |
| 18 | fprop_entname | 业务对象名称 | varchar | 60 |  | √ | ' ' | 业务对象名称 |
| 19 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 20 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_newdrprop |  | fid |
| 2 | idx_logid_entity4 |  | fperm_logid,fentity_name |
