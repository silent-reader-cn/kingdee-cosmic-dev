# 设置工作日历-bd_workcalendar

## 设置工作日历-多语言表 t_bd_workcalendar_l

- **表名称：** 设置工作日历-多语言表
- **表名：** t_bd_workcalendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_workcalendar_l_pkey |  | fpkid |
| 2 | idx_workcalendar_l_id |  | fid,flocaleid |

---

## 设置工作日历-主表 t_bd_workcalendar

- **表名称：** 设置工作日历-主表
- **表名：** t_bd_workcalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fiswedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fendworkdate | fendworkdate | timestamp | 0 |  |  | null |  |
| 7 | fholidaycolor | fholidaycolor | varchar | 50 |  | √ | ' ' |  |
| 8 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 9 | fishalfthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 10 | fhourofendtimeam | 工作日上午结束-时 | int8 | 64 |  | √ | 0 | 工作日上午结束-时 |
| 11 | fhourofbegintimeam | 工作日上午开始-时 | int8 | 64 |  | √ | 0 | 工作日上午开始-时 |
| 12 | fhourofhalfworkdate | fhourofhalfworkdate | int8 | 64 |  | √ | 0 |  |
| 13 | fisthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 14 | fworkdaycolor | fworkdaycolor | varchar | 50 |  | √ | ' ' |  |
| 15 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 16 | fissatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 17 | fishalffrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fexpiringmonthto | 结束月 | varchar | 30 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 21 | fissunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 22 | fexpiringyearto | 结束年 | varchar | 30 |  | √ | ' ' | 结束年,枚举: |
| 23 | fminofendtimeam | 工作日上午结束-分 | int8 | 64 |  | √ | 0 | 工作日上午结束-分 |
| 24 | fhalfworkdaycolor | fhalfworkdaycolor | varchar | 50 |  | √ | ' ' |  |
| 25 | fstartworkdate | fstartworkdate | timestamp | 0 |  |  | null |  |
| 26 | fishalfmonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 27 | fminofbegintimeam | 工作日上午开始-分 | int8 | 64 |  | √ | 0 | 工作日上午开始-分 |
| 28 | fishalftuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 29 | fishalfsatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 30 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fisforshare | fisforshare | bpchar | 1 |  | √ | ' ' |  |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 34 | fishalfwedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 35 | fhourofendtimepm | 工作日下午结束-时 | int8 | 64 |  | √ | 0 | 工作日下午结束-时 |
| 36 | fisfrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 37 | fismonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 38 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fminofbegintimepm | 工作日下午开始-分 | int8 | 64 |  | √ | 0 | 工作日下午开始-分 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fweekendcolor | fweekendcolor | varchar | 50 |  | √ | ' ' |  |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fisindividuation | 个性化标志 | bpchar | 1 |  | √ | ' ' | 个性化标志 |
| 44 | fishalfsunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 45 | fistuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 46 | fexpiringyearfrom | 有效期间 | varchar | 30 |  | √ | ' ' | 有效期间,枚举: |
| 47 | fhourofworkdate | fhourofworkdate | int8 | 64 |  | √ | 0 |  |
| 48 | fminofendtimepm | 工作日下午结束-分 | int8 | 64 |  | √ | 0 | 工作日下午结束-分 |
| 49 | fexpiringmonthfrom | 开始月 | varchar | 30 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 50 | fhourofbegintimepm | 工作日下午开始-时 | int8 | 64 |  | √ | 0 | 工作日下午开始-时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_workcalendar_pkey |  | fid |
| 2 | idx_workcalendar_org |  | forgid |
| 3 | idx_workcalendar_number |  | fnumber |

---

## 单据体-子表 t_bd_workcalendarentry

- **表名称：** 单据体-子表
- **表名：** t_bd_workcalendarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | varchar | 10 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fworkdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fweekseq | fweekseq | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_workcalendarentry_pkey |  | fentryid |
| 2 | idx_workcalendarentry_fid |  | fid |
| 3 | idx_workcalendarentry_date |  | fworkdate |
