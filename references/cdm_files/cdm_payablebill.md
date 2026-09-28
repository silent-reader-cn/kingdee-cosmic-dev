# 应付票据-cdm_payablebill

## 应付票据-主表 t_cdm_draftbill

- **表名称：** 应付票据-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 3 | fdeliveraccountbase | fdeliveraccountbase | varchar | 50 |  | √ | ' ' |  |
| 4 | fdeliveropenbanknum | fdeliveropenbanknum | varchar | 50 |  | √ | ' ' |  |
| 5 | fdeliverid | fdeliverid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 8 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fintopooltime | fintopooltime | timestamp | 0 |  |  | null |  |
| 11 | fsourcedraftid | fsourcedraftid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :已作废 |
| 16 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 17 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0.000000 | 实际占用授信金额 |
| 20 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 21 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 22 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 23 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 24 | fsubbillrange | 子票包区间 | varchar | 50 |  | √ | ' ' | 子票包区间 |
| 25 | fsubbillendflag | 子票包结束标识 | int8 | 64 |  | √ | 0 | 子票包结束标识 |
| 26 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 27 | fsubbillstartflag | 子票包开始标识 | int8 | 64 |  | √ | 0 | 子票包开始标识 |
| 28 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 29 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 payoffed :已解付 splited :已拆分 |
| 30 | fdraftbillnoid | 票据号码 | int8 | 64 |  | √ | 0 | 支票F7数据 cdm_cheque_f7data |
| 31 | fbillpoolid | fbillpoolid | int8 | 64 |  | √ | 0 |  |
| 32 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 33 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 34 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 35 | fpoollockorgid | fpoollockorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fbankaccountid | fbankaccountid | int8 | 64 |  | √ | 0 |  |
| 39 | fdeliveropenbank | fdeliveropenbank | int8 | 64 |  | √ | 0 |  |
| 40 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 41 | fclaimnoticebillno | fclaimnoticebillno | varchar | 80 |  | √ | ' ' |  |
| 42 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 43 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 44 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 apply :开票申请 |
| 45 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 46 | fdelivername | fdelivername | varchar | 800 |  | √ | ' ' |  |
| 47 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 48 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fpoollocktime | fpoollocktime | timestamp | 0 |  |  | null |  |
| 51 | fpoollockstatus | fpoollockstatus | bpchar | 1 |  | √ | '0' |  |
| 52 | fpaybilltype | 开票方式 | varchar | 50 |  | √ | ' ' | 开票方式,枚举: credit :授信 guarantee :担保 other :其他 |
| 53 | fdeliveraccounttext | fdeliveraccounttext | varchar | 50 |  | √ | ' ' |  |
| 54 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 57 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 58 | fissplit | 能否拆分 | bpchar | 1 |  | √ | '0' | 能否拆分 |
| 59 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 4 :抵押 5 :质押 |
| 60 | faccepterbankid | faccepterbankid | int8 | 64 |  | √ | 0 |  |
| 61 | fsubbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |
| 62 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 63 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 64 | fcasamount | 出纳下推金额 | numeric | 19 | 6 | √ | 0 | 出纳下推金额 |
| 65 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 66 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 67 | fbeendorsor | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 68 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 69 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 70 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 71 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 72 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | 授信额度管理 cfm_creditlimit |
| 73 | fdelivertype | fdelivertype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_pkey |  | fid |
| 2 | idx_cdm_draftbill_billpoolid |  | fbillpoolid |
| 3 | idx_t_cdm_draftbill |  | fbizdate,fdraftbillstatus |
| 4 | idx_cdm_draftbill_allocentid |  | fallocbillentryid |

---

## 保证金分录-子表 t_cdm_draftbill_surety_e

- **表名称：** 保证金分录-子表
- **表名：** t_cdm_draftbill_surety_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuretycurrency | fsuretycurrency | int8 | 64 |  | √ | 0 |  |
| 3 | fsuretyexpiredate | fsuretyexpiredate | timestamp | 0 |  |  | null |  |
| 4 | fsuretyfinorg | fsuretyfinorg | int8 | 64 |  | √ | 0 |  |
| 5 | fsuretyamount | fsuretyamount | numeric | 19 | 6 | √ | 0 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsuretyaccount | fsuretyaccount | int8 | 64 |  | √ | 0 |  |
| 8 | fsuretybill | 单据编号 | int8 | 64 |  | √ | 0 | 保证金存入处理F7 fbd_suretybill_f7 |
| 9 | fguaranteetype | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: deposit :保证金 |
| 10 | fsuretyintdate | fsuretyintdate | timestamp | 0 |  |  | null |  |
| 11 | fsuretyterm | fsuretyterm | varchar | 80 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsuretysource | 单据来源 | varchar | 80 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_surety_e |  | fentryid |
| 2 | idx_cdm_draftbill_surety_e |  | fguaranteetype,fsuretybill |

---

## 应付票据-关联追踪表 t_cdm_draftbill_tc

- **表名称：** 应付票据-关联追踪表
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

## 应付票据-多语言表 t_cdm_draftbill_l

- **表名称：** 应付票据-多语言表
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

## 应付票据-分表 t_cdm_draftbill_f

- **表名称：** 应付票据-分表
- **表名：** t_cdm_draftbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feledraftstatus | 电票状态 | varchar | 30 |  | √ | ' ' | 电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 destroy :票据已作废 |
| 3 | freturnnotetag | freturnnotetag | bpchar | 1 |  | √ | '0' |  |
| 4 | flockbilltime | flockbilltime | timestamp | 0 |  |  | null |  |
| 5 | fpredictunlocktime | fpredictunlocktime | timestamp | 0 |  |  | null |  |
| 6 | flockbilluser | flockbilluser | int8 | 64 |  | √ | 0 |  |
| 7 | faccepteraccountid | 承兑人账号(基础资料) | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 8 | fdraftbilltranstatus | 出票状态 | varchar | 30 |  | √ | ' ' | 出票状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 9 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 10 | faccepterbebankid | faccepterbebankid | int8 | 64 |  | √ | 0 |  |
| 11 | fcontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |

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

## 应付票据-分表 t_cdm_draftbill_e

- **表名称：** 应付票据-分表
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
| 9 | faccpromisetype | 承兑保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 10 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 11 | fissueticketgrade | 出票人评级机构 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 12 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 13 | fpromisecreditlevel | 承兑人信用等级 | varchar | 80 |  | √ | ' ' | 承兑人信用等级 |
| 14 | fissueticketexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 15 | facceptpromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 16 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 17 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 18 | fdraweraccountname | 出票人账户名称 | varchar | 80 |  | √ | ' ' | 出票人账户名称 |
| 19 | freceiverid | 收款人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fvouchernum | 凭证号 | varchar | 150 |  |  | null | 凭证号 |
| 21 | fdrawerbankname | 出票人开户银行 | varchar | 80 |  | √ | ' ' | 出票人开户银行 |
| 22 | fissuepromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 23 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 24 | fdrawerid | fdrawerid | int8 | 64 |  | √ | 0 |  |
| 25 | fissuepromiser | 出票保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fissuepromisertype | 出票保证人类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | facceptpromisertype | 承兑保证人类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 28 | fisvoucher | 生成凭证 | bpchar | 1 |  |  | '0' | 生成凭证 |
| 29 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 30 | fpromisegrade | 承兑人评级机构 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 31 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 32 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 33 | fissuepromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 34 | facceptpromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 35 | freceivertype | 收款人全称类型 | varchar | 30 |  | √ | ' ' | 收款人全称类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 36 | facceptpromisername | 承兑保证人名称 | varchar | 80 |  | √ | ' ' | 承兑保证人名称 |
| 37 | faccepterfinorgid | 承兑人全称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 38 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 39 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fissueticketcreditlevel | 出票人信用等级 | varchar | 80 |  | √ | ' ' | 出票人信用等级 |
| 41 | fdrawerbankid | fdrawerbankid | int8 | 64 |  | √ | 0 |  |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | 出票保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fissuepromisername | 出票保证人名称 | varchar | 80 |  | √ | ' ' | 出票保证人名称 |
| 48 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 49 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
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

## 应付票据-反写记录表 t_cdm_draftbill_wb

- **表名称：** 应付票据-反写记录表
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
| 2 | fbillamt | 票面金额 | numeric | 19 | 6 | √ | 0 | 票面金额 |
| 3 | forgfield | 我方组织： | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
