# 跨期调整底稿-tccit_period_summary

## 跨期调整底稿-主表 t_tccit_period_summary

- **表名称：** 跨期调整底稿-主表
- **表名：** t_tccit_period_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | ftaxamount | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行号 count :合计 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fpayamount | 本期支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期支付金额 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 9 | fadjustamount | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 10 | fzzjeamount | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 11 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 12 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 15 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_period_summary |  | fid |
| 2 | idx_tccit_period_summary |  | forgid,fskssqq,fskssqz |
