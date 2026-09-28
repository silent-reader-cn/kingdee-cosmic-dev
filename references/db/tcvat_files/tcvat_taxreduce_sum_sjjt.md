# 一般纳税人计提减免税台账单据-tcvat_taxreduce_sum_sjjt

## 一般纳税人计提减免税台账单据-主表 t_tcvat_taxreduc_sum_sjjt

- **表名称：** 一般纳税人计提减免税台账单据-主表
- **表名：** t_tcvat_taxreduc_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 6 | ftaxperioddate | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 7 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 12 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 13 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 14 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 15 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 16 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 19 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 20 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 21 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 22 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 23 | ftaxreductiontype | 减税项目类型 | varchar | 50 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 24 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0 | 本期发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_taxreduc_sum_sjjt |  | fid |
| 2 | idx_taxreduc_org_taxperi |  | forgid,ftaxperiod |
