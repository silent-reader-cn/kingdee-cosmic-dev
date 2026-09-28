# 投资资产持有收益调整底稿-tccit_invest_profit_sum

## 投资资产持有收益调整底稿-主表 t_tccit_invest_profit_sum

- **表名称：** 投资资产持有收益调整底稿-主表
- **表名：** t_tccit_invest_profit_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | ftaxincome | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 6010401 :交易性金融资产 6010402 :可供出售金融资产 6010403 :持有至到期投资 6010404 :衍生工具 6010405 :交易性金融负债 6010406 :长期股权投资 6010407 :短期投资 6010408 :长期债券投资 6010409 :其他 count :合计 |
| 6 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 8 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 9 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 10 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 11 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_invest_profit_sum |  | fid |
| 2 | idx_tccit_invest_profit_sum |  | forgid,fskssqq,fskssqz |
