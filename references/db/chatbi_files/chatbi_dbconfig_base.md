# 数据连接-chatbi_dbconfig_base

## 数据连接-主表 t_cbi_dbconfig

- **表名称：** 数据连接-主表
- **表名：** t_cbi_dbconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fdbtype | 连接类型 | varchar | 50 |  | √ | ' ' | 连接类型,枚举: 6 :MySQL 5 :PostgreSQL 2 :Oracle |
| 4 | fpwd | 登录密码 | varchar | 200 |  | √ | ' ' | 登录密码 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fother | 其他参数 | varchar | 500 |  |  | null | 其他参数 |
| 7 | fip | 服务器IP或域名 | varchar | 50 |  | √ | ' ' | 服务器IP或域名 |
| 8 | fpwd_enp | fpwd_enp | varchar | 500 |  | √ | ' ' |  |
| 9 | fcharacterset | 字符集 | varchar | 50 |  | √ | ' ' | 字符集 |
| 10 | fusername | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 11 | fstatus | 状态 | varchar | 10 |  | √ | '0' | 状态,枚举: 0 :不可用 1 :可用 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |
| 14 | fport | 服务器端口 | int4 | 32 |  | √ | 0 | 服务器端口 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdbname | 数据库名 | varchar | 200 |  | √ | ' ' | 数据库名 |
| 17 | fplugin | 自定义插件 | varchar | 500 |  | √ | ' ' | 自定义插件 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dbconfig |  | fid |
