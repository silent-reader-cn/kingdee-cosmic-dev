# 固定星期假期-public_holiday_fixedweek

## 固定星期假期-多语言表 t_int_publicholiday_l

- **表名称：** 固定星期假期-多语言表
- **表名：** t_int_publicholiday_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_int_publicholiday_l |  | fpkid |
| 2 | idx_int_publicholiday_l |  | fid,flocaleid |

---

## 固定星期假期-主表 t_int_publicholiday

- **表名称：** 固定星期假期-主表
- **表名：** t_int_publicholiday

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstartperiod | fstartperiod | int4 | 32 |  | √ | '-1' |  |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fdayofmonth | 日 | varchar | 50 |  | √ | ' ' | 日,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 31 :31 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 10 | fmonth | 月 | varchar | 50 |  | √ | ' ' | 月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 11 | fdayofweek | 星期几 | varchar | 50 |  | √ | ' ' | 星期几,枚举: 星期一 :星期一 星期二 :星期二 星期三 :星期三 星期四 :星期四 星期五 :星期五 星期六 :星期六 星期日 :星期日 |
| 12 | fextendrules | fextendrules | varchar | 255 |  | √ | ' ' |  |
| 13 | fendperiod | fendperiod | int4 | 32 |  | √ | '-1' |  |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftimeperiod | 工作时段 | int8 | 64 |  | √ | 0 | [工作时段 working_hours](../base_files/working_hours.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fcountryid | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 21 | fweekofmonth | 第几个 | varchar | 16 |  | √ | ' ' | 第几个,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 last :最后一个 |
| 22 | fholidayclass | 假期类型 | int8 | 64 |  | √ | 0 | [假期类型 int_holidayclass](../base_files/int_holidayclass.md) |
| 23 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :固定日期 2 :指定日期 3 :固定星期 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 26 | fholidaytype | 半天 | varchar | 10 |  | √ | 'all_day' | 半天 |
| 27 | fholiday | 假期日 | varchar | 255 |  | √ | ' ' | 假期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_int_publicholiday |  | fid |
| 2 | idx_int_holiday_number |  | fnumber |
| 3 | idx_int_holiday_type |  | ftype |
