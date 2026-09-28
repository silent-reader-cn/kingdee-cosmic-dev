# 城镇土地使用税-tcret_land_tax

## 城镇土地使用税-主表 t_tcret_land_tax

- **表名称：** 城镇土地使用税-主表
- **表名：** t_tcret_land_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 all :合计 |
| 3 | ftimestart | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 4 | fcurrentpaidin | 本期已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期已缴税额 |
| 5 | fcurrentsmallreduce | 本期增值税小规模纳税人减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期增值税小规模纳税人减征额 |
| 6 | flandtotalarea | 土地总面积 | numeric | 23 | 10 | √ | 0.0000000000 | 土地总面积 |
| 7 | fcurrenttaxamount | 本期应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税额 |
| 8 | flandnumber | 土地编号 | varchar | 100 |  | √ | ' ' | 土地编号 |
| 9 | fcurrentdrawback | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 10 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 11 | ftaxstandard | 税额标准 | varchar | 100 |  | √ | ' ' | 税额标准 |
| 12 | ftimeend | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 13 | flandparcelnumber | 宗地号 | varchar | 100 |  | √ | ' ' | 宗地号 |
| 14 | flandlevel | 土地等级 | varchar | 100 |  | √ | ' ' | 土地等级 |
| 15 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 16 | fcurrentreduce | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_land_tax_pkey |  | fid |
| 2 | idx_tcret_land_tax |  | fsbbid |
| 3 | idx_tcret_land_tax_1 |  | fewblxh,fsbbid |
