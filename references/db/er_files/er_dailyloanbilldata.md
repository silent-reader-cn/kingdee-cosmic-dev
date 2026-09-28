# 借款单基础资料-er_dailyloanbilldata

## 单据体-子表 t_er_accountinfo

- **表名称：** 单据体-子表
- **表名：** t_er_accountinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwriteoffamount | fwriteoffamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | faccountcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fbuildedamount | fbuildedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | forgirepaidamount | forgirepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpayeraccount01 | fpayeraccount01 | varchar | 100 |  | √ | ' ' |  |
| 8 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | '0' |  |
| 9 | fpayerdeptid | fpayerdeptid | int8 | 64 |  | √ | 0 |  |
| 10 | fpayercompid | fpayercompid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayertype | fpayertype | varchar | 30 |  | √ | ' ' |  |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | forgiapplyedreimamount | forgiapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | forgiwriteoffamount | forgiwriteoffamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | famount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 16 | foriaccnotpayamount | foriaccnotpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fpayername | fpayername | varchar | 100 |  | √ | ' ' |  |
| 19 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 20 | fentryrepaydate | fentryrepaydate | timestamp | 0 |  |  | null |  |
| 21 | fpayeraccountname | fpayeraccountname | varchar | 100 |  | √ | ' ' |  |
| 22 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 23 | faccbalanceamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 24 | fapplyedreimamount | fapplyedreimamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | facccostcompany | facccostcompany | int8 | 64 |  | √ | 0 |  |
| 26 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 27 | fpayerbankid | fpayerbankid | int8 | 64 |  | √ | 0 |  |
| 28 | frepaidamount | frepaidamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fpaymodeid | fpaymodeid | int8 | 64 |  | √ | 0 |  |
| 30 | foriaccpayedamount | foriaccpayedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | foriaccbalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 32 | faccpayedamount | faccpayedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fcasorg | fcasorg | int8 | 64 |  | √ | 0 |  |
| 34 | faccnotpayamount | faccnotpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fbanklogo | fbanklogo | varchar | 50 |  | √ | ' ' |  |
| 36 | faccounttype | faccounttype | varchar | 10 |  | √ | ' ' |  |
| 37 | fpayeraccount02 | fpayeraccount02 | varchar | 100 |  | √ | ' ' |  |
| 38 | fpayeraccount | fpayeraccount | varchar | 100 |  | √ | ' ' |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fquotetype | fquotetype | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_accountinfo_pkey |  | fentryid |
| 2 | idx_er_accountinfo_fseq |  | fid,fseq |

---

## 借款单基础资料-主表 t_er_dailyloanbill

- **表名称：** 借款单基础资料-主表
- **表名：** t_er_dailyloanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | funauditmsg | varchar | 1000 |  |  | null |  |
| 3 | fpaycompanyid | fpaycompanyid | int8 | 64 |  | √ | 0 |  |
| 4 | finvokeinvoicecloud | finvokeinvoicecloud | bpchar | 1 |  | √ | '0' |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fcostdeptid | fcostdeptid | int8 | 64 |  | √ | 0 |  |
| 7 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 8 | fhead_paydate | fhead_paydate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fstdcostcenterid | fstdcostcenterid | int8 | 64 |  | √ | 0 |  |
| 11 | fattachmentcount | fattachmentcount | int4 | 32 |  | √ | 0 |  |
| 12 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 13 | fismanualrepay | fismanualrepay | bpchar | 1 |  | √ | '0' |  |
| 14 | fbookeddate | fbookeddate | timestamp | 0 |  |  | null |  |
| 15 | fbillno | 借款单号 | varchar | 80 |  | √ | ' ' | 借款单号 |
| 16 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fdescription | 事由 | varchar | 1000 |  |  | null | 事由 |
| 19 | fisenableinvoice | fisenableinvoice | bpchar | 1 |  | √ | '0' |  |
| 20 | fimagenumber | fimagenumber | varchar | 80 |  | √ | ' ' |  |
| 21 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 22 | fappliedreimburseamount | fappliedreimburseamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fapproveamount | fapproveamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fnotpayamount | fnotpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 27 | fneedimagescan | fneedimagescan | bpchar | 1 |  | √ | '0' |  |
| 28 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 29 | fbalanceamount | fbalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fisoverbudget | fisoverbudget | bpchar | 1 |  | √ | '0' |  |
| 31 | ftel | ftel | varchar | 100 |  | √ | ' ' |  |
| 32 | fpayamount | fpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | freturnedamount | freturnedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | frelatedbiz | frelatedbiz | varchar | 50 |  | √ | 'relatedtype_other' |  |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fusedamount | fusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fisimport | fisimport | bpchar | 1 |  | √ | '0' |  |
| 38 | fcostcompanyid | fcostcompanyid | int8 | 64 |  | √ | 0 |  |
| 39 | fformid | fformid | varchar | 30 |  | √ | ' ' |  |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 42 | fismultireimburser | fismultireimburser | bpchar | 1 |  | √ | '0' |  |
| 43 | fiscurrency | fiscurrency | bpchar | 1 |  | √ | '0' |  |
| 44 | fisstopreim | fisstopreim | bpchar | 1 |  | √ | '0' |  |
| 45 | fauditopinion | fauditopinion | varchar | 255 |  | √ | ' ' |  |
| 46 | floanamount | floanamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | fisbuildreimbill | fisbuildreimbill | bpchar | 1 |  | √ | '0' |  |
| 48 | fapplierid | fapplierid | int8 | 64 |  | √ | 0 |  |
| 49 | fispaybyhead | fispaybyhead | bpchar | 1 |  | √ | '0' |  |
| 50 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 51 | fstopdescription | fstopdescription | varchar | 1000 |  | √ | ' ' |  |
| 52 | fisadvance | fisadvance | bpchar | 1 |  | √ | '0' |  |
| 53 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 54 | frepaymentdate | frepaymentdate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_dlb_fapplierid |  | fapplierid |
| 2 | idx_er_dlb_fcreatorid |  | fcreatorid |
| 3 | idx_er_dlb_fbillstatus |  | fbillstatus |
| 4 | idx_er_dlb_forgid |  | forgid |
| 5 | idx_er_dlb_fcompanyid |  | fcompanyid |
| 6 | t_er_dailyloanbill_pkey |  | fid |
| 7 | idx_er_dlb_fbizdate_fbillno |  | fbizdate,fbillno |
| 8 | idx_er_dlb_fbillno |  | fbillno |
