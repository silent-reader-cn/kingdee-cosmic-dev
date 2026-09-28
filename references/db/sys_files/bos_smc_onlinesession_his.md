# 在线用户明细-bos_smc_onlinesession_his

## 在线用户明细-主表 t_bas_session_history

- **表名称：** 在线用户明细-主表
- **表名：** t_bas_session_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompensatetime | 补偿时间 | numeric | 23 | 10 | √ | 0 | 补偿时间 |
| 3 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 4 | flogintime | 登录时间 | timestamp | 0 |  |  | null | 登录时间 |
| 5 | fiscalculation | 是否参与在线时长计算 | bpchar | 1 |  | √ | '0' | 是否参与在线时长计算 |
| 6 | fdatetime | 所属日期 | int8 | 64 |  | √ | 0 | 所属日期 |
| 7 | fyzjappid | 云之家appid | varchar | 50 |  | √ | ' ' | 云之家appid |
| 8 | flogouttime | 登出时间 | timestamp | 0 |  |  | null | 登出时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 10 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 11 | floginorg | 登录组织 | int8 | 64 |  | √ | 0 | 登录组织 |
| 12 | fuseropenid | useropenid | varchar | 50 |  | √ | ' ' | useropenid |
| 13 | fapi3rdappnum | api3rdappnum | varchar | 50 |  | √ | ' ' | api3rdappnum |
| 14 | fusertype | 用户类型 | varchar | 120 |  | √ | ' ' | 用户类型 |
| 15 | fapi3rdappid | api3rdappid | varchar | 50 |  | √ | ' ' | api3rdappid |
| 16 | fexpiredtime | expiredtime | timestamp | 0 |  |  | null | expiredtime |
| 17 | fmodifierid | 修改人id | int8 | 64 |  | √ | 0 | 修改人id |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 19 | flanguage | 语言 | varchar | 50 |  | √ | ' ' | 语言 |
| 20 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 21 | fbizpartnerid | bizpartnerid | int8 | 64 |  | √ | 0 | bizpartnerid |
| 22 | fkdcsrftoken | kdcsrftoken | varchar | 255 |  | √ | ' ' | kdcsrftoken |
| 23 | fyzjappticket | 云之家appticket | varchar | 200 |  | √ | ' ' | 云之家appticket |
| 24 | floginip | 登录ip | varchar | 512 |  | √ | ' ' | 登录ip |
| 25 | fsessionid | sessionid | varchar | 250 |  | √ | ' ' | sessionid |
| 26 | facccompanyid | acccompanyid | varchar | 50 |  | √ | ' ' | acccompanyid |
| 27 | fclient | 客户端 | varchar | 10 |  | √ | ' ' | 客户端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sessihis_fexpiredtime_n |  | flogouttime |
| 2 | pk_bas_session_history |  | fid |
| 3 | idx_sessionhis_fdatetime_n |  | fdatetime |
| 4 | idx_sessionhis_fsessionid_n |  | fsessionid |
| 5 | idx_sessionhis_fuserid_n |  | fuserid |
