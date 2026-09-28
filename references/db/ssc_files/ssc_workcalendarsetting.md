# 设置工作日历_共享中心-ssc_workcalendarsetting

## 时间段分录-子表 t_tk_workcalendartimentry

- **表名称：** 时间段分录-子表
- **表名：** t_tk_workcalendartimentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbegintimeam | 上午开始时间 | varchar | 30 |  | √ | ' ' | 上午开始时间 |
| 2 | fbegintimepm | 下午开始时间 | varchar | 30 |  | √ | ' ' | 下午开始时间 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | ftimetype | 时间段类型 | bpchar | 1 |  | √ | ' ' | 时间段类型,枚举: 1 :工作 2 :请假 3 :加班 |
| 7 | fendtimeam | 上午结束时间 | varchar | 30 |  | √ | ' ' | 上午结束时间 |
| 8 | fendtimepm | 下午结束时间 | varchar | 30 |  | √ | ' ' | 下午结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_workcalendartimentry_pkey |  | fdetailid |
| 2 | idx_ssc_workcalentime_ftp |  | ftimetype |
| 3 | idx_ssc_workcalentime_entryid |  | fentryid |

---

## 设置工作日历_共享中心-多语言表 t_tk_workcalendar_l

- **表名称：** 设置工作日历_共享中心-多语言表
- **表名：** t_tk_workcalendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_workcalen_l_fid |  | fid,flocaleid |
| 2 | t_tk_workcalendar_l_pkey |  | fpkid |

---

## 设置工作日历_共享中心-主表 t_tk_workcalendar

- **表名称：** 设置工作日历_共享中心-主表
- **表名：** t_tk_workcalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fishalfsunrestam | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 3 | fissunrest | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 4 | fexpiringyearto | 结束年 | varchar | 30 |  | √ | ' ' | 结束年,枚举: |
| 5 | fminofendtimeam | 结束分 | varchar | 30 |  | √ | ' ' | 结束分,枚举: |
| 6 | fishalffrirestpm | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 7 | fiswedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 8 | fminofbegintimeam | 开始分 | varchar | 30 |  | √ | ' ' | 开始分,枚举: |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fishalfsunrestpm | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 14 | fishalfthurestam | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 15 | fhourofendtimepm | 结束时 | varchar | 30 |  | √ | ' ' | 结束时,枚举: |
| 16 | fishalfwedrestam | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 17 | fisfrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 18 | fexpiringdayfrom | 开始日 | varchar | 30 |  | √ | ' ' | 开始日,枚举: |
| 19 | fismonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 20 | fhourofendtimeam | 结束时 | varchar | 30 |  | √ | ' ' | 结束时,枚举: |
| 21 | fminofbegintimepm | 开始分 | varchar | 30 |  | √ | ' ' | 开始分,枚举: |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fishalfmonrestam | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 24 | fexpiringdayto | 结束日 | varchar | 30 |  | √ | ' ' | 结束日,枚举: |
| 25 | fishalfsatrestpm | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 26 | fishalftuerestpm | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fishalfthurestpm | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 29 | fssccenterid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fhourofbegintimeam | 上午 | varchar | 30 |  | √ | ' ' | 上午,枚举: |
| 31 | fisthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 32 | fissatrest | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 33 | fishalfwedrestpm | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 34 | fistuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 35 | fishalfmonrestpm | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 36 | fexpiringyearfrom | 有效期间 | varchar | 30 |  | √ | ' ' | 有效期间,枚举: 2020 :2020 2019 :2019 |
| 37 | fishalfsatrestam | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 38 | fminofendtimepm | 结束分 | varchar | 30 |  | √ | ' ' | 结束分,枚举: |
| 39 | fishalftuerestam | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 40 | fishalffrirestam | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 41 | fexpiringmonthfrom | 开始月 | varchar | 30 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 42 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 43 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 44 | fhourofbegintimepm | 下午 | varchar | 30 |  | √ | ' ' | 下午,枚举: |
| 45 | fexpiringmonthto | 结束月 | varchar | 30 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_workcalendar_pkey |  | fid |
| 2 | idx_ssc_workcalen_fsscid |  | fssccenterid |
| 3 | idx_ssc_workcalen_fnumber |  | fnumber |

---

## 工作日历分录-子表 t_tk_workcalendarentry

- **表名称：** 工作日历分录-子表
- **表名：** t_tk_workcalendarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | bpchar | 1 |  | √ | '0' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 5 :半工作日上午 6 :半工作日下午 |
| 3 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flevel | 层级 | varchar | 1 |  | √ | ' ' | 层级,枚举: 1 :共享中心 2 :用户组 3 :员工 |
| 5 | fusergroupid | 用户组 | int8 | 64 |  | √ | 0 | [用户组 task_usergroup](../ssc_files/task_usergroup.md) |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fuserid | 员工 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_workcalenrentry_fid |  | fid |
| 2 | t_tk_workcalendarentry_pkey |  | fentryid |
| 3 | idx_ssc_workcalenentry_fug |  | fusergroupid |
| 4 | idx_ssc_workcalenentry_fsscid |  | fsscid |
| 5 | idx_ssc_workcalenentry_fdate |  | fdate |
