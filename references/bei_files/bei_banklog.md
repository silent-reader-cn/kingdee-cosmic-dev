# 银企日志查询-bei_banklog

## 业务信息-子表 t_bei_banklogentry

- **表名称：** 业务信息-子表
- **表名：** t_bei_banklogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 SF :提交失败 |
| 3 | fbanklogtype | 执行任务 | varchar | 30 |  | √ | ' ' | 执行任务,枚举: balance :查询账户余额 batchBalance :批量查询余额 detail :下载交易明细 receipt :下载电子回单 pay :提交银企付款 queryPay :同步付款状态 updatePayStatus :修改付款状态 listBankLogin :获取银企接口 syncAccount :同步银行账号 queryNotePayable :应付票据查询 queryNoteReceivable :应收票据查询 notePayable_remit_register :开票登记 notePayable_remit_revocation :撤销出票 notePayable_remit_accept :提示承兑 notePayable_remit_receive :提示收票 noteReceivable_note_endorse :票据背书 noteReceivable_note_discount :票据贴现 noteReceivable_note_signin :票据通用签收 noteReceivable_pledge_note :票据质押 noteReceivable_remove_pledge :票据解除质押 noteReceivable_note_cancle :票据通用撤销 queryNoteDetail_reply :查询待签收票据 currentAndFixed :活期定期转换 queryCurrentAndFixed :活期定期转换同步状态 updateCurAndFixedStatus :活期定期转换修改状态 withdrawFromNAcc :通知存款直接支取 |
| 4 | facctbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 5 | fpaybillid | 支付单据ID | int8 | 64 |  | √ | 0 | 支付单据ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpaybilltypeid | 支付单据类型 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fpayamt | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 9 | fbillnumber | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 10 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 11 | fbillorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbilltypeid | 单据类型 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_banklogentry_bidblt |  | fbillid,fbanklogtype |
| 2 | idx_t_bei_banklogentry_fid |  | fid |
| 3 | pk_t_bei_banklogentry |  | fentryid |

---

## 银企日志查询-多语言表 t_bei_banklog_l

- **表名称：** 银企日志查询-多语言表
- **表名：** t_bei_banklog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_banklog_l |  | fid,flocaleid,fcomment |
| 2 | t_bei_banklog_l_pkey |  | fpkid |

---

## 银企日志查询-主表 t_bei_banklog

- **表名称：** 银企日志查询-主表
- **表名：** t_bei_banklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常原因 | text | 0 |  |  | null | 异常原因 |
| 3 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbanklogtype | 执行任务 | varchar | 30 |  | √ | ' ' | 执行任务,枚举: balance :查询账户余额 batchBalance :批量查询余额 detail :下载交易明细 receipt :下载电子回单 pay :提交银企付款 queryPay :同步付款状态 updatePayStatus :修改付款状态 listBankLogin :获取银企接口 syncAccount :同步银行账号 queryNotePayable :应付票据查询 queryNoteReceivable :应收票据查询 notePayable_remit_register :开票登记 notePayable_remit_revocation :撤销出票 notePayable_remit_accept :提示承兑 notePayable_remit_receive :提示收票 noteReceivable_note_endorse :票据背书 noteReceivable_note_discount :票据贴现 noteReceivable_note_signin :票据通用签收 noteReceivable_pledge_note :票据质押 noteReceivable_remove_pledge :票据解除质押 noteReceivable_note_cancle :票据通用撤销 queryNoteDetail_reply :查询待签收票据 currentAndFixed :活期定期转换 queryCurrentAndFixed :活期定期转换同步状态 updateCurAndFixedStatus :活期定期转换修改状态 withdrawFromNAcc :通知存款直接支取 buyFinancing :在线理财申购 queryBuyFinancing :在线理财申购同步状态 redeemFinancing :在线理财赎回 queryRedeemFinancing :在线理财赎回同步状态 updateFinancingStatus :在线理财申购修改状态 overseaPay :提交银企付款 queryOverseaPay :同步付款状态 pay_for_agentpay :提交银企代发 linkpay :联动支付 queryLinkpay :联动支付查询 |
| 5 | fsourceid | 单据ID（兼容保留） | varchar | 100 |  | √ | ' ' | 单据ID（兼容保留） |
| 6 | fbizexceptioninfo_tag | 业务其他异常信息_详情 | text | 0 |  |  | null | 业务其他异常信息_详情 |
| 7 | fsrcbizid | 业务支付单id | int8 | 64 |  | √ | 0 | 业务支付单id |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbankinterface | 银行接口信息 | varchar | 100 |  | √ | ' ' | 银行接口信息 |
| 12 | fsendexceptioninfo | 发送异常信息 | text | 0 |  |  | null | 发送异常信息 |
| 13 | fbizexceptioninfo | 业务其他异常信息 | text | 0 |  |  | null | 业务其他异常信息 |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | freceiveinfo | 接收信息 | text | 0 |  |  | null | 接收信息 |
| 17 | freceiveinfo_tag | 接收信息_详情 | text | 0 |  |  | null | 接收信息_详情 |
| 18 | fsourcebillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fsourcebilltype | 业务单据 | varchar | 30 |  | √ | ' ' | 业务单据,枚举: bei_bankagentpay :银行代发单 bei_bankpaybill :银行付款单 bei_transdetail :交易明细 bei_bankbalance :账户余额 am_accountbank :银行账户 bei_elecreceipt :电子回单 bei_banktransdownbill :银行下拨单 bei_banktransupbill :银行上划单 cdm_electronicbill :电票交易 bd_accountbanks :银行账户 cim_deposit :存款业务处理 cim_release :存款解活处理 cim_noticedeposit :通知存款处理 cim_noticerelease :通知存款解活处理 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | faccountbank | 银行账户 | varchar | 30 |  | √ | ' ' | 银行账户 |
| 23 | fbankinterfaceid | 银行接口ID | varchar | 100 |  | √ | ' ' | 银行接口ID |
| 24 | fsendinfo | 发送日志 | text | 0 |  |  | null | 发送日志 |
| 25 | ftranstype | 传输类型 | varchar | 30 |  | √ | ' ' | 传输类型,枚举: send :发送 Receiver :接收 exceptionSend :发送异常 exceptionReceive :接收类型 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 29 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fbankpaystate | 付款状态 | varchar | 30 |  | √ | 'OP' | 付款状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 SF :提交失败 |
| 31 | fpaycurrencyid | 支付币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fstatus | 数据状态 | bpchar | 5 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 33 | fsendinfo_tag | 发送日志_详情 | text | 0 |  |  | null | 发送日志_详情 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 36 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 37 | fpaytotalamt | 支付总金额 | numeric | 19 | 6 | √ | 0 | 支付总金额 |
| 38 | fisexception | 执行结果 | varchar | 30 |  | √ | ' ' | 执行结果,枚举: 0 :成功 1 :失败 |
| 39 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | ftime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 41 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fsendexceptioninfo_tag | 发送异常信息_详情 | text | 0 |  |  | null | 发送异常信息_详情 |
| 44 | fcomment | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fpayeeacnt | 收款账户 | varchar | 100 |  | √ | ' ' | 收款账户 |
| 47 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 48 | freceiveexceptioninfo_tag | 接收异常信息_详情 | text | 0 |  |  | null | 接收异常信息_详情 |
| 49 | freceiveexceptioninfo | 接收异常信息 | text | 0 |  |  | null | 接收异常信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_banklog_pkey |  | fid |
| 2 | idx_bei_banklog_no |  | fsourcebillno |
| 3 | idx_bei_banklog |  | fcompanyid,ftime,fisexception |
| 4 | idx_t_bei_banklog_master |  | fmasterid |
| 5 | idx_bei_banklog_sidb |  | fsrcbizid,fbanklogtype |
| 6 | idx_bei_banklog_time |  | ftime |
| 7 | idx_t_bei_banklog_createorg |  | fcreateorgid |

---

## 关联子实体-子表 t_bei_banklog_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bei_banklog_lk

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
| 1 | idx_bei_banklog_lk_fk |  | fid |
| 2 | t_bei_banklog_lk_pkey |  | fpkid |
