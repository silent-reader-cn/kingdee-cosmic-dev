# 代发处理-cas_agentpaybill

## 分录-子表 t_cas_agentpaybillentry

- **表名称：** 分录-子表
- **表名：** t_cas_agentpaybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | falreadyreturnshr | 已退回s-HR | bpchar | 1 |  | √ | '0' | 已退回s-HR |
| 3 | fbankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |
| 4 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpayeebankid | 收款银行（基础资料） | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 7 | fchecktype | 支票类型 | varchar | 30 |  | √ | ' ' | 支票类型,枚举: |
| 8 | freccountryid | 收款方国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 9 | frefundamt | 退款金额 | numeric | 19 | 6 | √ | 0.000000 | 退款金额 |
| 10 | fentrymobile | 收款单位电话 | varchar | 50 |  | √ | ' ' | 收款单位电话 |
| 11 | finformrecemail | 通知收款单位邮箱 | varchar | 255 |  | √ | ' ' | 通知收款单位邮箱 |
| 12 | fpayeeacctbank | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 13 | frecbankaddress | 收款行地址 | varchar | 400 |  | √ | ' ' | 收款行地址 |
| 14 | fauditparam | 清算要求参数 | varchar | 200 |  | √ | ' ' | 清算要求参数 |
| 15 | fsourceagententryid | 源代发分录ID | int8 | 64 |  | √ | 0 | 源代发分录ID |
| 16 | fpayeebankname | 收款银行开户行 | varchar | 255 |  | √ | ' ' | 收款银行开户行 |
| 17 | frecroutingnum | 收款行Routing Number | varchar | 100 |  | √ | ' ' | 收款行Routing Number |
| 18 | frecprovince | 收款方省 | varchar | 30 |  | √ | ' ' | 收款方省 |
| 19 | frecothercode | 收款行其他行号 | varchar | 100 |  | √ | ' ' | 收款行其他行号 |
| 20 | fpaynature | 付款性质 | varchar | 30 |  | √ | ' ' | 付款性质,枚举: 0 :预付货款 1 :货到付款 2 :退款 3 :其他 |
| 21 | fcheckuse | 支票用途 | varchar | 30 |  | √ | ' ' | 支票用途,枚举: |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fplainamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 24 | frecswiftcode | 收款行Swift Code | varchar | 100 |  | √ | ' ' | 收款行Swift Code |
| 25 | fissuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 26 | frefunddes | 退款说明 | varchar | 255 |  |  | null | 退款说明 |
| 27 | fpaymentterm | 收款方式 | bpchar | 1 |  | √ | '0' | 收款方式,枚举: 0 :收款账号 1 :收款人FPS账号 2 :收款人电话 3 :收款方邮箱 |
| 28 | famount | 加密金额 | varchar | 100 |  | √ | ' ' | 加密金额 |
| 29 | fpaymentfps | 收款单位FPS账号 | varchar | 30 |  | √ | ' ' | 收款单位FPS账号 |
| 30 | finforpayment | 通知收款单位 | bpchar | 1 |  | √ | '0' | 通知收款单位 |
| 31 | fisrepaid | 是否已经重付 | bpchar | 1 |  | √ | '0' | 是否已经重付 |
| 32 | fisrefund | 是否退款退票 | bpchar | 1 |  | √ | '0' | 是否退款退票 |
| 33 | fpayeename | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 34 | ftranstypeid | 交易种类 | int8 | 64 |  | √ | 0 | [交易种类 bei_transtype](../bei_files/bei_transtype.md) |
| 35 | fremark | 转账附言 | varchar | 200 |  |  | null | 转账附言 |
| 36 | fpaymentareacode | 收款单位地区码 | varchar | 3 |  | √ | ' ' | 收款单位地区码 |
| 37 | flocalamount | 加密本位币 | varchar | 100 |  | √ | ' ' | 加密本位币 |
| 38 | fpayeebanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 39 | frecemail | 收款方邮箱 | varchar | 500 |  | √ | ' ' | 收款方邮箱 |
| 40 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 41 | freccity | 收款方市县 | varchar | 30 |  | √ | ' ' | 收款方市县 |
| 42 | fpayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fimportpayeetype | 收款单位类型(多类别基础类型,引入) | varchar | 100 |  | √ | ' ' | 收款单位类型(多类别基础类型,引入),枚举: bos_user :职员 bd_supplier :供应商 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 44 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 45 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 46 | fsendway | 寄送方式 | varchar | 30 |  | √ | ' ' | 寄送方式,枚举: |
| 47 | fplainlocalamount | 折本位币 | numeric | 19 | 6 | √ | 0.000000 | 折本位币 |
| 48 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  |  | null | 银行返回信息 |
| 49 | fpaymethod | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_apbe_fpid |  | fid |
| 2 | t_cas_agentpaybillentry_pkey |  | fentryid |
| 3 | idx_cas_apbe_fpayeeid |  | fpayeeid |

---

## 代发处理-反写记录表 t_cas_agentpaybill_wb

- **表名称：** 代发处理-反写记录表
- **表名：** t_cas_agentpaybill_wb

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
| 1 | t_cas_agentpaybill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_cas_agentpaybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_agentpaybillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_agentpaybillentry_lk_pkey |  | fpkid |

---

## 代发处理-关联追踪表 t_cas_agentpaybill_tc

- **表名称：** 代发处理-关联追踪表
- **表名：** t_cas_agentpaybill_tc

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
| 1 | t_cas_agentpaybill_tc_pkey |  | fid |
| 2 | idx_cas_agentpaybill_tc_tid |  | ftid |
| 3 | idx_cas_agentpaybill_tc_tbill |  | ftbillid |

---

## 代发处理-分表 t_cas_agentpaybill_e

- **表名称：** 代发处理-分表
- **表名：** t_cas_agentpaybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisheadpush | 是否整单下推 | bpchar | 1 |  | √ | '0' | 是否整单下推 |
| 3 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 4 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 5 | fhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 6 | fpaychangestatus | 支付信息变更状态 | varchar | 50 |  | √ | '1' | 支付信息变更状态,枚举: 1 :未变更 2 :变更中 3 :已变更 |
| 7 | fisagencypersonpay | 并笔入账 | bpchar | 1 |  | √ | '0' | 并笔入账 |
| 8 | fpaycountryid | 付款方国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 9 | fdpcurrency | 异币种付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fmobile | 收款单位电话 | varchar | 50 |  | √ | ' ' | 收款单位电话 |
| 11 | fissingleca | 是否加签 | bpchar | 1 |  | √ | '0' | 是否加签 |
| 12 | fhsourceentry | 源单分录标识 | varchar | 50 |  | √ | ' ' | 源单分录标识 |
| 13 | fapplyid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmatchresult | 是否已匹配 | bpchar | 1 |  | √ | '0' | 是否已匹配 |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | ffeeactbank | 手续费账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 17 | finstructmsg | 电文指示 | varchar | 30 |  | √ | ' ' | 电文指示,枚举: 1 :单电文 2 :双电文 |
| 18 | factpayamounloc | 实发金额折本位币 | numeric | 23 | 10 | √ | 0 | 实发金额折本位币 |
| 19 | fpaypurpose | 支付用途 | varchar | 64 |  | √ | ' ' | 支付用途,枚举: |
| 20 | fpayproxybankid | 付款代理行 | int8 | 64 |  | √ | 0 | [代理行 bei_proxybank](../bei_files/bei_proxybank.md) |
| 21 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 22 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 23 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 24 | fmatchdetailtype | 匹配流水方式 | varchar | 64 |  | √ | ' ' | 匹配流水方式,枚举: automatch :自动匹配 handmatch :手工匹配 beipay :对账标识码匹配 |
| 25 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 26 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fdppayquotation | 异币种付款汇率换算方式 | varchar | 30 |  | √ | '0' | 异币种付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 29 | fcrosstrantypeid | 交易类型 | int8 | 64 |  | √ | 0 | [银行交易类型 bei_crosstrantype](../bei_files/bei_crosstrantype.md) |
| 30 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 31 | fapplyname | 申请人姓名 | varchar | 70 |  | √ | ' ' | 申请人姓名 |
| 32 | fhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 33 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 34 | fispersonpay | 对私支付 | bpchar | 1 |  | √ | '0' | 对私支付 |
| 35 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 36 | fdpexchangerate | 异币种付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 异币种付款汇率 |
| 37 | flossamt | 汇兑损益 | numeric | 19 | 6 | √ | 0.000000 | 汇兑损益 |
| 38 | fismatchtransdetail | 是否匹配流水 | varchar | 16 |  | √ | '0' | 是否匹配流水 |
| 39 | fdpamt | 异币种付款金额 | numeric | 19 | 6 | √ | 0.000000 | 异币种付款金额 |
| 40 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 41 | fisrepay | 是否失败重付 | bpchar | 1 |  | √ | '0' | 是否失败重付 |
| 42 | ffeecurrency | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 43 | fsettlementmethod | 清算方式 | varchar | 50 |  | √ | ' ' | 清算方式 |
| 44 | fserlevel | 服务级别 | varchar | 30 |  | √ | ' ' | 服务级别,枚举: URGP :紧急支付 SDVA :当日支付 PRPT :优先支付 NURG :其他 : |
| 45 | fdplocalamt | 异币种付款金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 异币种付款金额折本位币 |
| 46 | fagreedquotation | 兑换汇率换算方式 | varchar | 30 |  | √ | '0' | 兑换汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 47 | fpurpose | 支付用途 | varchar | 256 |  | √ | ' ' | 支付用途 |
| 48 | fbookdate_hw | fbookdate_hw | timestamp | 0 |  |  | null |  |
| 49 | fcontractno | 兑换合约号 | varchar | 20 |  | √ | ' ' | 兑换合约号 |
| 50 | fisdiffcur | 异币种付款 | bpchar | 1 |  | √ | '0' | 异币种付款 |
| 51 | fnetbankacctid | 网银子账户 | int8 | 64 |  | √ | 0 | [网银子账户 bd_netbankacct](../basedata_files/bd_netbankacct.md) |
| 52 | fiscrosspay | 跨境支付 | bpchar | 1 |  | √ | '0' | 跨境支付 |
| 53 | ffeepayer | 手续费承担方 | varchar | 30 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方承担 02 :收款方承担 03 :共同承担 |
| 54 | fpayquotation | 付款汇率换算方式 | varchar | 30 |  | √ | '0' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 55 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 56 | fconfirmpaydate | 确认付款时间 | timestamp | 0 |  |  | null | 确认付款时间 |
| 57 | fapplyphone | 申请人电话 | varchar | 50 |  | √ | ' ' | 申请人电话 |
| 58 | fismatchbyhead | 是否按单头匹配 | bpchar | 1 |  | √ | '0' | 是否按单头匹配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_agentpaybill_e_pkey |  | fid |
| 2 | idx_agentpaybill_rb |  | fexratetableid |

---

## 单据体-子表 t_cas_agentbankcheckflag

- **表名称：** 单据体-子表
- **表名：** t_cas_agentbankcheckflag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | febankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_agentbankcf |  | febankcheckflag |
| 2 | idx_cas_agentbankcf_fid |  | fid |
| 3 | pk_t_cas_agentbankcheckflag |  | fentryid |

---

## 代发处理-主表 t_cas_agentpaybill

- **表名称：** 代发处理-主表
- **表名：** t_cas_agentpaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettlettype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faccountcashid | 付款账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 5 | fbankcheckflag | 对账标识码(旧) | varchar | 255 |  | √ | ' ' | 对账标识码(旧) |
| 6 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 9 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpaytime | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 11 | factcount | 实发笔数 | int8 | 64 |  | √ | 0 | 实发笔数 |
| 12 | fbankagentstatus | 银行代发单状态 | varchar | 30 |  | √ | ' ' | 银行代发单状态,枚举: OS :银企处理中 OZ :银企处理中止 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OP :准备提交 OF :银企异常 PS :部分成功 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fbatchseqid | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 15 | factpayamount | 实发金额 | numeric | 19 | 6 | √ | 0.000000 | 实发金额 |
| 16 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbookerid | 会计 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdelegorgid | 委托付款受托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 20 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: repay :代发单 er_dailyloanbill :日常借款单 er_tripreqbill :出差申请单 er_dailyreimbursebill :费用报销单 cas_betransdetail :交易明细 ap_finapbill :财务应付单 cas_recbill :收款单 er_vehiclecheckingbill :用车结算单 er_planecheckingbill :机票结算单 er_hotelcheckingbill :酒店结算单 er_tripreimbursebill :差旅报销单 er_checkingpaybill :月结付款单 CmpAgentPayBill :SHR代发单 fr_glreim_paybill :总账付款单 sHRAgentPayBill :s-HR代发单 er_publicreimbursebill :对公报销单 er_applypaybill :付款申请单 hrp_salarypayment :工资支付 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 F :银行退票 G :已退单 H :已作废 I :退款 |
| 22 | fpayeetype | 收款单位类型(多类别基础类型) | varchar | 50 |  | √ | ' ' | 收款单位类型(多类别基础类型),枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 other :其他 |
| 23 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 26 | fbitbackreason | 打回意见 | varchar | 50 |  | √ | ' ' | 打回意见 |
| 27 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fisbitback | 是否银企打回 | bpchar | 1 |  | √ | '0' | 是否银企打回 |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 32 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 33 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 34 | fsource | 单据来源 | varchar | 30 |  | √ | ' ' | 单据来源,枚举: new :手工新增 impot :导入 BOTP :BOTP |
| 35 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 38 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 39 | fcount | 总笔数 | int8 | 64 |  | √ | 0 | 总笔数 |
| 40 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 41 | fpayeracctbankid | 付款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 44 | flocalamount | 付款金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 付款金额本位币 |
| 45 | fapplyorgid | 委托付款委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 49 | fsettletnumber | 结算号 | varchar | 50 |  | √ | ' ' | 结算号 |
| 50 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 51 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 52 | fcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_apb_forg |  | forgid,fbizdate,fbillstatus |
| 2 | idx_cas_apb_fbillno |  | fbillno |
| 3 | t_cas_agentpaybill_pkey |  | fid |

---

## 分录-分表 t_cas_agentpaybillentry_e

- **表名称：** 分录-分表
- **表名：** t_cas_agentpaybillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 4 | fedplocalamt | 付款折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 付款折本位币金额 |
| 5 | frefundtype | 退类型 | varchar | 30 |  | √ | ' ' | 退类型,枚举: refund :退款 renote :退票 |
| 6 | fefee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 7 | fepaytime | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 8 | fmonproject | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 9 | fmatchresult | 是否已匹配 | bpchar | 1 |  | √ | '0' | 是否已匹配 |
| 10 | frecaddress | 收款方地址 | varchar | 400 |  | √ | ' ' | 收款方地址 |
| 11 | fedpamt | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 12 | frefundbillid | 退款单ID | int8 | 64 |  | √ | 0 | 退款单ID |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_agentpaytime |  | fepaytime |
| 2 | idx_cas_apbee_fpid |  | fid |
| 3 | t_cas_agentpaybillentry_e_pkey |  | fentryid |

---

## 关联子实体-子表 t_cas_agentpaybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_agentpaybill_lk

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
| 1 | t_cas_agentpaybill_lk_pkey |  | fpkid |
