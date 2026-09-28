# 应付电票查询-cdm_electronic_pay_query

## 单据体-子表 t_cdm_electronicbillleent

- **表名称：** 单据体-子表
- **表名：** t_cdm_electronicbillleent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpre4paydate | 提示付款申请日期 | varchar | 50 |  | √ | ' ' | 提示付款申请日期 |
| 3 | freplycode | 回复标记 | varchar | 50 |  | √ | ' ' | 回复标记 |
| 4 | fopponentlorg | 对手信用机构 | varchar | 50 |  | √ | ' ' | 对手信用机构 |
| 5 | ftransferflag | 不得转让标记 | varchar | 50 |  | √ | ' ' | 不得转让标记 |
| 6 | fdiscountrate | 贴现利率 | varchar | 50 |  | √ | ' ' | 贴现利率 |
| 7 | fendorsee | 被背书人名称 | varchar | 50 |  | √ | ' ' | 被背书人名称 |
| 8 | ftradeamount | 交易金额 | varchar | 50 |  | √ | ' ' | 交易金额 |
| 9 | fdiscountamount | 贴现金额 | varchar | 50 |  | √ | ' ' | 贴现金额 |
| 10 | fdefaultfpcode | 拒付代码 | varchar | 50 |  | √ | ' ' | 拒付代码 |
| 11 | fsigndate | 签收日期 | varchar | 50 |  | √ | ' ' | 签收日期 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | finitiatorname | 发起方名称 | varchar | 50 |  | √ | ' ' | 发起方名称 |
| 14 | fdealno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |
| 15 | ftracktype | 追索类型 | varchar | 50 |  | √ | ' ' | 追索类型 |
| 16 | faccountno | 入账账号 | varchar | 50 |  | √ | ' ' | 入账账号 |
| 17 | fdisredrate | 贴现赎回利率 | varchar | 50 |  | √ | ' ' | 贴现赎回利率 |
| 18 | fpaymentorder | 到期无条件支付委托 | varchar | 50 |  | √ | ' ' | 到期无条件支付委托 |
| 19 | fopponentduedate | 对手方评级到期日期 | varchar | 50 |  | √ | ' ' | 对手方评级到期日期 |
| 20 | ftrackdate | 追索到期日期 | varchar | 50 |  | √ | ' ' | 追索到期日期 |
| 21 | fnoteno | 票据号码 | varchar | 50 |  | √ | ' ' | 票据号码 |
| 22 | fopponentcl | 对手信用等级 | varchar | 50 |  | √ | ' ' | 对手信用等级 |
| 23 | folclearingflag | 线上清算标记 | varchar | 50 |  | √ | ' ' | 线上清算标记 |
| 24 | fdisredamount | 贴现赎回金额 | varchar | 50 |  | √ | ' ' | 贴现赎回金额 |
| 25 | fcleardate | 清偿日期 | varchar | 50 |  | √ | ' ' | 清偿日期 |
| 26 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 27 | fredemptionedate | 赎回截止日 | varchar | 50 |  | √ | ' ' | 赎回截止日 |
| 28 | fdetailseq | 明细号 | varchar | 50 |  | √ | ' ' | 明细号 |
| 29 | fremark | 备注信息 | varchar | 50 |  | √ | ' ' | 备注信息 |
| 30 | fdiscounttype | 贴现种类 | varchar | 50 |  | √ | ' ' | 贴现种类 |
| 31 | fopponentbankcnaps | 对手方账号 | varchar | 50 |  | √ | ' ' | 对手方账号 |
| 32 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 33 | fendorsedate | 背书日期 | timestamp | 0 |  |  | null | 背书日期 |
| 34 | finitiatororg | 发起方组织机构编码 | varchar | 50 |  | √ | ' ' | 发起方组织机构编码 |
| 35 | finitiatorbankcnaps | 发起方行号 | varchar | 50 |  | √ | ' ' | 发起方行号 |
| 36 | facountbankcnaps | 入账行号 | varchar | 50 |  | √ | ' ' | 入账行号 |
| 37 | fcontractno | 协议编码 | varchar | 50 |  | √ | ' ' | 协议编码 |
| 38 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 39 | fopponentorg | 对手组织机构 | varchar | 50 |  | √ | ' ' | 对手组织机构 |
| 40 | fbusinesscode | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码,枚举: 02 :提示承兑 03 :提示收票 10 :背书转让 18 :质押背书 |
| 41 | fpaymentaccept | 到期无条件支付承兑 | varchar | 50 |  | √ | ' ' | 到期无条件支付承兑 |
| 42 | fsubtype | 子业务类型 | varchar | 50 |  | √ | ' ' | 子业务类型 |
| 43 | fredemptionsdate | 贴现开发日 | varchar | 50 |  | √ | ' ' | 贴现开发日 |
| 44 | fendorser | 背书人名称 | varchar | 50 |  | √ | ' ' | 背书人名称 |
| 45 | finitiatoracno | 发起方账号 | varchar | 50 |  | √ | ' ' | 发起方账号 |
| 46 | fopponentname | 对手方名称 | varchar | 50 |  | √ | ' ' | 对手方名称 |
| 47 | fclearamount | 清偿金额 | varchar | 50 |  | √ | ' ' | 清偿金额 |
| 48 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_receivablehandleent |  | fid |
| 2 | pk_t_cdm_electronicbillleent |  | fentryid |

---

## 应付电票查询-多语言表 t_cdm_electronicbill_l

- **表名称：** 应付电票查询-多语言表
- **表名：** t_cdm_electronicbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_receivablehandle_l |  | fid |
| 2 | pk_t_cdm_electronicbill_l |  | fpkid |

---

## 应付电票查询-分表 t_cdm_electronicbill_g

- **表名称：** 应付电票查询-分表
- **表名：** t_cdm_electronicbill_g

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbaleac | 保证金账号 | varchar | 50 |  | √ | ' ' | 保证金账号 |
| 3 | finitamount | 原始子票包金额 | numeric | 23 | 10 | √ | 0 | 原始子票包金额 |
| 4 | facpfer | 承兑手续费率% | numeric | 23 | 10 | √ | 0 | 承兑手续费率% |
| 5 | fserieschecktimes | 连续性检查补偿次数 | int8 | 64 |  | √ | 0 | 连续性检查补偿次数 |
| 6 | fsuretyonlineacctname | 保证金账户名称 | varchar | 150 |  | √ | ' ' | 保证金账户名称 |
| 7 | fbaltyp | 保证金类型 | varchar | 50 |  | √ | ' ' | 保证金类型,枚举: 01 :单位活期保证金（招商银行） 11 :单位定期保证金（招商银行） 1 :单位活期保证金（兴业银行） 2 :单位定期保证金（兴业银行） |
| 8 | fautoexecuteop | fautoexecuteop | varchar | 30 |  | √ | ' ' |  |
| 9 | fisnotesideserror | 背面信息查询是否发生异常 | bpchar | 1 |  | √ | '0' | 背面信息查询是否发生异常 |
| 10 | fsuretyonlineterm | 保证金期限 | varchar | 50 |  | √ | ' ' | 保证金期限 |
| 11 | fsuretyonlineacct | 保证金账号 | varchar | 50 |  | √ | ' ' | 保证金账号 |
| 12 | facpflg | 承兑类型 | varchar | 50 |  | √ | ' ' | 承兑类型,枚举: 0 :全额保证金在线承兑 1 :授信项下在线承兑 2 :普通承兑 |
| 13 | fsuretyonline | 在线开立保证金 | bpchar | 1 |  | √ | '0' | 在线开立保证金 |
| 14 | finvcno | 发票号码 | varchar | 30 |  | √ | ' ' | 发票号码 |
| 15 | fcollectionorgno | 收票人机构号 | varchar | 50 |  | √ | ' ' | 收票人机构号 |
| 16 | ftrantype | 查询业务种类 | varchar | 50 |  | √ | ' ' | 查询业务种类,枚举: 02 :出票人提示承兑 03 :出票人提示收票 10 :背书转让 18 :质押 19 :质押解除 20 :提示付款 21 :逾期提示付款 |
| 17 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 18 | fisautosignin | 内部组织票据自动签收 | bpchar | 1 |  | √ | '0' | 内部组织票据自动签收 |
| 19 | finvcamt | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 20 | fsuretybankamt | 银行实际保证金金额 | numeric | 23 | 10 | √ | 0 | 银行实际保证金金额 |
| 21 | fclaimstatus | fclaimstatus | varchar | 30 |  | √ | ' ' |  |
| 22 | fsuretybizno | 保证金业务流水号 | varchar | 50 |  | √ | ' ' | 保证金业务流水号 |
| 23 | funiquecode | 票据识别码 | varchar | 100 |  | √ | ' ' | 票据识别码 |
| 24 | fseriescheckdate | 连续性检查更新时间 | timestamp | 0 |  |  | null | 连续性检查更新时间 |
| 25 | finvctype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 004 :专票 007 :普票 026 :电子发票 025 :卷票 005 :机动车 14 :通行费 |
| 26 | finterfacetype | 数据接口类型 | bpchar | 1 |  | √ | '0' | 数据接口类型,枚举: 0 :新一代票据接口 1 :传统票据接口 |
| 27 | fbackinfoseries | 背面信息连续 | bpchar | 1 |  | √ | '0' | 背面信息连续 |
| 28 | fsuretymoney | 保证金 | numeric | 23 | 10 | √ | 0 | 保证金 |
| 29 | finvcchkno | 校验码 | varchar | 30 |  | √ | ' ' | 校验码 |
| 30 | ftradetypetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 31 | fsuretyonlineinterest | 保证金利率（%） | numeric | 23 | 10 | √ | 0 | 保证金利率（%） |
| 32 | finvcdate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 33 | fpretradetype | 前次操作类型 | varchar | 50 |  | √ | ' ' | 前次操作类型,枚举: noteendorse :背书 remitaccept :提示承兑 remitreceive :提示收票 notediscount :贴现 notesignin :签收 ticketguarantee :出票保证 remitregister :开票登记 remitrevocation :撤销出票 notesigninreject :拒收 notecancle :撤销 remitcancle :取消出票 pledgenote :质押 removepledge :质押解除 presentpayment :票据托收 remitconfirm :合同确认 |
| 34 | fsuretyonlinetermunit | 保证金期限单位 | varchar | 30 |  | √ | ' ' | 保证金期限单位,枚举: year :年 month :月 day :日 |
| 35 | finvccode | 发票代码 | varchar | 30 |  | √ | ' ' | 发票代码 |
| 36 | fsuretyprotocolno | 保证金协议编号 | varchar | 50 |  | √ | ' ' | 保证金协议编号 |
| 37 | finitsubrange | 原始子票包区间 | varchar | 255 |  | √ | ' ' | 原始子票包区间 |
| 38 | fsuretypayacct | 保证金付款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cdm_electronicbill_g |  | fid |

---

## 应付电票查询-分表 t_cdm_electronicbill_f

- **表名称：** 应付电票查询-分表
- **表名：** t_cdm_electronicbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgrdbag | 票据分包流转允许标志 | bpchar | 1 |  | √ | '0' | 票据分包流转允许标志 |
| 3 | fdiscountdays | 贴现调整天数 | int4 | 32 |  | √ | 0 | 贴现调整天数 |
| 4 | fbankrefdate | 银行业务日期 | varchar | 50 |  | √ | ' ' | 银行业务日期 |
| 5 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | fconnchannelid | 直连渠道 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 7 | fpromiseraccid | 入账账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | ftraderemarks | 业务处理备注 | varchar | 255 |  | √ | ' ' | 业务处理备注 |
| 9 | fbackflag | 是否打回 | bpchar | 1 |  | √ | '0' | 是否打回,枚举: 0 :未打回 1 :已打回 |
| 10 | fnoticetime | fnoticetime | timestamp | 0 |  |  | null |  |
| 11 | foppbankaddr | 对手方开户行地址 | varchar | 50 |  | √ | ' ' | 对手方开户行地址 |
| 12 | ffilename | 电子合同文件名 | varchar | 512 |  | √ | ' ' | 电子合同文件名 |
| 13 | fopstatus | 操作状态(弃用空闲字段) | varchar | 50 |  | √ | ' ' | 操作状态(弃用空闲字段),枚举: 0 :初始化 1 :操作中 2 :待同步 3 :同步中 4 :同步成功 5 :同步失败 |
| 14 | fothercode | 其他代码 | varchar | 50 |  | √ | ' ' | 其他代码 |
| 15 | facceptpromiseraccount | 承兑保证人账号 | varchar | 50 |  | √ | ' ' | 承兑保证人账号 |
| 16 | fsettleway | 结算方式 | varchar | 255 |  | √ | ' ' | 结算方式,枚举: ST01 :票款兑付 ST02 :纯票过户 |
| 17 | fsignopinion | fsignopinion | varchar | 50 |  | √ | ' ' |  |
| 18 | fcurrencynumber | 币种编码 | varchar | 50 |  | √ | ' ' | 币种编码 |
| 19 | fsignnoticebill | fsignnoticebill | varchar | 255 |  | √ | ' ' |  |
| 20 | ffileencrypt | 电子合同文件MD5值 | varchar | 512 |  | √ | ' ' | 电子合同文件MD5值 |
| 21 | fissuepromiseraccount | 出票保证人账号 | varchar | 50 |  | √ | ' ' | 出票保证人账号 |
| 22 | fsubrange | 子票区间 | varchar | 255 |  | √ | ' ' | 子票区间 |
| 23 | freturnnotetag | 回头票据 | bpchar | 1 |  | √ | '0' | 回头票据 |
| 24 | fparametertable_tag | fparametertable_tag | text | 0 |  |  | null |  |
| 25 | fparametertable | fparametertable | varchar | 255 |  | √ | ' ' |  |
| 26 | fcustomeropstatus | 客户操作状态 | varchar | 50 |  | √ | ' ' | 客户操作状态 |
| 27 | fquerybatchseq | 获取在手票据批次号 | varchar | 255 |  | √ | ' ' | 获取在手票据批次号 |
| 28 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: bank :银企接口 import :模板导入 |
| 29 | ffileid | 电子合同文件id | varchar | 255 |  | √ | ' ' | 电子合同文件id |
| 30 | fquerydrafttype | 查询票据分类 | varchar | 50 |  | √ | ' ' | 查询票据分类,枚举: reply :待签收票据 hold :在手票据 historyhold :历史在手票据 acceptnote :承兑票据 preRegister :预出票 |
| 31 | fotherinfo | otherinfo | varchar | 50 |  | √ | ' ' | otherinfo |
| 32 | fissuepromiseraddr | 出票保证人地址 | varchar | 50 |  | √ | ' ' | 出票保证人地址 |
| 33 | facceptpromiseraddr | 承兑保证人地址 | varchar | 50 |  | √ | ' ' | 承兑保证人地址 |
| 34 | ftradetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: noteendorse :背书 remitaccept :提示承兑 remitreceive :提示收票 notediscount :贴现 notesignin :签收 ticketguarantee :出票保证 remitregister :开票登记 remitrevocation :撤销出票 notesigninreject :拒收 notecancle :撤销 remitcancle :取消出票 pledgenote :质押 removepledge :质押解除 presentpayment :票据托收 remitconfirm :合同确认 |
| 35 | fisinsertpayorrec | 是否入库应收应付票据 | bpchar | 1 |  | √ | '1' | 是否入库应收应付票据 |
| 36 | fnotestatus | 票据状态 | varchar | 255 |  | √ | ' ' | 票据状态,枚举: CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 preregister :预出票 |
| 37 | fusername | fusername | varchar | 255 |  | √ | ' ' |  |
| 38 | facceptpromisername | 承兑保证人名称 | varchar | 50 |  | √ | ' ' | 承兑保证人名称 |
| 39 | finterest | 贴现利息 | varchar | 255 |  | √ | ' ' | 贴现利息 |
| 40 | fdraftaccountid | 票据账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 41 | fprebatchseqid | 前次操作批次号 | varchar | 50 |  | √ | ' ' | 前次操作批次号 |
| 42 | fbankrefkey | 银行业务参考号 | varchar | 255 |  | √ | ' ' | 银行业务参考号 |
| 43 | fpromiseorgno | 承兑人机构号 | varchar | 50 |  | √ | ' ' | 承兑人机构号 |
| 44 | fconectno | 直连账号 | varchar | 50 |  | √ | ' ' | 直连账号 |
| 45 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: 1 :金融机构 2 :其他 |
| 46 | fissuepromisername | 出票保证人名称 | varchar | 50 |  | √ | ' ' | 出票保证人名称 |
| 47 | fcleartype | 清算类型 | varchar | 255 |  | √ | ' ' | 清算类型,枚举: CT01 :全额清算 CT02 :净额清算 |
| 48 | fcirstatus | 流通标识 | varchar | 255 |  | √ | ' ' | 流通标识,枚举: TF0101 :待收票 TF0301 :可流通 TF0302 :已锁定 TF0303 :不可转让 TF0304 :已质押 TF0305 :待赎回 TF0401 :托收在途 TF0402 :追索中 TF0501 :已结束 |
| 49 | fsourcenumber | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 50 | frptype | 电票收付类型 | varchar | 50 |  | √ | ' ' | 电票收付类型,枚举: paybill :应付电票 receivebill :应收电票 |
| 51 | ftradeoppname | 业务交易对手名称 | varchar | 255 |  | √ | ' ' | 业务交易对手名称 |
| 52 | ffilepath | 电子合同文件存储路径 | varchar | 512 |  | √ | ' ' | 电子合同文件存储路径 |
| 53 | fdiscountpaytype | 贴现付息方式 | varchar | 50 |  | √ | ' ' | 贴现付息方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_electronicbill_f |  | fid |
| 2 | idx_cdm_receivablehandle_f |  | fopstatus |
| 3 | idx_cdm_fquerybatchseq_f |  | fquerybatchseq |

---

## 应付电票查询-分表 t_cdm_electronicbill_e

- **表名称：** 应付电票查询-分表
- **表名：** t_cdm_electronicbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptorcountry | 开户行国家 | varchar | 50 |  | √ | ' ' | 开户行国家 |
| 3 | fdiscountrate | 贴现利率 | numeric | 23 | 10 | √ | 0 | 贴现利率 |
| 4 | fdetailbizno | 业务支付明细号 | varchar | 50 |  | √ | ' ' | 业务支付明细号 |
| 5 | fautoreceive | 自动提示收票 | bpchar | 1 |  | √ | '0' | 自动提示收票 |
| 6 | facceptorprovince | 开户行省份 | varchar | 50 |  | √ | ' ' | 开户行省份 |
| 7 | fholderbankname | 持票人银行 | varchar | 50 |  | √ | ' ' | 持票人银行 |
| 8 | finvoicenumber | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 9 | febstatusmsg | 银企提示信息 | varchar | 2000 |  | √ | ' ' | 银企提示信息 |
| 10 | fdisredrate | 赎回利率 | varchar | 50 |  | √ | ' ' | 赎回利率 |
| 11 | fcontractnumber | 协议号码 | varchar | 50 |  | √ | ' ' | 协议号码 |
| 12 | fdrafttype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: AC01 :银行承兑汇票 AC02 :商业承兑汇票 AC99 :财务公司承兑汇票 |
| 13 | fredemptionedate | 赎回截止日期 | varchar | 50 |  | √ | ' ' | 赎回截止日期 |
| 14 | foppprovince | 对手方省份 | varchar | 50 |  | √ | ' ' | 对手方省份 |
| 15 | foperationname | 操作中文名称 | varchar | 50 |  | √ | ' ' | 操作中文名称 |
| 16 | facceptorcity | 开户行城市 | varchar | 50 |  | √ | ' ' | 开户行城市 |
| 17 | findorsename | 被背书人名称 | varchar | 50 |  | √ | ' ' | 被背书人名称 |
| 18 | fredemptionsdate | 赎回开放日 | varchar | 50 |  | √ | ' ' | 赎回开放日 |
| 19 | fbizcode | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码,枚举: 01 :出票登记 02 :出票人提示承兑 03 :出票人提示收票 04 :撤票 10 :背书转让 11 :贴现 12 :贴现赎回 13 :转贴 14 :转贴赎回 15 :再贴 16 :再贴赎回 17 :保证 18 :质押 19 :质押解除 20 :提示付款 21 :逾期提示付款 22 :追索 23 :清偿 25 :人行卖票 40 :状态变更 41 :通用通知 43 :票据结清通知 50 :清算失败 A1 :待签收 D2 :已驳回 D1 :已签收 3q3eqqwssq :申请经办中 3qeqewq :取消 00 :初始 30 :撤销经办中 B2 :驳回经办中 B1 :签收经办中 E1 :清算失败 2q3eqe :撤票成功 wq2q :出票已登记 qqqq222 :回执失败 wqwqwqwqwwq :已撤销 qwqwqwqwq :申请发送待回执 wqwqwqwqwq :撤销发送待回执 C2 :驳回发送待回执 C1 :签收发送待回执 F1 :对方已撤销 222222222222 :对方已签收 wwwwwwwwwwww :对方已驳回 qqqqqqqqqqqq :对方待签收 |
| 20 | fkeepflag | 是否托管标识 | bpchar | 1 |  | √ | '0' | 是否托管标识 |
| 21 | fcustomerconsultno | 客户参考号 | varchar | 50 |  | √ | ' ' | 客户参考号 |
| 22 | fnotestate | 票据状态 | varchar | 50 |  | √ | ' ' | 票据状态 |
| 23 | fpreholdername | 上一持票人名称 | varchar | 50 |  | √ | ' ' | 上一持票人名称 |
| 24 | febstatus | 电票操作状态 | varchar | 50 |  | √ | ' ' | 电票操作状态,枚举: BANK_PROCESSING :银行处理中 BANK_SUCCESS :交易成功 BANK_FAIL :交易失败 BANK_EXCEPTION :交易未确认 EB_PROCESSING :银企处理中 BANK_UNKNOWN :交易未确认 |
| 25 | fbankmsg | 银行响应信息 | varchar | 2000 |  | √ | ' ' | 银行响应信息 |
| 26 | fpayagency | 到期无条件支付委托 | varchar | 50 |  | √ | ' ' | 到期无条件支付委托 |
| 27 | fincreaserate | 非卖方付息百分比 | varchar | 50 |  | √ | ' ' | 非卖方付息百分比 |
| 28 | frqstserialno | 银企请求流水号 | varchar | 50 |  | √ | ' ' | 银企请求流水号 |
| 29 | fdiscountamount | 实际贴现金额 | varchar | 50 |  | √ | ' ' | 实际贴现金额 |
| 30 | foperationcode | 交易类型 | varchar | 50 |  | √ | ' ' | 交易类型 |
| 31 | fflowserialno | 流程序列号 | varchar | 50 |  | √ | ' ' | 流程序列号 |
| 32 | frspserialno | 银企响应流水号 | varchar | 50 |  | √ | ' ' | 银企响应流水号 |
| 33 | facceptorbankaddr | 开户行地址 | varchar | 50 |  | √ | ' ' | 开户行地址 |
| 34 | febseqid | 银企系统支付流水 | varchar | 50 |  | √ | ' ' | 银企系统支付流水 |
| 35 | foppcnapscode | 对手方行号 | varchar | 50 |  | √ | ' ' | 对手方行号 |
| 36 | foppaccno | 对手方账号 | varchar | 50 |  | √ | ' ' | 对手方账号 |
| 37 | foppaccname | 对方名称 | varchar | 50 |  | √ | ' ' | 对方名称 |
| 38 | fautoaccept | 自动提示承兑 | bpchar | 1 |  | √ | '0' | 自动提示承兑 |
| 39 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 40 | fbankstatus | 银行响应码 | varchar | 50 |  | √ | ' ' | 银行响应码 |
| 41 | fadddate | 协商加天数 | varchar | 50 |  | √ | ' ' | 协商加天数 |
| 42 | fpretypeflag | 是否背书标识 | bpchar | 1 |  | √ | '0' | 是否背书标识 |
| 43 | fholdercnapscode | 持票人行号 | varchar | 50 |  | √ | ' ' | 持票人行号 |
| 44 | floanamount | 质押金额 | numeric | 19 | 6 | √ | 0 | 质押金额 |
| 45 | foppbankname | 对手方行名 | varchar | 50 |  | √ | ' ' | 对手方行名 |
| 46 | foppcountry | 对手方国家 | varchar | 50 |  | √ | ' ' | 对手方国家 |
| 47 | fholderaccno | 持票人账号 | varchar | 50 |  | √ | ' ' | 持票人账号 |
| 48 | foppcity | 对手方城市 | varchar | 50 |  | √ | ' ' | 对手方城市 |
| 49 | fexplain | 摘要 | varchar | 500 |  | √ | ' ' | 摘要 |
| 50 | fbankconsultno | 银行参考号 | varchar | 300 |  |  | ' ' | 银行参考号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_receivablehandle_e |  | finvoicenumber |
| 2 | pk_t_cdm_electronicbill_e |  | fid |

---

## 应付电票查询-主表 t_cdm_electronicbill

- **表名称：** 应付电票查询-主表
- **表名：** t_cdm_electronicbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpromiseexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 3 | fcollectioner | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 4 | fpromisegradebody | 评级主体 | varchar | 255 |  | √ | ' ' | 评级主体 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fissueticketbankno | 开户行行号 | varchar | 50 |  | √ | ' ' | 开户行行号 |
| 8 | fissueticketgrade | 评级主体 | varchar | 255 |  | √ | ' ' | 评级主体 |
| 9 | fapplicantname | 申请人名称 | varchar | 50 |  | √ | ' ' | 申请人名称 |
| 10 | fcollectionacc | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 11 | fpromisecreditlevel | 信用等级 | varchar | 255 |  | √ | ' ' | 信用等级 |
| 12 | fissueticketexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 13 | fticketstatus | 票据状态(旧) | varchar | 30 |  | √ | ' ' | 票据状态(旧),枚举: invoice :提示收票待签收 invoicesigned :提示收票已签收 recite :背书待签收 recitesigned :背书已签收 acceptance :提示承兑待签收 acceptancesigned :提示承兑已签收 registed :出票已登记 ensure :保证待签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 releaseofedgsigned :质押解除已签收 payment :提示付款待签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 preregister :预出票 |
| 14 | fbillno | 票据号码 | varchar | 50 |  | √ | ' ' | 票据号码 |
| 15 | fbatchseqid | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 16 | fpromiseinfo | 承兑人承兑 | varchar | 255 |  | √ | ' ' | 承兑人承兑 |
| 17 | fpromisedate | 承兑日期 | timestamp | 0 |  |  | null | 承兑日期 |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fissueticketbank | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 21 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 22 | fissueticketdate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 23 | fcollectionbank | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 24 | fpromisebankno | 承兑人行号 | varchar | 50 |  | √ | ' ' | 承兑人行号 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fexchangebillexpiredate | 汇票到期日 | timestamp | 0 |  |  | null | 汇票到期日 |
| 27 | flocamt | 本次操作金额 | numeric | 19 | 6 | √ | 0 | 本次操作金额 |
| 28 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fissueticketer | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 30 | fcollectionbankno | 开户行行号 | varchar | 50 |  | √ | ' ' | 开户行行号 |
| 31 | fdetailseqid | 明细号 | varchar | 100 |  | √ | ' ' | 明细号 |
| 32 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 33 | fpromisebank | 承兑人开户行 | varchar | 50 |  | √ | ' ' | 承兑人开户行 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fapplicantbankno | 申请人行号 | varchar | 50 |  | √ | ' ' | 申请人行号 |
| 36 | fissueticketcreditlevel | 信用等级 | varchar | 255 |  | √ | ' ' | 信用等级 |
| 37 | ftradecontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fapplicantacc | 申请人账号 | varchar | 50 |  | √ | ' ' | 申请人账号 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 42 | fpromiseensureinfo | 承兑保证信息 | varchar | 255 |  | √ | ' ' | 承兑保证信息 |
| 43 | fissueticketacc | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 44 | fissueticketpromise | 出票人承诺 | varchar | 255 |  | √ | ' ' | 出票人承诺 |
| 45 | fpromiser | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 46 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 47 | fapplicantbank | 申请人开户行 | varchar | 50 |  | √ | ' ' | 申请人开户行 |
| 48 | fsourcebillid | 源单id(弃用空闲字段) | int8 | 64 |  | √ | 0 | 源单id(弃用空闲字段) |
| 49 | fpromiseacc | 承兑人账户 | varchar | 50 |  | √ | ' ' | 承兑人账户 |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_receivablehandle |  | fbillno |
| 2 | pk_t_cdm_electronicbill |  | fid |
