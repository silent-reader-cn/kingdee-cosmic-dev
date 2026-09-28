# 一般纳税人计提免税台账汇总单据-tcvat_taxdeduce_sum_sjjt

## 一般纳税人计提免税台账汇总单据-主表 t_tcvat_taxdeduc_sum_sjjt

- **表名称：** 一般纳税人计提免税台账汇总单据-主表
- **表名：** t_tcvat_taxdeduc_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | fmzzzsxmxse | 免征增值税项目销售额 | numeric | 23 | 10 | √ | 0 | 免征增值税项目销售额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fkchmsxse | 扣除后免税销售额 | numeric | 23 | 10 | √ | 0 | 扣除后免税销售额 |
| 6 | fbqsjkcje | 本期实际扣除金额 | numeric | 23 | 10 | √ | 0 | 本期实际扣除金额 |
| 7 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 8 | fmsxsedyjxse | 免税销售额对应的进项税额 | numeric | 23 | 10 | √ | 0 | 免税销售额对应的进项税额 |
| 9 | funiquekey | 减免税数据分组标识 | varchar | 250 |  | √ | ' ' | 减免税数据分组标识 |
| 10 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmse | 免税额 | numeric | 23 | 10 | √ | 0 | 免税额 |
| 13 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 18 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 19 | fewbhxh | 二维表行序号 | varchar | 50 |  | √ | ' ' | 二维表行序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxdeduc_orgid_taxperiod |  | forgid,ftaxperiod |
| 2 | pk_tcvat_taxdeduc_sum_sjjt |  | fid |
