# 项目日历-mpm_calendar

## 单据体-子表 t_mpm_calendarentry

- **表名称：** 单据体-子表
- **表名：** t_mpm_calendarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | bpchar | 1 |  | √ | ' ' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fworkdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_calendarentry |  | fentryid |
| 2 | idx_mpm_calendaredate |  | fworkdate |
| 3 | idx_mpm_calendarentry |  | fid,fseq |

---

## 项目日历-使用范围表 t_mpm_calendar_u

- **表名称：** 项目日历-使用范围表
- **表名：** t_mpm_calendar_u

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
| 1 | pk_t_mpm_calendar_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpm_calendar_u_uo |  | fuseorgid |

---

## 项目日历-主表 t_mpm_calendar

- **表名称：** 项目日历-主表
- **表名：** t_mpm_calendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | '1' | 周日 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fiswedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fexpirenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 13 | fisfrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 14 | fexpirstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fismonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fisthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 21 | fissatrest | 周六 | bpchar | 1 |  | √ | '1' | 周六 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fexpirendtime | 时间范围.结束 | int4 | 32 |  | √ | 0 | 时间范围.结束 |
| 24 | fistuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fexpirstarttime | 时间范围.开始 | int4 | 32 |  | √ | 0 | 时间范围.开始 |
| 27 | fnumber | 日历编码 | varchar | 80 |  | √ | ' ' | 日历编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fisdefault | 默认日历 | bpchar | 1 |  | √ | '0' | 默认日历 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpm_calendar_master |  | fmasterid |
| 2 | pk_mpm_calendar |  | fid |
| 3 | idx_t_mpm_calendar_createorg |  | fcreateorgid |
| 4 | idx_mpm_calendar_fnumber |  | fnumber,fcreateorgid |

---

## 项目日历-多语言表 t_mpm_calendar_l

- **表名称：** 项目日历-多语言表
- **表名：** t_mpm_calendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 日历名称 | varchar | 255 |  | √ | ' ' | 日历名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_calendar_l |  | fpkid |
| 2 | idx_mpm_calendar_l |  | fid,flocaleid |
