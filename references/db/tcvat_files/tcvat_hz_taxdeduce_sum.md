# 总机构免税台账汇总单据-tcvat_hz_taxdeduce_sum

## 总机构免税台账汇总单据-主表 t_tcvat_hz_taxdeduce_sum

- **表名称：** 总机构免税台账汇总单据-主表
- **表名：** t_tcvat_hz_taxdeduce_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmzzzsxmxse | 免征增值税项目销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免征增值税项目销售额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fkchmsxse | 扣除后免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除后免税销售额 |
| 5 | fbqsjkcje | 本期实际扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期实际扣除金额 |
| 6 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 7 | fmsxsedyjxse | 免税销售额对应的进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额对应的进项税额 |
| 8 | funiquekey | 减免税数据分组标识 | varchar | 250 |  | √ | ' ' | 减免税数据分组标识 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmse | 免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税额 |
| 12 | fdeclaretype | fdeclaretype | varchar | 50 |  | √ | ' ' |  |
| 13 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 15 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 16 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 19 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 20 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 21 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 22 | fsuborg | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fewbhxh | 二维表行序号 | varchar | 50 |  | √ | ' ' | 二维表行序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_hz_taxdeduce_sum |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_hz_taxdeduce_sum |  | fid |
