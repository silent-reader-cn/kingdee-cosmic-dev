# 日志设置-bos_log_settings

## 日志设置-主表 t_log_settings

- **表名称：** 日志设置-主表
- **表名：** t_log_settings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改日期 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmodifier | 修改人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fusertype | 日志用户类型 | varchar | 10 |  | √ | ' ' | 日志用户类型 |
| 7 | fopuserformat | 操作用户名格式 | varchar | 50 |  | √ | ' ' | 操作用户名格式,枚举: name :姓名 name+number :姓名+工号 name+username :姓名+用户名 name+phone :姓名+手机号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_log_settings |  | fid |
| 2 | idx_t_log_settings_usertype |  | fusertype |
