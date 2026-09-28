# 城镇土地使用税减免信息-tcret_landtax_deduction

## 城镇土地使用税减免信息-主表 t_tcret_landtax_deduction

- **表名称：** 城镇土地使用税减免信息-主表
- **表名：** t_tcret_landtax_deduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 all :合计 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 |
| 3 | ftaxreducearea | 减免税面积 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税面积 |
| 4 | flandnumber | 土地编号 | varchar | 100 |  | √ | ' ' | 土地编号 |
| 5 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 6 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 7 | ftaxstandard | 税额标准 | varchar | 100 |  | √ | ' ' | 税额标准 |
| 8 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 9 | flandlevel | 土地等级 | varchar | 100 |  | √ | ' ' | 土地等级 |
| 10 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 11 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 12 | ftaxreduceproject | 减免项目名称 | varchar | 100 |  | √ | ' ' | 减免项目名称 |
| 13 | fcurrenttaxreduceamount | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_landtax_deduction_1 |  | fewblxh,fsbbid |
| 2 | t_tcret_landtax_deduction_pkey |  | fid |
| 3 | idx_tcret_landtax_deduction |  | fsbbid |
