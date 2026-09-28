# 收款单-cas_recbill_f7

## 收款单-分表 t_cas_receivingbill_e

- **表名称：** 收款单-分表
- **表名：** t_cas_receivingbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayernumber | fpayernumber | varchar | 255 |  | √ | ' ' |  |
| 3 | fitempayerid | fitempayerid | int8 | 64 |  | √ | 0 |  |
| 4 | facttradedate | facttradedate | timestamp | 0 |  |  | null |  |
| 5 | fadjusteprofitloss | fadjusteprofitloss | numeric | 19 | 6 | √ | 0 |  |
| 6 | fhandmttransdetail | fhandmttransdetail | bpchar | 1 |  | √ | '0' |  |
| 7 | fitempayertypeid | fitempayertypeid | varchar | 30 |  | √ | ' ' |  |
| 8 | fsalerid | fsalerid | int8 | 64 |  | √ | 0 |  |
| 9 | fbankcheckflagtag_tag | fbankcheckflagtag_tag | text | 0 |  |  | null |  |
| 10 | fbackdate | fbackdate | timestamp | 0 |  |  | null |  |
| 11 | ffee | ffee | numeric | 19 | 6 | √ | 0.000000 |  |
| 12 | fispushrefund | fispushrefund | bpchar | 1 |  | √ | '0' |  |
| 13 | fprojectdataid | fprojectdataid | int8 | 64 |  | √ | 0 |  |
| 14 | fquotation | fquotation | varchar | 30 |  | √ | '0' |  |
| 15 | fismatchtransdetail | fismatchtransdetail | varchar | 16 |  | √ | '0' |  |
| 16 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 17 | fbackuserid | fbackuserid | int8 | 64 |  | √ | 0 |  |
| 18 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 19 | fhotaccount | fhotaccount | bpchar | 1 |  | √ | '0' |  |
| 20 | fisrefund | fisrefund | bpchar | 1 |  | √ | '0' |  |
| 21 | fconfirmlogo | fconfirmlogo | bpchar | 1 |  | √ | '0' |  |
| 22 | fisclaimchange | fisclaimchange | bpchar | 1 |  | √ | '0' |  |
| 23 | frefundbatchseqid | frefundbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 24 | fisfullrefund | fisfullrefund | bpchar | 1 |  | √ | '0' |  |
| 25 | fvouchernum | fvouchernum | varchar | 255 |  | √ | ' ' |  |
| 26 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 27 | fbookdate_hw | fbookdate_hw | timestamp | 0 |  |  | null |  |
| 28 | factualrecdate_hw | factualrecdate_hw | timestamp | 0 |  |  | null |  |
| 29 | fimagenumber | fimagenumber | varchar | 50 |  | √ | ' ' |  |
| 30 | fmatchdetailtype | fmatchdetailtype | varchar | 64 |  | √ | ' ' |  |
| 31 | frecorgid | frecorgid | int8 | 64 |  | √ | 0 |  |
| 32 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 33 | fbankcheckflagtag | fbankcheckflagtag | text | 0 |  |  | null |  |
| 34 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 35 | fisunclaim | fisunclaim | bpchar | 1 |  | √ | '0' |  |
| 36 | fisperiod | fisperiod | bpchar | 1 |  | √ | '0' |  |
| 37 | fisvirtual | fisvirtual | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_rece_e |  | frefundbatchseqid |
| 2 | idx_cas_rece_finneraccountid |  | finneraccountid |
| 3 | t_cas_receivingbill_e_pkey |  | fid |
| 4 | idx_cas_rece_fitempayerid |  | fitempayerid |

---

## 收款单-多语言表 t_cas_receivingbill_l

- **表名称：** 收款单-多语言表
- **表名：** t_cas_receivingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 收款单-主表 t_cas_receivingbill

- **表名称：** 收款单-主表
- **表名：** t_cas_receivingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpaymentmode | fpaymentmode | varchar | 30 |  | √ | ' ' |  |
| 3 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fbankcheckflag | fbankcheckflag | varchar | 1024 |  | √ | ' ' |  |
| 5 | forgid | 收款人（公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 7 | freceivingtypeid | freceivingtypeid | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpayeeacctbankid | 银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 10 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fpayeeacctcashid | fpayeeacctcashid | int8 | 64 |  | √ | 0 |  |
| 12 | fpayername | fpayername | varchar | 255 |  | √ | ' ' |  |
| 13 | fclerk | fclerk | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 15 | fcashierid | fcashierid | int8 | 64 |  | √ | 0 |  |
| 16 | fisagent | fisagent | bpchar | 1 |  | √ | '0' |  |
| 17 | ffundflowitem | ffundflowitem | int8 | 64 |  | √ | 0 |  |
| 18 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 E :变更中 G :已退单 |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fdescription | fdescription | varchar | 255 |  |  | null |  |
| 22 | fpayeraccformid | fpayeraccformid | varchar | 30 |  | √ | ' ' |  |
| 23 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 26 | fpayeedate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 28 | fpayerbanknum | 付款账户 | varchar | 255 |  | √ | ' ' | 付款账户 |
| 29 | fbusinesstype | fbusinesstype | int8 | 64 |  | √ | 0 |  |
| 30 | fhotaccountbillid | fhotaccountbillid | int8 | 64 |  | √ | 0 |  |
| 31 | fbiztype | fbiztype | varchar | 30 |  | √ | ' ' |  |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | faccountcash | faccountcash | int8 | 64 |  | √ | 0 |  |
| 34 | fisarchive | fisarchive | bpchar | 1 |  | √ | '0' |  |
| 35 | factpayaccountid | factpayaccountid | int8 | 64 |  | √ | 0 |  |
| 36 | fpayerid | 付款人ID | int8 | 64 |  | √ | 0 | 付款人ID |
| 37 | fpayeracctbankid | fpayeracctbankid | int8 | 64 |  | √ | 0 |  |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 42 | fpayertypeid | fpayertypeid | varchar | 30 |  | √ | ' ' |  |
| 43 | fpayerformid | fpayerformid | varchar | 30 |  | √ | ' ' |  |
| 44 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 45 | fsourcebillnumber | fsourcebillnumber | varchar | 255 |  | √ | ' ' |  |
| 46 | flocalamt | flocalamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 47 | fsettletnumber | fsettletnumber | varchar | 2000 |  | √ | ' ' |  |
| 48 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 49 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 50 | factrecamt | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 51 | fcurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_rece_fsourcebillid |  | fsourcebillid |
| 2 | idx_cas_rece_fcurrencyid |  | fcurrencyid |
| 3 | t_cas_receivingbill_pkey |  | fid |
| 4 | idx_cas_rece_dateorg |  | fbizdate,forgid |
| 5 | idx_cas_rece_dso |  | fbizdate,fbillstatus,forgid |
| 6 | idx_cas_rece_statusorgid |  | fbillstatus,forgid |
| 7 | idx_cas_rece_billno |  | fbillno |
| 8 | idx_cas_rece_fpayername |  | fpayername |
| 9 | idx_cas_rece_forgid |  | forgid |
| 10 | idx_cas_rece__fpayerid |  | fpayerid |
| 11 | idx_cas_rece_freceivingtypeid |  | freceivingtypeid |
