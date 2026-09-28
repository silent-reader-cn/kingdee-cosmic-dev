# 票据登记-cdm_draftbillf7

## 票据登记-主表 t_cdm_draftbill

- **表名称：** 票据登记-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 3 | fdeliveraccountbase | fdeliveraccountbase | varchar | 50 |  | √ | ' ' |  |
| 4 | fdeliveropenbanknum | fdeliveropenbanknum | varchar | 50 |  | √ | ' ' |  |
| 5 | fdeliverid | 交票人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdraftbillexpiredate | 票据到期日期 | timestamp | 0 |  |  | null | 票据到期日期 |
| 8 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fintopooltime | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 11 | fsourcedraftid | 源票据id | int8 | 64 |  | √ | 0 | 源票据id |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpayeetype | 交票人类型 | varchar | 30 |  | √ | ' ' | 交票人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 17 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 21 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 22 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 23 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 24 | fsubbillrange | 子票包区间 | varchar | 50 |  | √ | ' ' | 子票包区间 |
| 25 | fsubbillendflag | 子票包结束标识 | int8 | 64 |  | √ | 0 | 子票包结束标识 |
| 26 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 27 | fsubbillstartflag | 子票包开始标识 | int8 | 64 |  | √ | 0 | 子票包开始标识 |
| 28 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 29 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 endorsed :已背书 discounted :已贴现 collected :已托收 refunded :已退票 payoffed :已解付 splited :已拆分 |
| 30 | fdraftbillnoid | fdraftbillnoid | int8 | 64 |  | √ | 0 |  |
| 31 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | 票据池维护 cdm_billpool |
| 32 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 33 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 34 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 35 | fpoollockorgid | 锁票人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 37 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fbankaccountid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 39 | fdeliveropenbank | fdeliveropenbank | int8 | 64 |  | √ | 0 |  |
| 40 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 41 | fclaimnoticebillno | fclaimnoticebillno | varchar | 80 |  | √ | ' ' |  |
| 42 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 43 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 44 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 cdm-draftallocate :票据调度 |
| 45 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 46 | fdelivername | 交票人全称 | varchar | 800 |  | √ | ' ' | 交票人全称 |
| 47 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 48 | fuse | fuse | varchar | 255 |  | √ | ' ' |  |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fpoollocktime | fpoollocktime | timestamp | 0 |  |  | null |  |
| 51 | fpoollockstatus | 锁定状态 | bpchar | 1 |  | √ | '0' | 锁定状态,枚举: 1 :锁定 0 :未锁定 |
| 52 | fpaybilltype | fpaybilltype | varchar | 50 |  | √ | ' ' |  |
| 53 | fdeliveraccounttext | fdeliveraccounttext | varchar | 50 |  | √ | ' ' |  |
| 54 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 57 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 58 | fissplit | 能否拆分 | bpchar | 1 |  | √ | '0' | 能否拆分 |
| 59 | fguarantee | fguarantee | varchar | 50 |  | √ | ' ' |  |
| 60 | faccepterbankid | faccepterbankid | int8 | 64 |  | √ | 0 |  |
| 61 | fsubbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |
| 62 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 63 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 64 | fcasamount | 出纳下推金额 | numeric | 19 | 6 | √ | 0 | 出纳下推金额 |
| 65 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 66 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 67 | fbeendorsor | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 68 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 69 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 70 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 71 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 72 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 73 | fdelivertype | 交票人基础资料类型 | varchar | 30 |  | √ | ' ' | 交票人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 |

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

## 票据登记-多语言表 t_cdm_draftbill_l

- **表名称：** 票据登记-多语言表
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

## 票据登记-分表 t_cdm_draftbill_f

- **表名称：** 票据登记-分表
- **表名：** t_cdm_draftbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feledraftstatus | 电票状态 | varchar | 30 |  | √ | ' ' | 电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 |
| 3 | freturnnotetag | freturnnotetag | bpchar | 1 |  | √ | '0' |  |
| 4 | flockbilltime | flockbilltime | timestamp | 0 |  |  | null |  |
| 5 | fpredictunlocktime | fpredictunlocktime | timestamp | 0 |  |  | null |  |
| 6 | flockbilluser | flockbilluser | int8 | 64 |  | √ | 0 |  |
| 7 | faccepteraccountid | faccepteraccountid | int8 | 64 |  | √ | 0 |  |
| 8 | fdraftbilltranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 porsuccess :部分成功 failing :交易失败 |
| 9 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 10 | faccepterbebankid | faccepterbebankid | int8 | 64 |  | √ | 0 |  |
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

## 票据登记-分表 t_cdm_draftbill_e

- **表名称：** 票据登记-分表
- **表名：** t_cdm_draftbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpromiseexpiredate | fpromiseexpiredate | timestamp | 0 |  |  | null |  |
| 3 | faccepteraccount | 承兑人账号 | varchar | 80 |  | √ | ' ' | 承兑人账号 |
| 4 | fissuepromiserdate | fissuepromiserdate | timestamp | 0 |  |  | null |  |
| 5 | faccepterorgid | faccepterorgid | int8 | 64 |  | √ | 0 |  |
| 6 | faccepterbankno | 承兑人开户行行号 | varchar | 80 |  | √ | ' ' | 承兑人开户行行号 |
| 7 | freceiverbankno | 收款人开户行行号 | varchar | 80 |  | √ | ' ' | 收款人开户行行号 |
| 8 | facceptpromiserdate | facceptpromiserdate | timestamp | 0 |  |  | null |  |
| 9 | faccpromisetype | faccpromisetype | varchar | 30 |  | √ | ' ' |  |
| 10 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 11 | fissueticketgrade | fissueticketgrade | int8 | 64 |  | √ | 0 |  |
| 12 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 13 | fpromisecreditlevel | fpromisecreditlevel | varchar | 80 |  | √ | ' ' |  |
| 14 | fissueticketexpiredate | fissueticketexpiredate | timestamp | 0 |  |  | null |  |
| 15 | facceptpromiseraccount | facceptpromiseraccount | varchar | 80 |  | √ | ' ' |  |
| 16 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 17 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 18 | fdraweraccountname | 出票人账号 | varchar | 80 |  | √ | ' ' | 出票人账号 |
| 19 | freceiverid | 收款人全称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fvouchernum | fvouchernum | varchar | 150 |  |  | null |  |
| 21 | fdrawerbankname | 出票人开户银行 | varchar | 80 |  | √ | ' ' | 出票人开户银行 |
| 22 | fissuepromiseraccount | fissuepromiseraccount | varchar | 80 |  | √ | ' ' |  |
| 23 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 24 | fdrawerid | 出票人全称 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 25 | fissuepromiser | fissuepromiser | int8 | 64 |  | √ | 0 |  |
| 26 | fissuepromisertype | fissuepromisertype | varchar | 30 |  | √ | ' ' |  |
| 27 | facceptpromisertype | facceptpromisertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 29 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 30 | fpromisegrade | fpromisegrade | int8 | 64 |  | √ | 0 |  |
| 31 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 32 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 33 | fissuepromiseraddr | fissuepromiseraddr | varchar | 80 |  | √ | ' ' |  |
| 34 | facceptpromiseraddr | facceptpromiseraddr | varchar | 80 |  | √ | ' ' |  |
| 35 | freceivertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 36 | facceptpromisername | facceptpromisername | varchar | 80 |  | √ | ' ' |  |
| 37 | faccepterfinorgid | faccepterfinorgid | int8 | 64 |  | √ | 0 |  |
| 38 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 39 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fissueticketcreditlevel | fissueticketcreditlevel | varchar | 80 |  | √ | ' ' |  |
| 41 | fdrawerbankid | 出票人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | fisspromisetype | varchar | 30 |  | √ | ' ' |  |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fissuepromisername | fissuepromisername | varchar | 80 |  | √ | ' ' |  |
| 48 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 49 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 50 | facceptpromiser | facceptpromiser | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_draftbill_e_pkey |  | fid |
| 2 | idx_t_cdm_draftbill_e |  | fdrawername |
