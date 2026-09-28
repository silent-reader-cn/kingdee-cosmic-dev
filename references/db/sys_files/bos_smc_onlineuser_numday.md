# 每日在线用户数-bos_smc_onlineuser_numday

## 每日在线用户数-主表 t_bas_daily_loginnumber

- **表名称：** 每日在线用户数-主表
- **表名：** t_bas_daily_loginnumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintegerfield | 整数1 | int8 | 64 |  | √ | 0 | 整数1 |
| 3 | fdatetype | 时间类型 | varchar | 50 |  | √ | ' ' | 时间类型 |
| 4 | ftextfield1 | 文本1 | varchar | 50 |  | √ | ' ' | 文本1 |
| 5 | fintegerfield1 | 整数2 | int8 | 64 |  | √ | 0 | 整数2 |
| 6 | fdatetimefield1 | 长日期1 | timestamp | 0 |  |  | null | 长日期1 |
| 7 | fdatetime | 日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 日期 |
| 8 | fdecimalfield | 小数 | numeric | 23 | 10 | √ | 0 | 小数 |
| 9 | fdecimalfield1 | 小数1 | numeric | 23 | 10 | √ | 0 | 小数1 |
| 10 | fdatetimefield | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 11 | fonlinenumber | 在线用户数 | int8 | 64 |  | √ | 0 | 在线用户数 |
| 12 | ftextfield | 文本 | varchar | 50 |  | √ | ' ' | 文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_daily_loginnumber |  | fid |
| 2 | idx_bas_login_num_ftime_n |  | fdatetime |
