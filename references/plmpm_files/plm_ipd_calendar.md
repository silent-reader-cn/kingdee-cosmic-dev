# 日历模版-plm_ipd_calendar

## 日历模版-使用范围表 t_plm_ipd_calendar_u

- **表名称：** 日历模版-使用范围表
- **表名：** t_plm_ipd_calendar_u

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
| 1 | pk_t_plm_ipd_calendar_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_ipd_calendar_u_uo |  | fuseorgid |

---

## 日历模版-多语言表 t_plm_ipd_calendar_l

- **表名称：** 日历模版-多语言表
- **表名：** t_plm_ipd_calendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_calendar_l |  | fpkid |
| 2 | idx_plm_ipd_calendar_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_plm_ipd_calendarentitys

- **表名称：** 单据体-子表
- **表名：** t_plm_ipd_calendarentitys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdatetype | 日期类型 | varchar | 50 |  | √ | ' ' | 日期类型,枚举: |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fworktime | 工作时间 | varchar | 50 |  | √ | ' ' | 工作时间,枚举: |
| 4 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fworkdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_calendarentitys |  | fentryid |
| 2 | idx_plm_ipd_calendarentitys_fk |  | fid |

---

## 日历模版-主表 t_plm_ipd_calendar

- **表名称：** 日历模版-主表
- **表名：** t_plm_ipd_calendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fweekdayamstart | 工作日上午.开始 | int4 | 32 |  | √ | '-1' | 工作日上午.开始 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ftextfield | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcalrangestart | 日历范围.开始 | timestamp | 0 |  |  | null | 日历范围.开始 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fcalrangeend | 日历范围.结束 | timestamp | 0 |  |  | null | 日历范围.结束 |
| 15 | fweekdaypmend | 工作日下午.结束 | int4 | 32 |  | √ | '-1' | 工作日下午.结束 |
| 16 | fweekdayamend | 工作日上午.结束 | int4 | 32 |  | √ | '-1' | 工作日上午.结束 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fcalendardsetid | 工作日历配置 | int8 | 64 |  | √ | 0 | 设置工作日历 plm_ipd_setcalendar |
| 23 | fweekdaypmstart | 工作日下午.开始 | int4 | 32 |  | √ | '-1' | 工作日下午.开始 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fisdefault | 默认日历 | bpchar | 1 |  | √ | '0' | 默认日历 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_calendar_m0 |  | fmasterid |
| 2 | idx_t_plm_ipd_calendar_master |  | fmasterid |
| 3 | idx_t_plm_ipd_calendar_createorg |  | fcreateorgid |
| 4 | pk_plm_ipd_calendar |  | fid |
