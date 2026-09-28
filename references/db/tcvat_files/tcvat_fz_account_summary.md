# 分支收入台账单据-tcvat_fz_account_summary

## 分支收入台账单据-主表 t_tcvat_fz_income_summary

- **表名称：** 分支收入台账单据-主表
- **表名：** t_tcvat_fz_income_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 合计 | numeric | 23 | 10 | √ | 0.0000000000 | 合计 |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 4 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdeclaretype | 申报类型 | varchar | 30 |  | √ | ' ' | 申报类型,枚举: 1 :汇总申报 2 :自主申报 |
| 7 | ftaxreductionid | 减免税性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 8 | fdescription | 业务描述 | varchar | 50 |  | √ | ' ' | 业务描述 |
| 9 | ftaxmethod | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 10 | fjzjt | 即征即退业务 | varchar | 30 |  | √ | ' ' | 即征即退业务,枚举: 0 :否 1 :是 |
| 11 | ftaxreductioncode | 减税性质代码 | varchar | 50 |  | √ | ' ' | 减税性质代码 |
| 12 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fbusinessamount | 业务口径 | numeric | 23 | 10 | √ | 0.0000000000 | 业务口径 |
| 14 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 15 | finvoiceamount | 发票收入 | numeric | 23 | 10 | √ | 0.0000000000 | 发票收入 |
| 16 | ftaxreductionname | 减税项目名称 | varchar | 200 |  | √ | ' ' | 减税项目名称 |
| 17 | ftaxmethodtype | 征收方式编码 | varchar | 20 |  | √ | ' ' | 征收方式编码 |
| 18 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 19 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 税收分类编码表 tpo_tcvat_taxrateentry |
| 20 | ftaxreductiontype | 减税项目类型 | varchar | 30 |  | √ | ' ' | 减税项目类型,枚举: 1 :免税 2 :减征 3 :扣减 4 :递减 : |
| 21 | faccountingamount | 未开票收入 | numeric | 23 | 10 | √ | 0.0000000000 | 未开票收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fz_income_summary |  | fid |
| 2 | idx_tcvat_fz_income_summary |  | forgid,fstartdate,fenddate |
