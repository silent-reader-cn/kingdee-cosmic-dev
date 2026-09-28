# 日历有效期（后台）-pmbd_calendarexpr

## 工作时间单据体-子表 t_pmbd_worktimeexpr

- **表名称：** 工作时间单据体-子表
- **表名：** t_pmbd_worktimeexpr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkstarttime | 工作开始时间 | int4 | 32 |  | √ | 0 | 工作开始时间 |
| 3 | fhalfworkstarttime | 半工作开始时间 | int4 | 32 |  | √ | 0 | 半工作开始时间 |
| 4 | fworkfinshtime | 工作结束时间 | int4 | 32 |  | √ | 0 | 工作结束时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fhalfworkfinshtime | 半工作结束时间 | int4 | 32 |  | √ | 0 | 半工作结束时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_worktimeexpr |  | fentryid |
| 2 | idx_pmbd_workpr_fid |  | fid |
| 3 | idx_pmbd_workpr_fseq |  | fseq |

---

## 日历有效期（后台）-主表 t_pmbd_calendarexpr

- **表名称：** 日历有效期（后台）-主表
- **表名：** t_pmbd_calendarexpr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatetype | 工作日期类型 | varchar | 5 |  | √ | ' ' | 工作日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsettype | 设置方式 | varchar | 5 |  | √ | ' ' | 设置方式,枚举: sys :系统预制 hand :手工指定 |
| 5 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpjcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | 项目日历 |
| 11 | fworkdate | 工作日期 | timestamp | 0 |  |  | null | 工作日期 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_calendarexpr |  | fid |
| 2 | idx_pmbd_calepr_fbillno |  | fbillno |
| 3 | idx_pmbd_calepr_fcreatetime |  | fcreatetime |
