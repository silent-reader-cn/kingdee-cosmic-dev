# 数据规则差异-perm_log_diff_newdr

## 数据规则差异-主表 t_perm_log_diff_newdr

- **表名称：** 数据规则差异-主表
- **表名：** t_perm_log_diff_newdr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fafter_data_ruleid | 变更后数据规则方案ID | int8 | 64 |  | √ | 0 | 变更后数据规则方案ID |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcloud_id | 云编码 | varchar | 36 |  | √ | ' ' | 云编码 |
| 6 | fcloud_name | 云 | varchar | 100 |  | √ | ' ' | 云 |
| 7 | fentity_name | 实体名 | varchar | 200 |  | √ | ' ' | 实体名 |
| 8 | fafter_data_rulename | 变更后数据规则方案 | varchar | 100 |  | √ | ' ' | 变更后数据规则方案 |
| 9 | fperm_item_name | 权限项 | varchar | 50 |  | √ | ' ' | 权限项 |
| 10 | fentity_id | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 11 | fperm_item_id | 权限项编码 | varchar | 36 |  | √ | ' ' | 权限项编码 |
| 12 | fpre_data_rulename | 变更前数据规则方案 | varchar | 100 |  | √ | ' ' | 变更前数据规则方案 |
| 13 | fapp_name | 应用 | varchar | 100 |  | √ | ' ' | 应用 |
| 14 | fpre_data_ruleid | 变更前数据规则方案ID | int8 | 64 |  | √ | 0 | 变更前数据规则方案ID |
| 15 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fdatachange_type | fdatachange_type | int4 | 32 |  | √ | 0 |  |
| 17 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 18 | fapp_id | 应用编码 | varchar | 36 |  | √ | ' ' | 应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_entity3 |  | fperm_logid,fentity_name |
| 2 | pk_perm_log_diff_newdr |  | fid |
