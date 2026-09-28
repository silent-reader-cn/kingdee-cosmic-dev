# 计划日历分录-fpm_planningcalendarentry

## 计划日历分录-主表 t_fpm_budgetperiod

- **表名称：** 计划日历分录-主表
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
| 9 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
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

## 计划日历分录-多语言表 t_fpm_budgetperiod_l

- **表名称：** 计划日历分录-多语言表
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
