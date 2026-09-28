# 提款处理单-cfm_loanbill_f7

## 提款处理单-分表 t_cfm_loanbill_e

- **表名称：** 提款处理单-分表
- **表名：** t_cfm_loanbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | fterm | varchar | 30 |  | √ | ' ' |  |
| 3 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpaybillno | fpaybillno | varchar | 80 |  | √ | ' ' |  |
| 5 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 6 | frateadjustcycletype | frateadjustcycletype | varchar | 30 |  | √ | ' ' |  |
| 7 | fregistorgid | fregistorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreditorgid | fcreditorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fconfirmdescription | fconfirmdescription | varchar | 255 |  | √ | ' ' |  |
| 10 | fcreditorid | fcreditorid | int8 | 64 |  | √ | 0 |  |
| 11 | freceamt | freceamt | numeric | 23 | 10 | √ | 0 |  |
| 12 | fratefloatpoint | 利率浮动基点值（BP） | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点值（BP） |
| 13 | fclientorgid | fclientorgid | int8 | 64 |  | √ | 0 |  |
| 14 | ftextdebtor | ftextdebtor | varchar | 80 |  | √ | ' ' |  |
| 15 | fproductfactoryid | fproductfactoryid | int8 | 64 |  | √ | 0 |  |
| 16 | floancontractbillid | floancontractbillid | int8 | 64 |  | √ | 0 |  |
| 17 | flastrepaydate | 最近还款日 | timestamp | 0 |  |  | null | 最近还款日 |
| 18 | fcontractname | fcontractname | varchar | 80 |  | √ | ' ' |  |
| 19 | frenewalinteresttype | frenewalinteresttype | varchar | 80 |  | √ | ' ' |  |
| 20 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 21 | ftextcreditor | ftextcreditor | varchar | 80 |  | √ | ' ' |  |
| 22 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期重置 cycle :周期性重置 hand :手工重置 noadjust :不重置 |
| 23 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 24 | freferencerateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 25 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 26 | fbasis | fbasis | varchar | 30 |  | √ | ' ' |  |
| 27 | fconfirmtime | fconfirmtime | timestamp | 0 |  |  | null |  |
| 28 | fexratetypeid | fexratetypeid | int8 | 64 |  | √ | 0 |  |
| 29 | fexratedeadlineid | fexratedeadlineid | int8 | 64 |  | √ | 0 |  |
| 30 | fexrateadjustcycle | fexrateadjustcycle | int8 | 64 |  | √ | 0 |  |
| 31 | frateadjustcycle | frateadjustcycle | int8 | 64 |  | √ | 0 |  |
| 32 | frenewalinterestrate | frenewalinterestrate | numeric | 23 | 10 | √ | 0 |  |
| 33 | fconfirmstatus | fconfirmstatus | varchar | 30 |  | √ | ' ' |  |
| 34 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 35 | freturnreason | freturnreason | varchar | 255 |  | √ | ' ' |  |
| 36 | fsettlestatus | fsettlestatus | varchar | 80 |  | √ | ' ' |  |
| 37 | fstartintdate | 起息日期 | timestamp | 0 |  |  | null | 起息日期 |
| 38 | fexratesign | fexratesign | varchar | 80 |  | √ | ' ' |  |
| 39 | fexrateadjuststyle | fexrateadjuststyle | varchar | 80 |  | √ | ' ' |  |
| 40 | fdebtorid | fdebtorid | int8 | 64 |  | √ | 0 |  |
| 41 | frepayacctbankid | frepayacctbankid | int8 | 64 |  | √ | 0 |  |
| 42 | frateadjustdate | frateadjustdate | timestamp | 0 |  |  | null |  |
| 43 | fexratefloatpoint | fexratefloatpoint | numeric | 19 | 6 | √ | 0.000000 |  |
| 44 | fsettleintmode | 结息方式 | varchar | 30 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 45 | fdebtortype | fdebtortype | varchar | 30 |  | √ | ' ' |  |
| 46 | floantype | 贷款类型 | varchar | 30 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 47 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 48 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 49 | floaneracctbankid | floaneracctbankid | int8 | 64 |  | √ | 0 |  |
| 50 | fexrateadjustdate | fexrateadjustdate | timestamp | 0 |  |  | null |  |
| 51 | fratesign | 利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 52 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loanbill_e |  | flender |
| 2 | t_cfm_loanbill_e_pkey |  | fid |

---

## 提款处理单-主表 t_cfm_loanbill

- **表名称：** 提款处理单-主表
- **表名：** t_cfm_loanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceivedate | freceivedate | timestamp | 0 |  |  | null |  |
| 3 | fcontractbizdate | fcontractbizdate | timestamp | 0 |  |  | null |  |
| 4 | fabstract | fabstract | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreditlimitcurrency | fcreditlimitcurrency | int8 | 64 |  | √ | 0 |  |
| 6 | frenewalexpiredate | frenewalexpiredate | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fbitbackinfo | fbitbackinfo | varchar | 255 |  | √ | ' ' |  |
| 10 | fbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 11 | ffinproductid | ffinproductid | int8 | 64 |  | √ | 0 |  |
| 12 | flendernature | flendernature | varchar | 30 |  | √ | ' ' |  |
| 13 | fbillstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 15 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 17 | frepaymentway | 还款方式 | varchar | 30 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 18 | fcreditrate | fcreditrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fcontractbillno | fcontractbillno | varchar | 80 |  | √ | ' ' |  |
| 20 | fdiscreditamount | fdiscreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 21 | fstageplanid | fstageplanid | int8 | 64 |  | √ | 0 |  |
| 22 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 23 | fdrawway | fdrawway | varchar | 30 |  | √ | ' ' |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | faccountbankid | faccountbankid | int8 | 64 |  | √ | 0 |  |
| 26 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 27 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 28 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 29 | finteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 30 | flastpayinstdate | 上次付息日 | timestamp | 0 |  |  | null | 上次付息日 |
| 31 | fnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 32 | fpayeebillno | fpayeebillno | varchar | 80 |  | √ | ' ' |  |
| 33 | famount | 借款金额 | numeric | 19 | 6 | √ | 0.000000 | 借款金额 |
| 34 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 35 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 36 | finitendpreinstdate | finitendpreinstdate | timestamp | 0 |  |  | null |  |
| 37 | fcalculaterateamount | fcalculaterateamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | fpayinterestamount | fpayinterestamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 41 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 42 | floanrate | 放款利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 放款利率（%） |
| 43 | fdrawamount | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 47 | fdrawtype | fdrawtype | varchar | 30 |  | √ | ' ' |  |
| 48 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 49 | frepayamount | frepayamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 50 | fbizdate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 51 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 52 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | finterestsettledplanid | finterestsettledplanid | int8 | 64 |  | √ | 0 |  |
| 54 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loanbill_pkey |  | fid |
| 2 | idx_t_cfm_loanbill_bd |  | fbillno |

---

## 提款处理单-多语言表 t_cfm_loanbill_l

- **表名称：** 提款处理单-多语言表
- **表名：** t_cfm_loanbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fabstract | fabstract | varchar | 255 |  | √ | ' ' |  |
| 3 | fbitbackinfo | fbitbackinfo | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loanbill_l |  | fid,flocaleid |
| 2 | t_cfm_loanbill_l_pkey |  | fpkid |
