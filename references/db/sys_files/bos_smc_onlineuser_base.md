# 在线用户基础资料-bos_smc_onlineuser_base

## 在线用户基础资料-主表 t_bas_sessions

- **表名称：** 在线用户基础资料-主表
- **表名：** t_bas_sessions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 256 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人id | int8 | 64 |  | √ | 0 | 修改人id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 4 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 5 | flogintime | 登录时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 登录时间 |
| 6 | flanguage | 语言 | varchar | 10 |  | √ | ' ' | 语言 |
| 7 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 8 | fbizpartnerid | bizpartnerid | int8 | 64 |  | √ | 0 | bizpartnerid |
| 9 | fyzjappid | 云之家appid | varchar | 50 |  |  | ' ' | 云之家appid |
| 10 | fkdcsrftoken | kdcsrftoken | varchar | 256 |  | √ | ' ' | kdcsrftoken |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fyzjappticket | 云之家appticket | varchar | 200 |  |  | ' ' | 云之家appticket |
| 13 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 14 | floginorg | 登录组织 | int8 | 64 |  | √ | 0 | 登录组织 |
| 15 | floginip | 登录ip | varchar | 512 |  | √ | ' ' | 登录ip |
| 16 | fuseropenid | useropenid | varchar | 50 |  | √ | ' ' | useropenid |
| 17 | fapi3rdappnum | api3rdappnum | varchar | 50 |  | √ | ' ' | api3rdappnum |
| 18 | fuid | fuid | int8 | 64 |  | √ | 0 |  |
| 19 | fusertype | 用户类型 | varchar | 100 |  | √ | ' ' | 用户类型 |
| 20 | facccompanyid | acccompanyid | varchar | 50 |  | √ | ' ' | acccompanyid |
| 21 | fapi3rdappid | api3rdappid | varchar | 50 |  | √ | ' ' | api3rdappid |
| 22 | fexpiredtime | expiredtime | timestamp | 0 |  |  | LOCALTIMESTAMP | expiredtime |
| 23 | fclient | 客户端 | varchar | 10 |  | √ | ' ' | 客户端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_sessions |  | fid |
| 2 | index_t_bas_sessions_expire |  | fexpiredtime |
| 3 | index_t_bas_sessions_user |  | fuserid |
