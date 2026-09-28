# 银行借款合同变更申请-cfm_contract_apply

## 担保信息分录-子表 t_gm_guaranteeuse_info

- **表名称：** 担保信息分录-子表
- **表名：** t_gm_guaranteeuse_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcreditortext | fgcreditortext | varchar | 80 |  | √ | ' ' |  |
| 3 | fgcreditguarantee | 是否额度担保 | bpchar | 1 |  | √ | '0' | 是否额度担保 |
| 4 | fgsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fgcontractcurrency | 担保合同币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 8 | fgcreditorid | fgcreditorid | int8 | 64 |  | √ | 0 |  |
| 9 | fgcontractid | 担保合同编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 10 | fgsrcbilltype | 来源单据 | varchar | 80 |  | √ | ' ' | 来源单据 |
| 11 | fgcurrencyid | fgcurrencyid | int8 | 64 |  | √ | 0 |  |
| 12 | fgstatus | 状态 | varchar | 80 |  | √ | ' ' | 状态,枚举: A :担保中 C :已解除 |
| 13 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 14 | fgratio | 担保比例(%) | numeric | 19 | 6 | √ | 0 | 担保比例(%) |
| 15 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fgcreditortype | fgcreditortype | varchar | 50 |  | √ | ' ' |  |
| 18 | fgcontractamount | 担保合同金额 | numeric | 19 | 6 | √ | 0 | 担保合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_info_efid |  | fid |
| 2 | pk_t_gm_guaranteeuse_info |  | fentryid |

---

## 银行借款合同变更申请-主表 t_cfm_contract_apply

- **表名称：** 银行借款合同变更申请-主表
- **表名：** t_cfm_contract_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限(ymd) | varchar | 50 |  | √ | ' ' | 期限(ymd) |
| 3 | flenderapplyno | 融资借款申请 | varchar | 100 |  | √ | ' ' | 融资借款申请 |
| 4 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 5 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | frateadjustcycletype | 利率重置周期 | varchar | 50 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 7 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | floanuseid | 借款用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 10 | fenddate | 合同到期日期 | timestamp | 0 |  |  | null | 合同到期日期 |
| 11 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fratefloatpoint | 利率浮动基点 | numeric | 16 | 6 | √ | 0 | 利率浮动基点 |
| 13 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 14 | 4 | √ | 0 | 逾期利率浮动比例（%） |
| 14 | fapplytype | 申请类型 | varchar | 50 |  | √ | ' ' | 申请类型,枚举: 1 :变更 |
| 15 | fbillno | 申请单号 | varchar | 30 |  | √ | ' ' | 申请单号 |
| 16 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 17 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 20 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
| 21 | floancontractbillid | 借款合同 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 22 | fcontractname | fcontractname | varchar | 50 |  | √ | ' ' |  |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | ftextcreditor | 债权人 | varchar | 100 |  | √ | ' ' | 债权人 |
| 25 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 27 | frepaymentway | 还款方式 | varchar | 50 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 28 | fcreditortype | 债权人类型 | varchar | 50 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 29 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 30 | fcontractbillno | 合同单据编号 | varchar | 50 |  | √ | ' ' | 合同单据编号 |
| 31 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual_360 :Actual/360 Actual_365 :Actual/365 |
| 32 | fstageplanid | 分期还款方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 33 | fdrawway | 提款方式 | varchar | 50 |  | √ | ' ' | 提款方式,枚举: once :一次性 stage :分期 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | faccountbankid | 借款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 36 | fislimitclause | 有限制性条款 | bpchar | 1 |  | √ | '0' | 有限制性条款 |
| 37 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 38 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 39 | fnotrepayamount | 合同剩余未还金额 | numeric | 23 | 10 | √ | 0 | 合同剩余未还金额 |
| 40 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :已办理 |
| 41 | famount | 借款金额 | numeric | 23 | 10 | √ | 0 | 借款金额 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fdrawamount | 合同提款金额 | numeric | 23 | 10 | √ | 0 | 合同提款金额 |
| 44 | fregion | 地域范围 | varchar | 50 |  | √ | ' ' | 地域范围,枚举: R1 :中国大陆 R2 :港澳台 R3 :境外 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | frateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 49 | fsettleintmode | 结息方式 | varchar | 50 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 50 | fcontractno | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 51 | fiscallint | 计息 | bpchar | 1 |  | √ | '0' | 计息 |
| 52 | floantype | 借款类型 | varchar | 50 |  | √ | ' ' | 借款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 53 | fbizdate | 合同签约日期 | timestamp | 0 |  |  | null | 合同签约日期 |
| 54 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 55 | finterestrate | 合同签订利率（%） | numeric | 23 | 10 | √ | 0 | 合同签订利率（%） |
| 56 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 57 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_contract_apply |  | fid |
| 2 | index_contract_apply |  | fcontractbillno |

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

## 银行借款合同变更申请-多语言表 t_cfm_contract_apply_l

- **表名称：** 银行借款合同变更申请-多语言表
- **表名：** t_cfm_contract_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 3 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
| 4 | fcontractname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_contract_apply_l |  | fpkid |
| 2 | index_contract_apply_l |  | fid |

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
| 5 | fbankentryid | fbankentryid | int8 | 64 |  | √ | 0 |  |
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
