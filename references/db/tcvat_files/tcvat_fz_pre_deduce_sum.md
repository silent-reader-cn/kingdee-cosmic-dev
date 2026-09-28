# 预缴分支免税台账汇总单据-tcvat_fz_pre_deduce_sum

## 预缴分支免税台账汇总单据-主表 t_tcvat_fz_pre_deduce_sum

- **表名称：** 预缴分支免税台账汇总单据-主表
- **表名：** t_tcvat_fz_pre_deduce_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmzzzsxmxse | 免征增值税项目销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免征增值税项目销售额 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fkchmsxse | 扣除后免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除后免税销售额 |
| 5 | fbqsjkcje | 本期实际扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期实际扣除金额 |
| 6 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 7 | fmsxsedyjxse | 免税销售额对应的进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额对应的进项税额 |
| 8 | funiquekey | 减免税数据分组标识 | varchar | 250 |  | √ | ' ' | 减免税数据分组标识 |
| 9 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmse | 免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税额 |
| 12 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 18 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 19 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 20 | fewbhxh | 二维表行序号 | varchar | 50 |  | √ | ' ' | 二维表行序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fz_pre_deduce_sum |  | fid |
| 2 | idx_tcvat_fz_pre_deduce_sum |  | forgid,fstartdate,fenddate |
