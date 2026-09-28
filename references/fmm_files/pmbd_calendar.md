# 项目日历-pmbd_calendar

## 项目日历-主表 t_pmbd_calendar

- **表名称：** 项目日历-主表
- **表名：** t_pmbd_calendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmondayradio | 周一工作类型 | varchar | 5 |  | √ | ' ' | 周一工作类型,枚举: |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fsundayradio | 周日工作类型 | varchar | 5 |  | √ | ' ' | 周日工作类型,枚举: 1 :半天工作日 3 :固定休息日 |
| 13 | ffridayradio | 周五工作类型 | varchar | 5 |  | √ | ' ' | 周五工作类型,枚举: 1 :半天工作日 2 :全天工作日 3 :固定休息日 |
| 14 | fhourday | 小时/天 | numeric | 23 | 10 | √ | 0 | 小时/天 |
| 15 | fexpirstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 16 | fhourmonth | 小时/月 | numeric | 23 | 10 | √ | 0 | 小时/月 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fname | 项目日历名称 | varchar | 50 |  | √ | ' ' | 项目日历名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ftuesdayradio | 周二工作类型 | varchar | 5 |  | √ | ' ' | 周二工作类型,枚举: 1 :半天工作日 2 :全天工作日 3 :固定休息日 |
| 22 | fhourweekend | 小时/周 | numeric | 23 | 10 | √ | 0 | 小时/周 |
| 23 | fsaturdayradio | 周六工作类型 | varchar | 5 |  | √ | ' ' | 周六工作类型,枚举: 1 :半天工作日 3 :固定休息日 |
| 24 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fexpirendate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 26 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 项目日历编码 | varchar | 30 |  | √ | ' ' | 项目日历编码 |
| 28 | fisdefalt | 默认日历 | bpchar | 1 |  | √ | '0' | 默认日历 |
| 29 | fthursdayradio | 周四工作类型 | varchar | 5 |  | √ | ' ' | 周四工作类型,枚举: 1 :半天工作日 2 :全天工作日 3 :固定休息日 |
| 30 | fwednesdayradio | 周三工作类型 | varchar | 5 |  | √ | ' ' | 周三工作类型,枚举: 1 :半天工作日 2 :全天工作日 3 :固定休息日 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fhouryear | 小时/年 | numeric | 23 | 10 | √ | 0 | 小时/年 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_calendar |  | fid |
| 2 | idx_t_pmbd_calendar_createorg |  | fcreateorgid |
| 3 | idx_pmbd_calear_fnumber |  | fnumber |
| 4 | idx_t_pmbd_calendar_master |  | fmasterid |
| 5 | idx_pmbd_calear_fcreatetime |  | fcreatetime |

---

## 项目日历-使用范围表 t_pmbd_calendar_u

- **表名称：** 项目日历-使用范围表
- **表名：** t_pmbd_calendar_u

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
| 1 | pk_t_pmbd_calendar_u |  | fdataid,fuseorgid |
| 2 | idx_t_pmbd_calendar_u_uo |  | fuseorgid |

---

## 项目日历-使用范围位图表 t_pmbd_calendar_m

- **表名称：** 项目日历-使用范围位图表
- **表名：** t_pmbd_calendar_m

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
| 1 | pk_t_pmbd_calendar_m |  | forgid |

---

## 项目日历-多语言表 t_pmbd_calendar_l

- **表名称：** 项目日历-多语言表
- **表名：** t_pmbd_calendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目日历名称 | varchar | 50 |  | √ | ' ' | 项目日历名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_calearl_fname |  | fname |
| 2 | pk_pmbd_calendar_l |  | fpkid |
| 3 | idx_pmbd_calearl_fid |  | fid,flocaleid |

---

## 工作日单据体-子表 t_pmbd_worktime

- **表名称：** 工作日单据体-子表
- **表名：** t_pmbd_worktime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkstarttime | 开始时间 | int4 | 32 |  | √ | 0 | 开始时间 |
| 3 | fworkfinshtime | 结束时间 | int4 | 32 |  | √ | 0 | 结束时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_workme_fseq |  | fseq |
| 2 | pk_pmbd_worktime |  | fentryid |
| 3 | idx_pmbd_workme_fid |  | fid |

---

## 半工作日单据体-子表 t_pmbd_halfworktime

- **表名称：** 半工作日单据体-子表
- **表名：** t_pmbd_halfworktime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhalfworkstarttime | 开始时间 | int4 | 32 |  | √ | 0 | 开始时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fhalfworkfinshtime | 结束时间 | int4 | 32 |  | √ | 0 | 结束时间 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_halfme_fid |  | fid |
| 2 | pk_pmbd_halfworktime |  | fentryid |
| 3 | idx_pmbd_halfme_fseq |  | fseq |
