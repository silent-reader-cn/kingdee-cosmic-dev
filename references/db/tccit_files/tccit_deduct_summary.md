# 抵扣汇总单据列表-tccit_deduct_summary

## 抵扣汇总单据列表-主表 t_tccit_deduct_summary_dg

- **表名称：** 抵扣汇总单据列表-主表
- **表名：** t_tccit_deduct_summary_dg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 3 | ftaxamount | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 4 | flimitamount | 扣除限额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除限额 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fsjje | 实际支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际支出金额 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: gonghui :工会经费 zhigong :职工福利费 yanglao :补充养老保险 yiliao :补充医疗保险 dangfei :党组织工作经费 |
| 9 | fsalary | 本年实际发生的工资薪金 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际发生的工资薪金 |
| 10 | frate | 扣除比例 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除比例 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 13 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_deduct_summary_dg |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_deduct_summary_dg |  | fid |
