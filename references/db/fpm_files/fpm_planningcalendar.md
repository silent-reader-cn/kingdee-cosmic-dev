# 计划日历-fpm_planningcalendar

## 树形单据体-子表 t_fpm_budgetperiod

- **表名称：** 树形单据体-子表
- **表名：** t_fpm_budgetperiod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperiodstartdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 3 | fperiodname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fperiodnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 5 | fperiodshortname | 短名称 | varchar | 500 |  | √ | ' ' | 短名称 |
| 6 | fperiodtype | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 4 :旬 5 :周 6 :日 |
| 7 | fperiodenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 11 | fperiodyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_budgetperiod |  | fentryid |
| 2 | idx_fpm_budgetperiod |  | fid,fparententryid |

---

## 计划日历-多语言表 t_fpm_planningcalendar_l

- **表名称：** 计划日历-多语言表
- **表名：** t_fpm_planningcalendar_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpm_planningcalendar_l |  | fpkid |
| 2 | idx_fpm_planningcalendar_l |  | fid,flocaleid |

---

## 树形单据体-多语言表 t_fpm_budgetperiod_l

- **表名称：** 树形单据体-多语言表
- **表名：** t_fpm_budgetperiod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fperiodname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 2 | fperiodshortname | 短名称 | varchar | 500 |  | √ | ' ' | 短名称 |
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
| 1 | idx_fpm_budgetperiod_l |  | fentryid,flocaleid |
| 2 | pk_fpm_budgetperiod_l |  | fpkid |

---

## 计划日历-主表 t_fpm_planningcalendar

- **表名称：** 计划日历-主表
- **表名：** t_fpm_planningcalendar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcycleselecttype | 周起点 | varchar | 50 |  | √ | ' ' | 周起点,枚举: 0 :星期日 1 :星期一 2 :星期二 3 :星期三 4 :星期四 5 :星期五 6 :星期六 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fstartyear | 起始年度 | varchar | 50 |  | √ | ' ' | 起始年度,枚举: |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fisshowday | 显示期间的开始结束日期 | bpchar | 1 |  | √ | ' ' | 显示期间的开始结束日期 |
| 10 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 11 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | facid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 16 | fbudgetcalendartype | 日历类型 | varchar | 50 |  | √ | ' ' | 日历类型,枚举: 1 :会计日历 |
| 17 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fbudgetcalendarid | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 20 | fcycles | 周期类型 | varchar | 50 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 21 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_planningcalendar |  | fstartyear,fcycles |
| 2 | pk_fpm_planningcalendar |  | fid |
