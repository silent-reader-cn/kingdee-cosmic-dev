# 用户国际化设置-inte_formatcfg

## 用户国际化设置-主表 t_int_formatcfg

- **表名称：** 用户国际化设置-主表
- **表名：** t_int_formatcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fiscustom | 是否自定义 | bpchar | 1 |  |  | '0' | 是否自定义 |
| 3 | fcurrsign | 币种符号 | varchar | 30 |  |  | ' ' | 币种符号,枚举: ¥ :¥ |
| 4 | ftimeformat | 时间格式 | varchar | 30 |  |  | null | 时间格式,枚举: H:mm :H:mm HH:mm :HH:mm a h:mm :a h:mm a hh:mm :a hh:mm H:mm:ss :H:mm:ss HH:mm:ss :HH:mm:ss a h:mm:ss :a h:mm:ss a hh:mm:ss :a hh:mm:ss |
| 5 | fzeroshow | 零起始位置 | varchar | 30 |  |  | null | 零起始位置,枚举: .7 :.7 0.7 :0.7 |
| 6 | fcnyshowprefix | 货币显示前缀 | bpchar | 1 |  | √ | '1' | 货币显示前缀,枚举: 1 :币种符号 2 :币种代码 3 :不显示前缀 |
| 7 | fcurrnegformat | 负数格式 | varchar | 30 |  |  | ' ' | 负数格式,枚举: (¥1.1) :(¥1.1) -¥1.1 :-¥1.1 ¥-1.1 :¥-1.1 ¥1.1- :¥1.1- (1.1¥) :(1.1¥) -1.1¥ :-1.1¥ 1.1¥- :1.1¥- -¥ 1.1 :-¥ 1.1 ¥ 1.1- :¥ 1.1- ¥ -1.1 :¥ -1.1 1.1-¥ :1.1-¥ (¥ 1.1) :(¥ 1.1) (1.1 ¥) :(1.1 ¥) |
| 8 | fuserid | 用户 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdemocurrency | 演示币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fnegativesign | 负号 | varchar | 1 |  |  | null | 负号,枚举: : - :- |
| 11 | fplanid | 格式方案 | int8 | 64 |  |  | null | [区域格式 inte_programme](../base_files/inte_programme.md) |
| 12 | fdateformat | 日期格式 | varchar | 30 |  |  | null | 日期格式,枚举: d/M/yyyy :d/M/yyyy d/MM/yyyy :d/MM/yyyy dd.MM.yyyy :dd.MM.yyyy dd/MM/yyyy :dd/MM/yyyy dd-MM-yyyy :dd-MM-yyyy M/d/yyyy :M/d/yyyy yyyy/M/d :yyyy/M/d yyyy/MM/dd :yyyy/MM/dd yyyy-M-d :yyyy-M-d |
| 13 | fnumgroupformat | 数字分组格式 | varchar | 30 |  |  | null | 数字分组格式,枚举: 123456789 :123456789 123,456,789 :123,456,789 123456,789 :123456,789 12,34,56,789 :12,34,56,789 |
| 14 | fpmsign | PM符号 | varchar | 30 |  |  | ' ' | PM符号,枚举: 下午 :下午 PM :PM CH :CH 午後 :午後 : : : : |
| 15 | fcurrposformat | 正数格式 | varchar | 30 |  |  | ' ' | 正数格式,枚举: ¥100 :¥100 100¥ :100¥ ¥ 100 :¥ 100 100 ¥ :100 ¥ |
| 16 | fnegativeformat | 负数格式 | varchar | 30 |  |  | null | 负数格式,枚举: (1.1) :(1.1) -1.1 :-1.1 - 1.1 :- 1.1 1.1- :1.1- 1.1 - :1.1 - |
| 17 | ftimezoneid | 时区 | int8 | 64 |  |  | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 18 | fdecimalpoint | 小数点 | varchar | 1 |  |  | null | 小数点,枚举: . :. |
| 19 | fnumseparator | 数字分组符号 | varchar | 1 |  |  | null | 数字分组符号,枚举: , :, . :. |
| 20 | famsign | AM符号 | varchar | 30 |  |  | ' ' | AM符号,枚举: 上午 :上午 AM :AM SA :SA 午前 :午前 : : : : |
| 21 | ffirstdayofweek | 一周的第一天 | varchar | 50 |  | √ | ' ' | 一周的第一天,枚举: 0 :星期日 1 :星期一 2 :星期二 3 :星期三 4 :星期四 5 :星期五 6 :星期六 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_formatcfg_user |  | fuserid |
| 2 | t_int_formatcfg_pkey |  | fid |
