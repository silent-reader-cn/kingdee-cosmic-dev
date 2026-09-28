# 今日在线用户数-bos_smc_onlineuser_number

## 今日在线用户数-主表 t_bas_daily_onlinenumber

- **表名称：** 今日在线用户数-主表
- **表名：** t_bas_daily_onlinenumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时间 | int8 | 64 |  | √ | 0 | 时间 |
| 3 | ftextfield2 | 扩展字段2 | varchar | 50 |  | √ | ' ' | 扩展字段2 |
| 4 | fintegerfield | 整数扩展字段 | int8 | 64 |  | √ | 0 | 整数扩展字段 |
| 5 | fmodifierid | 修改人id | int8 | 64 |  | √ | 0 | 修改人id |
| 6 | ftextfield1 | 扩展字段1 | varchar | 50 |  | √ | ' ' | 扩展字段1 |
| 7 | fintegerfield2 | 整数扩展字段2 | int8 | 64 |  | √ | 0 | 整数扩展字段2 |
| 8 | fminute | 分钟 | int8 | 64 |  | √ | '-1' | 分钟 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 10 | ftextfield | 扩展字段 | varchar | 50 |  | √ | ' ' | 扩展字段 |
| 11 | fonlineusernum | 在线用户数 | int8 | 64 |  | √ | 0 | 在线用户数 |
| 12 | fdatetimefield2 | 长日期扩展字段3 | timestamp | 0 |  |  | null | 长日期扩展字段3 |
| 13 | fintegerfield1 | 整数扩展字段1 | int8 | 64 |  | √ | 0 | 整数扩展字段1 |
| 14 | fdatetimefield1 | 长日期扩展字段2 | timestamp | 0 |  |  | null | 长日期扩展字段2 |
| 15 | fdatetimefield | 长日期扩展字段1 | timestamp | 0 |  |  | null | 长日期扩展字段1 |
| 16 | fclient | 统计类型 | varchar | 50 |  | √ | ' ' | 统计类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_online_num_ftime_n |  | ftime |
| 2 | idx_bas_online_num_fminute_n |  | fminute |
| 3 | pk_bas_daily_onlinenumber |  | fid |
