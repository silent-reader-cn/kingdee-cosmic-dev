# 应付票据-cdm_payablebill

## 应付票据-主表 t_cdm_draftbill

- **表名称：** 应付票据-主表
- **表名：** t_cdm_draftbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeliveraccountbase | fdeliveraccountbase | varchar | 50 |  | √ | ' ' |  |
| 3 | finnerendorsetradeid | finnerendorsetradeid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 6 | facpflg | 承兑类型 | varchar | 255 |  | √ | ' ' | 承兑类型,枚举: 0 :全额保证金在线承兑 1 :授信项下在线承兑 2 :普通承兑 |
| 7 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 8 | finnerendorsepayid | finnerendorsepayid | int8 | 64 |  | √ | 0 |  |
| 9 | fsupperbillamount | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fvouchernum | fvouchernum | varchar | 50 |  |  | null |  |
| 12 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0.000000 | 实际占用授信金额 |
| 13 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 14 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 15 | fsubbillendflag | 子票终止序号 | int8 | 64 |  | √ | 0 | 子票终止序号 |
| 16 | fstandardbillamount | 标准票据金额 | numeric | 19 | 6 | √ | 0.01 | 标准票据金额 |
| 17 | fsubbillstartflag | 子票开始序号 | int8 | 64 |  | √ | 0 | 子票开始序号 |
| 18 | favailableamount | 可用金额 | numeric | 19 | 6 | √ | 0 | 可用金额 |
| 19 | fequaltradebillid | 等分化业务id | int8 | 64 |  | √ | 0 | 等分化业务id |
| 20 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 21 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 payoffed :已解付 splited :已拆分 |
| 22 | fbillpoolid | fbillpoolid | int8 | 64 |  | √ | 0 |  |
| 23 | fisvoucher | fisvoucher | bpchar | 1 |  |  | '0' |  |
| 24 | fpoollockorgid | fpoollockorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbankmsg | fbankmsg | varchar | 2000 |  | √ | ' ' |  |
| 27 | fbankaccountid | fbankaccountid | int8 | 64 |  | √ | 0 |  |
| 28 | fclaimnoticebillno | fclaimnoticebillno | varchar | 80 |  | √ | ' ' |  |
| 29 | famount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.000000 | 票面金额(子票包金额) |
| 30 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 apply :开票申请 |
| 31 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 32 | fdelivername | fdelivername | varchar | 800 |  | √ | ' ' |  |
| 33 | fisinit | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 34 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fpoollocktime | fpoollocktime | timestamp | 0 |  |  | null |  |
| 37 | fpoollockstatus | fpoollockstatus | bpchar | 1 |  | √ | '0' |  |
| 38 | fpaybilltype | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: credit :授信 guarantee :保证金 other :其他 |
| 39 | finneraccountid | 内部账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 40 | fdeliveraccounttext | fdeliveraccounttext | varchar | 50 |  | √ | ' ' |  |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | faccepterbankid | faccepterbankid | int8 | 64 |  | √ | 0 |  |
| 44 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 45 | foriginalsubbillamount | 原始子票包金额 | numeric | 23 | 10 | √ | 0 | 原始子票包金额 |
| 46 | foriginalsubbillrang | 原始子票包区间 | varchar | 255 |  | √ | ' ' | 原始子票包区间 |
| 47 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 48 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 49 | fbaleac | 保证金账号 | varchar | 255 |  | √ | ' ' | 保证金账号 |
| 50 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 51 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 52 | fdeliveropenbanknum | fdeliveropenbanknum | varchar | 50 |  | √ | ' ' |  |
| 53 | fsuretyremainamount | 保证金剩余金额 | numeric | 19 | 4 | √ | 0 | 保证金剩余金额 |
| 54 | fdeliverid | fdeliverid | int8 | 64 |  | √ | 0 |  |
| 55 | facceptdate | 承兑日期 | timestamp | 0 |  |  | null | 承兑日期 |
| 56 | flockedamount | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 57 | fintopooltime | fintopooltime | timestamp | 0 |  |  | null |  |
| 58 | fsourcedraftid | fsourcedraftid | int8 | 64 |  | √ | 0 |  |
| 59 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 60 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 H :已作废 |
| 62 | fsuretyinput | 存入保证金 | bpchar | 1 |  | √ | '0' | 存入保证金 |
| 63 | fbillidentitycode | 票据识别码 | varchar | 255 |  | √ | ' ' | 票据识别码 |
| 64 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 65 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 66 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 67 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 68 | fsubbillrange | 子票区间 | varchar | 50 |  | √ | ' ' | 子票区间 |
| 69 | feuqaldifferetype | 等分化业务类型 | varchar | 255 |  | √ | ' ' | 等分化业务类型 |
| 70 | fdraftbillnoid | 票据号码 | int8 | 64 |  | √ | 0 | [支票F7数据 cdm_cheque_f7data](../cdm_files/cdm_cheque_f7data.md) |
| 71 | fsubbillamount | fsubbillamount | numeric | 19 | 6 | √ | 0 |  |
| 72 | fuseamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 73 | fsupperbillid | 拆票母票id | int8 | 64 |  | √ | 0 | 拆票母票id |
| 74 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fisfromalloc | fisfromalloc | bpchar | 1 |  | √ | '0' |  |
| 76 | fdeliveropenbank | fdeliveropenbank | int8 | 64 |  | √ | 0 |  |
| 77 | facpfer | 承兑手续费率% | numeric | 23 | 10 | √ | 0 | 承兑手续费率% |
| 78 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 79 | fbaltyp | 保证金类型 | varchar | 255 |  | √ | ' ' | 保证金类型,枚举: 01 :单位活期保证金（招商银行） 11 :单位定期保证金（招商银行） 1 :单位活期保证金（兴业银行） 2 :单位定期保证金（兴业银行） |
| 80 | fishistorydata | 等分化前历史数据 | bpchar | 1 |  | √ | '0' | 等分化前历史数据 |
| 81 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 82 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 83 | fusedamount | 已用金额 | numeric | 19 | 6 | √ | 0 | 已用金额 |
| 84 | fisrefund | 发生退票 | bpchar | 1 |  | √ | '0' | 发生退票 |
| 85 | fisfromequalspilt | 来源等分化拆分 | bpchar | 1 |  | √ | '0' | 来源等分化拆分 |
| 86 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 87 | fequaltradebilltype | 等分化业务类型 | varchar | 255 |  | √ | ' ' | 等分化业务类型 |
| 88 | fissplit | 能否拆分 | bpchar | 1 |  | √ | '0' | 能否拆分 |
| 89 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 4 :抵押 5 :质押 |
| 90 | fsuretymoney | 保证金 | numeric | 23 | 10 | √ | 0 | 保证金 |
| 91 | fsubbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |
| 92 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 93 | famountofcredit | 占用授信额度 | numeric | 23 | 10 | √ | 0 | 占用授信额度 |
| 94 | fcasamount | 出纳下推金额 | numeric | 19 | 6 | √ | 0 | 出纳下推金额 |
| 95 | fbizdate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 96 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 97 | fbeendorsor | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 98 | fsplitlogid | 拆分对应的日志 | int8 | 64 |  | √ | 0 | 拆分对应的日志 |
| 99 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 100 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 101 | fisequalbill | 等分化票据 | bpchar | 1 |  | √ | '0' | 等分化票据 |
| 102 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 103 | fdelivertype | fdelivertype | varchar | 30 |  | √ | ' ' |  |

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
| 6 | frel_bizdate | 出纳单据业务日期 | timestamp | 0 |  |  | null | 出纳单据业务日期 |
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
| 2 | feledraftstatus | 电票状态(旧) | varchar | 30 |  | √ | ' ' | 电票状态(旧),枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款待签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 destroy :票据已作废 |
| 3 | flockbilltime | flockbilltime | timestamp | 0 |  |  | null |  |
| 4 | fpredictunlocktime | fpredictunlocktime | timestamp | 0 |  |  | null |  |
| 5 | flockbilluser | flockbilluser | int8 | 64 |  | √ | 0 |  |
| 6 | fpledgeetypebase | fpledgeetypebase | varchar | 50 |  | √ | ' ' |  |
| 7 | frelatedelcbillid | 关联电票ID | int8 | 64 |  | √ | 0 | 关联电票ID |
| 8 | fpledgeebase | fpledgeebase | int8 | 64 |  | √ | 0 |  |
| 9 | fautoreceive | 自动提示收票 | bpchar | 1 |  | √ | '0' | 自动提示收票 |
| 10 | fpromisrate | 保证金比例(%) | numeric | 19 | 6 | √ | 0 | 保证金比例(%) |
| 11 | fsuretyonline | 在线开立保证金 | bpchar | 1 |  | √ | '0' | 在线开立保证金 |
| 12 | fpledgeetext | fpledgeetext | varchar | 512 |  | √ | ' ' |  |
| 13 | faccepteraccountid | 承兑人账号(基础资料) | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | fdraftbilltranstatus | 出票状态 | varchar | 30 |  | √ | ' ' | 出票状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 15 | felectag | 提交电票 | varchar | 1 |  | √ | ' ' | 提交电票 |
| 16 | fpledgeeaccount | fpledgeeaccount | varchar | 100 |  | √ | ' ' |  |
| 17 | felccirculatestatus | 电票流通标识 | varchar | 255 |  | √ | ' ' | 电票流通标识,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 18 | fpledgeeopenbank | fpledgeeopenbank | int8 | 64 |  | √ | 0 |  |
| 19 | fautoaccept | 自动提示承兑 | bpchar | 1 |  | √ | '0' | 自动提示承兑 |
| 20 | fpledgeeaccounttext | fpledgeeaccounttext | varchar | 100 |  | √ | ' ' |  |
| 21 | fbizfinishdate | 业务处理完成日期 | timestamp | 0 |  |  | null | 业务处理完成日期 |
| 22 | fbatchno | 预开票批次号 | varchar | 255 |  | √ | ' ' | 预开票批次号 |
| 23 | frectype | frectype | varchar | 30 |  | √ | ' ' |  |
| 24 | fpledgeetype | fpledgeetype | varchar | 50 |  | √ | ' ' |  |
| 25 | feledraftstatusnew | 电票状态 | varchar | 255 |  | √ | ' ' | 电票状态,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 preregister :预出票 registering :待出票 |
| 26 | faccepterbebankid | faccepterbebankid | int8 | 64 |  | √ | 0 |  |
| 27 | fcontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |
| 28 | ftradetypenew | ftradetypenew | varchar | 50 |  | √ | ' ' |  |
| 29 | freturnnotetag | freturnnotetag | bpchar | 1 |  | √ | '0' |  |
| 30 | fisrelatedprebill | 关联预出票 | bpchar | 1 |  | √ | '0' | 关联预出票 |
| 31 | fsuretypayacct | 保证金付款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 32 | frulename | frulename | varchar | 100 |  | √ | ' ' |  |
| 33 | febstatus | febstatus | varchar | 50 |  | √ | ' ' |  |
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
| 11 | fissueticketgrade | 出票人评级机构 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 12 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
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
| 30 | fpromisegrade | 承兑人评级机构 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 31 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 32 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 33 | fissuepromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 34 | facceptpromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 35 | freceivertype | 收款人全称类型 | varchar | 30 |  | √ | ' ' | 收款人全称类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 36 | facceptpromisername | 承兑保证人名称 | varchar | 80 |  | √ | ' ' | 承兑保证人名称 |
| 37 | faccepterfinorgid | 承兑人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 38 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 39 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fissueticketcreditlevel | 出票人信用等级 | varchar | 80 |  | √ | ' ' | 出票人信用等级 |
| 41 | fdrawerbankid | fdrawerbankid | int8 | 64 |  | √ | 0 |  |
| 42 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 43 | freceivername | 收款人全称 | varchar | 1024 |  | √ | ' ' | 收款人全称 |
| 44 | fisspromisetype | 出票保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 45 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 46 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 3 | forgfield | 我方组织： | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
