# 税额抵免优惠动态行-tccit_qysds_a107050_dyn

## 税额抵免优惠动态行-主表 t_tccit_qysds_a107050_dyn

- **表名称：** 税额抵免优惠动态行-主表
- **表名：** t_tccit_qysds_a107050_dyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 3 | fkdmse | 可抵免税额 | numeric | 23 | 10 | √ | 0 | 可抵免税额 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :行号 count :合计行 |
| 5 | fdmbl | 抵免比例 | numeric | 23 | 10 | √ | 0 | 抵免比例 |
| 6 | fitem | 投资类型 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | ftze | 投资额 | numeric | 23 | 10 | √ | 0 | 投资额 |
| 9 | fewblname | 二维表名称 | varchar | 200 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qysds_a107050_dyn_sbbid |  | fsbbid |
| 2 | pk_tccit_qysds_a107050_dyn |  | fid |
