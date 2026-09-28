# 特殊数据权限例外用户差异-perm_log_diff_oprexusr

## 特殊数据权限例外用户差异-主表 t_perm_log_diff_oprexusr

- **表名称：** 特殊数据权限例外用户差异-主表
- **表名：** t_perm_log_diff_oprexusr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fname | 用户名称 | varchar | 50 |  | √ | ' ' | 用户名称 |
| 3 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fuser_name | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 6 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 7 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 8 | forgid | 部门ID | int8 | 64 |  | √ | 0 | 部门ID |
| 9 | forg_name | 部门名 | varchar | 255 |  | √ | ' ' | 部门名 |
| 10 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 12 | fposition | 职位名称 | varchar | 255 |  | √ | ' ' | 职位名称 |
| 13 | fuser_id | 用户编码 | int8 | 64 |  | √ | 0 | 用户编码 |
| 14 | fnumber | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |
| 15 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_oprexusr |  | fid |
| 2 | idx_logid_oprexusr |  | fperm_logid |
