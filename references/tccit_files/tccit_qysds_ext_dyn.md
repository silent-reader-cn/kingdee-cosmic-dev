# 动态扩展区域1-tccit_qysds_ext_dyn

## 动态扩展区域1-主表 t_tccit_qysds_ext_dyn

- **表名称：** 动态扩展区域1-主表
- **表名：** t_tccit_qysds_ext_dyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frownumber | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :7.1优惠事项名称 |
| 4 | fitem | 优惠项目取数 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | fitemamount | 项目金额 | numeric | 23 | 10 | √ | 0 | 项目金额 |
| 7 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_ext_dyn |  | fsbbid,fewblxh |
| 2 | pk_tccit_qysds_ext_dyn |  | fid |
