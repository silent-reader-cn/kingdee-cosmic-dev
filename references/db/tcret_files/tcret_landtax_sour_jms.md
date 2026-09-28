# 城镇土地使用税税源明细减免税部分-tcret_landtax_sour_jms

## 城镇土地使用税税源明细减免税部分-主表 t_tcret_landtax_sour_jms

- **表名称：** 城镇土地使用税税源明细减免税部分-主表
- **表名：** t_tcret_landtax_sour_jms

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 减免结束时间 | timestamp | 0 |  |  | null | 减免结束时间 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :合计 |
| 4 | fstartdate | 减免开始时间 | timestamp | 0 |  |  | null | 减免开始时间 |
| 5 | freducelandarea | 减免税土地面积 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税土地面积 |
| 6 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 7 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 8 | ftaxreduceproject | 减免项目名称 | varchar | 100 |  | √ | ' ' | 减免项目名称 |
| 9 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 10 | fmonthreduceamount | 月减免税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 月减免税金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_landtax_sour_jms_pkey |  | fid |
| 2 | idx_tcret_landtax_sour_jms |  | fsbbid |
| 3 | idx_tcret_landtax_sour_jms_1 |  | fewblxh,fsbbid |
