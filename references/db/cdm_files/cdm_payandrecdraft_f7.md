# 应收应付票据登记-cdm_payandrecdraft_f7

## 应收应付票据登记-主表 t_cdm_draftbill

- **表名称：** 应收应付票据登记-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeliveraccountbase | fdeliveraccountbase | varchar | 50 |  | √ | ' ' |  |
| 3 | finnerendorsetradeid | finnerendorsetradeid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdraftbillexpiredate | 票据到期日期 | timestamp | 0 |  |  | null | 票据到期日期 |
| 6 | facpflg | facpflg | varchar | 255 |  | √ | ' ' |  |
| 7 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 8 | finnerendorsepayid | finnerendorsepayid | int8 | 64 |  | √ | 0 |  |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 12 | fcreditamount | fcreditamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 14 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 15 | fsubbillendflag | 子票终止序号 | int8 | 64 |  | √ | 0 | 子票终止序号 |
| 16 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 17 | fsubbillstartflag | 子票开始序号 | int8 | 64 |  | √ | 0 | 子票开始序号 |
| 18 | favailableamount | 可用金额 | numeric | 19 | 6 | √ | 0 | 可用金额 |
| 19 | fequaltradebillid | 等分化业务id | int8 | 64 |  | √ | 0 | 等分化业务id |
| 20 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 21 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 endorsed :已背书 discounted :已贴现 collected :已托收 refunded :已退票 payoffed :已解付 splited :已拆分 |
| 22 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | [票据池维护 cdm_billpool](../cdm_files/cdm_billpool.md) |
| 23 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 24 | fpoollockorgid | 锁票人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fbankmsg | 银行响应信息 | varchar | 2000 |  | √ | ' ' | 银行响应信息 |
| 27 | fbankaccountid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 28 | fclaimnoticebillno | 收款认领通知单 | varchar | 80 |  | √ | ' ' | 收款认领通知单 |
| 29 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 30 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 cdm-draftallocate :票据调度 |
| 31 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 32 | fdelivername | 交票人全称 | varchar | 800 |  | √ | ' ' | 交票人全称 |
| 33 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 34 | fuse | fuse | varchar | 255 |  | √ | ' ' |  |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fpoollocktime | fpoollocktime | timestamp | 0 |  |  | null |  |
| 37 | fpoollockstatus | 锁定状态 | bpchar | 1 |  | √ | '0' | 锁定状态,枚举: 1 :锁定 0 :未锁定 |
| 38 | fpaybilltype | fpaybilltype | varchar | 50 |  | √ | ' ' |  |
| 39 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 40 | fdeliveraccounttext | fdeliveraccounttext | varchar | 50 |  | √ | ' ' |  |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | faccepterbankid | faccepterbankid | int8 | 64 |  | √ | 0 |  |
| 44 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 45 | foriginalsubbillamount | 原始子票包金额 | numeric | 23 | 10 | √ | 0 | 原始子票包金额 |
| 46 | foriginalsubbillrang | 原始子票包区间 | varchar | 255 |  | √ | ' ' | 原始子票包区间 |
| 47 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 48 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 49 | fbaleac | fbaleac | varchar | 255 |  | √ | ' ' |  |
| 50 | fsourcemigratedata | fsourcemigratedata | varchar | 80 |  | √ | ' ' |  |
| 51 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 52 | fdeliveropenbanknum | fdeliveropenbanknum | varchar | 50 |  | √ | ' ' |  |
| 53 | fsuretyremainamount | fsuretyremainamount | numeric | 19 | 4 | √ | 0 |  |
| 54 | fdeliverid | 交票人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 55 | facceptdate | facceptdate | timestamp | 0 |  |  | null |  |
| 56 | flockedamount | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 57 | fintopooltime | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 58 | fsourcedraftid | 源票据id | int8 | 64 |  | √ | 0 | 源票据id |
| 59 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 60 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 62 | fsuretyinput | fsuretyinput | bpchar | 1 |  | √ | '0' |  |
| 63 | fbillidentitycode | 票据识别码 | varchar | 255 |  | √ | ' ' | 票据识别码 |
| 64 | fpayeetype | 交票人类型 | varchar | 30 |  | √ | ' ' | 交票人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 65 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 66 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 67 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 68 | fsubbillrange | 子票区间 | varchar | 50 |  | √ | ' ' | 子票区间 |
| 69 | feuqaldifferetype | 等分化业务类型 | varchar | 255 |  | √ | ' ' | 等分化业务类型 |
| 70 | fdraftbillnoid | fdraftbillnoid | int8 | 64 |  | √ | 0 |  |
| 71 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 72 | fuseamount | fuseamount | numeric | 23 | 10 | √ | 0 |  |
| 73 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 74 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fisfromalloc | fisfromalloc | bpchar | 1 |  | √ | '0' |  |
| 76 | fdeliveropenbank | fdeliveropenbank | int8 | 64 |  | √ | 0 |  |
| 77 | facpfer | facpfer | numeric | 23 | 10 | √ | 0 |  |
| 78 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 79 | fbaltyp | fbaltyp | varchar | 255 |  | √ | ' ' |  |
| 80 | fishistorydata | fishistorydata | bpchar | 1 |  | √ | '0' |  |
| 81 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 82 | fpoolprotocolid | fpoolprotocolid | int8 | 64 |  | √ | 0 |  |
| 83 | fusedamount | 已用金额 | numeric | 19 | 6 | √ | 0 | 已用金额 |
| 84 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 85 | fisfromequalspilt | 来源等分化拆分 | bpchar | 1 |  | √ | '0' | 来源等分化拆分 |
| 86 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 87 | fequaltradebilltype | fequaltradebilltype | varchar | 255 |  | √ | ' ' |  |
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
| 98 | fsplitlogid | fsplitlogid | int8 | 64 |  | √ | 0 |  |
| 99 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :应付票据 receivebill :应收票据 |
| 100 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 101 | fisequalbill | 等分化票据 | bpchar | 1 |  | √ | '0' | 等分化票据 |
| 102 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 103 | fdelivertype | 交票人基础资料类型 | varchar | 30 |  | √ | ' ' | 交票人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |

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

## 应收应付票据登记-多语言表 t_cdm_draftbill_l

- **表名称：** 应收应付票据登记-多语言表
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

## 应收应付票据登记-分表 t_cdm_draftbill_f

- **表名称：** 应收应付票据登记-分表
- **表名：** t_cdm_draftbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feledraftstatus | 电票状态(旧) | varchar | 30 |  | √ | ' ' | 电票状态(旧),枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 |
| 3 | flockbilltime | flockbilltime | timestamp | 0 |  |  | null |  |
| 4 | fpredictunlocktime | fpredictunlocktime | timestamp | 0 |  |  | null |  |
| 5 | flockbilluser | flockbilluser | int8 | 64 |  | √ | 0 |  |
| 6 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 bd_finorginfo :金融机构 |
| 7 | frelatedelcbillid | frelatedelcbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 9 | fautoreceive | fautoreceive | bpchar | 1 |  | √ | '0' |  |
| 10 | fpromisrate | fpromisrate | numeric | 19 | 6 | √ | 0 |  |
| 11 | fsuretyonline | fsuretyonline | bpchar | 1 |  | √ | '0' |  |
| 12 | fpledgeetext | 质权人 | varchar | 512 |  | √ | ' ' | 质权人 |
| 13 | faccepteraccountid | faccepteraccountid | int8 | 64 |  | √ | 0 |  |
| 14 | fdraftbilltranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 porsuccess :部分成功 failing :交易失败 |
| 15 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 16 | fpledgeeaccount | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 17 | felccirculatestatus | 电票流通标识 | varchar | 255 |  | √ | ' ' | 电票流通标识,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 18 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 19 | fautoaccept | fautoaccept | bpchar | 1 |  | √ | '0' |  |
| 20 | fpledgeeaccounttext | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 21 | fbizfinishdate | fbizfinishdate | timestamp | 0 |  |  | null |  |
| 22 | fbatchno | fbatchno | varchar | 255 |  | √ | ' ' |  |
| 23 | frectype | frectype | varchar | 30 |  | √ | ' ' |  |
| 24 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 other :其他 bd_finorginfo :合作金融机构 |
| 25 | feledraftstatusnew | 电票状态 | varchar | 255 |  | √ | ' ' | 电票状态,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 26 | faccepterbebankid | faccepterbebankid | int8 | 64 |  | √ | 0 |  |
| 27 | fcontractno | fcontractno | varchar | 50 |  | √ | ' ' |  |
| 28 | ftradetypenew | 电票操作类型 | varchar | 50 |  | √ | ' ' | 电票操作类型,枚举: noteendorse :背书 remitaccept :提示承兑 remitreceive :提示收票 notediscount :贴现 notesignin :签收 ticketguarantee :出票保证 remitregister :开票登记 remitrevocation :撤销出票 notesigninreject :拒收 notecancle :撤销 remitcancle :取消出票 pledgenote :质押 removepledge :质押解除 presentpayment :票据托收 remitconfirm :合同确认 nonnegotiablecancle :不可转让撤销 |
| 29 | freturnnotetag | freturnnotetag | bpchar | 1 |  | √ | '0' |  |
| 30 | fisrelatedprebill | fisrelatedprebill | bpchar | 1 |  | √ | '0' |  |
| 31 | fsuretypayacct | fsuretypayacct | int8 | 64 |  | √ | 0 |  |
| 32 | frulename | frulename | varchar | 100 |  | √ | ' ' |  |
| 33 | febstatus | 电票操作状态 | varchar | 50 |  | √ | ' ' | 电票操作状态,枚举: BANK_PROCESSING :银行处理中 BANK_SUCCESS :交易成功 BANK_FAIL :交易失败 BANK_EXCEPTION :交易未确认 EB_PROCESSING :银企处理中 BANK_UNKNOWN :交易未确认 |
| 34 | fisinnerendorse | fisinnerendorse | bpchar | 1 |  | √ | '0' |  |

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

## 应收应付票据登记-分表 t_cdm_draftbill_e

- **表名称：** 应收应付票据登记-分表
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
| 12 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
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
| 24 | fdrawerid | 出票人全称 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 25 | fissuepromiser | fissuepromiser | int8 | 64 |  | √ | 0 |  |
| 26 | fissuepromisertype | fissuepromisertype | varchar | 30 |  | √ | ' ' |  |
| 27 | facceptpromisertype | facceptpromisertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 29 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 30 | fpromisegrade | fpromisegrade | int8 | 64 |  | √ | 0 |  |
| 31 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 32 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 33 | fissuepromiseraddr | fissuepromiseraddr | varchar | 80 |  | √ | ' ' |  |
| 34 | facceptpromiseraddr | facceptpromiseraddr | varchar | 80 |  | √ | ' ' |  |
| 35 | freceivertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 36 | facceptpromisername | facceptpromisername | varchar | 80 |  | √ | ' ' |  |
| 37 | faccepterfinorgid | faccepterfinorgid | int8 | 64 |  | √ | 0 |  |
| 38 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 39 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fissueticketcreditlevel | fissueticketcreditlevel | varchar | 80 |  | √ | ' ' |  |
| 41 | fdrawerbankid | 出票人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | fisspromisetype | varchar | 30 |  | √ | ' ' |  |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fissuepromisername | fissuepromisername | varchar | 80 |  | √ | ' ' |  |
| 48 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 49 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
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
