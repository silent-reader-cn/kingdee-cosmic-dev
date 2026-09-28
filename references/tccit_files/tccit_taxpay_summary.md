# 所得税缴纳明细台账-tccit_taxpay_summary

## 所得税缴纳明细台账-主表 t_tccit_taxpay_summary

- **表名称：** 所得税缴纳明细台账-主表
- **表名：** t_tccit_taxpay_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 4 | fljs1 | 一季度累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 一季度累计数 |
| 5 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: income :收入 cost :成本 profit :利润总额 prepay :已预交税额 |
| 6 | fljs2 | 二季度累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 二季度累计数 |
| 7 | fljs3 | 三季度累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 三季度累计数 |
| 8 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 9 | fljs4 | 四季度累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 四季度累计数 |
| 10 | fbqs1 | 一季度本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 一季度本期数 |
| 11 | fbqs4 | 四季度本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 四季度本期数 |
| 12 | fbqs3 | 三季度本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 三季度本期数 |
| 13 | fbqs2 | 二季度本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 二季度本期数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_taxpay_summary |  | forgid,fskssqq,fskssqz |
| 2 | t_tccit_taxpay_summary_pkey |  | fid |
