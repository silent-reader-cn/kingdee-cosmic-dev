# 收入台账单据-tcvat_account_summary

## 收入台账单据-主表 t_tcvat_income_summary

- **表名称：** 收入台账单据-主表
- **表名：** t_tcvat_income_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fewblxh | ewblxh | varchar | 30 |  | √ | ' ' | ewblxh,枚举: 1 :行号 count :合计行 |
| 4 | ftaxrate | 税率 | varchar | 100 |  | √ | ' ' | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 7 | finvoicetaxamount | 发票收入（合计税额） | numeric | 23 | 10 | √ | 0.0000000000 | 发票收入（合计税额） |
| 8 | fspecialtaxamount | 开专票税额 | numeric | 23 | 10 | √ | 0 | 开专票税额 |
| 9 | ftaxplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 10 | fjzjt | 即征即退业务 | varchar | 30 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 11 | fnonetaxamount | 未开票税额 | numeric | 23 | 10 | √ | 0 | 未开票税额 |
| 12 | fpricetaxamount | 价税合计-合计 | numeric | 23 | 10 | √ | 0 | 价税合计-合计 |
| 13 | fspecialinvoiceamount | 开专票销售额 | numeric | 23 | 10 | √ | 0 | 开专票销售额 |
| 14 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0.0000000000 | 业务口径 |
| 15 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 16 | fothertaxamount | 开其他票税额 | numeric | 23 | 10 | √ | 0 | 开其他票税额 |
| 17 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 18 | finitaccountingamount | 未开票收入(未开票销售额)-初始值 | numeric | 23 | 10 | √ | 0 | 未开票收入(未开票销售额)-初始值 |
| 19 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 21 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 22 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 23 | ftaxreductiontype | 减税项目类型 | varchar | 30 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 24 | fnrjzjtjs | 纳入进项即征即退分摊计算 | varchar | 50 |  | √ | ' ' | 纳入进项即征即退分摊计算,枚举: 0 :否 1 :是 |
| 25 | faccountingamount | 未开票收入(未开票销售额) | numeric | 23 | 10 | √ | 0.0000000000 | 未开票收入(未开票销售额) |
| 26 | fextendtaxperiod | 所属税期起扩展字段 | timestamp | 0 |  |  | null | 所属税期起扩展字段 |
| 27 | ftaxamount | 合计(合计销售额) | numeric | 23 | 10 | √ | 0.0000000000 | 合计(合计销售额) |
| 28 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 29 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 30 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 31 | fotherinvoiceamount | 开其他票销售额 | numeric | 23 | 10 | √ | 0 | 开其他票销售额 |
| 32 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 33 | fbizdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 34 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 35 | fdescription | 业务描述 | varchar | 100 |  | √ | ' ' | 业务描述 |
| 36 | fewblname | ewblname | varchar | 50 |  | √ | ' ' | ewblname |
| 37 | ftaxmethod | 征收方式 | varchar | 100 |  | √ | ' ' | 征收方式 |
| 38 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 39 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0.0000000000 | 发票收入 |
| 40 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 41 | fsbbid | sbbid | varchar | 50 |  | √ | ' ' | sbbid |
| 42 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 43 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 44 | ftotaltaxamount | 税额-合计 | numeric | 23 | 10 | √ | 0 | 税额-合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_income_summary_pkey |  | fid |
| 2 | idx_income_summary_fserialno |  | fserialno |
| 3 | idx_t_tcvat_income_summary |  | forgid,ftaxperiod |
