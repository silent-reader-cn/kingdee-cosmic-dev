# 设置项目日历-plm_ipd_prosetcal

## 节假日-子表 t_plm_ipd_holidayentry

- **表名称：** 节假日-子表
- **表名：** t_plm_ipd_holidayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdaterangebegin | 循环日期范围.开始 | timestamp | 0 |  |  | null | 循环日期范围.开始 |
| 3 | fsettype | 设置方式 | int8 | 64 |  | √ | 0 | 设置方式 |
| 4 | fdaterangeend | 循环日期范围.结束 | timestamp | 0 |  |  | null | 循环日期范围.结束 |
| 5 | fholidayname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcyclelength | 循环步长 | int8 | 64 |  | √ | 0 | 循环步长 |
| 8 | fholidaydesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 9 | fholidaydateend | 法定节假日期.结束 | timestamp | 0 |  |  | null | 法定节假日期.结束 |
| 10 | fholidayyear | 年份 | int8 | 64 |  | √ | 0 | 年份 |
| 11 | fcycletype | 循环方式 | varchar | 50 |  | √ | ' ' | 循环方式,枚举: 1 :按天 2 :按周 |
| 12 | fholidaydatebegin | 法定节假日期.开始 | timestamp | 0 |  |  | null | 法定节假日期.开始 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_holidayentry |  | fentryid |
| 2 | idx_plm_ipd_holidayentry_fk |  | fid |

---

## 例外日期-子表 t_plm_ipd_exceentry

- **表名称：** 例外日期-子表
- **表名：** t_plm_ipd_exceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcedateend | 日期.结束 | timestamp | 0 |  |  | null | 日期.结束 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fexcedatetype | 日期类型 | varchar | 50 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半工作日 3 :节假日 4 :休息日 |
| 5 | fexcedatestart | 日期.开始 | timestamp | 0 |  |  | null | 日期.开始 |
| 6 | fexcedatedesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexceworktime | 工作时间 | varchar | 50 |  | √ | ' ' | 工作时间,枚举: 1 :上午 2 :下午 3 :整天 4 : |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_exceentry |  | fentryid |
| 2 | idx_plm_ipd_exceentry_fk |  | fid |

---

## 设置项目日历-主表 t_plm_ipd_prosetcal

- **表名称：** 设置项目日历-主表
- **表名：** t_plm_ipd_prosetcal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffriday | 周五 | bpchar | 1 |  | √ | '1' | 周五 |
| 3 | weekdayamstart | 工作日上午.开始 | int4 | 32 |  | √ | '-1' | 工作日上午.开始 |
| 4 | fsaturdayam | 上午 | bpchar | 1 |  | √ | '0' | 上午 |
| 5 | ftuesday | 周二 | bpchar | 1 |  | √ | '1' | 周二 |
| 6 | fwednesdayam | 上午 | bpchar | 1 |  | √ | '1' | 上午 |
| 7 | ftuesdaypm | 下午 | bpchar | 1 |  | √ | '1' | 下午 |
| 8 | fweeksizeenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 9 | fprojectcalendarld | 项目日历 | int8 | 64 |  | √ | 0 | [配置-项目日历 plm_ipd_projectcal](../plmpm_files/plm_ipd_projectcal.md) |
| 10 | fcaltempleteld | 日历模版 | int8 | 64 |  | √ | 0 | [日历模板 plm_ipd_calendar](../plmpm_files/plm_ipd_calendar.md) |
| 11 | fsaturdaypm | 下午 | bpchar | 1 |  | √ | '0' | 下午 |
| 12 | fweekdaypmend | 工作日下午.结束 | int4 | 32 |  | √ | '-1' | 工作日下午.结束 |
| 13 | ffridaypm | 下午 | bpchar | 1 |  | √ | '1' | 下午 |
| 14 | fsaturday | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 15 | fweekdayamend | 工作日上午.结束 | int4 | 32 |  | √ | '-1' | 工作日上午.结束 |
| 16 | fwednesdaypm | 下午 | bpchar | 1 |  | √ | '1' | 下午 |
| 17 | fwednesday | 周三 | bpchar | 1 |  | √ | '1' | 周三 |
| 18 | fthursdayam | 上午 | bpchar | 1 |  | √ | '1' | 上午 |
| 19 | ftuesdayam | 上午 | bpchar | 1 |  | √ | '1' | 上午 |
| 20 | fweeksizestartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 21 | fsundayam | 上午 | bpchar | 1 |  | √ | '0' | 上午 |
| 22 | fsunday | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 23 | fmondaypm | 下午 | bpchar | 1 |  | √ | '1' | 下午 |
| 24 | ffridayam | 上午 | bpchar | 1 |  | √ | '1' | 上午 |
| 25 | fthursdaypm | 下午 | bpchar | 1 |  | √ | '1' | 下午 |
| 26 | fweekdaypmstart | 工作日下午.开始 | int4 | 32 |  | √ | '-1' | 工作日下午.开始 |
| 27 | fthursday | 周四 | bpchar | 1 |  | √ | '1' | 周四 |
| 28 | fweeksizesetcheckld | 启用大小周 | bpchar | 1 |  | √ | '0' | 启用大小周 |
| 29 | fsundaypm | 下午 | bpchar | 1 |  | √ | '0' | 下午 |
| 30 | fmonday | 周一 | bpchar | 1 |  | √ | '1' | 周一 |
| 31 | fmondayam | 上午 | bpchar | 1 |  | √ | '1' | 上午 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_prosetcal_m0 |  | fprojectcalendarld |
| 2 | pk_plm_ipd_prosetcal |  | fid |
