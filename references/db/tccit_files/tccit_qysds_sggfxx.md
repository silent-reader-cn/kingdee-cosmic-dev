# 收购外国企业股份情况-tccit_qysds_sggfxx

## 收购外国企业股份情况-主表 t_tccit_qysds_sggfxx

- **表名称：** 收购外国企业股份情况-主表
- **表名：** t_tccit_qysds_sggfxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 |
| 3 | fsghbgrzwgqycgfe | 5.收购后报告人在外国企业持股份额 | numeric | 23 | 10 | √ | 0.0000000000 | 5.收购后报告人在外国企业持股份额 |
| 4 | fsgfs | 3.收购方式 | varchar | 100 |  | √ | ' ' | 3.收购方式 |
| 5 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 6 | fbsggflx | 1.被收购股份类型 | varchar | 100 |  | √ | ' ' | 1.被收购股份类型 |
| 7 | fjyrq | 2.交易日期 | timestamp | 0 |  |  | null | 2.交易日期 |
| 8 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 9 | fsgqbgrzwgqycgfe | 4.收购前报告人在外国企业持股份额 | numeric | 23 | 10 | √ | 0.0000000000 | 4.收购前报告人在外国企业持股份额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_qysds_sggfxx_pkey |  | fid |
| 2 | idx_tccit_qysds_sggfxx_1 |  | fewblxh,fsbbid |
| 3 | idx_tccit_qysds_sggfxx |  | fsbbid |
