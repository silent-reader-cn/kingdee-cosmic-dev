# 在线用户峰值-bos_smc_onlineuser_max

## 在线用户峰值-主表 t_bas_daily_onlinemax

- **表名称：** 在线用户峰值-主表
- **表名：** t_bas_daily_onlinemax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时间 | int8 | 64 |  | √ | 0 | 时间 |
| 3 | ftextfield2 | 扩展字段2 | varchar | 50 |  | √ | ' ' | 扩展字段2 |
| 4 | fintegerfield | 整数扩展字段 | int8 | 64 |  | √ | 0 | 整数扩展字段 |
| 5 | ftextfield1 | 扩展字段1 | varchar | 50 |  | √ | ' ' | 扩展字段1 |
| 6 | fintegerfield2 | 整数扩展字段2 | int8 | 64 |  | √ | 0 | 整数扩展字段2 |
| 7 | fminute | 分钟 | int8 | 64 |  | √ | 0 | 分钟 |
| 8 | ftextfield | 扩展字段 | varchar | 50 |  | √ | ' ' | 扩展字段 |
| 9 | fonlineusernum | 在线用户数 | int8 | 64 |  | √ | 0 | 在线用户数 |
| 10 | fdatetimefield2 | 长日期扩展字段3 | timestamp | 0 |  |  | null | 长日期扩展字段3 |
| 11 | fintegerfield1 | 整数扩展字段1 | int8 | 64 |  | √ | 0 | 整数扩展字段1 |
| 12 | fdatetimefield1 | 长日期扩展字段2 | timestamp | 0 |  |  | null | 长日期扩展字段2 |
| 13 | fdatetimefield | 长日期扩展字段1 | timestamp | 0 |  |  | null | 长日期扩展字段1 |
| 14 | fclient | 统计类型 | varchar | 50 |  | √ | ' ' | 统计类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_onlinemax_ftime |  | ftime |
| 2 | pk_bas_daily_onlinemax |  | fid |
| 3 | idx_onlinemax_fminute |  | fminute |
