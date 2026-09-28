# 用户差异表-perm_log_diff_user

## 用户差异表-主表 t_perm_log_diff_user

- **表名称：** 用户差异表-主表
- **表名：** t_perm_log_diff_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fuser_name | 用户姓名 | varchar | 50 |  | √ | ' ' | 用户姓名 |
| 5 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 6 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 7 | fuser_number | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |
| 8 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fuser_username | 用户用户名 | varchar | 255 |  | √ | ' ' | 用户用户名 |
| 10 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 12 | fuser_id | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 13 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 14 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_user |  | fid |
| 2 | idx_logid_diffuser |  | fperm_logid |
