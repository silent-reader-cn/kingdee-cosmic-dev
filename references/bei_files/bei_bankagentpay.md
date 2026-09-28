# 银行代发单-bei_bankagentpay

## 银行代发单-主表 t_bei_bankagentpaybill

- **表名称：** 银行代发单-主表
- **表名：** t_bei_bankagentpaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fproxybankadds | 代理行地址 | varchar | 255 |  | √ | ' ' | 代理行地址 |
| 4 | fissalary | 是否代发 | bpchar | 1 |  | √ | '0' | 是否代发 |
| 5 | fservicelevel | 付款服务类别 | varchar | 60 |  | √ | ' ' | 付款服务类别 |
| 6 | fproxyswiftcode | 代理行SWIFT码 | varchar | 60 |  | √ | ' ' | 代理行SWIFT码 |
| 7 | fmobile | 收款人电话 | varchar | 50 |  | √ | ' ' | 收款人电话 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fisupdatingstatus | 是否正在修改付款状态 | bpchar | 1 |  | √ | '0' | 是否正在修改付款状态 |
| 11 | fissingleca | fissingleca | bpchar | 1 |  | √ | ' ' |  |
| 12 | fpayerfeeaccno | 手续费账号 | varchar | 60 |  | √ | ' ' | 手续费账号 |
| 13 | factamount | 确认金额 | numeric | 19 | 6 | √ | 0.000000 | 确认金额 |
| 14 | factcount | 确认笔数 | int8 | 64 |  | √ | 0 | 确认笔数 |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 F :已失败重付 T :已打回 E :银企处理中 |
| 17 | fsubmittime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 18 | fagentpaybillno | 代发单号 | varchar | 100 |  | √ | ' ' | 代发单号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 21 | fproxybankcountry | 代理行国家或地区 | varchar | 60 |  | √ | ' ' | 代理行国家或地区 |
| 22 | fproxyaccname | 代理账号名 | varchar | 60 |  | √ | ' ' | 代理账号名 |
| 23 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 24 | fusecn | 交易类型 | varchar | 30 |  | √ | ' ' | 交易类型 |
| 25 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | faccountbankid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 28 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | flocamt | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 30 | fisbitback | 打回标识 | bpchar | 1 |  | √ | '0' | 打回标识 |
| 31 | flastsourcebillid | 失败重付源单 | int8 | 64 |  | √ | 0 | 失败重付源单 |
| 32 | fistranspay | 是否跨境支付 | bpchar | 1 |  | √ | '0' | 是否跨境支付 |
| 33 | fapplyname | 申请人 | varchar | 80 |  | √ | ' ' | 申请人 |
| 34 | fpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OP :准备提交 PS :部分成功 OS :银企处理中 OF :银企异常 OZ :银企处理中止 |
| 35 | fexcontract | 兑换合约号 | varchar | 60 |  | √ | ' ' | 兑换合约号 |
| 36 | famount | 总金额 | numeric | 19 | 6 | √ | 0.000000 | 总金额 |
| 37 | fpayerfeecurrencyid | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fispersonpay | 对私付款 | bpchar | 1 |  | √ | '0' | 对私付款 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 41 | fpayerfeetype | 手续费方式 | varchar | 60 |  | √ | ' ' | 手续费方式,枚举: 01 :付款方承担 02 :收款方承担 03 :共同承担 |
| 42 | fcount | 总笔数 | int8 | 64 |  | √ | 0 | 总笔数 |
| 43 | fsettlementmethod | 清算方式 | varchar | 50 |  | √ | ' ' | 清算方式 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | ftempstatus | 中间状态 | varchar | 30 |  | √ | ' ' | 中间状态,枚举: 0 :正常 1 :待签名 2 :待提交银企 |
| 46 | fproxybankarea | 代理行地区 | varchar | 60 |  | √ | ' ' | 代理行地区 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fserialnumber | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 49 | fpayunique | 付款防重字段 | int8 | 64 |  | √ | 0 | 付款防重字段 |
| 50 | ftolexchangerate | 协定汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 协定汇率 |
| 51 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 52 | fproxyaccno | 代理账号 | varchar | 60 |  | √ | ' ' | 代理账号 |
| 53 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 54 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 55 | fproxybankname | 代理行名 | varchar | 255 |  | √ | ' ' | 代理行名 |
| 56 | fapplyphone | 申请人电话 | varchar | 50 |  | √ | ' ' | 申请人电话 |
| 57 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_bankagentunique |  | fsourcebillid,fpayunique |
| 2 | idx_bei_bankagentpaybill |  | fbillno,fbillstatus |
| 3 | t_bei_bankagentpaybill_pkey |  | fid |

---

## 银行代发单-多语言表 t_bei_bankagentpaybill_l

- **表名称：** 银行代发单-多语言表
- **表名：** t_bei_bankagentpaybill_l

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
| 1 | idx_bei_bankagentpaybill_l |  | fid,flocaleid,fdescription |
| 2 | t_bei_bankagentpaybill_l_pkey |  | fpkid |

---

## 分录-子表 t_bei_bankagentpay_entry

- **表名称：** 分录-子表
- **表名：** t_bei_bankagentpay_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisagencypersonpay | 是否并笔入账 | bpchar | 1 |  | √ | '0' | 是否并笔入账 |
| 3 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 4 | fsourceentryid | 源分录ID | int8 | 64 |  | √ | 0 | 源分录ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ftransremarks | 交易种类 | varchar | 60 |  | √ | ' ' | 交易种类 |
| 7 | frecname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 8 | fpaymentfps | 收款人FPS账号 | varchar | 30 |  | √ | ' ' | 收款人FPS账号 |
| 9 | fisupdatestate | 是否手动修改付款状态 | bpchar | 1 |  | √ | '0' | 是否手动修改付款状态 |
| 10 | fdeliverymethod | 支票寄送方式 | varchar | 60 |  | √ | ' ' | 支票寄送方式 |
| 11 | facctbanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 12 | finforpayment | 通知收款人 | bpchar | 1 |  | √ | '0' | 通知收款人 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: OP :准备提交 TS :交易成功 TF :交易失败 NC :交易未确认 OS :银企处理中 BP :银行处理中 OF :银企异常 OZ :银企处理中止 |
| 14 | frecamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 15 | fchequeusage | 支票用途 | varchar | 60 |  | √ | ' ' | 支票用途 |
| 16 | fcity | 收款市 | varchar | 50 |  | √ | ' ' | 收款市 |
| 17 | fentrymobile | 收款人电话 | varchar | 50 |  | √ | ' ' | 收款人电话 |
| 18 | fisrefund | 是否退票 | bpchar | 1 |  | √ | '0' | 是否退票 |
| 19 | finformrecemail | 通知收款人邮箱 | varchar | 255 |  | √ | ' ' | 通知收款人邮箱 |
| 20 | frecbank | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 21 | fremark | 转账附言 | varchar | 200 |  | √ | ' ' | 转账附言 |
| 22 | fpaymentareacode | 收款人地区码 | varchar | 3 |  | √ | ' ' | 收款人地区码 |
| 23 | frecemail | 收款方邮箱 | varchar | 500 |  | √ | ' ' | 收款方邮箱 |
| 24 | fincomeradds | 收款人地址 | varchar | 300 |  | √ | ' ' | 收款人地址 |
| 25 | frecbanknumber | 收款行行号 | varchar | 80 |  | √ | ' ' | 收款行行号 |
| 26 | fincomebankcode | 收款行代码 | varchar | 60 |  | √ | ' ' | 收款行代码 |
| 27 | fchequetype | 支票类别 | varchar | 60 |  | √ | ' ' | 支票类别 |
| 28 | fpaymentmethod | 付款种类 | varchar | 60 |  | √ | ' ' | 付款种类 |
| 29 | fincomeswiftcode | 收款方SWIFT码 | varchar | 60 |  | √ | ' ' | 收款方SWIFT码 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fprovince | 收款省 | varchar | 50 |  | √ | ' ' | 收款省 |
| 32 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 33 | frecamount_enp | frecamount_enp | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_bankagentpay_entry_pkey |  | fentryid |
| 2 | idx_bei_bankagentpayentry |  | fid,fsourceentryid |
