# A108020境外分支机构弥补亏损明细表-tccit_qysds_a108020

## A108020境外分支机构弥补亏损明细表-主表 t_tccit_qysds_a108020

- **表名称：** A108020境外分支机构弥补亏损明细表-主表
- **表名：** t_tccit_qysds_a108020

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyqjzwmbsjkseqwn | fyqjzwmbsjkseqwn | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | frownumber | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 4 | fyqjzwmbsjkseqsann | fyqjzwmbsjkseqsann | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :合计 |
| 6 | fbnfsfsjkse | 3.非实际亏损额的弥补本年发生的非实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 3.非实际亏损额的弥补本年发生的非实际亏损额 |
| 7 | fbnmbyqsjkse | 8.实际亏损额的弥补_本年弥补的以前年度实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 8.实际亏损额的弥补_本年弥补的以前年度实际亏损额 |
| 8 | fjzhndmbsjkseqyn | fjzhndmbsjkseqyn | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fjzhndmbsjksebn | fjzhndmbsjksebn | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fyqjzwmbsjkseqsin | fyqjzwmbsjkseqsin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fbnmbyqfsjkse | 4.非实际亏损额的弥补本年弥补的以前年度非实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 4.非实际亏损额的弥补本年弥补的以前年度非实际亏损额 |
| 12 | fjzhndmbsjksexj | 9.实际亏损额的弥补_结转以后年度弥补的实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 9.实际亏损额的弥补_结转以后年度弥补的实际亏损额 |
| 13 | fyqndjzwmbfsjkse | 2.非实际亏损额的弥补以前年度结转尚未弥补的非实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 2.非实际亏损额的弥补以前年度结转尚未弥补的非实际亏损额 |
| 14 | fjzhndmbfsjkse | 5.非实际亏损额的弥补结转以后年度弥补的非实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 5.非实际亏损额的弥补结转以后年度弥补的非实际亏损额 |
| 15 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 16 | fjzhndmbsjkseqen | fjzhndmbsjkseqen | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fbnfssjkse | 7.实际亏损额的弥补_本年发生的实际亏损额 | numeric | 23 | 10 | √ | 0.0000000000 | 7.实际亏损额的弥补_本年发生的实际亏损额 |
| 18 | fyqjzwmbsjkseqen | fyqjzwmbsjkseqen | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fjzhndmbsjkseqsin | fjzhndmbsjkseqsin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 21 | fgjdq | 1.国家地区 | varchar | 100 |  | √ | ' ' | 1.国家地区 |
| 22 | fjzhndmbsjkseqsann | fjzhndmbsjkseqsann | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fyqjzwmbsjkseqyn | fyqjzwmbsjkseqyn | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fyqjzwmbsjksexj | 6.实际亏损额的弥补_以前年度结转尚未弥补的实际亏损额_小计 | numeric | 23 | 10 | √ | 0.0000000000 | 6.实际亏损额的弥补_以前年度结转尚未弥补的实际亏损额_小计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_qysds_a108020_pkey |  | fid |
| 2 | idx_tccit_qysds_a108020 |  | fsbbid |
| 3 | idx_tccit_qysds_a108020_1 |  | fewblxh,fsbbid |
