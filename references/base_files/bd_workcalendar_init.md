# 维护历史日历-bd_workcalendar_init

## 维护历史日历-主表 t_bd_workcalendar_init

- **表名称：** 维护历史日历-主表
- **表名：** t_bd_workcalendar_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 3 | fexpiringyearto | 结束年 | varchar | 64 |  | √ | ' ' | 结束年,枚举: |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fminofendtimeam | 工作日上午结束-分 | int8 | 64 |  | √ | 0 | 工作日上午结束-分 |
| 6 | fiswedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 7 | fishalfmonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 8 | fminofbegintimeam | 工作日上午开始-分 | int8 | 64 |  | √ | 0 | 工作日上午开始-分 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fishalftuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 11 | fishalfsatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 12 | fstatus | 数据状态 | varchar | 64 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fishalfwedrest | 周三 | bpchar | 1 |  | √ | ' ' | 周三 |
| 16 | fhourofendtimepm | 工作日下午结束-时 | int8 | 64 |  | √ | 0 | 工作日下午结束-时 |
| 17 | fisfrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 18 | fishalfthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 19 | fismonrest | 周一 | bpchar | 1 |  | √ | ' ' | 周一 |
| 20 | fhourofendtimeam | 工作日上午结束-时 | int8 | 64 |  | √ | 0 | 工作日上午结束-时 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fminofbegintimepm | 工作日下午开始-分 | int8 | 64 |  | √ | 0 | 工作日下午开始-分 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fisindividuation | 个性化标志 | int4 | 32 |  | √ | 0 | 个性化标志 |
| 27 | fhourofbegintimeam | 工作日上午开始-时 | int8 | 64 |  | √ | 0 | 工作日上午开始-时 |
| 28 | fisthurest | 周四 | bpchar | 1 |  | √ | ' ' | 周四 |
| 29 | fissatrest | 周六 | bpchar | 1 |  | √ | ' ' | 周六 |
| 30 | fishalfsunrest | 周日 | bpchar | 1 |  | √ | ' ' | 周日 |
| 31 | fistuerest | 周二 | bpchar | 1 |  | √ | ' ' | 周二 |
| 32 | fexpiringyearfrom | 有效期间 | varchar | 64 |  | √ | ' ' | 有效期间,枚举: |
| 33 | fishalffrirest | 周五 | bpchar | 1 |  | √ | ' ' | 周五 |
| 34 | fminofendtimepm | 工作日下午结束-分 | int8 | 64 |  | √ | 0 | 工作日下午结束-分 |
| 35 | fexpiringmonthfrom | 开始月 | varchar | 64 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 36 | fenable | 使用状态 | varchar | 64 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 编码 | varchar | 32 |  | √ | ' ' | 编码 |
| 38 | fexpiringmonthto | 结束月 | varchar | 64 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 39 | fhourofbegintimepm | 工作日下午开始-时 | int8 | 64 |  | √ | 0 | 工作日下午开始-时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_workcal_init |  | fnumber |
| 2 | pk_t_bd_workcalendar_init |  | fid |

---

## 例外日期-子表 t_bd_exceptiondate

- **表名称：** 例外日期-子表
- **表名：** t_bd_exceptiondate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | varchar | 64 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fenddate | 日期.结束 | timestamp | 0 |  |  | null | 日期.结束 |
| 4 | fstartdate | 日期.开始 | timestamp | 0 |  |  | null | 日期.开始 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_excdate |  | fid |
| 2 | pk_t_bd_exceptiondate |  | fentryid |

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

---

## 维护历史日历-多语言表 t_bd_workcalendar_init_l

- **表名称：** 维护历史日历-多语言表
- **表名：** t_bd_workcalendar_init_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_workcalendar_init_l |  | fpkid |
| 2 | pk_t_bd_workcal_init_l |  | fid |
