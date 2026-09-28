# 生产日历-mpdm_calendar

## 单据体-子表 t_mpdm_calendarentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_calendarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | varchar | 30 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fworkdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_calendarentry |  | fid,fseq |
| 2 | t_mpdm_calendarentry_pkey |  | fentryid |
| 3 | idx_calendare_wkdate |  | fworkdate |

---

## 生产日历-使用范围表 t_mpdm_calendar_u

- **表名称：** 生产日历-使用范围表
- **表名：** t_mpdm_calendar_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_calendar_u_uo |  | fuseorgid |
| 2 | t_mpdm_calendar_u_pkey |  | fdataid,fuseorgid |

---

## 生产日历-多语言表 t_mpdm_calendar_l

- **表名称：** 生产日历-多语言表
- **表名：** t_mpdm_calendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 日历名称 | varchar | 100 |  | √ | ' ' | 日历名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_calendar_l |  | fid,flocaleid |
| 2 | t_mpdm_calendar_l_pkey |  | fpkid |

---

## 生产日历-使用范围位图表 t_mpdm_calendar_m

- **表名称：** 生产日历-使用范围位图表
- **表名：** t_mpdm_calendar_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_calendar_m |  | forgid |

---

## 生产日历-主表 t_mpdm_calendar

- **表名称：** 生产日历-主表
- **表名：** t_mpdm_calendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | '1' | 周日 |
| 3 | fexpiringyearto | 结束年 | varchar | 30 |  | √ | ' ' | 结束年,枚举: |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fiswedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fishalfmonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fishalftuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 11 | fishalfsatrest | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fishalfwedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fisfrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 19 | fishalfthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fuserorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fismonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fisindividuation | 个性化标志 | int8 | 64 |  | √ | 0 | 个性化标志 |
| 26 | fisthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 27 | fisrsyncplancalendar | 同步计划日历 | bpchar | 1 |  | √ | ' ' | 同步计划日历 |
| 28 | fissatrest | 周六 | bpchar | 1 |  | √ | '1' | 周六 |
| 29 | fishalfsunrest | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 30 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fistuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 32 | fexpiringyearfrom | 开始年 | varchar | 30 |  | √ | ' ' | 开始年,枚举: |
| 33 | fishalffrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 34 | fexpiringmonthfrom | 开始月 | varchar | 30 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 35 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 日历编码 | varchar | 60 |  | √ | ' ' | 日历编码 |
| 37 | fexpiringmonthto | 结束月 | varchar | 30 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 38 | fisdefalt | 默认日历 | bpchar | 1 |  | √ | '0' | 默认日历 |
| 39 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_calendar_pkey |  | fid |
| 2 | idx_mpdm_calendar_fnumber |  | fnumber,fcreateorgid |
| 3 | idx_t_mpdm_calendar_createorg |  | fcreateorgid |
| 4 | idx_t_mpdm_calendar_master |  | fmasterid |
