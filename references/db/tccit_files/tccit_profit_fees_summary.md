# 费用成本底稿-tccit_profit_fees_summary

## 费用成本底稿-主表 t_tccit_profit_fees_sum

- **表名称：** 费用成本底稿-主表
- **表名：** t_tccit_profit_fees_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fselloutside | 境外销售支付 | numeric | 23 | 10 | √ | 0.0000000000 | 境外销售支付 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | ffinanceoutside | 境外财务支付 | numeric | 23 | 10 | √ | 0.0000000000 | 境外财务支付 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 8 | fsellcost | 销售费用 | numeric | 23 | 10 | √ | 0.0000000000 | 销售费用 |
| 9 | fmanagecost | 管理费用 | numeric | 23 | 10 | √ | 0.0000000000 | 管理费用 |
| 10 | fmanageoutside | 境外管理支付 | numeric | 23 | 10 | √ | 0.0000000000 | 境外管理支付 |
| 11 | ffinancecost | 财务费用 | numeric | 23 | 10 | √ | 0.0000000000 | 财务费用 |
| 12 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_profit_fees_sum |  | fitemtype,forgid,fskssqq,fskssqz |
| 2 | pk_tccit_profit_fees_sum |  | fid |
