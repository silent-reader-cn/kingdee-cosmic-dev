# 收票处理-bei_receivablehandle

## 收票处理-分表 t_bei_receivablehandle_e

- **表名称：** 收票处理-分表
- **表名：** t_bei_receivablehandle_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptorcountry | 承兑方国家 | varchar | 50 |  | √ | ' ' | 承兑方国家 |
| 3 | fdiscountrate | 贴现利率 | numeric | 23 | 10 | √ | 0.0000000000 | 贴现利率 |
| 4 | fdetailbizno | 业务支付明细号 | varchar | 50 |  | √ | ' ' | 业务支付明细号 |
| 5 | fautoreceive | 自动提示收票 | bpchar | 1 |  | √ | '0' | 自动提示收票 |
| 6 | facceptorprovince | 承兑方省份 | varchar | 50 |  | √ | ' ' | 承兑方省份 |
| 7 | fholderbankname | 持票人银行 | varchar | 50 |  | √ | ' ' | 持票人银行 |
| 8 | finvoicenumber | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 9 | febstatusmsg | 银企提示信息 | varchar | 50 |  | √ | ' ' | 银企提示信息 |
| 10 | fdisredrate | 赎回利率 | varchar | 50 |  | √ | ' ' | 赎回利率 |
| 11 | fcontractnumber | 协议号码 | varchar | 50 |  | √ | ' ' | 协议号码 |
| 12 | fdrafttype | 票据类型 | varchar | 50 |  | √ | ' ' | 票据类型,枚举: AC01 :银行承兑汇票 AC02 :商业承兑汇票 |
| 13 | fredemptionedate | 赎回截止日期 | varchar | 50 |  | √ | ' ' | 赎回截止日期 |
| 14 | foppprovince | 对手方省份 | varchar | 50 |  | √ | ' ' | 对手方省份 |
| 15 | foperationname | 操作中文名称 | varchar | 50 |  | √ | ' ' | 操作中文名称 |
| 16 | facceptorcity | 承兑方城市 | varchar | 50 |  | √ | ' ' | 承兑方城市 |
| 17 | findorsename | 被背书人名称 | varchar | 50 |  | √ | ' ' | 被背书人名称 |
| 18 | fredemptionsdate | 赎回开放日 | varchar | 50 |  | √ | ' ' | 赎回开放日 |
| 19 | fbizcode | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码,枚举: 01 :出票登记 02 :出票人提示承兑 03 :出票人提示收票 04 :撤票 10 :背书转让 11 :贴现 12 :贴现赎回 13 :转贴 14 :转贴赎回 15 :再贴 16 :再贴赎回 17 :保证 18 :质押 19 :质押解除 20 :提示付款 21 :逾期提示付款 22 :追索 23 :清偿 25 :人行卖票 40 :状态变更 41 :通用通知 43 :票据结清通知 50 :清算失败 A1 :待签收 D2 :已驳回 D1 :已签收 3q3eqqwssq :申请经办中 3qeqewq :取消 00 :初始 30 :撤销经办中 B2 :驳回经办中 B1 :签收经办中 E1 :清算失败 2q3eqe :撤票成功 wq2q :出票已登记 qqqq222 :回执失败 wqwqwqwqwwq :已撤销 qwqwqwqwq :申请发送待回执 wqwqwqwqwq :撤销发送待回执 C2 :驳回发送待回执 C1 :签收发送待回执 F1 :对方已撤销 222222222222 :对方已签收 wwwwwwwwwwww :对方已驳回 qqqqqqqqqqqq :对方待签收 |
| 20 | fkeepflag | 是否托管标识 | bpchar | 1 |  | √ | '0' | 是否托管标识 |
| 21 | fcustomerconsultno | 客户参考号 | varchar | 50 |  | √ | ' ' | 客户参考号 |
| 22 | fnotestate | 票据状态 | varchar | 50 |  | √ | ' ' | 票据状态 |
| 23 | fpreholdername | 上一代持票人名称 | varchar | 50 |  | √ | ' ' | 上一代持票人名称 |
| 24 | febstatus | 银企状态 | varchar | 50 |  | √ | ' ' | 银企状态 |
| 25 | fbankmsg | 银行响应信息 | varchar | 50 |  | √ | ' ' | 银行响应信息 |
| 26 | fpayagency | 到期无条件支付委托 | varchar | 50 |  | √ | ' ' | 到期无条件支付委托 |
| 27 | fincreaserate | 非卖方付息百分比 | varchar | 50 |  | √ | ' ' | 非卖方付息百分比 |
| 28 | frqstserialno | 银企请求流水号 | varchar | 50 |  | √ | ' ' | 银企请求流水号 |
| 29 | fdiscountamount | 实际贴现金额 | varchar | 50 |  | √ | ' ' | 实际贴现金额 |
| 30 | foperationcode | 交易类型 | varchar | 50 |  | √ | ' ' | 交易类型 |
| 31 | fflowserialno | 流程序列号 | varchar | 50 |  | √ | ' ' | 流程序列号 |
| 32 | frspserialno | 银企响应流水号 | varchar | 50 |  | √ | ' ' | 银企响应流水号 |
| 33 | facceptorbankaddr | 承兑开户行地址 | varchar | 50 |  | √ | ' ' | 承兑开户行地址 |
| 34 | febseqid | 银企系统支付流水 | varchar | 50 |  | √ | ' ' | 银企系统支付流水 |
| 35 | foppcnapscode | 对手方行号 | varchar | 50 |  | √ | ' ' | 对手方行号 |
| 36 | foppaccno | 对手方账号 | varchar | 50 |  | √ | ' ' | 对手方账号 |
| 37 | foppaccname | 对手方账户名 | varchar | 50 |  | √ | ' ' | 对手方账户名 |
| 38 | fautoaccept | 自动提示承兑 | bpchar | 1 |  | √ | '0' | 自动提示承兑 |
| 39 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 40 | fbankstatus | 银行响应码 | varchar | 50 |  | √ | ' ' | 银行响应码 |
| 41 | fadddate | 协商加填数 | varchar | 50 |  | √ | ' ' | 协商加填数 |
| 42 | fpretypeflag | 是否背书标识 | bpchar | 1 |  | √ | '0' | 是否背书标识 |
| 43 | fholdercnapscode | 持票人行号 | varchar | 50 |  | √ | ' ' | 持票人行号 |
| 44 | floanamount | 质押金额 | numeric | 19 | 6 | √ | 0.000000 | 质押金额 |
| 45 | foppbankname | 对手方行名 | varchar | 50 |  | √ | ' ' | 对手方行名 |
| 46 | foppcountry | 对手方国家 | varchar | 50 |  | √ | ' ' | 对手方国家 |
| 47 | fholderaccno | 持票人账号 | varchar | 50 |  | √ | ' ' | 持票人账号 |
| 48 | foppcity | 对手方城市 | varchar | 50 |  | √ | ' ' | 对手方城市 |
| 49 | fexplain | 摘要 | varchar | 50 |  | √ | ' ' | 摘要 |
| 50 | fbankconsultno | 银行参考号 | varchar | 50 |  | √ | ' ' | 银行参考号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_receivablehandle_e |  | fid |
| 2 | idx_bei_receivablehandle_e |  | finvoicenumber |

---

## 收票处理-分表 t_bei_receivablehandle_f

- **表名称：** 收票处理-分表
- **表名：** t_bei_receivablehandle_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptpromiseraccount | 承兑保证人账号 | varchar | 50 |  | √ | ' ' | 承兑保证人账号 |
| 3 | facceptpromisername | 承兑保证人名称 | varchar | 50 |  | √ | ' ' | 承兑保证人名称 |
| 4 | fcustomeropstatus | 客户操作状态 | varchar | 50 |  | √ | ' ' | 客户操作状态 |
| 5 | fopstatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: 0 :初始化 1 :操作中 2 :待同步 3 :同步中 4 :同步成功 5 :同步失败 |
| 6 | fotherinfo | otherinfo | varchar | 50 |  | √ | ' ' | otherinfo |
| 7 | fissuepromiseraddr | 出票保证人地址 | varchar | 50 |  | √ | ' ' | 出票保证人地址 |
| 8 | facceptpromiseraddr | 承兑保证人地址 | varchar | 50 |  | √ | ' ' | 承兑保证人地址 |
| 9 | fissuepromisername | 出票保证人名称 | varchar | 50 |  | √ | ' ' | 出票保证人名称 |
| 10 | fissuepromiseraccount | 出票保证人账号 | varchar | 50 |  | √ | ' ' | 出票保证人账号 |
| 11 | foppbankaddr | 对手方开户行地址 | varchar | 50 |  | √ | ' ' | 对手方开户行地址 |
| 12 | fdiscountpaytype | 贴现付息方式 | varchar | 50 |  | √ | ' ' | 贴现付息方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_receivablehandle_f |  | fopstatus |
| 2 | pk_t_bei_receivablehandle_f |  | fid |

---

## 收票处理-多语言表 t_bei_receivablehandle_l

- **表名称：** 收票处理-多语言表
- **表名：** t_bei_receivablehandle_l

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
| 1 | pk_t_bei_receivablehandle_l |  | fpkid |
| 2 | idx_bei_receivablehandle_l |  | fid |

---

## 收票处理-主表 t_bei_receivablehandle

- **表名称：** 收票处理-主表
- **表名：** t_bei_receivablehandle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpromiseexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 3 | fcollectioner | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 4 | fpromisegradebody | 评级主体 | varchar | 255 |  | √ | ' ' | 评级主体 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 7 | fissueticketbankno | 出票人行号 | varchar | 50 |  | √ | ' ' | 出票人行号 |
| 8 | fissueticketgrade | 评级主体 | varchar | 255 |  | √ | ' ' | 评级主体 |
| 9 | fapplicantname | 申请人名称 | varchar | 50 |  | √ | ' ' | 申请人名称 |
| 10 | fcollectionacc | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 11 | fpromisecreditlevel | 信用等级 | varchar | 255 |  | √ | ' ' | 信用等级 |
| 12 | fissueticketexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 13 | fticketstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 |
| 14 | fbillno | 票据号码 | varchar | 50 |  | √ | ' ' | 票据号码 |
| 15 | fbatchseqid | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 16 | fpromiseinfo | 承兑人承兑 | varchar | 255 |  | √ | ' ' | 承兑人承兑 |
| 17 | fpromisedate | 承兑日期 | timestamp | 0 |  |  | null | 承兑日期 |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fissueticketbank | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 21 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 22 | fissueticketdate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 23 | fcollectionbank | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 24 | fpromisebankno | 承兑人行号 | varchar | 50 |  | √ | ' ' | 承兑人行号 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fexchangebillexpiredate | 汇票到期日 | timestamp | 0 |  |  | null | 汇票到期日 |
| 27 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 28 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fissueticketer | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 30 | fcollectionbankno | 收款人行号 | varchar | 50 |  | √ | ' ' | 收款人行号 |
| 31 | fdetailseqid | 明细号 | varchar | 100 |  | √ | ' ' | 明细号 |
| 32 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 33 | fpromisebank | 承兑人开户行 | varchar | 50 |  | √ | ' ' | 承兑人开户行 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fapplicantbankno | 申请人行号 | varchar | 50 |  | √ | ' ' | 申请人行号 |
| 36 | fissueticketcreditlevel | 信用等级 | varchar | 255 |  | √ | ' ' | 信用等级 |
| 37 | ftradecontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fapplicantacc | 申请人账号 | varchar | 50 |  | √ | ' ' | 申请人账号 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 42 | fpromiseensureinfo | 承兑保证信息 | varchar | 255 |  | √ | ' ' | 承兑保证信息 |
| 43 | fissueticketacc | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 44 | fissueticketpromise | 出票保证 | varchar | 255 |  | √ | ' ' | 出票保证 |
| 45 | fpromiser | 全称 | varchar | 50 |  | √ | ' ' | 全称 |
| 46 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 47 | fapplicantbank | 申请人开户行 | varchar | 50 |  | √ | ' ' | 申请人开户行 |
| 48 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 49 | fpromiseacc | 承兑人账户 | varchar | 50 |  | √ | ' ' | 承兑人账户 |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_receivablehandle |  | fid |
| 2 | idx_bei_receivablehandle |  | fbillno |

---

## 单据体-子表 t_bei_receivablehandleent

- **表名称：** 单据体-子表
- **表名：** t_bei_receivablehandleent

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
| 32 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 33 | fendorsedate | 背书日期 | timestamp | 0 |  |  | null | 背书日期 |
| 34 | finitiatororg | 发起方组织机构编码 | varchar | 50 |  | √ | ' ' | 发起方组织机构编码 |
| 35 | finitiatorbankcnaps | 发起方行号 | varchar | 50 |  | √ | ' ' | 发起方行号 |
| 36 | facountbankcnaps | 入账行号 | varchar | 50 |  | √ | ' ' | 入账行号 |
| 37 | fcontractno | 协议编码 | varchar | 50 |  | √ | ' ' | 协议编码 |
| 38 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 39 | fopponentorg | 对手组织机构 | varchar | 50 |  | √ | ' ' | 对手组织机构 |
| 40 | fbusinesscode | 业务编码 | varchar | 50 |  | √ | ' ' | 业务编码 |
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
| 1 | pk_t_bei_receivablehandleent |  | fentryid |
| 2 | idx_bei_receivablehandleent |  | fid |
