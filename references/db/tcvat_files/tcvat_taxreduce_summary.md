# 减免税台账单据-tcvat_taxreduce_summary

## 减免税台账单据-主表 t_tcvat_taxreduce_summary

- **表名称：** 减免税台账单据-主表
- **表名：** t_tcvat_taxreduce_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 6 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 11 | fdescription | 业务描述 | varchar | 150 |  | √ | ' ' | 业务描述 |
| 12 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 13 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 14 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 18 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 19 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 20 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 21 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 22 | ftaxreductiontype | 减税项目类型 | varchar | 30 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 23 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_taxreduce_summary_pkey |  | fid |
| 2 | idx_tcvat_taxreduce_summary |  | forgid,ftaxperiod |
