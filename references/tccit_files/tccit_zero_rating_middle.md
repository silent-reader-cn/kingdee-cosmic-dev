# 不征税收入及支出中间表-tccit_zero_rating_middle

## 不征税收入及支出中间表-主表 t_tccit_zero_rating_midd

- **表名称：** 不征税收入及支出中间表-主表
- **表名：** t_tccit_zero_rating_midd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumpayamount | 累计计入支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计计入支出金额 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 4 | fexpensingamount | 其中费用化金额 | numeric | 23 | 10 | √ | 0.0000000000 | 其中费用化金额 |
| 5 | fsumfinancialamount | 累计上缴财政金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计上缴财政金额 |
| 6 | fbizno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 7 | fpayamount | 当年计入支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年计入支出金额 |
| 8 | fincomedate | 取得日期 | timestamp | 0 |  |  | null | 取得日期 |
| 9 | fincludedtaxamount | 当年计入应税收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年计入应税收入金额 |
| 10 | ffinancialamount | 当年上缴财政金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年上缴财政金额 |
| 11 | ftype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型 |
| 12 | fzeroratingamount | 其中：不征税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：不征税收入 |
| 13 | fsumincludedtaxamount | 累计计入应税收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计计入应税收入金额 |
| 14 | fyear | 年份 | int8 | 64 |  | √ | 0 | 年份 |
| 15 | ffiscalamount | 财政性资金 | numeric | 23 | 10 | √ | 0.0000000000 | 财政性资金 |
| 16 | fsumincomeamount | 累计计入收益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计计入收益金额 |
| 17 | fincomeamount | 当年计入收益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 当年计入收益金额 |
| 18 | fbalanceamount | 结余可用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结余可用金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_zero_rating_midd |  | forgid,fyear |
| 2 | pk_tccit_zero_rating_midd |  | fid |
