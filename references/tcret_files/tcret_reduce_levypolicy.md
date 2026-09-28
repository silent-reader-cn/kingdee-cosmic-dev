# 减征政策-tcret_reduce_levypolicy

## 减征政策-主表 t_tcret_reduce_levypolicy

- **表名称：** 减征政策-主表
- **表名：** t_tcret_reduce_levypolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1-城镇土地使用税 2 :2-房产税 |
| 3 | ftimestart | 本期适用增值税小规模纳税人减征政策起始时间 | timestamp | 0 |  |  | null | 本期适用增值税小规模纳税人减征政策起始时间 |
| 4 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 5 | fminusrate | 减征比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减征比例 |
| 6 | fissuitableforsmall | 本期是否适用增值税小规模纳税人减征政策 | varchar | 30 |  | √ | ' ' | 本期是否适用增值税小规模纳税人减征政策,枚举: 1 :是 0 :否 |
| 7 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 8 | ftaxtype | 税种类型（房产税或土地使用税） | varchar | 30 |  | √ | ' ' | 税种类型（房产税或土地使用税）,枚举: urbanLandTax :城镇土地使用税 buildingTax :房产税 |
| 9 | ftimeend | 本期适用增值税小规模纳税人减征政策终止时间 | timestamp | 0 |  |  | null | 本期适用增值税小规模纳税人减征政策终止时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_reduce_levypolicy_1 |  | fewblxh,fsbbid |
| 2 | t_tcret_reduce_levypolicy_pkey |  | fid |
| 3 | idx_tcret_reduce_levypolicy |  | fsbbid |
