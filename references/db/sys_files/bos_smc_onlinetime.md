# 在线用户时长-bos_smc_onlinetime

## 在线用户时长-主表 t_bas_daily_logintime

- **表名称：** 在线用户时长-主表
- **表名：** t_bas_daily_logintime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fonlinetime | 时长 | numeric | 23 | 10 | √ | 0 | 时长 |
| 3 | ftextfield2 | 扩展字段2 | varchar | 50 |  | √ | ' ' | 扩展字段2 |
| 4 | fintegerfield | 整数扩展字段 | int8 | 64 |  | √ | 0 | 整数扩展字段 |
| 5 | fdatetype | 统计类型 | varchar | 50 |  | √ | ' ' | 统计类型 |
| 6 | ftextfield1 | 扩展字段1 | varchar | 50 |  | √ | ' ' | 扩展字段1 |
| 7 | fcompensatetime | 补偿时间 | int8 | 64 |  | √ | 0 | 补偿时间 |
| 8 | fintegerfield2 | 整数扩展字段2 | int8 | 64 |  | √ | 0 | 整数扩展字段2 |
| 9 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdatetime | 日期 | int8 | 64 |  | √ | '-1' | 日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 12 | ftextfield | 扩展字段 | varchar | 50 |  | √ | ' ' | 扩展字段 |
| 13 | fcalculationend | 结束计算时间 | varchar | 50 |  | √ | ' ' | 结束计算时间 |
| 14 | flogintimes | 登录次数 | int8 | 64 |  | √ | 0 | 登录次数 |
| 15 | fuserfield | fuserfield | int8 | 64 |  | √ | 0 |  |
| 16 | flastlogintime | 最近一次登录时间 | timestamp | 0 |  |  | null | 最近一次登录时间 |
| 17 | flastlogouttime | 最近一次登出时间 | timestamp | 0 |  |  | null | 最近一次登出时间 |
| 18 | fcalculationstart | 开始计算时间 | varchar | 50 |  | √ | ' ' | 开始计算时间 |
| 19 | fdatetimefield2 | 长日期扩展字段3 | timestamp | 0 |  |  | null | 长日期扩展字段3 |
| 20 | fintegerfield1 | 整数扩展字段1 | int8 | 64 |  | √ | 0 | 整数扩展字段1 |
| 21 | fdatetimefield1 | 长日期扩展字段2 | timestamp | 0 |  |  | null | 长日期扩展字段2 |
| 22 | fdatetimefield | 长日期扩展字段1 | timestamp | 0 |  |  | null | 长日期扩展字段1 |
| 23 | fislogout | 是否登出(全部登出) | bpchar | 1 |  | √ | '0' | 是否登出(全部登出) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_daily_logintime |  | fid |
| 2 | idx_logintime_fuserid_n |  | fuserid |
| 3 | idx_logintime_fdatetime_n |  | fdatetime |
