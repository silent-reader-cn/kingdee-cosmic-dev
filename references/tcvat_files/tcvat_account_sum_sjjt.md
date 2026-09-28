# 一般纳税人计提收入台账单据-tcvat_account_sum_sjjt

## 一般纳税人计提收入台账单据-主表 t_tcvat_income_sum_sjjt

- **表名称：** 一般纳税人计提收入台账单据-主表
- **表名：** t_tcvat_income_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvoicetaxamount | 发票收入（合计税额） | numeric | 23 | 10 | √ | 0 | 发票收入（合计税额） |
| 5 | fspecialtaxamount | 开专票税额 | numeric | 23 | 10 | √ | 0 | 开专票税额 |
| 6 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 7 | fpricetaxamount | 价税合计-合计 | numeric | 23 | 10 | √ | 0 | 价税合计-合计 |
| 8 | fnonetaxamount | 未开票税额 | numeric | 23 | 10 | √ | 0 | 未开票税额 |
| 9 | fspecialinvoiceamount | 开专票销售额 | numeric | 23 | 10 | √ | 0 | 开专票销售额 |
| 10 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0 | 业务口径 |
| 11 | fothertaxamount | 开其他票税额 | numeric | 23 | 10 | √ | 0 | 开其他票税额 |
| 12 | finitaccountingamount | 未开票收入(未开票销售额)-初始值 | numeric | 23 | 10 | √ | 0 | 未开票收入(未开票销售额)-初始值 |
| 13 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 14 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 15 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 16 | ftaxreductiontype | 减税项目类型 | varchar | 50 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 17 | faccountingamount | 未开票收入(未开票销售额) | numeric | 23 | 10 | √ | 0 | 未开票收入(未开票销售额) |
| 18 | ftaxperiod | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 19 | ftaxamount | 合计(合计销售额) | numeric | 23 | 10 | √ | 0 | 合计(合计销售额) |
| 20 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 21 | fotherinvoiceamount | 开其他票销售额 | numeric | 23 | 10 | √ | 0 | 开其他票销售额 |
| 22 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 23 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 24 | ftaxmethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 25 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 26 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0 | 发票收入 |
| 27 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 28 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 29 | ftotaltaxamount | 税额-合计 | numeric | 23 | 10 | √ | 0 | 税额-合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_income_sum_sjjt |  | fid |
| 2 | idx_orgid_taxperiod |  | forgid,ftaxperiod |
