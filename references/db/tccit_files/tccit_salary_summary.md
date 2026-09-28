# 工资薪金汇总单据-tccit_salary_summary

## 工资薪金汇总单据-主表 t_tccit_salary_summary_dg

- **表名称：** 工资薪金汇总单据-主表
- **表名：** t_tccit_salary_summary_dg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int4 | 32 |  | √ | 0 | 行次 |
| 3 | ftaxamount | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: salarystock :工资及股权激励 salary :工资薪金 stock :股权激励 insurance :社会保险 commreserve :住房公积金 sumamount :合计 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fsjje | 实际发放的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际发放的金额 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fsjjebeforetax | 实际发放的金额中，不符合税前扣除规定的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际发放的金额中，不符合税前扣除规定的金额 |
| 9 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 10 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: salarystock :工资及股权激励 salary :工资薪金 stock :股权激励 insurance :社会保险 commreserve :住房公积金 sumamount :合计 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fzzje | 账面计提的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账面计提的金额 |
| 13 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 14 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_salary_summary_dg |  | fid |
| 2 | idx_tccit_salary_summary_dg |  | forgid,fskssqq,fskssqz |
