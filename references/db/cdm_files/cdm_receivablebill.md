# 应收票据-cdm_receivablebill

## 应收票据-主表 t_cdm_draftbill

- **表名称：** 应收票据-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeliveraccountbase | 交票人账号 | varchar | 50 |  | √ | ' ' | 交票人账号 |
| 3 | finnerendorsetradeid | 内部调票银企签收业务单据id | int8 | 64 |  | √ | 0 | 内部调票银企签收业务单据id |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 6 | facpflg | facpflg | varchar | 255 |  | √ | ' ' |  |
| 7 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 8 | finnerendorsepayid | 内部调票对应出纳付款单id | int8 | 64 |  | √ | 0 | 内部调票对应出纳付款单id |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 12 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 14 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 15 | fsubbillendflag | 子票终止序号 | int8 | 64 |  | √ | 0 | 子票终止序号 |
| 16 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 17 | fsubbillstartflag | 子票开始序号 | int8 | 64 |  | √ | 0 | 子票开始序号 |
| 18 | favailableamount | 可用金额 | numeric | 19 | 6 | √ | 0 | 可用金额 |
| 19 | fequaltradebillid | 等分化业务id | int8 | 64 |  | √ | 0 | 等分化业务id |
| 20 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 21 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 endorsed :已背书 discounted :已贴现 collected :已托收 splited :已拆分 |
| 22 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | [票据池维护 cdm_billpool](../cdm_files/cdm_billpool.md) |
| 23 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 24 | fpoollockorgid | 锁票人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbankmsg | 银行响应信息 | varchar | 2000 |  | √ | ' ' | 银行响应信息 |
| 27 | fbankaccountid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 28 | fclaimnoticebillno | 收款认领通知单 | varchar | 80 |  | √ | ' ' | 收款认领通知单 |
| 29 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 30 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 cdm-draftallocate :票据调度 |
| 31 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 32 | fdelivername | 交票人全称 | varchar | 800 |  | √ | ' ' | 交票人全称 |
| 33 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 34 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fpoollocktime | 锁定时间 | timestamp | 0 |  |  | null | 锁定时间 |
| 37 | fpoollockstatus | 锁定状态 | bpchar | 1 |  | √ | '0' | 锁定状态,枚举: 1 :锁定 0 :未锁定 |
| 38 | fpaybilltype | fpaybilltype | varchar | 50 |  | √ | ' ' |  |
| 39 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 40 | fdeliveraccounttext | 交票人账号 | varchar | 50 |  | √ | ' ' | 交票人账号 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | faccepterbankid | 承兑人开户行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 44 | fallocbillentryid | 票据池调度分录ID | int8 | 64 |  | √ | 0 | 票据池调度分录ID |
| 45 | foriginalsubbillamount | 原始子票包金额 | numeric | 23 | 10 | √ | 0 | 原始子票包金额 |
| 46 | foriginalsubbillrang | 原始子票包区间 | varchar | 255 |  | √ | ' ' | 原始子票包区间 |
| 47 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 48 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 49 | fbaleac | fbaleac | varchar | 255 |  | √ | ' ' |  |
| 50 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 51 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 52 | fdeliveropenbanknum | 交票人开户行行号 | varchar | 50 |  | √ | ' ' | 交票人开户行行号 |
| 53 | fsuretyremainamount | fsuretyremainamount | numeric | 19 | 4 | √ | 0 |  |
| 54 | fdeliverid | 交票人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 55 | facceptdate | 承兑日期 | timestamp | 0 |  |  | null | 承兑日期 |
| 56 | flockedamount | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 57 | fintopooltime | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 58 | fsourcedraftid | 源票据号码id | int8 | 64 |  | √ | 0 | 源票据号码id |
| 59 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 60 | fsourcebilltype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: cdm_payablebill :开票登记 cdm_drafttradebill :票据业务处理单 |
| 61 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :已作废 |
| 62 | fsuretyinput | fsuretyinput | bpchar | 1 |  | √ | '0' |  |
| 63 | fbillidentitycode | 票据识别码 | varchar | 255 |  | √ | ' ' | 票据识别码 |
| 64 | fpayeetype | 交票人类型 | varchar | 30 |  | √ | ' ' | 交票人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 65 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 66 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 67 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 68 | fsubbillrange | 子票区间 | varchar | 50 |  | √ | ' ' | 子票区间 |
| 69 | feuqaldifferetype | 等分化业务类型 | varchar | 255 |  | √ | ' ' | 等分化业务类型 |
| 70 | fdraftbillnoid | fdraftbillnoid | int8 | 64 |  | √ | 0 |  |
| 71 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 72 | fuseamount | fuseamount | numeric | 23 | 10 | √ | 0 |  |
| 73 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 74 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fisfromalloc | 票据池调度结果 | bpchar | 1 |  | √ | '0' | 票据池调度结果 |
| 76 | fdeliveropenbank | 交票人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 77 | facpfer | facpfer | numeric | 23 | 10 | √ | 0 |  |
| 78 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 79 | fbaltyp | fbaltyp | varchar | 255 |  | √ | ' ' |  |
| 80 | fishistorydata | 等分化前历史数据 | bpchar | 1 |  | √ | '0' | 等分化前历史数据 |
| 81 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 82 | fpoolprotocolid | fpoolprotocolid | int8 | 64 |  | √ | 0 |  |
| 83 | fusedamount | 已用金额 | numeric | 19 | 6 | √ | 0 | 已用金额 |
| 84 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 85 | fisfromequalspilt | 来源等分化拆分 | bpchar | 1 |  | √ | '0' | 来源等分化拆分 |
| 86 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 87 | fequaltradebilltype | 等分化业务类型 | varchar | 255 |  | √ | ' ' | 等分化业务类型 |
| 88 | fissplit | 能否拆分 | bpchar | 1 |  | √ | '0' | 能否拆分 |
| 89 | fguarantee | fguarantee | varchar | 50 |  | √ | ' ' |  |
| 90 | fsuretymoney | fsuretymoney | numeric | 23 | 10 | √ | 0 |  |
| 91 | fsubbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |
| 92 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 93 | famountofcredit | famountofcredit | numeric | 23 | 10 | √ | 0 |  |
| 94 | fcasamount | 出纳下推金额 | numeric | 19 | 6 | √ | 0 | 出纳下推金额 |
| 95 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 96 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 97 | fbeendorsor | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 98 | fsplitlogid | 拆分对应的日志 | int8 | 64 |  | √ | 0 | 拆分对应的日志 |
| 99 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 100 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 101 | fisequalbill | 等分化票据 | bpchar | 1 |  | √ | '0' | 等分化票据 |
| 102 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 103 | fdelivertype | 交票人基础资料类型 | varchar | 30 |  | √ | ' ' | 交票人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_pkey |  | fid |
| 2 | idx_cdm_draftbill_billpoolid |  | fbillpoolid |
| 3 | idx_cdm_draftbill_allocentid |  | fallocbillentryid |
| 4 | idx_t_cdm_draftbill |  | fbizdate,fdraftbillstatus |

---

## 关联出纳单据信息-子表 t_cdm_releatedcasbills

- **表名称：** 关联出纳单据信息-子表
- **表名：** t_cdm_releatedcasbills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frel_billamount | 单据金额 | numeric | 23 | 10 | √ | 0 | 单据金额 |
| 3 | frel_isrefuse | 票据退票 | bpchar | 1 |  | √ | '0' | 票据退票 |
| 4 | frel_billno | 关联单据编号 | varchar | 80 |  | √ | ' ' | 关联单据编号 |
| 5 | frel_modifytime | 记录修改时间 | timestamp | 0 |  |  | null | 记录修改时间 |
| 6 | frel_bizdate | 单据业务日期 | timestamp | 0 |  |  | null | 单据业务日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frel_billid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 9 | frel_createtime | 关联信息创建时间 | timestamp | 0 |  |  | null | 关联信息创建时间 |
| 10 | frel_billtype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型,枚举: cas_paybill :付款单 ifm_transhandlebill :付款交易处理 cas_recbill :收款单 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | frel_batchuseflag | 多单共用标识 | varchar | 80 |  | √ | ' ' | 多单共用标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_releatedcasbills_fid |  | fid |
| 2 | pk_t_cdm_releatedcasbills |  | fentryid |

---

## 单据体-子表 t_cdm_draftbill_endorse

- **表名称：** 单据体-子表
- **表名：** t_cdm_draftbill_endorse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fopponentname | 对手方全称 | varchar | 512 |  | √ | ' ' | 对手方全称 |
| 3 | fendorseistransfer | 是否转让 | bpchar | 1 |  | √ | '0' | 是否转让 |
| 4 | fsigndate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | finitiatorname | 发起方全称 | varchar | 512 |  | √ | ' ' | 发起方全称 |
| 7 | fendorsetype | 背书类型 | varchar | 30 |  | √ | ' ' | 背书类型,枚举: transfer :转让背书 pledge :质押背书 promise :保证背书 acceptance :提示承兑 invoice :提示收票 notediscount :买断式贴现 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpledgereleasedate | 质押解除日期 | timestamp | 0 |  |  | null | 质押解除日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_draftbill_endorse |  | fid |
| 2 | pk_t_cdm_draftbill_endorse |  | fentryid |

---

## 应收票据-多语言表 t_cdm_draftbill_l

- **表名称：** 应收票据-多语言表
- **表名：** t_cdm_draftbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_l_pkey |  | fpkid |
| 2 | idx_t_cdm_draftbill_l |  | fid,flocaleid |

---

## 应收票据-分表 t_cdm_draftbill_f

- **表名称：** 应收票据-分表
- **表名：** t_cdm_draftbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feledraftstatus | 电票状态(旧) | varchar | 30 |  | √ | ' ' | 电票状态(旧),枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 |
| 3 | flockbilltime | 锁票时间 | timestamp | 0 |  |  | null | 锁票时间 |
| 4 | fpredictunlocktime | 预计解锁时间 | timestamp | 0 |  |  | null | 预计解锁时间 |
| 5 | flockbilluser | 锁票用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 bd_finorginfo :金融机构 |
| 7 | frelatedelcbillid | frelatedelcbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | fautoreceive | fautoreceive | bpchar | 1 |  | √ | '0' |  |
| 10 | fpromisrate | fpromisrate | numeric | 19 | 6 | √ | 0 |  |
| 11 | fsuretyonline | fsuretyonline | bpchar | 1 |  | √ | '0' |  |
| 12 | fpledgeetext | 质权人 | varchar | 512 |  | √ | ' ' | 质权人 |
| 13 | faccepteraccountid | faccepteraccountid | int8 | 64 |  | √ | 0 |  |
| 14 | fdraftbilltranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 15 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 16 | fpledgeeaccount | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 17 | felccirculatestatus | 电票流通标识 | varchar | 255 |  | √ | ' ' | 电票流通标识,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 18 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 19 | fautoaccept | fautoaccept | bpchar | 1 |  | √ | '0' |  |
| 20 | fpledgeeaccounttext | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 21 | fbizfinishdate | 业务处理完成日期 | timestamp | 0 |  |  | null | 业务处理完成日期 |
| 22 | fbatchno | fbatchno | varchar | 255 |  | √ | ' ' |  |
| 23 | frectype | 收款方式 | varchar | 30 |  | √ | ' ' | 收款方式,枚举: 1 :手工关联 2 :收票登记 3 :规则生单 4 :手工生单 5 :规则匹配 6 :认领确认 |
| 24 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 other :其他 bd_finorginfo :合作金融机构 |
| 25 | feledraftstatusnew | 电票状态 | varchar | 255 |  | √ | ' ' | 电票状态,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 26 | faccepterbebankid | 承兑人全称 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 27 | fcontractno | fcontractno | varchar | 50 |  | √ | ' ' |  |
| 28 | ftradetypenew | 电票操作类型 | varchar | 50 |  | √ | ' ' | 电票操作类型,枚举: noteendorse :背书 remitaccept :提示承兑 remitreceive :提示收票 notediscount :贴现 notesignin :签收 ticketguarantee :出票保证 remitregister :开票登记 remitrevocation :撤销出票 notesigninreject :拒收 notecancle :撤销 remitcancle :取消出票 pledgenote :质押 removepledge :质押解除 presentpayment :票据托收 remitconfirm :合同确认 nonnegotiablecancle :不可转让撤销 |
| 29 | freturnnotetag | 回头票据 | bpchar | 1 |  | √ | '0' | 回头票据 |
| 30 | fisrelatedprebill | fisrelatedprebill | bpchar | 1 |  | √ | '0' |  |
| 31 | fsuretypayacct | fsuretypayacct | int8 | 64 |  | √ | 0 |  |
| 32 | frulename | 适配规则 | varchar | 100 |  | √ | ' ' | 适配规则 |
| 33 | febstatus | 电票操作状态 | varchar | 50 |  | √ | ' ' | 电票操作状态,枚举: BANK_PROCESSING :银行处理中 BANK_SUCCESS :交易成功 BANK_FAIL :交易失败 BANK_EXCEPTION :交易未确认 EB_PROCESSING :银企处理中 BANK_UNKNOWN :交易未确认 |
| 34 | fisinnerendorse | 内部调票 | bpchar | 1 |  | √ | '0' | 内部调票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_f |  | fid |
| 2 | idx_t_cdm_draftbill_f |  | fdraftbilltranstatus |

---

## 应收票据-分表 t_cdm_draftbill_e

- **表名称：** 应收票据-分表
- **表名：** t_cdm_draftbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpromiseexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 3 | faccepteraccount | 承兑人账号 | varchar | 80 |  | √ | ' ' | 承兑人账号 |
| 4 | fissuepromiserdate | 保证日期 | timestamp | 0 |  |  | null | 保证日期 |
| 5 | faccepterorgid | faccepterorgid | int8 | 64 |  | √ | 0 |  |
| 6 | faccepterbankno | 承兑人开户行行号 | varchar | 80 |  | √ | ' ' | 承兑人开户行行号 |
| 7 | freceiverbankno | 收款人开户行行号 | varchar | 80 |  | √ | ' ' | 收款人开户行行号 |
| 8 | facceptpromiserdate | 保证日期 | timestamp | 0 |  |  | null | 保证日期 |
| 9 | faccpromisetype | 承兑保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 10 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 11 | fissueticketgrade | 出票人评级机构 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 12 | fdrawerorgid | fdrawerorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fpromisecreditlevel | 承兑人信用等级 | varchar | 80 |  | √ | ' ' | 承兑人信用等级 |
| 14 | fissueticketexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 15 | facceptpromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 16 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 17 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 18 | fdraweraccountname | 出票人账号 | varchar | 80 |  | √ | ' ' | 出票人账号 |
| 19 | freceiverid | freceiverid | int8 | 64 |  | √ | 0 |  |
| 20 | fvouchernum | 凭证号 | varchar | 150 |  |  | null | 凭证号 |
| 21 | fdrawerbankname | fdrawerbankname | varchar | 80 |  | √ | ' ' |  |
| 22 | fissuepromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 23 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 24 | fdrawerid | 出票人全称 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 25 | fissuepromiser | 出票保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fissuepromisertype | 出票保证人类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | facceptpromisertype | 承兑保证人类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 28 | fisvoucher | 生成凭证 | bpchar | 1 |  |  | '0' | 生成凭证 |
| 29 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 30 | fpromisegrade | 承兑人评级机构 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 31 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 32 | fdraweraccountid | fdraweraccountid | int8 | 64 |  | √ | 0 |  |
| 33 | fissuepromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 34 | facceptpromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 35 | freceivertype | freceivertype | varchar | 30 |  | √ | ' ' |  |
| 36 | facceptpromisername | 承兑保证人名称 | varchar | 80 |  | √ | ' ' | 承兑保证人名称 |
| 37 | faccepterfinorgid | faccepterfinorgid | int8 | 64 |  | √ | 0 |  |
| 38 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 39 | facceptercompanyid | facceptercompanyid | int8 | 64 |  | √ | 0 |  |
| 40 | fissueticketcreditlevel | 出票人信用等级 | varchar | 80 |  | √ | ' ' | 出票人信用等级 |
| 41 | fdrawerbankid | 出票人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | 出票保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | fdrawercompanyid | int8 | 64 |  | √ | 0 |  |
| 47 | fissuepromisername | 出票保证人名称 | varchar | 80 |  | √ | ' ' | 出票保证人名称 |
| 48 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 49 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 50 | facceptpromiser | 承兑保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_e_pkey |  | fid |
| 2 | idx_t_cdm_draftbill_e |  | fdrawername |

---

## 应收票据-关联追踪表 t_cdm_draftbill_tc

- **表名称：** 应收票据-关联追踪表
- **表名：** t_cdm_draftbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_cdm_draftbill_tc_tbill |  | ftbillid |
| 2 | idx_cdm_draftbill_tc_tid |  | ftid |
| 3 | t_cdm_draftbill_tc_pkey |  | fid |

---

## 关联子实体-子表 t_cdm_draftbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_draftbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_draftbill_lk_fk |  | fid |
| 2 | t_cdm_draftbill_lk_pkey |  | fpkid |

---

## 应收票据-反写记录表 t_cdm_draftbill_wb

- **表名称：** 应收票据-反写记录表
- **表名：** t_cdm_draftbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_wb_pkey |  | fentryid |
| 2 | idx_cdm_draftbill_wb_fk |  | fid |

---

## 票据流转单据体-子表 t_cdm_draftbill_circulat

- **表名称：** 票据流转单据体-子表
- **表名：** t_cdm_draftbill_circulat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillamt |  | numeric | 19 | 6 | √ | 0 |  |
| 3 | forgfield |  | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frelabillid | 关联单据内码 | int8 | 64 |  | √ | 0 | 关联单据内码 |
| 5 | fdrafttradebillid | 业务处理单内码 | int8 | 64 |  | √ | 0 | 业务处理单内码 |
| 6 | fedelivername |  | varchar | 80 |  | √ | ' ' |  |
| 7 | frelabilltype | 关联单据： | varchar | 80 |  | √ | ' ' | 关联单据：,枚举: cas_recbill :收款单： cas_paybill :付款单： |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftradetype | 业务操作 | varchar | 30 |  | √ | ' ' | 业务操作,枚举: endorse :背书转让 discount :票据贴现 pledge :票据质押 rlspledge :质押解除 collect :票据托收 trusteeship :票据托管 retrieve :托管取回 refund :票据退票 payoff :票据解付 billsplit :票据拆分 payinterest :买方付息 reccdm :收票登记 paycdm :开票登记 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | frecsubbillrange |  | varchar | 80 |  | √ | ' ' |  |
| 12 | fdrafttradebillno | 票据处理单编码 | varchar | 80 |  | √ | ' ' | 票据处理单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_draftbill_circulat |  | fid |
| 2 | pk_cdm_draftbill_circulat |  | fentryid |
