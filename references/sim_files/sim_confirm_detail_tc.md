# 单据发票关系(废弃)-sim_confirm_detail_tc

## 单据发票关系(废弃)-主表 t_sim_confirm_detail_tc

- **表名称：** 单据发票关系(废弃)-主表
- **表名：** t_sim_confirm_detail_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fredtax | 已红冲税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已红冲税额 |
| 3 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 4 | ftargetdetailid | 目标单明细ID | int8 | 64 |  | √ | 0 | 目标单明细ID |
| 5 | famounts | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fissuedtax | 已开税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开税额 |
| 7 | fbilldetailid | 单据明细ID | int8 | 64 |  | √ | 0 | 单据明细ID |
| 8 | famts | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | fissuedamount | 已开金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开金额 |
| 10 | ftargettype | 目标单 | varchar | 50 |  | √ | ' ' | 目标单,枚举: 0 :待开列表 1 :红字信息表 |
| 11 | ftargetid | 目标单ID | int8 | 64 |  | √ | 0 | 目标单ID |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fredamount | 已红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已红冲金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_confirm_detail_tc |  | fbillno |
| 2 | pk_sim_confirm_detail_tc |  | fid |
