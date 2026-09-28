# 二次认证日志-bos_authoperate_log

## 二次认证日志-主表 t_bd_secondauth_log

- **表名称：** 二次认证日志-主表
- **表名：** t_bd_secondauth_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizobjname | fbizobjname | varchar | 100 |  | √ | ' ' |  |
| 3 | foperateuser | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | foperateresult | 认证结果 | varchar | 250 |  | √ | ' ' | 认证结果 |
| 5 | foperatedate | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 6 | fverifymode | 认证方式 | bpchar | 1 |  | √ | ' ' | 认证方式,枚举: 0 :密码验证 1 :短信验证 2 :邮箱验证 |
| 7 | fbizobj | 业务对象编码 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fverifyoperate | 认证操作 | varchar | 250 |  | √ | ' ' | 认证操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_secondauth_log |  | fid |
| 2 | idx_auth_log_bizobj |  | fbizobj |
| 3 | idx_auth_log_user |  | foperateuser |
