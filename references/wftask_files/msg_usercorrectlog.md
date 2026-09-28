# 用户登录校正日志-msg_usercorrectlog

## 用户登录校正日志-主表 t_msg_usercorrectlog

- **表名称：** 用户登录校正日志-主表
- **表名：** t_msg_usercorrectlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfig | 参数 | text | 0 |  |  | null | 参数 |
| 3 | flogintime | 登录时间 | timestamp | 0 |  |  | null | 登录时间 |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 5 | fcorrecttime | 校正时间 | timestamp | 0 |  |  | null | 校正时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_usercorrlog_logintime |  | flogintime |
| 2 | pk_msg_usercorrectlog |  | fid |
| 3 | idx_msg_usercorrlog_userid |  | fuserid |
