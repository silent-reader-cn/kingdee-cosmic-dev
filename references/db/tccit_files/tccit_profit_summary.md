# 会计利润明细台账-tccit_profit_summary

## 会计利润明细台账-主表 t_tccit_profit_summary

- **表名称：** 会计利润明细台账-主表
- **表名：** t_tccit_profit_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: income :营业收入 jcost :营业成本 profit :利润总额 |
| 3 | fsqfse | 上期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 上期发生额 |
| 4 | fsqlje | 上期累计额 | numeric | 23 | 10 | √ | 0.0000000000 | 上期累计额 |
| 5 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbqlje | 本期累计额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期累计额 |
| 8 | fbqfse | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_profit_summary |  | forgid,fskssqq,fskssqz,ftype |
| 2 | t_tccit_profit_summary_pkey |  | fid |
