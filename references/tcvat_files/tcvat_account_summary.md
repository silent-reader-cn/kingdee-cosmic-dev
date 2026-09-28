# 收入台账单据-tcvat_account_summary

## 收入台账单据-主表 t_tcvat_income_summary

- **表名称：** 收入台账单据-主表
- **表名：** t_tcvat_income_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率 | varchar | 100 |  | √ | ' ' | 税率 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcreaterid | fcreaterid | int8 | 64 |  | √ | 0 |  |
| 5 | finvoicetaxamount | 发票收入（合计税额） | numeric | 23 | 10 | √ | 0.0000000000 | 发票收入（合计税额） |
| 6 | fspecialtaxamount | 开专票税额 | numeric | 23 | 10 | √ | 0 | 开专票税额 |
| 7 | fjzjt | 即征即退业务 | varchar | 30 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 8 | fnonetaxamount | 未开票税额 | numeric | 23 | 10 | √ | 0 | 未开票税额 |
| 9 | fpricetaxamount | 价税合计-合计 | numeric | 23 | 10 | √ | 0 | 价税合计-合计 |
| 10 | fspecialinvoiceamount | 开专票销售额 | numeric | 23 | 10 | √ | 0 | 开专票销售额 |
| 11 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0.0000000000 | 业务口径 |
| 12 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 13 | fothertaxamount | 开其他票税额 | numeric | 23 | 10 | √ | 0 | 开其他票税额 |
| 14 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 15 | finitaccountingamount | 未开票收入(未开票销售额)-初始值 | numeric | 23 | 10 | √ | 0 | 未开票收入(未开票销售额)-初始值 |
| 16 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 17 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 18 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 19 | ftaxreductiontype | 减税项目类型 | varchar | 30 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 20 | faccountingamount | 未开票收入(未开票销售额) | numeric | 23 | 10 | √ | 0.0000000000 | 未开票收入(未开票销售额) |
| 21 | fextendtaxperiod | 所属税期起扩展字段 | timestamp | 0 |  |  | null | 所属税期起扩展字段 |
| 22 | ftaxamount | 合计(合计销售额) | numeric | 23 | 10 | √ | 0.0000000000 | 合计(合计销售额) |
| 23 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 24 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 25 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 26 | fotherinvoiceamount | 开其他票销售额 | numeric | 23 | 10 | √ | 0 | 开其他票销售额 |
| 27 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 28 | fdescription | 业务描述 | varchar | 100 |  | √ | ' ' | 业务描述 |
| 29 | ftaxmethod | 征收方式 | varchar | 100 |  | √ | ' ' | 征收方式 |
| 30 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 31 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0.0000000000 | 发票收入 |
| 32 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 33 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 34 | ftotaltaxamount | 税额-合计 | numeric | 23 | 10 | √ | 0 | 税额-合计 |

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
