# 代发处理-cas_agentpaybill

## 分录-子表 t_cas_agentpaybillentry

- **表名称：** 分录-子表
- **表名：** t_cas_agentpaybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 3 | falreadyreturnshr | 已退回s-HR | bpchar | 1 |  | √ | '0' | 已退回s-HR |
| 4 | fbankcheckflag | 对账标识码 | varchar | 50 |  | √ | ' ' | 对账标识码 |
| 5 | frefunddes | 退款说明 | varchar | 255 |  |  | null | 退款说明 |
| 6 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpaymentterm | 收款方式 | bpchar | 1 |  | √ | '0' | 收款方式,枚举: 0 :收款账号 1 :收款人FPS账号 2 :收款人电话 3 :收款方邮箱 |
| 9 | fpayeebankid | 收款银行（基础资料） | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 10 | famount | 加密金额 | varchar | 100 |  | √ | ' ' | 加密金额 |
| 11 | fpaymentfps | 收款单位FPS账号 | varchar | 30 |  | √ | ' ' | 收款单位FPS账号 |
| 12 | fchecktype | 支票类型 | varchar | 30 |  | √ | ' ' | 支票类型,枚举: |
| 13 | finforpayment | 通知收款单位 | bpchar | 1 |  | √ | '0' | 通知收款单位 |
| 14 | freccountryid | 收款方国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 15 | fisrepaid | 是否已经重付 | bpchar | 1 |  | √ | '0' | 是否已经重付 |
| 16 | frefundamt | 退款金额 | numeric | 19 | 6 | √ | 0.000000 | 退款金额 |
| 17 | fentrymobile | 收款单位电话 | varchar | 50 |  | √ | ' ' | 收款单位电话 |
| 18 | fisrefund | 是否退款退票 | bpchar | 1 |  | √ | '0' | 是否退款退票 |
| 19 | finformrecemail | 通知收款单位邮箱 | varchar | 255 |  | √ | ' ' | 通知收款单位邮箱 |
| 20 | fpayeename | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 21 | fpayeeacctbank | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 22 | ftranstypeid | 交易种类 | int8 | 64 |  | √ | 0 | 交易种类 bei_transtype |
| 23 | frecbankaddress | 收款行地址 | varchar | 400 |  | √ | ' ' | 收款行地址 |
| 24 | fauditparam | 清算要求参数 | varchar | 200 |  | √ | ' ' | 清算要求参数 |
| 25 | fremark | 转账附言 | varchar | 200 |  |  | null | 转账附言 |
| 26 | fsourceagententryid | 源代发分录ID | int8 | 64 |  | √ | 0 | 源代发分录ID |
| 27 | fpaymentareacode | 收款单位地区码 | varchar | 3 |  | √ | ' ' | 收款单位地区码 |
| 28 | flocalamount | 加密本位币 | varchar | 100 |  | √ | ' ' | 加密本位币 |
| 29 | fpayeebanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 30 | frecemail | 收款方邮箱 | varchar | 500 |  | √ | ' ' | 收款方邮箱 |
| 31 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 32 | fpayeebankname | 收款银行开户行 | varchar | 255 |  | √ | ' ' | 收款银行开户行 |
| 33 | freccity | 收款方市县 | varchar | 30 |  | √ | ' ' | 收款方市县 |
| 34 | frecroutingnum | 收款行Routing Number | varchar | 100 |  | √ | ' ' | 收款行Routing Number |
| 35 | fpayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | frecprovince | 收款方省 | varchar | 30 |  | √ | ' ' | 收款方省 |
| 37 | fimportpayeetype | 收款单位类型(多类别基础类型,引入) | varchar | 100 |  | √ | ' ' | 收款单位类型(多类别基础类型,引入),枚举: bos_user :职员 bd_supplier :供应商 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 38 | frecothercode | 收款行其他行号 | varchar | 100 |  | √ | ' ' | 收款行其他行号 |
| 39 | fpaynature | 付款性质 | varchar | 30 |  | √ | ' ' | 付款性质,枚举: 0 :预付货款 1 :货到付款 2 :退款 3 :其他 |
| 40 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 41 | fsendway | 寄送方式 | varchar | 30 |  | √ | ' ' | 寄送方式,枚举: |
| 42 | fcheckuse | 支票用途 | varchar | 30 |  | √ | ' ' | 支票用途,枚举: |
| 43 | fplainlocalamount | 折本位币 | numeric | 19 | 6 | √ | 0.000000 | 折本位币 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  |  | null | 银行返回信息 |
| 46 | fpaymethod | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: |
| 47 | fplainamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 48 | frecswiftcode | 收款行Swift Code | varchar | 100 |  | √ | ' ' | 收款行Swift Code |

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
| 4 | fhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 5 | fisagencypersonpay | 并笔入账 | bpchar | 1 |  | √ | '0' | 并笔入账 |
| 6 | fpaycountryid | 付款方国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 7 | fdpcurrency | 异币别付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | fmobile | 收款单位电话 | varchar | 50 |  | √ | ' ' | 收款单位电话 |
| 9 | fissingleca | 是否加签 | bpchar | 1 |  | √ | '0' | 是否加签 |
| 10 | fhsourceentry | 源单分录标识 | varchar | 50 |  | √ | ' ' | 源单分录标识 |
| 11 | fapplyid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmatchresult | 是否已匹配 | bpchar | 1 |  | √ | '0' | 是否已匹配 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | ffeeactbank | 手续费账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | finstructmsg | 电文指示 | varchar | 30 |  | √ | ' ' | 电文指示,枚举: 1 :单电文 2 :双电文 |
| 16 | factpayamounloc | 实发金额折本位币 | numeric | 23 | 10 | √ | 0 | 实发金额折本位币 |
| 17 | fpayproxybankid | 付款代理行 | int8 | 64 |  | √ | 0 | 代理行 bei_proxybank |
| 18 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 19 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 20 | fmatchdetailtype | 匹配流水方式 | varchar | 64 |  | √ | ' ' | 匹配流水方式,枚举: automatch :自动匹配 handmatch :手工匹配 beipay :对账标识码匹配 |
| 21 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 22 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fdppayquotation | 异币别付款汇率换算方式 | varchar | 30 |  | √ | '0' | 异币别付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 25 | fcrosstrantypeid | 交易类型 | int8 | 64 |  | √ | 0 | 银行交易类型 bei_crosstrantype |
| 26 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 27 | fapplyname | 申请人姓名 | varchar | 70 |  | √ | ' ' | 申请人姓名 |
| 28 | fhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 29 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 30 | fispersonpay | 对私支付 | bpchar | 1 |  | √ | '0' | 对私支付 |
| 31 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 32 | fdpexchangerate | 异币别付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 异币别付款汇率 |
| 33 | flossamt | 汇兑损益 | numeric | 19 | 6 | √ | 0.000000 | 汇兑损益 |
| 34 | fismatchtransdetail | 是否匹配流水 | varchar | 16 |  | √ | '0' | 是否匹配流水 |
| 35 | fdpamt | 异币别付款金额 | numeric | 19 | 6 | √ | 0.000000 | 异币别付款金额 |
| 36 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 37 | fisrepay | 是否失败重付 | bpchar | 1 |  | √ | '0' | 是否失败重付 |
| 38 | ffeecurrency | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fsettlementmethod | 清算方式 | varchar | 50 |  | √ | ' ' | 清算方式 |
| 40 | fserlevel | 服务级别 | varchar | 30 |  | √ | ' ' | 服务级别,枚举: URGP :紧急支付 SDVA :当日支付 PRPT :优先支付 NURG :其他 : |
| 41 | fdplocalamt | 异币别付款金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 异币别付款金额折本位币 |
| 42 | fagreedquotation | 兑换汇率换算方式 | varchar | 30 |  | √ | '0' | 兑换汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fbookdate_hw | fbookdate_hw | timestamp | 0 |  |  | null |  |
| 44 | fcontractno | 兑换合约号 | varchar | 20 |  | √ | ' ' | 兑换合约号 |
| 45 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 46 | fnetbankacctid | 网银子账户 | int8 | 64 |  | √ | 0 | 网银子账户 bd_netbankacct |
| 47 | fiscrosspay | 跨境支付 | bpchar | 1 |  | √ | '0' | 跨境支付 |
| 48 | ffeepayer | 手续费承担方 | varchar | 30 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方承担 02 :收款方承担 03 :共同承担 |
| 49 | fpayquotation | 付款汇率换算方式 | varchar | 30 |  | √ | '0' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 50 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 51 | fconfirmpaydate | 确认付款时间 | timestamp | 0 |  |  | null | 确认付款时间 |
| 52 | fapplyphone | 申请人电话 | varchar | 50 |  | √ | ' ' | 申请人电话 |
| 53 | fismatchbyhead | 是否按单头匹配 | bpchar | 1 |  | √ | '0' | 是否按单头匹配 |

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
| 2 | fsettlettype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | faccountcashid | 付款账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 5 | fbankcheckflag | 对账标识码(旧) | varchar | 255 |  | √ | ' ' | 对账标识码(旧) |
| 6 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 9 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fpaytime | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 11 | factcount | 实发笔数 | int8 | 64 |  | √ | 0 | 实发笔数 |
| 12 | fbankagentstatus | 银行代发单状态 | varchar | 30 |  | √ | ' ' | 银行代发单状态,枚举: OS :银企处理中 OZ :银企处理中止 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OP :准备提交 OF :银企异常 PS :部分成功 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fbatchseqid | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 15 | factpayamount | 实发金额 | numeric | 19 | 6 | √ | 0.000000 | 实发金额 |
| 16 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbookerid | 会计 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fdelegorgid | 委托付款受托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: repay :代发单 er_dailyloanbill :日常借款单 er_tripreqbill :出差申请单 er_dailyreimbursebill :费用报销单 cas_betransdetail :交易明细 ap_finapbill :财务应付单 cas_recbill :收款单 er_vehiclecheckingbill :用车结算单 er_planecheckingbill :机票结算单 er_hotelcheckingbill :酒店结算单 er_tripreimbursebill :差旅报销单 er_checkingpaybill :月结付款单 CmpAgentPayBill :SHR代发单 fr_glreim_paybill :总账付款单 sHRAgentPayBill :s-HR代发单 |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 F :银行退票 G :已退单 H :已作废 I :退款 |
| 21 | fpayeetype | 收款单位类型(多类别基础类型) | varchar | 50 |  | √ | ' ' | 收款单位类型(多类别基础类型),枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 other :其他 |
| 22 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 25 | fbitbackreason | 打回意见 | varchar | 50 |  | √ | ' ' | 打回意见 |
| 26 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fisbitback | 是否银企打回 | bpchar | 1 |  | √ | '0' | 是否银企打回 |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 31 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 32 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 33 | fsource | 单据来源 | varchar | 30 |  | √ | ' ' | 单据来源,枚举: new :手工新增 impot :导入 BOTP :BOTP |
| 34 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 37 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 38 | fcount | 总笔数 | int8 | 64 |  | √ | 0 | 总笔数 |
| 39 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 40 | fpayeracctbankid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 43 | flocalamount | 付款金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 付款金额本位币 |
| 44 | fapplyorgid | 委托付款委托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 47 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 48 | fsettletnumber | 结算号 | varchar | 50 |  | √ | ' ' | 结算号 |
| 49 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 50 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 51 | fcurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 4 | fmatchresult | 是否已匹配 | bpchar | 1 |  | √ | '0' | 是否已匹配 |
| 5 | frecaddress | 收款方地址 | varchar | 400 |  | √ | ' ' | 收款方地址 |
| 6 | fedpamt | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 7 | fedplocalamt | 付款折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 付款折本位币金额 |
| 8 | frefundtype | 退类型 | varchar | 30 |  | √ | ' ' | 退类型,枚举: refund :退款 renote :退票 |
| 9 | frefundbillid | 退款单ID | int8 | 64 |  | √ | 0 | 退款单ID |
| 10 | fefee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 11 | fepaytime | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
