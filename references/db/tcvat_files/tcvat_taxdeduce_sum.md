# 免税台账汇总单据-tcvat_taxdeduce_sum

## 免税台账汇总单据-主表 t_tcvat_taxdeduce_sum

- **表名称：** 免税台账汇总单据-主表
- **表名：** t_tcvat_taxdeduce_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fmzzzsxmxse | 免征增值税项目销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免征增值税项目销售额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fkchmsxse | 扣除后免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除后免税销售额 |
| 6 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 7 | fbqsjkcje | 本期实际扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期实际扣除金额 |
| 8 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 9 | fmsxsedyjxse | 免税销售额对应的进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额对应的进项税额 |
| 10 | funiquekey | 减免税数据分组标识 | varchar | 250 |  | √ | ' ' | 减免税数据分组标识 |
| 11 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmse | 免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税额 |
| 14 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 15 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 16 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 17 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 18 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 19 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 20 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 21 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 22 | fewbhxh | 二维表行序号 | varchar | 50 |  | √ | ' ' | 二维表行序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_taxdeduce_sum |  | forgid,ftaxperiod |
| 2 | t_tcvat_taxdeduce_sum_pkey |  | fid |
