# 区域格式-inte_programme

## 区域格式-主表 t_int_formatplan

- **表名称：** 区域格式-主表
- **表名：** t_int_formatplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcurrsign | 币种符号 | varchar | 30 |  |  | ' ' | 币种符号,枚举: ¥ :¥ |
| 4 | ftimeformat | 时间格式 | varchar | 30 |  |  | null | 时间格式,枚举: H:mm :H:mm HH:mm :HH:mm a h:mm :a h:mm a hh:mm :a hh:mm H:mm:ss :H:mm:ss HH:mm:ss :HH:mm:ss a h:mm:ss :a h:mm:ss a hh:mm:ss :a hh:mm:ss hh:mm:ss a :hh:mm:ss a hh:mm a :hh:mm a |
| 5 | fzeroshow | 零起始位置 | varchar | 30 |  |  | null | 零起始位置,枚举: 0 :.7 1 :0.7 |
| 6 | fcnyshowprefix | 货币显示前缀 | bpchar | 1 |  | √ | '1' | 货币显示前缀,枚举: 1 :币种符号 2 :币种代码 3 :不显示前缀 |
| 7 | fcurrnegformat | 负数格式 | varchar | 30 |  |  | ' ' | 负数格式,枚举: (¥,) :(¥1.1) -¥, :-¥1.1 ¥-, :¥-1.1 ¥,- :¥1.1- (,¥) :(1.1¥) -,¥ :-1.1¥ ,¥- :1.1¥- -¥ , :-¥ 1.1 -, ¥ :-1.1 ¥ ¥ ,- :¥ 1.1- ¥ -, :¥ -1.1 ,-¥ :1.1-¥ (¥ ,) :(¥ 1.1) (, ¥) :(1.1 ¥) ,- ¥ :1,1- ￥ , ￥- :1,1 ￥- |
| 8 | fdemocurrency | 演示币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fnegativesign | fnegativesign | varchar | 1 |  |  | null |  |
| 11 | fdateformat | 日期格式 | varchar | 30 |  |  | null | 日期格式,枚举: d/M/yyyy :d/M/yyyy d/MM/yyyy :d/MM/yyyy dd.MM.yyyy :dd.MM.yyyy dd/MM/yyyy :dd/MM/yyyy dd-MM-yyyy :dd-MM-yyyy M/d/yyyy :M/d/yyyy yyyy/M/d :yyyy/M/d yyyy/MM/dd :yyyy/MM/dd yyyy-M-d :yyyy-M-d dd/MM/yy :dd/MM/yy yyyy-MM-dd :yyyy-MM-dd |
| 12 | fnumgroupformat | 数字分组格式 | varchar | 30 |  |  | null | 数字分组格式,枚举: 123456789 :123456789 1,2345,6789 :1,2345,6789 123,456,789 :123,456,789 123456,789 :123456,789 12,34,56,789 :12,34,56,789 |
| 13 | fpmsign | PM符号 | varchar | 30 |  |  | ' ' | PM符号,枚举: 下午 :下午 PM :PM CH :CH 午後 :午後 : : : : |
| 14 | fcurrposformat | 正数格式 | varchar | 30 |  |  | ' ' | 正数格式,枚举: ¥, :¥1.1 ,¥ :1.1¥ ¥ , :¥ 1.1 , ¥ :1.1 ¥ |
| 15 | fnegativeformat | 负数格式 | varchar | 30 |  |  | null | 负数格式,枚举: (,) :(1.1) -, :-1.1 - , :- 1.1 ,- :1.1- , - :1.1 - |
| 16 | fdecimalpoint | 小数点 | varchar | 1 |  |  | null | 小数点,枚举: . :. , :, |
| 17 | fnumseparator | 数字分组符号 | varchar | 1 |  |  | null | 数字分组符号,枚举: , :, . :. ' :' b :空格 |
| 18 | famsign | AM符号 | varchar | 30 |  |  | ' ' | AM符号,枚举: 上午 :上午 AM :AM SA :SA 午前 :午前 : : : : |
| 19 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 20 | fisdefault | 设为默认 | bpchar | 1 |  |  | null | 设为默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_int_formatplan_pkey |  | fid |
| 2 | idx_t_int_formatplan_number |  | fnumber |

---

## 区域格式-多语言表 t_int_formatplan_l

- **表名称：** 区域格式-多语言表
- **表名：** t_int_formatplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fname | 名称 | varchar | 255 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_formatplan_l_fid |  | fid,flocaleid |
| 2 | t_int_formatplan_l_pkey |  | fpkid |
