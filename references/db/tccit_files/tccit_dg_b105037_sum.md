# 符合免税条件的投资收益底稿单据-tccit_dg_b105037_sum

## 符合免税条件的投资收益底稿单据-主表 t_tccit_dg_b105037_sum

- **表名称：** 符合免税条件的投资收益底稿单据-主表
- **表名：** t_tccit_dg_b105037_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fmssrje | 享受免税优惠的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 享受免税优惠的金额 |
| 4 | fnumorrate | 投资数量/比例 | numeric | 23 | 10 | √ | 0.0000000000 | 投资数量/比例 |
| 5 | flabel | 标识 | int8 | 64 |  | √ | 0 | 标识 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | finvesttype | 投资性质 | varchar | 50 |  | √ | ' ' | 投资性质 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | ftzbdname | 投资标的名称 | varchar | 50 |  | √ | ' ' | 投资标的名称 |
| 10 | ftaxpayerid | 被投资企业纳税人识别号 | varchar | 50 |  | √ | ' ' | 被投资企业纳税人识别号 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fbizdate | 纳税义务时间 | timestamp | 0 |  |  | null | 纳税义务时间 |
| 13 | ftzssyhje | 调整税收优惠金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整税收优惠金额 |
| 14 | fcysytype | 收入类型 | varchar | 50 |  | √ | ' ' | 收入类型 |
| 15 | fincost | 投资成本 | numeric | 23 | 10 | √ | 0.0000000000 | 投资成本 |
| 16 | fbillno | 资产编号 | varchar | 50 |  | √ | ' ' | 资产编号 |
| 17 | fqddbtzzc | 调整后的免税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整后的免税金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dg_b105037_sum |  | fid |
| 2 | idx_tccit_dg_b105037_sum |  | fitemno,forgid,fskssqq,fskssqz |
