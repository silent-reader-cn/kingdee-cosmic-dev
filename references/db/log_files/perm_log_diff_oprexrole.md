# 特殊数据权限例外通用角色差异-perm_log_diff_oprexrole

## 特殊数据权限例外通用角色差异-主表 t_perm_log_diff_oprexrole

- **表名称：** 特殊数据权限例外通用角色差异-主表
- **表名：** t_perm_log_diff_oprexrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | frole_remark | 通用角色备注 | varchar | 255 |  | √ | ' ' | 通用角色备注 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frole_id | 通用角色ID | varchar | 18 |  | √ | ' ' | 通用角色ID |
| 7 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 8 | frole_number | 通用角色编码 | varchar | 30 |  | √ | ' ' | 通用角色编码 |
| 9 | frole_name | 通用角色名称 | varchar | 255 |  | √ | ' ' | 通用角色名称 |
| 10 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_oprexrole |  | fid |
| 2 | idx_logid_oprexrole |  | fperm_logid |
