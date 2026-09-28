# 计划日历-mrp_plancalendar

## 计划日历-主表 t_mrp_plancalendar

- **表名称：** 计划日历-主表
- **表名：** t_mrp_plancalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | '1' | 周日 |
| 3 | fexpiringyearto | 结束年 | varchar | 30 |  | √ | ' ' | 结束年,枚举: |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fiswedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 6 | fishalfmonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fishalftuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 9 | fishalfsatrest | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fmpdmcalendarid | 生产日历 | int8 | 64 |  | √ | 0 | [生产日历 mpdm_calendar](../mpdm_files/mpdm_calendar.md) |
| 14 | fishalfwedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 15 | fisfrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 16 | fishalfthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fismonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fisthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 22 | fissatrest | 周六 | bpchar | 1 |  | √ | '1' | 周六 |
| 23 | fishalfsunrest | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 24 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 25 | fistuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 26 | fexpiringyearfrom | 有效期间 | varchar | 30 |  | √ | ' ' | 有效期间,枚举: |
| 27 | fishalffrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 28 | fexpiringmonthfrom | 开始月 | varchar | 30 |  | √ | ' ' | 开始月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 29 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 日历编码 | varchar | 60 |  | √ | ' ' | 日历编码 |
| 31 | fexpiringmonthto | 结束月 | varchar | 30 |  | √ | ' ' | 结束月,枚举: 1 :01 2 :02 3 :03 4 :04 5 :05 6 :06 7 :07 8 :08 9 :09 10 :10 11 :11 12 :12 |
| 32 | fisdefalt | 默认日历 | bpchar | 1 |  | √ | '0' | 默认日历 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plancalendar |  | fnumber,fcreateorgid |
| 2 | pk_t_mrp_plancalendar |  | fid |

---

## 单据体-子表 t_mrp_plancalendarentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_plancalendarentry

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
| 1 | pk_t_mrp_plancalendarentry |  | fentryid |
| 2 | idx_mrp_plancalendarentry |  | fid,fseq |

---

## 计划日历-多语言表 t_mrp_plancalendar_l

- **表名称：** 计划日历-多语言表
- **表名：** t_mrp_plancalendar_l

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
| 1 | idx_mrp_plancalendar_l |  | fid,flocaleid |
| 2 | pk_t_mrp_plancalendar_l |  | fpkid |
