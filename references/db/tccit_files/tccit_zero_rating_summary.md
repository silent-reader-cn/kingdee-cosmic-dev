# 不征税收入及资产底稿-tccit_zero_rating_summary

## 不征税收入及资产底稿-主表 t_tccit_zero_rating_sum

- **表名称：** 不征税收入及资产底稿-主表
- **表名：** t_tccit_zero_rating_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fincomedate | 取得日期 | timestamp | 0 |  |  | null | 取得日期 |
| 3 | ftype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型,枚举: specialfund :专项用途财政性资金 other :其他 |
| 4 | fzeroratingamount | 其中：不征税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：不征税收入 |
| 5 | fincomedateyear | 取得日期年份 | int8 | 64 |  | √ | 0 | 取得日期年份 |
| 6 | fparentorgid | 汇总组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | forgid | 组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ffiscalamount | 财政性资金 | numeric | 23 | 10 | √ | 0.0000000000 | 财政性资金 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_zero_rating_sum |  | fid |
| 2 | idx_tccit_zero_rating_sum |  | forgid,fskssqq,fskssqz |

---

## 单据体-子表 t_tccit_zero_rating_entry

- **表名称：** 单据体-子表
- **表名：** t_tccit_zero_rating_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fincludedtaxamount | 计入应税收入金额 （当前申报年份金额调增 | numeric | 23 | 10 | √ | 0.0000000000 | 计入应税收入金额 （当前申报年份金额调增 |
| 3 | ffinancialamount | 其中：上缴财政 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：上缴财政 |
| 4 | fyear | 年份 | int8 | 64 |  | √ | 0 | 年份 |
| 5 | fexpensingamount | 其中：费用化 （当前申报年份金额调增） | numeric | 23 | 10 | √ | 0.0000000000 | 其中：费用化 （当前申报年份金额调增） |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpayamount | 支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 支出金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fincomeamount | 计入损益金额 （当前申报年份金额调减 | numeric | 23 | 10 | √ | 0.0000000000 | 计入损益金额 （当前申报年份金额调减 |
| 10 | fbalanceamount | 结余金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结余金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_zero_rating_entry_fk |  | fid |
| 2 | pk_tccit_zero_rating_entry |  | fentryid |
