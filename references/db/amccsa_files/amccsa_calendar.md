# 客户日历-amccsa_calendar

## 单据体-子表 t_amccsa_calendarentry

- **表名称：** 单据体-子表
- **表名：** t_amccsa_calendarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 日期类型 | bpchar | 1 |  | √ | '1' | 日期类型,枚举: 1 :工作日 2 :半休日 3 :节假日 4 :休息日 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fworkdate | 日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_calen_fid |  | fid |
| 2 | pk_t_amccsa_calendarentry |  | fentryid |

---

## 客户日历-多语言表 t_amccsa_calendar_l

- **表名称：** 客户日历-多语言表
- **表名：** t_amccsa_calendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 日历名称 | varchar | 100 |  | √ | ' ' | 日历名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_amccsa_calendar_l |  | fpkid |
| 2 | idx_t_amccsa_cal_l_fid |  | fid,flocaleid |

---

## 客户日历-使用范围表 t_amccsa_calendar_u

- **表名称：** 客户日历-使用范围表
- **表名：** t_amccsa_calendar_u

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
| 1 | idx_t_amccsa_calendar_u_uo |  | fuseorgid |
| 2 | pk_t_amccsa_calendar_u |  | fdataid,fuseorgid |

---

## 客户日历-主表 t_amccsa_calendar

- **表名称：** 客户日历-主表
- **表名：** t_amccsa_calendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissunrest | 周日 | bpchar | 1 |  | √ | '0' | 周日 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fiswedrest | 周三 | bpchar | 1 |  | √ | '0' | 周三 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fisfrirest | 周五 | bpchar | 1 |  | √ | '0' | 周五 |
| 14 | fismonrest | 周一 | bpchar | 1 |  | √ | '0' | 周一 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 日历名称 | varchar | 50 |  | √ | ' ' | 日历名称 |
| 17 | fcustomer | 订货/收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fisthurest | 周四 | bpchar | 1 |  | √ | '0' | 周四 |
| 21 | fissatrest | 周六 | bpchar | 1 |  | √ | '0' | 周六 |
| 22 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fistuerest | 周二 | bpchar | 1 |  | √ | '0' | 周二 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 日历编码 | varchar | 30 |  | √ | ' ' | 日历编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_amccsa_calendar_master |  | fmasterid |
| 2 | pk_t_amccsa_calendar |  | fid |
| 3 | idx_t_amccsa_calendar_createorg |  | fcreateorgid |
| 4 | idx_t_amccsa_cal_cust |  | fcustomer |
