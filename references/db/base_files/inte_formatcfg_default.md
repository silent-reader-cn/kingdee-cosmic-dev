# 默认区域格式-inte_formatcfg_default

## 默认区域格式-主表 t_int_formatdefault

- **表名称：** 默认区域格式-主表
- **表名：** t_int_formatdefault

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fiscustom | 自定义 | bpchar | 1 |  | √ | ' ' | 自定义 |
| 4 | ftimeformat | 时间格式 | varchar | 32 |  | √ | ' ' | 时间格式,枚举: H:mm :H:mm HH:mm :HH:mm a h:mm :a h:mm a hh:mm :a hh:mm H:mm:ss :H:mm:ss HH:mm:ss :HH:mm:ss a h:mm:ss :a h:mm:ss a hh:mm:ss :a hh:mm:ss |
| 5 | fzeroshow | 零起始位置 | varchar | 32 |  | √ | ' ' | 零起始位置,枚举: 0 :.7 1 :0.7 |
| 6 | fcnyshowprefix | 货币显示前缀 | varchar | 1 |  | √ | ' ' | 货币显示前缀,枚举: 1 :币种符号 2 :币种代码 3 :不显示前缀 |
| 7 | fcurrnegformat | 负数格式 | varchar | 32 |  | √ | ' ' | 负数格式,枚举: (¥,) :(¥1.1) -¥, :-¥1.1 ¥-, :¥-1.1 ¥,- :¥1.1- (,¥) :(1.1¥) -,¥ :-1.1¥ ,¥- :1.1¥- -¥ , :-¥ 1.1 -, ¥ :-1.1 ¥ ¥ ,- :¥ 1.1- ¥ -, :¥ -1.1 ,-¥ :1.1-¥ (¥ ,) :(¥ 1.1) (, ¥) :(1.1 ¥) |
| 8 | fdemocurrency | 演示币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fnumformat | 数字格式 | varchar | 32 |  | √ | ' ' | 数字格式,枚举: |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdateformat | 日期格式 | varchar | 32 |  | √ | ' ' | 日期格式,枚举: d/M/yyyy :d/M/yyyy d/MM/yyyy :d/MM/yyyy dd.MM.yyyy :dd.MM.yyyy dd/MM/yyyy :dd/MM/yyyy dd-MM-yyyy :dd-MM-yyyy M/d/yyyy :M/d/yyyy yyyy/M/d :yyyy/M/d yyyy/MM/dd :yyyy/MM/dd yyyy-M-d :yyyy-M-d |
| 12 | fpmsign | PM符号 | varchar | 32 |  | √ | ' ' | PM符号,枚举: 下午 :下午 PM :PM CH :CH 午後 :午後 |
| 13 | fnumgroupformat | 数字分组格式 | varchar | 32 |  | √ | ' ' | 数字分组格式,枚举: 123456789 :123456789 1,2345,6789 :1,2345,6789 123,456,789 :123,456,789 |
| 14 | fplanid | 区域格式 | int8 | 64 |  | √ | 0 | [区域格式 inte_programme](../base_files/inte_programme.md) |
| 15 | fcurrposformat | 正数格式 | varchar | 32 |  | √ | ' ' | 正数格式,枚举: ¥, :¥1.1 ,¥ :1.1¥ ¥ , :¥ 1.1 , ¥ :1.1 ¥ |
| 16 | fnegativeformat | 负数格式 | varchar | 32 |  | √ | ' ' | 负数格式,枚举: (,) :(1.1) -, :-1.1 - , :- 1.1 ,- :1.1- , - :1.1 - |
| 17 | fdecimalpoint | 小数点 | varchar | 1 |  | √ | ' ' | 小数点,枚举: . :. , :, |
| 18 | ffirstdayofweek | 一周的第一天 | varchar | 32 |  | √ | ' ' | 一周的第一天,枚举: 1 :星期一 2 :星期二 3 :星期三 4 :星期四 5 :星期五 6 :星期六 0 :星期日 |
| 19 | famsign | AM符号 | varchar | 32 |  | √ | ' ' | AM符号,枚举: 上午 :上午 AM :AM SA :SA 午前 :午前 |
| 20 | fnumseparator | 数字分组符号 | varchar | 1 |  | √ | ' ' | 数字分组符号,枚举: , :, . :. ' :' b :空格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_formatdefault |  | fid |
| 2 | idx_t_inf_cfgdefault |  | fplanid |
