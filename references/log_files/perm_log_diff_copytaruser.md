# 复制权限差异-perm_log_diff_copytaruser

## 复制权限差异-主表 t_perm_log_copytaruser

- **表名称：** 复制权限差异-主表
- **表名：** t_perm_log_copytaruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fname | 目标用户名 | varchar | 50 |  | √ | ' ' | 目标用户名 |
| 3 | fuser_name | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuser_id | 目标用户ID | int8 | 64 |  | √ | 0 | 目标用户ID |
| 7 | fnumber | 目标用户编码 | varchar | 36 |  | √ | ' ' | 目标用户编码 |
| 8 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_uname |  | fuser_name |
| 2 | pk_perm_log_copytaruser |  | fid |
| 3 | idx_logid_copytaruser |  | fperm_logid |
