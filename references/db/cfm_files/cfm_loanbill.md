# 提款模板-cfm_loanbill

## 利率调整分录-子表 t_cfm_loanbill_rh_entry

- **表名称：** 利率调整分录-子表
- **表名：** t_cfm_loanbill_rh_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frhmodifydate | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 3 | frhremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | frhmodifier | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frheffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | frhrateadjno | 调整单编号 | varchar | 60 |  | √ | ' ' | 调整单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loanbill_rh_entry |  | fid |
| 2 | pk_t_cfm_loanbill_rh_entry |  | fentryid |

---

## 提款模板-分表 t_cfm_loanbill_e

- **表名称：** 提款模板-分表
- **表名：** t_cfm_loanbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 期限(ymd) | varchar | 30 |  | √ | ' ' | 期限(ymd) |
| 3 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpaybillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 5 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 6 | frateadjustcycletype | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 7 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcreditorgid | 债权人(组织) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 11 | freceamt | freceamt | numeric | 23 | 10 | √ | 0 |  |
| 12 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点 |
| 13 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 14 | ftextdebtor | 借款人(文本) | varchar | 80 |  | √ | ' ' | 借款人(文本) |
| 15 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 16 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 17 | flastrepaydate | 最近还款日 | timestamp | 0 |  |  | null | 最近还款日 |
| 18 | fcontractname | 合同名称 | varchar | 80 |  | √ | ' ' | 合同名称 |
| 19 | frenewalinteresttype | 展期计息方式 | varchar | 80 |  | √ | ' ' | 展期计息方式,枚举: fixed :固定利率 float :浮动利率 |
| 20 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 21 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 22 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期重置 cycle :周期性重置 hand :手工重置 noadjust :不重置 |
| 23 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 24 | freferencerateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 25 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 26 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_360 :Actual/360 Actual_365 :Acutal/365 |
| 27 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 28 | fexratetypeid | 展期利率类型 | int8 | 64 |  | √ | 0 | [市场码表 fbd_lendingmarketcode](../fbd_files/fbd_lendingmarketcode.md) |
| 29 | fexratedeadlineid | 展期利率期限 | int8 | 64 |  | √ | 0 | [期限类别码表 fbd_termcategorycode](../fbd_files/fbd_termcategorycode.md) |
| 30 | fexrateadjustcycle | 展期利率调整周期（月） | int8 | 64 |  | √ | 0 | 展期利率调整周期（月） |
| 31 | frateadjustcycle | 利率重置周期值 | int8 | 64 |  | √ | 0 | 利率重置周期值 |
| 32 | frenewalinterestrate | 展期利率（%） | numeric | 23 | 10 | √ | 0 | 展期利率（%） |
| 33 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已退回 |
| 34 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 35 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 36 | fsettlestatus | 提交结算中心状态 | varchar | 80 |  | √ | ' ' | 提交结算中心状态,枚举: addnew :新增 submit :已提交 accept :已受理 bitback :已退回 |
| 37 | fstartintdate | 起息日期 | timestamp | 0 |  |  | null | 起息日期 |
| 38 | fexratesign | 展期利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 展期利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 39 | fexrateadjuststyle | 展期利率调整方式 | varchar | 80 |  | √ | ' ' | 展期利率调整方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 |
| 40 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 41 | frepayacctbankid | frepayacctbankid | int8 | 64 |  | √ | 0 |  |
| 42 | frateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 43 | fexratefloatpoint | 展期利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 展期利率浮动基点 |
| 44 | fsettleintmode | 结息方式 | varchar | 30 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 45 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 46 | floantype | 贷款类型 | varchar | 30 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 47 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 48 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | floaneracctbankid | 贷款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 50 | fexrateadjustdate | 首次展期利率调整日 | timestamp | 0 |  |  | null | 首次展期利率调整日 |
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

## 提款模板-主表 t_cfm_loanbill

- **表名称：** 提款模板-主表
- **表名：** t_cfm_loanbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceivedate | 到账日期 | timestamp | 0 |  |  | null | 到账日期 |
| 3 | fcontractbizdate | fcontractbizdate | timestamp | 0 |  |  | null |  |
| 4 | fabstract | fabstract | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreditlimitcurrency | 折授信币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | frenewalexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 10 | fbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 11 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 12 | flendernature | 贷款人性质 | varchar | 30 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 13 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 15 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | frepaymentway | 还款方式 | varchar | 30 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 18 | fcreditrate | fcreditrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fcontractbillno | fcontractbillno | varchar | 80 |  | √ | ' ' |  |
| 20 | fdiscreditamount | fdiscreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 21 | fstageplanid | 分期还款方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 22 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 23 | fdrawway | 提款方式 | varchar | 30 |  | √ | ' ' | 提款方式,枚举: once :一次性 stage :分期 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | faccountbankid | 提款银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 26 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 27 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 28 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 29 | finteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 30 | flastpayinstdate | 上次付息日 | timestamp | 0 |  |  | null | 上次付息日 |
| 31 | fnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 32 | fpayeebillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 33 | famount | 借款金额 | numeric | 19 | 6 | √ | 0.000000 | 借款金额 |
| 34 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 35 | fisinit | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 36 | finitendpreinstdate | 初始化上次预提结束日 | timestamp | 0 |  |  | null | 初始化上次预提结束日 |
| 37 | fcalculaterateamount | 测算未付利息 | numeric | 19 | 6 | √ | 0.000000 | 测算未付利息 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 40 | fpayinterestamount | 已付利息 | numeric | 19 | 6 | √ | 0.000000 | 已付利息 |
| 41 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 42 | floanrate | 放款利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 放款利率（%） |
| 43 | fdrawamount | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 47 | fdrawtype | 提款业务状态 | varchar | 30 |  | √ | ' ' | 提款业务状态,枚举: drawing :提款中 drawed :已提款 partpayment :已部分还款 closeout :已结清 bitback :已退回 |
| 48 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 49 | frepayamount | 已还本金 | numeric | 19 | 6 | √ | 0.000000 | 已还本金 |
| 50 | fbizdate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 51 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 52 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
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

## 提款模板-分表 t_cfm_loanbill_t

- **表名称：** 提款模板-分表
- **表名：** t_cfm_loanbill_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flenddraccountid | 借款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 4 | fratejumpperpoint | fratejumpperpoint | numeric | 23 | 10 | √ | 0 |  |
| 5 | funderwritemethod | funderwritemethod | varchar | 30 |  | √ | ' ' |  |
| 6 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 7 | fshortname | fshortname | varchar | 80 |  | √ | ' ' |  |
| 8 | fratefloor | fratefloor | numeric | 23 | 10 | √ | 0 |  |
| 9 | fpublishprice | fpublishprice | numeric | 19 | 6 | √ | 0 |  |
| 10 | floanuseid | floanuseid | int8 | 64 |  | √ | 0 |  |
| 11 | fissetcondt | fissetcondt | bpchar | 1 |  | √ | '0' |  |
| 12 | fticketamt | fticketamt | numeric | 19 | 6 | √ | 0 |  |
| 13 | fbondtype | fbondtype | varchar | 80 |  | √ | ' ' |  |
| 14 | fissparkb | fissparkb | bpchar | 1 |  | √ | '0' |  |
| 15 | fratejumpcyclekey | fratejumpcyclekey | varchar | 80 |  | √ | ' ' |  |
| 16 | fratejumpcycleval | fratejumpcycleval | int4 | 32 |  | √ | 0 |  |
| 17 | fadjustcondt | fadjustcondt | varchar | 255 |  | √ | ' ' |  |
| 18 | fregion | 地域范围 | varchar | 80 |  | √ | ' ' | 地域范围,枚举: R1 :中国大陆 R2 :港澳台 R3 :境外 |
| 19 | floandraccountid | 贷款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 20 | fratingagencyid | fratingagencyid | int8 | 64 |  | √ | 0 |  |
| 21 | frecamtcondb | frecamtcondb | varchar | 255 |  | √ | ' ' |  |
| 22 | fratingscale | fratingscale | varchar | 255 |  | √ | ' ' |  |
| 23 | flendcraccountid | 借款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 24 | fissparkt | fissparkt | bpchar | 1 |  | √ | '0' |  |
| 25 | fissparks | fissparks | bpchar | 1 |  | √ | '0' |  |
| 26 | fcustodianfinorgid | fcustodianfinorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fhandinstplan | 手工维护付息计划 | bpchar | 1 |  | √ | '0' | 手工维护付息计划 |
| 28 | foccupybondlimitid | foccupybondlimitid | int8 | 64 |  | √ | 0 |  |
| 29 | firr | firr | numeric | 23 | 10 | √ | 0 |  |
| 30 | fissetconds | fissetconds | bpchar | 1 |  | √ | '0' |  |
| 31 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 32 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 33 | floancraccountid | 贷款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 34 | frecamtconds | frecamtconds | varchar | 255 |  | √ | ' ' |  |
| 35 | fissetpluspoint | fissetpluspoint | bpchar | 1 |  | √ | '0' |  |
| 36 | fishandend | 手工结束合同 | bpchar | 1 |  | √ | '0' | 手工结束合同 |
| 37 | fissetcondb | fissetcondb | bpchar | 1 |  | √ | '0' |  |
| 38 | fguaranteeway | fguaranteeway | varchar | 30 |  | √ | ' ' |  |
| 39 | frateceil | frateceil | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loanbill_t |  | fshortname |
| 2 | pk_t_cfm_loanbill_t |  | fid |
| 3 | idx_t_cfm_loanbill_region |  | fregion |

---

## 提款模板-多语言表 t_cfm_loanbill_l

- **表名称：** 提款模板-多语言表
- **表名：** t_cfm_loanbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fabstract | fabstract | varchar | 255 |  | √ | ' ' |  |
| 3 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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

---

## 提款模板-反写记录表 t_cfm_loanbill_wb

- **表名称：** 提款模板-反写记录表
- **表名：** t_cfm_loanbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loanbill_wb_pkey |  | fentryid |
| 2 | idx_t_cfm_loanbill_wb |  | fid |

---

## 利率重置分录-子表 t_cfm_loanbill_ra_entry

- **表名称：** 利率重置分录-子表
- **表名：** t_cfm_loanbill_ra_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fraeffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fraremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | frayearrate | 年利率（%） | numeric | 23 | 10 | √ | 0 | 年利率（%） |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | framodifier | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | framodifydate | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fconfirmdate | 利率确定日 | timestamp | 0 |  |  | null | 利率确定日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_loanbill_ra_entry |  | fentryid |
| 2 | idx_t_cfm_loanbill_ra_entry |  | fid |

---

## 银团分录-子表 t_cfm_loancontractbill_ba

- **表名称：** 银团分录-子表
- **表名：** t_cfm_loancontractbill_ba

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbankrole | 银团角色 | varchar | 30 |  | √ | ' ' | 银团角色,枚举: MB :管理行 MP :管理行-参与行 PB :参与行 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fbankentryid | fbankentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fshareamount | 份额金额 | numeric | 19 | 6 | √ | 0 | 份额金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 9 | floanamount | floanamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | ffinorginfoid | 银行名称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loancontractbi_ba_fid |  | fid |
| 2 | pk_cfm_loancontractbill_ba |  | fentryid |

---

## 关联子实体-子表 t_cfm_loanbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_loanbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loanbill_lk |  | fid |
| 2 | t_cfm_loanbill_lk_pkey |  | fpkid |

---

## 利息测算单据体-子表 t_cfm_loanbill_ic_entry

- **表名称：** 利息测算单据体-子表
- **表名：** t_cfm_loanbill_ic_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finteresdate | 预计付息日期 | timestamp | 0 |  |  | null | 预计付息日期 |
| 3 | finterestseq | 期数 | varchar | 30 |  | √ | ' ' | 期数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finstdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | finterestcalamount | 预计利息 | numeric | 19 | 6 | √ | 0.000000 | 预计利息 |
| 7 | fintaccountld | 付息账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loanbill_ic_entry_pkey |  | fentryid |
| 2 | idx_t_cfm_loanbill_ic_entry |  | fid |

---

## 还款计划单据体-子表 t_cfm_loanbill_rp_entry

- **表名称：** 还款计划单据体-子表
- **表名：** t_cfm_loanbill_rp_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frepaymentmodifier | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fexrepaymentdate | 预计还款日期 | timestamp | 0 |  |  | null | 预计还款日期 |
| 4 | ferepayamount | 已还本金 | numeric | 19 | 6 | √ | 0.000000 | 已还本金 |
| 5 | frepaymentdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 6 | frepayaccountld | 还款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fexdrawamount | 预计还本金 | numeric | 19 | 6 | √ | 0.000000 | 预计还本金 |
| 9 | fenotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 10 | frepaymentscseq | frepaymentscseq | int8 | 64 |  | √ | 0 |  |
| 11 | frepaymentmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | frepaymentdesc | 备注 | text | 0 |  |  | null | 备注 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loanbill_rp_entry_pkey |  | fentryid |
| 2 | idx_t_cfm_loanbill_rp_entry |  | fid |

---

## 提款模板-关联追踪表 t_cfm_loanbill_tc

- **表名称：** 提款模板-关联追踪表
- **表名：** t_cfm_loanbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loanbill_tc_tid |  | ftid |
| 2 | idx_cfm_loanbill_tc_tbill |  | ftbillid |
| 3 | idx_t_cfm_loanbill_tc |  | ftbillid |
| 4 | t_cfm_loanbill_tc_pkey |  | fid |

---

## 利息测算子单据体-子表 t_cfm_loanbill_ic_sentry

- **表名称：** 利息测算子单据体-子表
- **表名：** t_cfm_loanbill_ic_sentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finterestdays | 利率转换天数 | int8 | 64 |  | √ | 0 | 利率转换天数 |
| 2 | ffloatrate | 加点利率（%） | numeric | 23 | 10 | √ | 0 | 加点利率（%） |
| 3 | flasttotalint | 上期累计未付利息 | numeric | 19 | 6 | √ | 0 | 上期累计未付利息 |
| 4 | fconfirmratedate | 利率确定日 | timestamp | 0 |  |  | null | 利率确定日 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finterestenddate | 计息结束日 | timestamp | 0 |  |  | null | 计息结束日 |
| 7 | ffloatint | 加点利息 | numeric | 19 | 6 | √ | 0 | 加点利息 |
| 8 | flookdays | 计息天数（观察日） | int4 | 32 |  | √ | 0 | 计息天数（观察日） |
| 9 | finterestbalance | 计息本金 | numeric | 19 | 6 | √ | 0.000000 | 计息本金 |
| 10 | fintereststartdate | 计息开始日 | timestamp | 0 |  |  | null | 计息开始日 |
| 11 | finterestway | 利息类别 | varchar | 30 |  | √ | ' ' | 利息类别,枚举: normal :正常利息 extend :展期利息 overdue :逾期 |
| 12 | finterestdate | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 13 | finterestamount | 利息金额 | numeric | 19 | 6 | √ | 0.000000 | 利息金额 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | finterestrate | 利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 利率（%） |
| 17 | fcurtotalint | 当期累计未付利息 | numeric | 19 | 6 | √ | 0 | 当期累计未付利息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loanbill_ic_sentry_pkey |  | fdetailid |
| 2 | idx_t_cfm_loanbill_ic_sentry |  | fentryid |
