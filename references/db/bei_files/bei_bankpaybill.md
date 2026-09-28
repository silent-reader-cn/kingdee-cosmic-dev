# 银行付款单-bei_bankpaybill

## 关联子实体-子表 t_bei_bankpayingbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bei_bankpayingbill_lk

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
| 1 | t_bei_bankpayingbill_lk_pkey |  | fpkid |
| 2 | idx_bei_bankpayingbill_lk_fk |  | fid |

---

## 银行付款单-关联追踪表 t_bei_bankpayingbill_tc

- **表名称：** 银行付款单-关联追踪表
- **表名：** t_bei_bankpayingbill_tc

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
| 1 | t_bei_bankpayingbill_tc_pkey |  | fid |
| 2 | idx_bei_bankpayingbill_tc_tbill |  | ftbillid |
| 3 | idx_bei_bankpayingbill_tc_tid |  | ftid |

---

## 银行付款单-分表 t_bei_bankpayingbill_e

- **表名称：** 银行付款单-分表
- **表名：** t_bei_bankpayingbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fincomeareacode | fincomeareacode | varchar | 80 |  | √ | ' ' |  |
| 3 | fcontract | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 4 | freportbiztype | 申报业务类型 | varchar | 50 |  | √ | ' ' | 申报业务类型,枚举: X :保税区 E :出口加工区 D :钻石交易所 S :离岸账户 M :深加工结转 O :其他 A :其他特殊经济区 |
| 5 | fproxybankadds | 代理行地址 | varchar | 100 |  | √ | ' ' | 代理行地址 |
| 6 | fdeliverymethod | 支票寄送方式 | varchar | 60 |  | √ | ' ' | 支票寄送方式 |
| 7 | fmobile | 收款人电话 | varchar | 30 |  | √ | ' ' | 收款人电话 |
| 8 | fservicelevel | 付款服务类别 | varchar | 60 |  | √ | ' ' | 付款服务类别 |
| 9 | fproxyswiftcode | 代理行SWIFT码 | varchar | 60 |  | √ | ' ' | 代理行SWIFT码 |
| 10 | fissingleca | fissingleca | bpchar | 1 |  | √ | '0' |  |
| 11 | fpayerfeeaccno | 手续费账号 | varchar | 60 |  | √ | ' ' | 手续费账号 |
| 12 | fthirdpaystatus | 支付平台支付状态 | varchar | 255 |  | √ | ' ' | 支付平台支付状态 |
| 13 | finvoicenumber | 发票号 | varchar | 95 |  | √ | ' ' | 发票号 |
| 14 | finformrecemail | 通知收款人邮箱 | varchar | 255 |  | √ | ' ' | 通知收款人邮箱 |
| 15 | fincomeradds | 收款人地址 | varchar | 255 |  | √ | ' ' | 收款人地址 |
| 16 | fisbonded | 是否为保税货物项下付款 | bpchar | 1 |  | √ | '0' | 是否为保税货物项下付款 |
| 17 | femail | femail | varchar | 30 |  | √ | ' ' |  |
| 18 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 19 | fproxybankcountry | 代理行国家或地区 | varchar | 60 |  | √ | ' ' | 代理行国家或地区 |
| 20 | fexplanation | fexplanation | varchar | 255 |  | √ | ' ' |  |
| 21 | fincomebankcode | 收款行代码 | varchar | 60 |  | √ | ' ' | 收款行代码 |
| 22 | fproxyaccname | 代理账号名 | varchar | 60 |  | √ | ' ' | 代理账号名 |
| 23 | fusecn | 交易类型 | varchar | 30 |  | √ | ' ' | 交易类型 |
| 24 | fincomeswiftcode | 收款方SWIFT码 | varchar | 80 |  | √ | ' ' | 收款方SWIFT码 |
| 25 | fpaymentanture | 付款性质 | varchar | 50 |  | √ | ' ' | 付款性质,枚举: 0 :预付货款 1 :货到付款 2 :退款 3 :其他 |
| 26 | fistranspay | 跨境支付 | bpchar | 1 |  | √ | '0' | 跨境支付 |
| 27 | fpaycurrencyid | fpaycurrencyid | int8 | 64 |  | √ | 0 |  |
| 28 | fincomecalparam | fincomecalparam | varchar | 60 |  | √ | ' ' |  |
| 29 | ftransactioncode | 交易编码 | varchar | 6 |  | √ | ' ' | 交易编码 |
| 30 | fincomeadds | fincomeadds | varchar | 100 |  | √ | ' ' |  |
| 31 | fexcontract | 兑换合约号 | varchar | 100 |  | √ | ' ' | 兑换合约号 |
| 32 | ftransremarks | 交易种类 | varchar | 60 |  | √ | ' ' | 交易种类 |
| 33 | fpaymentfps | 收款人FPS账号 | varchar | 30 |  | √ | ' ' | 收款人FPS账号 |
| 34 | fpayerfeecurrencyid | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | finforpayment | 通知收款人 | bpchar | 1 |  | √ | '0' | 通知收款人 |
| 36 | fchequeusage | 支票用途 | varchar | 60 |  | √ | ' ' | 支票用途 |
| 37 | fpayerfeetype | 手续费方式 | varchar | 60 |  | √ | ' ' | 手续费方式,枚举: 01 :付款方承担 02 :收款方承担 03 :共同承担 |
| 38 | fincomerproxybank | fincomerproxybank | varchar | 60 |  | √ | ' ' |  |
| 39 | fsettlementmethod | 清算方式 | varchar | 50 |  | √ | ' ' | 清算方式 |
| 40 | funiformsocialcreditcode | 付款单位统一社会信用代码 | varchar | 100 |  | √ | ' ' | 付款单位统一社会信用代码 |
| 41 | fpaymentareacode | 收款人地区码 | varchar | 3 |  | √ | ' ' | 收款人地区码 |
| 42 | ftempstatus | 中间状态 | varchar | 30 |  | √ | ' ' | 中间状态,枚举: 0 :正常 1 :待签名 2 :待提交银企 |
| 43 | fproxybankarea | 代理行地区 | varchar | 100 |  | √ | ' ' | 代理行地区 |
| 44 | frecemail | 收款方邮箱 | varchar | 500 |  | √ | ' ' | 收款方邮箱 |
| 45 | fincomebanksubcode | fincomebanksubcode | varchar | 60 |  | √ | ' ' |  |
| 46 | ftolexchangerate | 协定汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 协定汇率 |
| 47 | fproxyaccno | 代理账号 | varchar | 60 |  | √ | ' ' | 代理账号 |
| 48 | fchequetype | 支票类别 | varchar | 60 |  | √ | ' ' | 支票类别 |
| 49 | fproxybankname | 代理行名 | varchar | 60 |  | √ | ' ' | 代理行名 |
| 50 | fpaymentmethod | 付款种类 | varchar | 60 |  | √ | ' ' | 付款种类 |
| 51 | factualamount | factualamount | numeric | 19 | 6 | √ | 0.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_bankpayingbill_e_pkey |  | fid |
| 2 | idx_t_bei_bankpayingbill_e |  | fissingleca |

---

## 银行付款单-多语言表 t_bei_bankpayingbill_l

- **表名称：** 银行付款单-多语言表
- **表名：** t_bei_bankpayingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_bankpayingbill_l_pkey |  | fpkid |
| 2 | idx_bei_bankpayingbill_l |  | fid,flocaleid,fdescription |

---

## 银行付款单-主表 t_bei_bankpayingbill

- **表名称：** 银行付款单-主表
- **表名：** t_bei_bankpayingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freturntime | 银行返回时间 | timestamp | 0 |  |  | null | 银行返回时间 |
| 3 | fsubmituserid | 提交银企人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fisupdatestate | 是否手动修改付款状态 | bpchar | 1 |  | √ | '0' | 是否手动修改付款状态 |
| 6 | fagentpayeraccount | 母账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fisupdatingstatus | 是否正在修改付款状态 | bpchar | 1 |  | √ | '0' | 是否正在修改付款状态 |
| 10 | freccountryid | 收款方国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 11 | fpaytime | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fbatchseqid | 提交银企批次流水 | varchar | 80 |  | √ | ' ' | 提交银企批次流水 |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 T :已打回 E :银企处理中 F :已失败重付 |
| 15 | fpayeebankname | fpayeebankname | varchar | 80 |  | √ | ' ' |  |
| 16 | fsubmittime | 提交银行时间 | timestamp | 0 |  |  | null | 提交银行时间 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 19 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 20 | fisprivatepay | 对私付款 | bpchar | 1 |  | √ | '0' | 对私付款 |
| 21 | fpayeebank | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 22 | fsigntext | 签名 | varchar | 1000 |  |  | null | 签名 |
| 23 | fpayapplyorgnm | fpayapplyorgnm | varchar | 100 |  | √ | ' ' |  |
| 24 | fsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_paybill :付款单 ifm_transhandlebill :付款结算单 ifm_linkpaybill :联动支付单 cas_paybill_cossentity :跨主体转账 |
| 25 | fbankid | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | faccountbankid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 28 | fbitbackerid | 打回处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fisbitback | 打回 | bpchar | 1 |  | √ | '0' | 打回 |
| 31 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fbankpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 OS :银企处理中 OZ :银企处理中止 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 33 | flastsourcebillid | 失败重付源单 | int8 | 64 |  | √ | 0 | 失败重付源单 |
| 34 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 35 | fapplyname | 申请人 | varchar | 80 |  | √ | ' ' | 申请人 |
| 36 | famount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 37 | fstatementrefno | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 38 | fpayeraddress | 付款人地址 | varchar | 255 |  | √ | ' ' | 付款人地址 |
| 39 | fusage | 附言 | varchar | 255 |  |  | null | 附言 |
| 40 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fislinkpay | 联动支付 | bpchar | 1 |  | √ | '0' | 联动支付 |
| 42 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 43 | fpayeeacct | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 44 | fpayerid | 付款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fisrefund | 是否退票 | bpchar | 1 |  | √ | '0' | 是否退票 |
| 46 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 47 | frecbankadds | 收款行地址 | varchar | 255 |  | √ | ' ' | 收款行地址 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fpayeebanknum | fpayeebanknum | varchar | 80 |  | √ | ' ' |  |
| 50 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fpaybillauditor | fpaybillauditor | int8 | 64 |  | √ | 0 |  |
| 53 | fpaybillcreator | fpaybillcreator | int8 | 64 |  | √ | 0 |  |
| 54 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 55 | fserialnumber | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 56 | fpayunique | 付款防重字段 | int8 | 64 |  | √ | 0 | 付款防重字段 |
| 57 | fnetbankacctid | 网银子账户 | int8 | 64 |  | √ | 0 | [网银子账户 bd_netbankacct](../basedata_files/bd_netbankacct.md) |
| 58 | frecbanknumber | 收款行号 | varchar | 30 |  | √ | ' ' | 收款行号 |
| 59 | fbitbacktime | 打回日期 | timestamp | 0 |  |  | null | 打回日期 |
| 60 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 61 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 62 | fpayeraccount | 子账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 63 | fapplyphone | 申请人电话 | varchar | 50 |  | √ | ' ' | 申请人电话 |
| 64 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 65 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  |  | null | 银行返回信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_bankpayingbill |  | fbillno,fbillstatus |
| 2 | t_bei_bankpayingbill_pkey |  | fid |
| 3 | idx_bei_bankpayunique |  | fsourcebillid,fpayunique |

---

## 银行付款单-反写记录表 t_bei_bankpayingbill_wb

- **表名称：** 银行付款单-反写记录表
- **表名：** t_bei_bankpayingbill_wb

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
| 1 | t_bei_bankpayingbill_wb_pkey |  | fentryid |
| 2 | idx_bei_bankpayingbill_wb_fk |  | fid |
