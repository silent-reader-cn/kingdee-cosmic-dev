# 从租计征房产税-tcret_housetax_hire

## 从租计征房产税-主表 t_tcret_housetax_hire

- **表名称：** 从租计征房产税-主表
- **表名：** t_tcret_housetax_hire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 all :合计 4 :4 5 :5 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | fcurrentdeclarerent | 本期申报租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本期申报租金收入 |
| 5 | fcurrentpaidin | 本期已缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期已缴税额 |
| 6 | fcurrentsmallreduce | 本期增值税小规模纳税人减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期增值税小规模纳税人减征额 |
| 7 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 8 | fcurrenttaxamount | 本期应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应纳税额 |
| 9 | fcurrentreduce | 本期减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期减免税额 |
| 10 | fcurrentdrawback | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 11 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_housetax_hire |  | fsbbid |
| 2 | idx_tcret_housetax_hire_1 |  | fewblxh,fsbbid |
| 3 | t_tcret_housetax_hire_pkey |  | fid |
