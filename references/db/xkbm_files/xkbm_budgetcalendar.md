# 预算日历-xkbm_budgetcalendar

## 预算日历-主表 t_xkbm_budgetcalendar

- **表名称：** 预算日历-主表
- **表名：** t_xkbm_budgetcalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcycleselecttype | 周起点 | varchar | 30 |  | √ | ' ' | 周起点,枚举: 0 :星期日 1 :星期一 2 :星期二 3 :星期三 4 :星期四 5 :星期五 6 :星期六 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fstartyear | 起始年度 | varchar | 50 |  | √ | ' ' | 起始年度,枚举: |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fisshowalias | 显示别名 | bpchar | 1 |  | √ | '0' | 显示别名 |
| 10 | fisshowday | 显示期间的起止日期 | bpchar | 1 |  | √ | ' ' | 显示期间的起止日期 |
| 11 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 12 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | facid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 17 | fbudgetcalendartype | 日历类型 | varchar | 30 |  | √ | ' ' | 日历类型,枚举: 1 :会计日历 |
| 18 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fcycles | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 21 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | faliasgeneratetype | 别名生成方式 | varchar | 10 |  | √ | '0' | 别名生成方式,枚举: 0 :按起始日期 1 :按结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetcalendar |  | fid |
| 2 | idx_xkbm_budgetcalendar |  | fstartyear,fcycles |

---

## 树形单据体-多语言表 t_xkbm_budgetperiod_l

- **表名称：** 树形单据体-多语言表
- **表名：** t_xkbm_budgetperiod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fperiodname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | fperiodshortname | 短名称 | varchar | 255 |  | √ | ' ' | 短名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetperiod_l |  | fentryid,flocaleid |
| 2 | pk_xkbm_budgetperiod_l |  | fpkid |

---

## 树形单据体-子表 t_xkbm_budgetperiod

- **表名称：** 树形单据体-子表
- **表名：** t_xkbm_budgetperiod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperiodstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 3 | fperiodname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fperiodnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fperiodalias | 别名 | int4 | 32 |  | √ | 0 | 别名 |
| 7 | fperiodshortname | 短名称 | varchar | 255 |  | √ | ' ' | 短名称 |
| 8 | fperiodtype | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 4 :旬 5 :周 6 :日 |
| 9 | fperiodenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fperiodyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetperiod |  | fentryid |
| 2 | idx_xkbm_budgetperiod |  | fid,fparententryid |

---

## 预算日历-多语言表 t_xkbm_budgetcalendar_l

- **表名称：** 预算日历-多语言表
- **表名：** t_xkbm_budgetcalendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetcalendar_l |  | fpkid |
| 2 | idx_xkbm_budgetcalendar_l |  | fid,flocaleid |
