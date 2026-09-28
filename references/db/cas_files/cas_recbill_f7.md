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
| 5 | fsourcemigratedata | fsourcemigratedata | varchar | 80 |  | √ | ' ' |  |
| 6 | fislockexratedate | fislockexratedate | bpchar | 1 |  | √ | '0' |  |
| 7 | fadjusteprofitloss | fadjusteprofitloss | numeric | 19 | 6 | √ | 0 |  |
| 8 | fhandmttransdetail | fhandmttransdetail | bpchar | 1 |  | √ | '0' |  |
| 9 | fitempayertypeid | fitempayertypeid | varchar | 30 |  | √ | ' ' |  |
| 10 | fmigrateentrydata | fmigrateentrydata | varchar | 1000 |  | √ | ' ' |  |
| 11 | fsalerid | fsalerid | int8 | 64 |  | √ | 0 |  |
| 12 | fbankcheckflagtag_tag | fbankcheckflagtag_tag | text | 0 |  |  | null |  |
| 13 | fbackdate | fbackdate | timestamp | 0 |  |  | null |  |
| 14 | ffee | ffee | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | fispushrefund | fispushrefund | bpchar | 1 |  | √ | '0' |  |
| 16 | fprojectdataid | fprojectdataid | int8 | 64 |  | √ | 0 |  |
| 17 | fquotation | fquotation | varchar | 30 |  | √ | '0' |  |
| 18 | fismatchtransdetail | fismatchtransdetail | varchar | 16 |  | √ | '0' |  |
| 19 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 20 | fbackuserid | fbackuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 22 | fchangeamount | fchangeamount | numeric | 23 | 10 | √ | 0 |  |
| 23 | fhotaccount | fhotaccount | bpchar | 1 |  | √ | '0' |  |
| 24 | fdetailid | fdetailid | varchar | 200 |  | √ | ' ' |  |
| 25 | fisrefund | fisrefund | bpchar | 1 |  | √ | '0' |  |
| 26 | fconfirmlogo | fconfirmlogo | bpchar | 1 |  | √ | '0' |  |
| 27 | fisclaimchange | fisclaimchange | bpchar | 1 |  | √ | '0' |  |
| 28 | frefundbatchseqid | frefundbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 29 | fischangeamount | fischangeamount | bpchar | 1 |  | √ | '0' |  |
| 30 | fisfullrefund | fisfullrefund | bpchar | 1 |  | √ | '0' |  |
| 31 | fvouchernum | fvouchernum | varchar | 255 |  | √ | ' ' |  |
| 32 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 33 | fbookdate_hw | fbookdate_hw | timestamp | 0 |  |  | null |  |
| 34 | factualrecdate_hw | factualrecdate_hw | timestamp | 0 |  |  | null |  |
| 35 | fistransfer | fistransfer | bpchar | 1 |  | √ | '0' |  |
| 36 | fimagenumber | fimagenumber | varchar | 50 |  | √ | ' ' |  |
| 37 | fmatchdetailtype | fmatchdetailtype | varchar | 64 |  | √ | ' ' |  |
| 38 | ftransfertype | ftransfertype | varchar | 30 |  | √ | ' ' |  |
| 39 | frecorgid | frecorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 41 | fbankcheckflagtag | fbankcheckflagtag | text | 0 |  |  | null |  |
| 42 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 43 | fisunclaim | fisunclaim | bpchar | 1 |  | √ | '0' |  |
| 44 | fisperiod | fisperiod | bpchar | 1 |  | √ | '0' |  |
| 45 | fisvirtual | fisvirtual | bpchar | 1 |  | √ | '0' |  |

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
| 4 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 5 | fbankcheckflag | fbankcheckflag | varchar | 1024 |  | √ | ' ' |  |
| 6 | forgid | 收款人（公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 8 | fk_bj73_dsorg | fk_bj73_dsorg | int8 | 64 |  | √ | 0 |  |
| 9 | freceivingtypeid | freceivingtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fpayeeacctbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 12 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fpayeeacctcashid | fpayeeacctcashid | int8 | 64 |  | √ | 0 |  |
| 14 | fpayername | fpayername | varchar | 255 |  | √ | ' ' |  |
| 15 | fclerk | fclerk | int8 | 64 |  | √ | 0 |  |
| 16 | fbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 17 | fcashierid | fcashierid | int8 | 64 |  | √ | 0 |  |
| 18 | fisagent | fisagent | bpchar | 1 |  | √ | '0' |  |
| 19 | ffundflowitem | ffundflowitem | int8 | 64 |  | √ | 0 |  |
| 20 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 E :变更中 G :已退单 |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fdescription | fdescription | varchar | 255 |  |  | null |  |
| 24 | fpayeraccformid | fpayeraccformid | varchar | 30 |  | √ | ' ' |  |
| 25 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 27 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 28 | fpayeedate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 29 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 30 | fpayerbanknum | 付款账户 | varchar | 255 |  | √ | ' ' | 付款账户 |
| 31 | fbusinesstype | fbusinesstype | int8 | 64 |  | √ | 0 |  |
| 32 | fhotaccountbillid | fhotaccountbillid | int8 | 64 |  | √ | 0 |  |
| 33 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 34 | fk_bj73_textfield1 | fk_bj73_textfield1 | varchar | 50 |  | √ | ' ' |  |
| 35 | fbiztype | fbiztype | varchar | 30 |  | √ | ' ' |  |
| 36 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 37 | faccountcash | faccountcash | int8 | 64 |  | √ | 0 |  |
| 38 | fisarchive | fisarchive | bpchar | 1 |  | √ | '0' |  |
| 39 | factpayaccountid | factpayaccountid | int8 | 64 |  | √ | 0 |  |
| 40 | fpayerid | 付款人ID | int8 | 64 |  | √ | 0 | 付款人ID |
| 41 | fpayeracctbankid | fpayeracctbankid | int8 | 64 |  | √ | 0 |  |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 44 | fsuretybiztype | fsuretybiztype | varchar | 50 |  | √ | ' ' |  |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 47 | fpayertypeid | fpayertypeid | varchar | 30 |  | √ | ' ' |  |
| 48 | fpayerformid | fpayerformid | varchar | 30 |  | √ | ' ' |  |
| 49 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 50 | fsourcebillnumber | fsourcebillnumber | varchar | 255 |  | √ | ' ' |  |
| 51 | flocalamt | flocalamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 52 | fsettletnumber | fsettletnumber | varchar | 2000 |  | √ | ' ' |  |
| 53 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 54 | fk_bj73_dsamount | fk_bj73_dsamount | numeric | 23 | 10 |  | null |  |
| 55 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 56 | fk_bj73_textfield | fk_bj73_textfield | varchar | 50 |  | √ | ' ' |  |
| 57 | factrecamt | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 58 | fcurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
| 7 | idx_cas_rece_fpayername |  | fpayername |
| 8 | idx_cas_rece_billno |  | fbillno |
| 9 | idx_cas_rece_forgid |  | forgid |
| 10 | idx_cas_rece__fpayerid |  | fpayerid |
| 11 | idx_cas_rece_freceivingtypeid |  | freceivingtypeid |
