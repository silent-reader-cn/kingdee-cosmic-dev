# 池内票据查询-cdm_pooldraftbill_query

## 池内票据查询-主表 t_cdm_draftbill

- **表名称：** 池内票据查询-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 3 | fdeliveraccountbase | 交票人账号 | varchar | 50 |  | √ | ' ' | 交票人账号 |
| 4 | fdeliveropenbanknum | 交票人开户行行号 | varchar | 50 |  | √ | ' ' | 交票人开户行行号 |
| 5 | fdeliverid | 交票人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 8 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fintopooltime | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 11 | fsourcedraftid | 源票据号码id | int8 | 64 |  | √ | 0 | 源票据号码id |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fsourcebillentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 14 | fsourcebilltype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: cdm_payablebill :开票登记 cdm_drafttradebill :票据业务处理单 |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :已作废 |
| 16 | fpayeetype | 交票人类型 | varchar | 30 |  | √ | ' ' | 交票人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 17 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 21 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 22 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 23 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 24 | fsubbillrange | 子票包区间 | varchar | 50 |  | √ | ' ' | 子票包区间 |
| 25 | fsubbillendflag | 子票包结束标识 | int8 | 64 |  | √ | 0 | 子票包结束标识 |
| 26 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 27 | fsubbillstartflag | 子票包开始标识 | int8 | 64 |  | √ | 0 | 子票包开始标识 |
| 28 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 29 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 endorsed :已背书 discounted :已贴现 collected :已托收 splited :已拆分 |
| 30 | fdraftbillnoid | fdraftbillnoid | int8 | 64 |  | √ | 0 |  |
| 31 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | 票据池维护 cdm_billpool |
| 32 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 33 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 34 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 35 | fpoollockorgid | 锁票人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fbankaccountid | 银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 39 | fdeliveropenbank | 交票人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 40 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 41 | fclaimnoticebillno | 收款认领通知单 | varchar | 80 |  | √ | ' ' | 收款认领通知单 |
| 42 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 43 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 44 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 cdm-draftallocate :票据调度 |
| 45 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 46 | fdelivername | 交票人全称 | varchar | 800 |  | √ | ' ' | 交票人全称 |
| 47 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 48 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fpoollocktime | 锁定时间 | timestamp | 0 |  |  | null | 锁定时间 |
| 51 | fpoollockstatus | 锁定状态 | bpchar | 1 |  | √ | '0' | 锁定状态,枚举: 1 :锁定 0 :未锁定 |
| 52 | fpaybilltype | fpaybilltype | varchar | 50 |  | √ | ' ' |  |
| 53 | fdeliveraccounttext | 交票人账号 | varchar | 50 |  | √ | ' ' | 交票人账号 |
| 54 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 57 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 58 | fissplit | 能否拆分 | bpchar | 1 |  | √ | '0' | 能否拆分 |
| 59 | fguarantee | fguarantee | varchar | 50 |  | √ | ' ' |  |
| 60 | faccepterbankid | 承兑人开户行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 61 | fsubbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |
| 62 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 63 | fallocbillentryid | 票据池调度分录ID | int8 | 64 |  | √ | 0 | 票据池调度分录ID |
| 64 | fcasamount | 出纳下推金额 | numeric | 19 | 6 | √ | 0 | 出纳下推金额 |
| 65 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 66 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 67 | fbeendorsor | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 68 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 69 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 70 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 71 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 72 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 73 | fdelivertype | 交票人基础资料类型 | varchar | 30 |  | √ | ' ' | 交票人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |

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

## 池内票据查询-关联追踪表 t_cdm_draftbill_tc

- **表名称：** 池内票据查询-关联追踪表
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

## 池内票据查询-多语言表 t_cdm_draftbill_l

- **表名称：** 池内票据查询-多语言表
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

## 池内票据查询-分表 t_cdm_draftbill_f

- **表名称：** 池内票据查询-分表
- **表名：** t_cdm_draftbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feledraftstatus | 电票状态 | varchar | 30 |  | √ | ' ' | 电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 |
| 3 | freturnnotetag | 回头票据 | bpchar | 1 |  | √ | '0' | 回头票据 |
| 4 | flockbilltime | 锁票时间 | timestamp | 0 |  |  | null | 锁票时间 |
| 5 | fpredictunlocktime | 预计解锁时间 | timestamp | 0 |  |  | null | 预计解锁时间 |
| 6 | flockbilluser | 锁票用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | faccepteraccountid | faccepteraccountid | int8 | 64 |  | √ | 0 |  |
| 8 | fdraftbilltranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 9 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 10 | faccepterbebankid | 承兑人全称 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 11 | fcontractno | fcontractno | varchar | 50 |  | √ | ' ' |  |

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

## 池内票据查询-分表 t_cdm_draftbill_e

- **表名称：** 池内票据查询-分表
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
| 11 | fissueticketgrade | 出票人评级机构 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
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
| 24 | fdrawerid | 出票人全称 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 25 | fissuepromiser | 出票保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fissuepromisertype | 出票保证人类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | facceptpromisertype | 承兑保证人类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 28 | fisvoucher | 生成凭证 | bpchar | 1 |  |  | '0' | 生成凭证 |
| 29 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 30 | fpromisegrade | 承兑人评级机构 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
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
| 41 | fdrawerbankid | 出票人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | 出票保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | fdrawercompanyid | int8 | 64 |  | √ | 0 |  |
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

## 池内票据查询-反写记录表 t_cdm_draftbill_wb

- **表名称：** 池内票据查询-反写记录表
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
| 3 | forgfield |  | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
