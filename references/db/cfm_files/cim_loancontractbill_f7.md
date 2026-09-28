# 贷款合同-cim_loancontractbill_f7

## 贷款合同-主表 t_cfm_loancontractbill

- **表名称：** 贷款合同-主表
- **表名：** t_cfm_loancontractbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnotdrawamount | 未放款金额 | numeric | 19 | 6 | √ | 0.000000 | 未放款金额 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | floanuseid | floanuseid | int8 | 64 |  | √ | 0 |  |
| 6 | fenddate | 合同结束日期 | timestamp | 0 |  |  | null | 合同结束日期 |
| 7 | ffloatingratio | ffloatingratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fisextend | fisextend | bpchar | 1 |  | √ | '0' |  |
| 9 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 10 | fclientorgid | fclientorgid | int8 | 64 |  | √ | 0 |  |
| 11 | fotherexplain | fotherexplain | varchar | 255 |  | √ | ' ' |  |
| 12 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 13 | flendernature | flendernature | varchar | 30 |  | √ | ' ' |  |
| 14 | fconversiondays | fconversiondays | varchar | 30 |  | √ | ' ' |  |
| 15 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcontractstatus | 合同状态 | varchar | 30 |  | √ | ' ' | 合同状态,枚举: A :登记中 B :已登记 C :执行中 D :已结清 |
| 18 | flimitclauseexplain | flimitclauseexplain | varchar | 255 |  | √ | ' ' |  |
| 19 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | frepaymentway | frepaymentway | varchar | 30 |  | √ | ' ' |  |
| 23 | fextendstatus | fextendstatus | varchar | 30 |  | √ | ' ' |  |
| 24 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 25 | fnotpayinterestamount | fnotpayinterestamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 26 | finitid | finitid | int8 | 64 |  | √ | 0 |  |
| 27 | fstageplanid | fstageplanid | int8 | 64 |  | √ | 0 |  |
| 28 | fdrawway | 放款方式 | varchar | 30 |  | √ | ' ' | 放款方式,枚举: once :一次性 stage :分期 |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | faccountbankid | 借款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 31 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 32 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 33 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 34 | fislimitclause | fislimitclause | bpchar | 1 |  | √ | '0' |  |
| 35 | finteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 36 | fisclientloan | fisclientloan | bpchar | 1 |  | √ | '0' |  |
| 37 | fnotrepayamount | 未收回本金 | numeric | 19 | 6 | √ | 0.000000 | 未收回本金 |
| 38 | famount | 贷款金额 | numeric | 19 | 6 | √ | 0.000000 | 贷款金额 |
| 39 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 42 | fpayinterestamount | fpayinterestamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 43 | fdrawamount | 已放款金额 | numeric | 19 | 6 | √ | 0.000000 | 已放款金额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fguarantee | 担保方式 | varchar | 300 |  |  | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 47 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 48 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 49 | frepayamount | frepayamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 50 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 51 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | finterestrate | 合同签订利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订利率（%） |
| 53 | finterestsettledplanid | finterestsettledplanid | int8 | 64 |  | √ | 0 |  |
| 54 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 55 | fisoverdue | fisoverdue | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loancontractbill_pkey |  | fid |
| 2 | idx_t_cfm_loancontractbill_bns |  | fbillno,fbillstatus |

---

## 日历-多选基础资料表 t_cfm_loancontractbill_ca

- **表名称：** 日历-多选基础资料表
- **表名：** t_cfm_loancontractbill_ca

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作日历 tbd_workcalendar](../fbd_files/tbd_workcalendar.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_ca |  | fpkid |
| 2 | idx_cfm_loanctract_ca_fid |  | fid |

---

## 贷款合同-分表 t_cfm_loancontractbill_f

- **表名称：** 贷款合同-分表
- **表名：** t_cfm_loancontractbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 3 | fisunifyloanreturn | fisunifyloanreturn | bpchar | 1 |  | √ | '0' |  |
| 4 | frenewalexpiredate | 展期后合同到期日期 | timestamp | 0 |  |  | null | 展期后合同到期日期 |
| 5 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 6 | floanapplyid | floanapplyid | int8 | 64 |  | √ | 0 |  |
| 7 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 8 | fisunifydebit | fisunifydebit | bpchar | 1 |  | √ | '0' |  |
| 9 | fisunifycredit | fisunifycredit | bpchar | 1 |  | √ | '0' |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fenable | 使用状态 | varchar | 30 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fregion | fregion | varchar | 80 |  | √ | ' ' |  |
| 13 | fishandend | fishandend | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loancontract_f_mid |  | floanapplyid |
| 2 | pk_cfm_loancontractbill_f |  | fid |

---

## 贷款合同-多语言表 t_cfm_loancontractbill_l

- **表名称：** 贷款合同-多语言表
- **表名：** t_cfm_loancontractbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherexplain | fotherexplain | varchar | 255 |  | √ | ' ' |  |
| 3 | flimitclauseexplain | flimitclauseexplain | varchar | 255 |  | √ | ' ' |  |
| 4 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loancontractbill_l_pkey |  | fpkid |
| 2 | idx_t_cfm_loancontractbill_l |  | fid,flocaleid |

---

## 贷款合同-分表 t_cfm_loancontractbill_e

- **表名称：** 贷款合同-分表
- **表名：** t_cfm_loancontractbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscandefer | fiscandefer | bpchar | 1 |  | √ | '0' |  |
| 3 | fterm | fterm | varchar | 30 |  | √ | ' ' |  |
| 4 | flenderapplyno | flenderapplyno | varchar | 100 |  | √ | ' ' |  |
| 5 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 6 | forgid | 借款人(组织) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 8 | frateadjustcycletype | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: W :周 M :月 |
| 9 | fshortname | fshortname | varchar | 30 |  | √ | ' ' |  |
| 10 | fregistorgid | fregistorgid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreditorgid | 债权人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fconfirmdescription | fconfirmdescription | varchar | 255 |  | √ | ' ' |  |
| 13 | fcreditorid | fcreditorid | int8 | 64 |  | √ | 0 |  |
| 14 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点 |
| 15 | fratingagencyid | fratingagencyid | int8 | 64 |  | √ | 0 |  |
| 16 | ftextdebtor | 借款人 | varchar | 255 |  | √ | ' ' | 借款人 |
| 17 | fotherexplain | fotherexplain | varchar | 255 |  | √ | ' ' |  |
| 18 | fratingscale | fratingscale | varchar | 30 |  | √ | ' ' |  |
| 19 | fissuemethodid | fissuemethodid | int8 | 64 |  | √ | 0 |  |
| 20 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 21 | flimitclauseexplain | flimitclauseexplain | varchar | 255 |  | √ | ' ' |  |
| 22 | fcontractname | fcontractname | varchar | 255 |  | √ | ' ' |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | ftextcreditor | ftextcreditor | varchar | 255 |  | √ | ' ' |  |
| 25 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 26 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 27 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 |
| 28 | fbasis | fbasis | varchar | 30 |  | √ | ' ' |  |
| 29 | fconfirmtime | fconfirmtime | timestamp | 0 |  |  | null |  |
| 30 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 31 | funderwritemethod | funderwritemethod | varchar | 30 |  | √ | ' ' |  |
| 32 | fconfirmstatus | fconfirmstatus | varchar | 30 |  | √ | ' ' |  |
| 33 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 34 | freturnreason | freturnreason | varchar | 255 |  | √ | ' ' |  |
| 35 | fsettlestatus | fsettlestatus | varchar | 80 |  | √ | ' ' |  |
| 36 | fbondtype | fbondtype | varchar | 30 |  | √ | ' ' |  |
| 37 | fdebtorid | fdebtorid | int8 | 64 |  | √ | 0 |  |
| 38 | frateresetadjustrule | 利率重置日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 利率重置日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 39 | frateadjustdate | frateadjustdate | timestamp | 0 |  |  | null |  |
| 40 | fissuemarketid | fissuemarketid | int8 | 64 |  | √ | 0 |  |
| 41 | fsettleintmode | fsettleintmode | varchar | 30 |  | √ | ' ' |  |
| 42 | fcustodianfinorgid | fcustodianfinorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fdebtortype | fdebtortype | varchar | 30 |  | √ | ' ' |  |
| 44 | fiscallint | fiscallint | bpchar | 1 |  | √ | '0' |  |
| 45 | floantype | 贷款类型 | varchar | 30 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券 |
| 46 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 47 | fconfirmerid | fconfirmerid | int8 | 64 |  | √ | 0 |  |
| 48 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 49 | floaneracctbankid | 贷款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 50 | fpayintadjustrule | 付息日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 付息日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 51 | fratesign | 利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 52 | fcreditlimitid | 授信额度 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 53 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loancontractbill_e |  | flender |
| 2 | idx_cfm_loancontract_eorgid |  | forgid |
| 3 | t_cfm_loancontractbill_e_pkey |  | fid |
