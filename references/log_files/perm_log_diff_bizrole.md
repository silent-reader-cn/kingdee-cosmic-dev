# 业务角色差异-perm_log_diff_bizrole

## 业务角色差异-主表 t_perm_log_diff_busirole

- **表名称：** 业务角色差异-主表
- **表名：** t_perm_log_diff_busirole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 6 | frole_number | 角色编码 | varchar | 36 |  | √ | ' ' | 角色编码 |
| 7 | frole_name | 角色名称 | varchar | 255 |  | √ | ' ' | 角色名称 |
| 8 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 10 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_busirole |  | fid |
| 2 | idx_logid_busirole |  | fperm_logid |
