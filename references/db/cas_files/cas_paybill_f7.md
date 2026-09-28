# 付款单-cas_paybill_f7

## 付款单-主表 t_cas_paymentbill

- **表名称：** 付款单-主表
- **表名：** t_cas_paymentbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 内码 | int8 | 64 |  | √ | 0 | 内码 |
| 2 | fpayernumber | fpayernumber | varchar | 500 |  | √ | ' ' |  |
| 3 | fpaymentmode | fpaymentmode | varchar | 30 |  | √ | ' ' |  |
| 4 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fbankcheckflag | fbankcheckflag | varchar | 1024 |  | √ | ' ' |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fpayeetypeid | fpayeetypeid | varchar | 30 |  | √ | ' ' |  |
| 8 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 9 | fpaymentidentifyid | fpaymentidentifyid | int8 | 64 |  | √ | 0 |  |
| 10 | fpayeeaccformid | fpayeeaccformid | varchar | 30 |  | √ | ' ' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fpayeeformid | fpayeeformid | varchar | 30 |  | √ | ' ' |  |
| 13 | fpayeeacctbankid | fpayeeacctbankid | int8 | 64 |  | √ | 0 |  |
| 14 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | freccountryid | freccountryid | int8 | 64 |  | √ | 0 |  |
| 16 | fbankpaystatus | fbankpaystatus | varchar | 5 |  | √ | ' ' |  |
| 17 | fissingle | fissingle | bpchar | 1 |  | √ | '0' |  |
| 18 | fbusinesstypebase | fbusinesstypebase | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 20 | fbatchseqid | fbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 21 | factpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 22 | fcashierid | fcashierid | int8 | 64 |  | √ | 0 |  |
| 23 | fpayeeacctbank | fpayeeacctbank | int8 | 64 |  | √ | 0 |  |
| 24 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 F :银行退票 G :已退单 H :已作废 I :退款 J :票据处理中 |
| 26 | fpayeebankname | fpayeebankname | varchar | 255 |  | √ | ' ' |  |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fdescription | fdescription | varchar | 255 |  |  | null |  |
| 29 | frecprovince | frecprovince | varchar | 80 |  | √ | ' ' |  |
| 30 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 31 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 33 | fcommitbetime | fcommitbetime | timestamp | 0 |  |  | null |  |
| 34 | fpriority | fpriority | varchar | 30 |  | √ | ' ' |  |
| 35 | frecaccbankname | frecaccbankname | varchar | 255 |  | √ | ' ' |  |
| 36 | fdetailseqid | fdetailseqid | varchar | 80 |  | √ | ' ' |  |
| 37 | fbankpayingid | fbankpayingid | int8 | 64 |  | √ | 0 |  |
| 38 | fhotaccountbillid | fhotaccountbillid | int8 | 64 |  | √ | 0 |  |
| 39 | fistop | fistop | bpchar | 1 |  | √ | '0' |  |
| 40 | fusage | fusage | varchar | 255 |  |  | null |  |
| 41 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 42 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 43 | fisarchive | fisarchive | bpchar | 1 |  | √ | '0' |  |
| 44 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 45 | fiscommitbe | fiscommitbe | bpchar | 1 |  | √ | '0' |  |
| 46 | fisrefund | fisrefund | bpchar | 1 |  | √ | '0' |  |
| 47 | fpayeename | fpayeename | varchar | 255 |  | √ | ' ' |  |
| 48 | funiformsocialcreditcode | funiformsocialcreditcode | varchar | 100 |  | √ | ' ' |  |
| 49 | fpayeracctbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 50 | fpayeracctcashid | fpayeracctcashid | int8 | 64 |  | √ | 0 |  |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 53 | fpayeebanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 54 | flocalamount | flocalamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 55 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 56 | ffundflowitemid | ffundflowitemid | int8 | 64 |  | √ | 0 |  |
| 57 | fsettlettypeid | fsettlettypeid | int8 | 64 |  | √ | 0 |  |
| 58 | freccity | freccity | varchar | 80 |  | √ | ' ' |  |
| 59 | fpayeenumber | fpayeenumber | varchar | 500 |  | √ | ' ' |  |
| 60 | fpayeeid | fpayeeid | int8 | 64 |  | √ | 0 |  |
| 61 | frecbanknumber | frecbanknumber | varchar | 30 |  | √ | ' ' |  |
| 62 | fentrance | fentrance | varchar | 10 |  | √ | ' ' |  |
| 63 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 64 | fsourcebillnumber | fsourcebillnumber | varchar | 255 |  | √ | ' ' |  |
| 65 | fsettletnumber | fsettletnumber | varchar | 2000 |  | √ | ' ' |  |
| 66 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 67 | fpaymenttypeid | fpaymenttypeid | int8 | 64 |  | √ | 0 |  |
| 68 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 69 | fcurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 70 | fbankreturnmsg | fbankreturnmsg | varchar | 255 |  |  | null |  |
| 71 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pb_dos |  | fbizdate,forgid,fbillstatus |
| 2 | idx_cas_pb_fbilltypeid |  | fbilltypeid |
| 3 | t_cas_paymentbill_pkey |  | fid |
| 4 | idx_cas_pb_fcurrencyid |  | fcurrencyid |
| 5 | idx_cas_pb_obd |  | forgid,fbilltypeid,fbizdate |
| 6 | idx_cas_pb_fbillno |  | fbillno |
| 7 | idx_cas_pb_fopenorgid |  | fopenorgid |
| 8 | idx_cas_pb_fpayeracctbankid |  | fpayeracctbankid |
| 9 | idx_cas_pb_fsourcebilltype |  | fsourcebilltype |
| 10 | idx_cas_pb_fpaydate |  | fpaydate |
| 11 | idx_cas_pb_fsourcebillid |  | fsourcebillid |
| 12 | idx_cas_pb_fpaymenttypeid |  | fpaymenttypeid |

---

## 付款单-多语言表 t_cas_paymentbill_l

- **表名称：** 付款单-多语言表
- **表名：** t_cas_paymentbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
