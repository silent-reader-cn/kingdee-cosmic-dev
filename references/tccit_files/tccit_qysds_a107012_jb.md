# A107012研发费用加计扣除优惠基本信息-tccit_qysds_a107012_jb

## A107012研发费用加计扣除优惠基本信息-主表 t_tccit_qysds_a107012_jb

- **表名称：** A107012研发费用加计扣除优惠基本信息-主表
- **表名：** t_tccit_qysds_a107012_jb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintegerfield | 扣除项目数量 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除项目数量 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :基本信息 |
| 4 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 5 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 6 | fcombofield | 企业类型 | varchar | 30 |  | √ | ' ' | 企业类型,枚举: 1 :一般企业 2 :科技型中小企业 |
| 7 | ftextfield | 登记编号 | varchar | 100 |  | √ | ' ' | 登记编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qysds_a107012_jb_1 |  | fewblxh,fsbbid |
| 2 | idx_tccit_qysds_a107012_jb |  | fsbbid |
| 3 | t_tccit_qysds_a107012_jb_pkey |  | fid |
