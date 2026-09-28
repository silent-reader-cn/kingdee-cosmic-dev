# 从价计征房产税税源明细减免税部分-tcret_housetax_p_s_jms

## 从价计征房产税税源明细减免税部分-主表 t_tcret_housetax_p_s_jms

- **表名称：** 从价计征房产税税源明细减免税部分-主表
- **表名：** t_tcret_housetax_p_s_jms

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 减免结束时间 | timestamp | 0 |  |  | null | 减免结束时间 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 |
| 4 | fstartdate | 减免开始时间 | timestamp | 0 |  |  | null | 减免开始时间 |
| 5 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 6 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 7 | ftaxreduceproject | 减免项目名称 | varchar | 100 |  | √ | ' ' | 减免项目名称 |
| 8 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 9 | fmonthreduceamount | 月减免税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 月减免税金额 |
| 10 | freducebuildingvalue | 减免税房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税房产原值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_housetax_p_s_jms_pkey |  | fid |
| 2 | idx_tcret_housetax_p_s_jms_1 |  | fewblxh,fsbbid |
| 3 | idx_tcret_housetax_p_s_jms |  | fsbbid |
