# 从价计征房产税-tcret_housetax_price

## 从价计征房产税-主表 t_tcret_housetax_price

- **表名称：** 从价计征房产税-主表
- **表名：** t_tcret_housetax_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 all :合计 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | fcurrentpaidin | 本期已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期已缴税额 |
| 5 | fcurrentsmallreduce | 本期增值税小规模纳税人减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期增值税小规模纳税人减征额 |
| 6 | fcurrenttaxamount | 本期应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税额 |
| 7 | fbuildingnumber | 房产编号 | varchar | 100 |  | √ | ' ' | 房产编号 |
| 8 | fhousevalue | 房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 房产原值 |
| 9 | fcurrentdrawback | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 10 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 11 | fenddate | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 12 | frentalhousevalue | 其中：出租房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：出租房产原值 |
| 13 | ftaxationratio | 计税比例 | numeric | 23 | 10 | √ | 0.0000000000 | 计税比例 |
| 14 | fstartdate | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 15 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 16 | fcurrentreduce | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_housetax_price_pkey |  | fid |
| 2 | idx_tcret_housetax_price_1 |  | fewblxh,fsbbid |
| 3 | idx_tcret_housetax_price |  | fsbbid |
