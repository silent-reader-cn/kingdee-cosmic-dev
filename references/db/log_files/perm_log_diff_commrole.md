# 通用角色差异-perm_log_diff_commrole

## 通用角色差异-主表 t_perm_log_diff_commrole

- **表名称：** 通用角色差异-主表
- **表名：** t_perm_log_diff_commrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fop_enable_desc | 启用操作描述 | varchar | 20 |  | √ | ' ' | 启用操作描述 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 7 | frole_number | 角色编码 | varchar | 36 |  | √ | ' ' | 角色编码 |
| 8 | frole_name | 角色名 | varchar | 255 |  | √ | ' ' | 角色名 |
| 9 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 10 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_entity_a |  | fperm_logid |
| 2 | pk_perm_log_diff_commrole |  | fid |
