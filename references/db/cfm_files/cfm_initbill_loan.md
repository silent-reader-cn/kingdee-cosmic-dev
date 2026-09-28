# 借款业务初始化-cfm_initbill_loan

## 借款业务初始化-多语言表 t_cfm_initbill_l

- **表名称：** 借款业务初始化-多语言表
- **表名：** t_cfm_initbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 3 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
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
| 1 | t_cfm_initbill_l_pkey |  | fpkid |
| 2 | idx_t_cfm_initbill_l |  | fid,flocaleid |

---

## 合同费用信息分录-子表 t_cfm_initbill_fee

- **表名称：** 合同费用信息分录-子表
- **表名：** t_cfm_initbill_fee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeeamt | 费用金额 | numeric | 19 | 6 | √ | 0 | 费用金额 |
| 3 | ffeepaydate | 费用日期 | timestamp | 0 |  |  | null | 费用日期 |
| 4 | ffeeoppunittype | 对方单位类型 | varchar | 30 |  | √ | ' ' | 对方单位类型,枚举: bos_org :内部单位 bd_finorginfo :合作金融机构 bd_supplier :供应商 bd_customer :客户 fbd_other :其他 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffeeschemeid | 费用方案 | int8 | 64 |  | √ | 0 | [费用方案 fbd_feescheme](../fbd_files/fbd_feescheme.md) |
| 7 | ffeeoppunittext | 对方单位 | varchar | 80 |  | √ | ' ' | 对方单位 |
| 8 | ffeeoppunitid | 对方单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ffeerate | 费率（%） | numeric | 19 | 6 | √ | 0 | 费率（%） |
| 10 | ffeeacctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 11 | fexcrate | 折债务币种汇率 | numeric | 23 | 10 | √ | 0 | 折债务币种汇率 |
| 12 | ffeesettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 13 | ffeeoppbebankid | 对方开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 14 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |
| 15 | ffeeoppacctbank | 对方银行账号 | varchar | 80 |  | √ | ' ' | 对方银行账号 |
| 16 | fishandexcrate | 是否手动填写汇率 | bpchar | 1 |  | √ | '0' | 是否手动填写汇率 |
| 17 | ffeesource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: hand :手工新增 linkgen :费用关联生成 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | ffeeissettle | 已结算 | bpchar | 1 |  | √ | '0' | 已结算 |
| 20 | ffeeremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | ffeecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_initbill_fee |  | fentryid |
| 2 | idx_t_cfm_initbill_fee |  | fid |

---

## 借款业务初始化-分表 t_cfm_initbill_e

- **表名称：** 借款业务初始化-分表
- **表名：** t_cfm_initbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 期限(ymd) | varchar | 30 |  | √ | ' ' | 期限(ymd) |
| 3 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 4 | frateadjustcycletype | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: W :按周 M :按月 |
| 5 | fshortname | fshortname | varchar | 80 |  | √ | ' ' |  |
| 6 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreditorgid | 债权组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 10 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点 |
| 11 | fratingagencyid | fratingagencyid | int8 | 64 |  | √ | 0 |  |
| 12 | ftextdebtor | 借款人 | varchar | 80 |  | √ | ' ' | 借款人 |
| 13 | fratingscale | fratingscale | varchar | 80 |  | √ | ' ' |  |
| 14 | fissuemethodid | fissuemethodid | int8 | 64 |  | √ | 0 |  |
| 15 | fcontractname | 合同名称 | varchar | 80 |  | √ | ' ' | 合同名称 |
| 16 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 17 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 18 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 19 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 20 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_360 :Actual/360 Actual_365 :Acutal/365 |
| 21 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 22 | fexrateadjustcycletype | 展期利率重置周期 | varchar | 30 |  | √ | ' ' | 展期利率重置周期,枚举: W :按周 M :按月 |
| 23 | faccountbankid | 借款组织银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 24 | fexratetypeid | 展期利率类型(弃用) | int8 | 64 |  | √ | 0 | [市场码表 fbd_lendingmarketcode](../fbd_files/fbd_lendingmarketcode.md) |
| 25 | fexratedeadlineid | 展期利率期限(弃用) | int8 | 64 |  | √ | 0 | [期限类别码表 fbd_termcategorycode](../fbd_files/fbd_termcategorycode.md) |
| 26 | fexrateadjustcycle | 展期利率重置周期 | int8 | 64 |  | √ | 0 | 展期利率重置周期 |
| 27 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 28 | funderwritemethod | funderwritemethod | varchar | 30 |  | √ | ' ' |  |
| 29 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已退回 |
| 30 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 31 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 32 | fexratesign | 展期利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 展期利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 33 | fexrateadjuststyle | 展期利率调整方式 | varchar | 80 |  | √ | ' ' | 展期利率调整方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 |
| 34 | fbondtype | fbondtype | varchar | 30 |  | √ | ' ' |  |
| 35 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 36 | fregion | 地域范围 | varchar | 30 |  | √ | ' ' | 地域范围,枚举: R1 :中国大陆 R2 :港澳台 R3 :境外 |
| 37 | frateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 38 | fissuemarketid | fissuemarketid | int8 | 64 |  | √ | 0 |  |
| 39 | fexratefloatpoint | 展期利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 展期利率浮动基点 |
| 40 | fsettleintmode | 结息方式 | varchar | 30 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 41 | fcustodianfinorgid | fcustodianfinorgid | int8 | 64 |  | √ | 0 |  |
| 42 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 43 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 44 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 45 | fexreferencerateid | 展期参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 46 | floantype | 借款类型 | varchar | 30 |  | √ | ' ' | 借款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 47 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 48 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | floaneracctbankid | 债权人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 50 | fratesign | 利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 51 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_initbill_e |  | fid |
| 2 | idx_t_cfm_initbill_e |  | fratetypeid,fratedeadlineid |

---

## 提款信息明细-子表 t_cfm_initbill_entry

- **表名称：** 提款信息明细-子表
- **表名：** t_cfm_initbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditcurrencyid | 授信币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | floanbillid | 提款ID | int8 | 64 |  | √ | 0 | 提款ID |
| 4 | freceivedate | 到账日期 | timestamp | 0 |  |  | null | 到账日期 |
| 5 | floanexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fextrateajustdate | 首次展期利率重置日 | timestamp | 0 |  |  | null | 首次展期利率重置日 |
| 8 | fshortname | fshortname | varchar | 80 |  | √ | ' ' |  |
| 9 | fpublishprice | fpublishprice | numeric | 19 | 6 | √ | 0 |  |
| 10 | floanuseid | floanuseid | int8 | 64 |  | √ | 0 |  |
| 11 | fticketamt | fticketamt | numeric | 19 | 6 | √ | 0 |  |
| 12 | floadacctbankid | 提款银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 13 | fstartinstdate | 起息日期 | timestamp | 0 |  |  | null | 起息日期 |
| 14 | fratingagencyid | fratingagencyid | int8 | 64 |  | √ | 0 |  |
| 15 | floanterm | 期限(ymd) | varchar | 60 |  | √ | ' ' | 期限(ymd) |
| 16 | fratingscale | fratingscale | varchar | 80 |  | √ | ' ' |  |
| 17 | fcontractname | fcontractname | varchar | 80 |  | √ | ' ' |  |
| 18 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0.000000 | 实际占用授信金额 |
| 19 | frepaymentway | frepaymentway | varchar | 30 |  | √ | ' ' |  |
| 20 | fcreditrate | 折授信币种汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 折授信币种汇率 |
| 21 | fdiscreditamount | 折授信币种金额 | numeric | 19 | 6 | √ | 0.000000 | 折授信币种金额 |
| 22 | frepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 23 | floanratesign | 利率浮动基数符号 | varchar | 30 |  | √ | ' ' | 利率浮动基数符号,枚举: add :加 subtract :减 |
| 24 | floaddate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 25 | freferencerateid | freferencerateid | int8 | 64 |  | √ | 0 |  |
| 26 | fbasis | fbasis | varchar | 30 |  | √ | ' ' |  |
| 27 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 28 | fstageplanid | fstageplanid | int8 | 64 |  | √ | 0 |  |
| 29 | floanrateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fisloanextend | 展期 | bpchar | 1 |  | √ | '0' | 展期 |
| 32 | finteresttype | finteresttype | varchar | 30 |  | √ | ' ' |  |
| 33 | funderwritemethod | funderwritemethod | varchar | 30 |  | √ | ' ' |  |
| 34 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 35 | floanrateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 no :不调整 |
| 36 | fpayinterestamount | 已付利息 | numeric | 19 | 6 | √ | 0.000000 | 已付利息 |
| 37 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 38 | floanrate | 放款利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 放款利率(%) |
| 39 | fdrawamount | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 40 | floanrateadjusttype | 利率重置周期类型 | varchar | 30 |  | √ | ' ' | 利率重置周期类型,枚举: W :按周 M :按月 |
| 41 | floanbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 42 | fsettleintmode | fsettleintmode | varchar | 30 |  | √ | ' ' |  |
| 43 | fcustodianfinorgid | fcustodianfinorgid | int8 | 64 |  | √ | 0 |  |
| 44 | floanrateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 45 | foccupybondlimitid | foccupybondlimitid | int8 | 64 |  | √ | 0 |  |
| 46 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 47 | frepayamount | 已还本金 | numeric | 19 | 6 | √ | 0.000000 | 已还本金 |
| 48 | floanratefloatpoint | 利率浮动基点（BP） | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点（BP） |
| 49 | finterestsettledplanid | finterestsettledplanid | int8 | 64 |  | √ | 0 |  |
| 50 | fcreditlimitid | 占用授信单号 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_initbill_entry |  | fid |
| 2 | t_cfm_initbill_entry_pkey |  | fentryid |

---

## 项目分录-子表 t_cfm_loancontractbill_pj

- **表名称：** 项目分录-子表
- **表名：** t_cfm_loancontractbill_pj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目编号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_pj |  | fentryid |
| 2 | idx_cfm_loancontractbi_pj_fid |  | fid |

---

## 借款业务初始化-主表 t_cfm_initbill

- **表名称：** 借款业务初始化-主表
- **表名：** t_cfm_initbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frenewaldate | 展期签订日期 | timestamp | 0 |  |  | null | 展期签订日期 |
| 3 | forgid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 5 | frenewalexpiredate | 展期后合同到期日期 | timestamp | 0 |  |  | null | 展期后合同到期日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | floanuseid | 借款用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 9 | fenddate | 合同结束日期 | timestamp | 0 |  |  | null | 合同结束日期 |
| 10 | floancontractid | 借款合同ID | int8 | 64 |  | √ | 0 | 借款合同ID |
| 11 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 逾期利率浮动比例（%） |
| 12 | fisextend | 合同展期 | bpchar | 1 |  | √ | '0' | 合同展期 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 15 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 16 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 17 | flendernature | 贷款人性质 | varchar | 30 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 18 | fconversiondays | 利率转换天数(弃用) | varchar | 30 |  | √ | ' ' | 利率转换天数(弃用),枚举: 360 :360 365 :365 |
| 19 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
| 22 | frenewalinteresttype | 展期利率类型 | varchar | 30 |  | √ | ' ' | 展期利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | frepaymentway | 还款方式 | varchar | 30 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 26 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 27 | fstageplanid | 分期还款方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 28 | fdrawway | 提款方式 | varchar | 30 |  | √ | ' ' | 提款方式,枚举: once :一次性 stage :分期 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 31 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 32 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 33 | fislimitclause | 有限制性条款 | bpchar | 1 |  | √ | '0' | 有限制性条款 |
| 34 | finteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 35 | fisclientloan | 委托贷款 | bpchar | 1 |  | √ | '0' | 委托贷款 |
| 36 | frenewalinterestrate | 展期利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 展期利率（%） |
| 37 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 38 | finitstatus | 初始化状态 | varchar | 30 |  | √ | ' ' | 初始化状态,枚举: A :初始化中 B :完成 |
| 39 | famount | 借款金额 | numeric | 19 | 6 | √ | 0.000000 | 借款金额 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fguarantee | 担保方式 | varchar | 30 |  | √ | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 44 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 45 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 46 | fbizdate | 合同签订日期 | timestamp | 0 |  |  | null | 合同签订日期 |
| 47 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | finterestrate | 合同签订利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订利率（%） |
| 49 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 50 | fprotocolno | 展期协议号 | varchar | 80 |  | √ | ' ' | 展期协议号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_initbill_pkey |  | fid |
| 2 | idx_t_cfm_initbill_bns |  | fbillno,fbillstatus |

---

## 供应链融资分录-子表 t_cfm_loancontractbill_sc

- **表名称：** 供应链融资分录-子表
- **表名：** t_cfm_loancontractbill_sc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexecutedate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 3 | frelationtype | 关联类型 | varchar | 30 |  | √ | ' ' | 关联类型,枚举: PO :采购订单 SO :销售订单 |
| 4 | fbdpartnerid | 核心企业 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | forderno | 订单编号 | varchar | 50 |  | √ | ' ' | 订单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_sc |  | fentryid |
| 2 | t_cfm_loancontractb_sc_fid |  | fid |

---

## 提款费用信息-子表 t_cfm_initbill_sloanfee

- **表名称：** 提款费用信息-子表
- **表名：** t_cfm_initbill_sloanfee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffeeamt | 费用金额 | numeric | 19 | 6 | √ | 0 | 费用金额 |
| 2 | ffeepaydate | 费用日期 | timestamp | 0 |  |  | null | 费用日期 |
| 3 | ffeeoppunittype | 对方单位类型 | varchar | 30 |  | √ | ' ' | 对方单位类型,枚举: bos_org :内部单位 bd_finorginfo :合作金融机构 bd_supplier :供应商 bd_customer :客户 fbd_other :其他 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ffeeschemeid | 费用方案 | int8 | 64 |  | √ | 0 | [费用方案 fbd_feescheme](../fbd_files/fbd_feescheme.md) |
| 6 | ffeeoppunittext | 对方单位 | varchar | 80 |  | √ | ' ' | 对方单位 |
| 7 | ffeeoppunitid | 对方单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | ffeerate | 费率（%） | numeric | 19 | 6 | √ | 0 | 费率（%） |
| 9 | ffeeacctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 10 | fexcrate | 折债务币种汇率 | numeric | 23 | 10 | √ | 0 | 折债务币种汇率 |
| 11 | ffeesettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 12 | ffeeoppbebankid | 对方开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 13 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |
| 14 | ffeeoppacctbank | 对方银行账号 | varchar | 80 |  | √ | ' ' | 对方银行账号 |
| 15 | fishandexcrate | 是否手动填写汇率 | bpchar | 1 |  | √ | '0' | 是否手动填写汇率 |
| 16 | ffeesource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: hand :手工新增 linkgen :费用关联生成 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | ffeeissettle | 已结算 | bpchar | 1 |  | √ | '0' | 已结算 |
| 20 | ffeeremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | ffeecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_initbill_sloanfee |  | fentryid |
| 2 | pk_t_cfm_initbill_sloanfee |  | fdetailid |

---

## 银团分录-子表 t_cfm_loancontractbill_ba

- **表名称：** 银团分录-子表
- **表名：** t_cfm_loancontractbill_ba

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbankrole | 银团角色 | varchar | 30 |  | √ | ' ' | 银团角色,枚举: MB :管理行 PB :参与行 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fbankentryid | 银团分录ID | int8 | 64 |  | √ | 0 | 银团分录ID |
| 6 | fshareamount | 份额金额 | numeric | 19 | 6 | √ | 0 | 份额金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcreditlimitid | 占用授信单号 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
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

## 还款计划-子表 t_cfm_initbill_sentry

- **表名称：** 还款计划-子表
- **表名：** t_cfm_initbill_sentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexrepaymentdate | 预计还款日期 | timestamp | 0 |  |  | null | 预计还款日期 |
| 2 | frepaymentscseq | 期数 | int8 | 64 |  | √ | 0 | 期数 |
| 3 | frepaymentdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frepaymentdesc | 备注 | text | 0 |  |  | null | 备注 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fexdrawamount | 预计还本金 | numeric | 19 | 6 | √ | 0.000000 | 预计还本金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_initbill_sentry_pkey |  | fdetailid |
| 2 | idx_t_cfm_initbill_sentry |  | fentryid |

---

## 贸融关联分录-子表 t_cfm_loancontractbill_tf

- **表名称：** 贸融关联分录-子表
- **表名：** t_cfm_loancontractbill_tf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelatebillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 3 | fletter | fletter | varchar | 50 |  | √ | ' ' |  |
| 4 | frelationtype | 关联类型 | varchar | 30 |  | √ | ' ' | 关联类型,枚举: IO :进口订单 EO :出口订单 IL :进口信用证 EL :出口信用证 |
| 5 | fbeneficiary | 受益人 | varchar | 50 |  | √ | ' ' | 受益人 |
| 6 | frelatebillid | frelatebillid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 10 | frelatebilltype | frelatebilltype | varchar | 30 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | funpaidamount | 未付（收）金额 | numeric | 19 | 6 | √ | 0 | 未付（收）金额 |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_tf |  | fentryid |
| 2 | t_cfm_loancontractb_tf_fid |  | fid |
