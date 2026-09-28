# 从价计征房产税减免信息-tcret_housetax_p_info

## 从价计征房产税减免信息-主表 t_tcret_housetax_p_info

- **表名称：** 从价计征房产税减免信息-主表
- **表名：** t_tcret_housetax_p_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 all :合计 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | fbuildingnumber | 房产编号 | varchar | 100 |  | √ | ' ' | 房产编号 |
| 5 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 6 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 7 | ftaxreducehousevalue | 减免税房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税房产原值 |
| 8 | ftaxcountratio | 计税比例 | numeric | 23 | 10 | √ | 0.0000000000 | 计税比例 |
| 9 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
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
| 1 | t_tcret_housetax_p_info_pkey |  | fid |
| 2 | idx_tcret_housetax_p_info_1 |  | fewblxh,fsbbid |
| 3 | idx_tcret_housetax_p_info |  | fsbbid |
