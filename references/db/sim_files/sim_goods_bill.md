# 商品统计单据-sim_goods_bill

## 商品统计单据-主表 t_sim_goods_bill

- **表名称：** 商品统计单据-主表
- **表名：** t_sim_goods_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0.000 :0 0.010 :1% 0.030 :3% 0.050 :5% 0.060 :6% 0.090 :9% 0.100 :10% 0.110 :11% 0.130 :13% 0.015 :1.5% |
| 4 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 5 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 6 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 7 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | finvoicenum | 发票数量 | int8 | 64 |  | √ | 0 | 发票数量 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 11 | funit | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_goods_bill |  | fid |
| 2 | idx_sim_goods_bill |  | fdate |
