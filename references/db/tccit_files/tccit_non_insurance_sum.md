# 其他企业佣金手续费底稿单据-tccit_non_insurance_sum

## 其他企业佣金手续费底稿单据-主表 t_tccit_non_insurance_sum

- **表名称：** 其他企业佣金手续费底稿单据-主表
- **表名：** t_tccit_non_insurance_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | ftaxincome | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 5 | flimitbase | 限额扣除基数 | numeric | 23 | 10 | √ | 0.0000000000 | 限额扣除基数 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fdeductamount | 扣除限额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除限额 |
| 9 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 10 | frate | 扣除比例 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除比例 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 13 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 14 | fnonallowamount | 不允许扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不允许扣除金额 |
| 15 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_non_insurance_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_non_insurance_sum |  | fid |
