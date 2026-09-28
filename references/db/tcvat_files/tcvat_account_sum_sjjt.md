# 一般纳税人计提收入台账单据-tcvat_account_sum_sjjt

## 一般纳税人计提收入台账单据-主表 t_tcvat_income_sum_sjjt

- **表名称：** 一般纳税人计提收入台账单据-主表
- **表名：** t_tcvat_income_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 4 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 5 | ftaxperioddate | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvoicetaxamount | 发票收入（合计税额） | numeric | 23 | 10 | √ | 0 | 发票收入（合计税额） |
| 8 | fspecialtaxamount | 开具专票税额 | numeric | 23 | 10 | √ | 0 | 开具专票税额 |
| 9 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 10 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 11 | fpricetaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 12 | fnonetaxamount | 未开具发票税额 | numeric | 23 | 10 | √ | 0 | 未开具发票税额 |
| 13 | fspecialinvoiceamount | 开具专票销售额 | numeric | 23 | 10 | √ | 0 | 开具专票销售额 |
| 14 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0 | 业务口径 |
| 15 | fothertaxamount | 开具其他发票税额 | numeric | 23 | 10 | √ | 0 | 开具其他发票税额 |
| 16 | finitaccountingamount | 未开票收入(未开票销售额)-初始值 | numeric | 23 | 10 | √ | 0 | 未开票收入(未开票销售额)-初始值 |
| 17 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 19 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 20 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 21 | ftaxreductiontype | 减税项目类型 | varchar | 50 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 22 | fnrjzjtjs | 纳入进项即征即退分摊计算 | varchar | 50 |  | √ | ' ' | 纳入进项即征即退分摊计算,枚举: 0 :否 1 :是 |
| 23 | faccountingamount | 未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 未开具发票销售额 |
| 24 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 25 | ftaxamount | 销售额合计 | numeric | 23 | 10 | √ | 0 | 销售额合计 |
| 26 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 27 | fotherinvoiceamount | 开具其他发票销售额 | numeric | 23 | 10 | √ | 0 | 开具其他发票销售额 |
| 28 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 29 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 30 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 31 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 32 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 33 | ftaxmethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 34 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 35 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0 | 发票收入 |
| 36 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 37 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 38 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 39 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 40 | ftotaltaxamount | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_income_sum_sjjt |  | fid |
| 2 | idx_orgid_taxperiod |  | forgid,ftaxperiod |
