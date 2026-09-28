# 收入其他调整底稿-tccit_income_other_sum

## 收入其他调整底稿-主表 t_tccit_income_other_sum

- **表名称：** 收入其他调整底稿-主表
- **表名：** t_tccit_income_other_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 3 | fitemno | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行号 count :合计 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 8 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 9 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 11 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 12 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 13 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 14 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_income_other_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_income_other_sum |  | fid |
