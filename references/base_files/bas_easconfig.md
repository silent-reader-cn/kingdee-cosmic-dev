# EAS系统配置-bas_easconfig

## EAS系统配置-主表 t_bas_easconfig

- **表名称：** EAS系统配置-主表
- **表名：** t_bas_easconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatacenter | 数据中心 | varchar | 50 |  | √ | ' ' | 数据中心 |
| 3 | fusername | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 4 | fdbtype | 数据库类型 | varchar | 10 |  | √ | ' ' | 数据库类型,枚举: 0 :SQLServer 1 :DB2 2 :Oracle |
| 5 | fport | 端口 | varchar | 10 |  | √ | ' ' | 端口 |
| 6 | fexternalsysid | 外部系统 | int8 | 64 |  | √ | 0 | 外部系统 bas_externalsys |
| 7 | flanguage | 语言 | varchar | 10 |  | √ | ' ' | 语言 |
| 8 | fip | IP地址 | varchar | 50 |  | √ | ' ' | IP地址 |
| 9 | fpassword | 密码 | varchar | 50 |  | √ | ' ' | 密码 |
| 10 | fsolution | 解决方案 | varchar | 50 |  | √ | ' ' | 解决方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_easconfig_pkey |  | fid |
| 2 | idx_easconfig_extsys |  | fexternalsysid |
