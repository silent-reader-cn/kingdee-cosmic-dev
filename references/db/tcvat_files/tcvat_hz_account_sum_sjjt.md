# 总机构收入台账单据-tcvat_hz_account_sum_sjjt

## 总机构收入台账单据-主表 t_tcvat_hz_account_sum_jt

- **表名称：** 总机构收入台账单据-主表
- **表名：** t_tcvat_hz_account_sum_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsuborgname | fsuborgname | varchar | 50 |  | √ | ' ' |  |
| 5 | finvoicetaxamount | 发票收入（合计税额） | numeric | 23 | 10 | √ | 0 | 发票收入（合计税额） |
| 6 | fspecialtaxamount | 开专票税额 | numeric | 23 | 10 | √ | 0 | 开专票税额 |
| 7 | fjzjt | 即征即退业务 | varchar | 50 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 8 | fpricetaxamount | 价税合计-合计 | numeric | 23 | 10 | √ | 0 | 价税合计-合计 |
| 9 | fnonetaxamount | 未开票税额 | numeric | 23 | 10 | √ | 0 | 未开票税额 |
| 10 | fspecialinvoiceamount | 开专票销售额 | numeric | 23 | 10 | √ | 0 | 开专票销售额 |
| 11 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0 | 业务口径 |
| 13 | fothertaxamount | 开其他票税额 | numeric | 23 | 10 | √ | 0 | 开其他票税额 |
| 14 | fsuborgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | finitaccountingamount | 未开票收入-初始值 | numeric | 23 | 10 | √ | 0 | 未开票收入-初始值 |
| 16 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 17 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 18 | ftaxpayertype | 纳税人类型 | varchar | 50 |  | √ | ' ' | 纳税人类型 |
| 19 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 20 | ftaxreductiontype | 减税项目类型 | varchar | 50 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 21 | fnrjzjtjs | 纳入进项即征即退分摊计算 | varchar | 50 |  | √ | ' ' | 纳入进项即征即退分摊计算,枚举: 0 :否 1 :是 |
| 22 | faccountingamount | 未开票收入 | numeric | 23 | 10 | √ | 0 | 未开票收入 |
| 23 | ftaxamount | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 24 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 25 | fotherinvoiceamount | 开其他票销售额 | numeric | 23 | 10 | √ | 0 | 开其他票销售额 |
| 26 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: |
| 27 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 28 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 29 | ftaxmethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 30 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 31 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 32 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0 | 发票收入 |
| 33 | fdeadline | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 34 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 35 | ftotaltaxamount | 税额-合计 | numeric | 23 | 10 | √ | 0 | 税额-合计 |
| 36 | flevelname | 层级 | varchar | 50 |  | √ | ' ' | 层级,枚举: 1 :1级 2 :2级 3 :3级 4 :4级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_hz_account_sum_jt |  | forgid,fstartdate,fenddate |
| 2 | pk_tcvat_hz_account_sum_jt |  | fid |
