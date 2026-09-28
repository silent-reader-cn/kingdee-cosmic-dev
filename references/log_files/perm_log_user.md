# 影响用户-perm_log_user

## 影响用户-主表 t_perm_log_user

- **表名称：** 影响用户-主表
- **表名：** t_perm_log_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 操作日志用户关联ID | int8 | 64 |  | √ | 0 | 操作日志用户关联ID |
| 2 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 3 | fname | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 4 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 5 | fuser_name | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 6 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 7 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 8 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fuser_id | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 10 | fnumber | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fperm_logid |  | fperm_logid |
| 2 | idx_username |  | fuser_name |
| 3 | pk_perm_log_user |  | fid |
