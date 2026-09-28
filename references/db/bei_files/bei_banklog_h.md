# 银企日志查询_归档-bei_banklog_h

## 银企日志查询_归档-主表 t_bei_banklog_h

- **表名称：** 银企日志查询_归档-主表
- **表名：** t_bei_banklog_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常原因 | text | 0 |  |  | null | 异常原因 |
| 3 | fbankpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 SF :提交失败 |
| 4 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbanklogtype | 执行任务 | varchar | 30 |  | √ | ' ' | 执行任务,枚举: balance :查询账户余额 batchBalance :批量查询余额 detail :下载交易明细 receipt :下载电子回单 pay :提交银企付款 queryPay :同步付款状态 updatePayStatus :修改付款状态 listBankLogin :获取银企接口 syncAccount :同步银行账号 queryNotePayable :应付票据查询 queryNoteReceivable :应收票据查询 notePayable_remit_register :开票登记 notePayable_remit_revocation :撤销出票 notePayable_remit_accept :提示承兑 notePayable_remit_receive :提示收票 noteReceivable_note_endorse :票据背书 noteReceivable_note_discount :票据贴现 noteReceivable_note_signin :票据通用签收 noteReceivable_pledge_note :票据质押 noteReceivable_remove_pledge :票据解除质押 noteReceivable_note_cancle :票据通用撤销 queryNoteDetail_reply :查询待签收票据 currentAndFixed :活期定期转换 queryCurrentAndFixed :活期定期转换同步状态 updateCurAndFixedStatus :活期定期转换修改状态 withdrawFromNAcc :通知存款直接支取 buyFinancing :在线理财申购 queryBuyFinancing :在线理财申购同步状态 redeemFinancing :在线理财赎回 queryRedeemFinancing :在线理财赎回同步状态 updateFinancingStatus :在线理财申购修改状态 overseaPay :提交银企付款 queryOverseaPay :同步付款状态 pay_for_agentpay :提交银企代发 linkpay :联动支付 queryLinkpay :联动支付查询 |
| 6 | fsourceid | 单据ID（兼容保留） | varchar | 100 |  | √ | ' ' | 单据ID（兼容保留） |
| 7 | fbizexceptioninfo_tag | 业务其他异常信息_详情 | text | 0 |  |  | null | 业务其他异常信息_详情 |
| 8 | fpaycurrencyid | 支付币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fsrcbizid | 业务支付单id | int8 | 64 |  | √ | 0 | 业务支付单id |
| 10 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 5 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fsendinfo_tag | 发送日志_详情 | text | 0 |  |  | null | 发送日志_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fbankinterface | 银行接口信息 | varchar | 100 |  | √ | ' ' | 银行接口信息 |
| 17 | fsendexceptioninfo | 发送异常信息 | text | 0 |  |  | null | 发送异常信息 |
| 18 | fbizexceptioninfo | 业务其他异常信息 | text | 0 |  |  | null | 业务其他异常信息 |
| 19 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | freceiveinfo | 接收信息 | text | 0 |  |  | null | 接收信息 |
| 21 | freceiveinfo_tag | 接收信息_详情 | text | 0 |  |  | null | 接收信息_详情 |
| 22 | fpaytotalamt | 支付总金额 | numeric | 19 | 6 | √ | 0 | 支付总金额 |
| 23 | fisexception | 执行结果 | varchar | 30 |  | √ | ' ' | 执行结果,枚举: 0 :成功 1 :失败 |
| 24 | fsourcebillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 25 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | ftime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 29 | fsendexceptioninfo_tag | 发送异常信息_详情 | text | 0 |  |  | null | 发送异常信息_详情 |
| 30 | fsourcebilltype | 业务单据 | varchar | 30 |  | √ | ' ' | 业务单据,枚举: bei_bankagentpay :银行代发单 bei_bankpaybill :银行付款单 bei_transdetail :交易明细 bei_bankbalance :账户余额 am_accountbank :银行账户 bei_elecreceipt :电子回单 bei_banktransdownbill :银行下拨单 bei_banktransupbill :银行上划单 cdm_electronicbill :电票交易 bd_accountbanks :银行账户 cim_deposit :存款业务处理 cim_release :存款解活处理 cim_noticedeposit :通知存款处理 cim_noticerelease :通知存款解活处理 |
| 31 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fpayeeacnt | 收款账户 | varchar | 100 |  | √ | ' ' | 收款账户 |
| 34 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 35 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | faccountbank | 银行账户 | varchar | 30 |  | √ | ' ' | 银行账户 |
| 37 | fbankinterfaceid | 银行接口ID | varchar | 100 |  | √ | ' ' | 银行接口ID |
| 38 | freceiveexceptioninfo_tag | 接收异常信息_详情 | text | 0 |  |  | null | 接收异常信息_详情 |
| 39 | fsendinfo | 发送日志 | text | 0 |  |  | null | 发送日志 |
| 40 | freceiveexceptioninfo | 接收异常信息 | text | 0 |  |  | null | 接收异常信息 |
| 41 | ftranstype | 传输类型 | varchar | 30 |  | √ | ' ' | 传输类型,枚举: send :发送 Receiver :接收 exceptionSend :发送异常 exceptionReceive :接收类型 |
| 42 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 43 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 44 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_banklog_h |  | fid |
| 2 | idx_bei_banklog_h |  | fcompanyid,ftime,fisexception |

---

## 业务信息-子表 t_bei_banklogentry_h

- **表名称：** 业务信息-子表
- **表名：** t_bei_banklogentry_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 SF :提交失败 OZ :银企处理中止 |
| 3 | fbanklogtype | 执行任务 | varchar | 30 |  | √ | ' ' | 执行任务,枚举: balance :查询账户余额 batchBalance :批量查询余额 detail :下载交易明细 receipt :下载电子回单 pay :提交银企付款 queryPay :同步付款状态 updatePayStatus :修改付款状态 listBankLogin :获取银企接口 syncAccount :同步银行账号 queryNotePayable :应付票据查询 queryNoteReceivable :应收票据查询 notePayable_remit_register :开票登记 notePayable_remit_revocation :撤销出票 notePayable_remit_accept :提示承兑 notePayable_remit_receive :提示收票 noteReceivable_note_endorse :票据背书 noteReceivable_note_discount :票据贴现 noteReceivable_note_signin :票据通用签收 noteReceivable_pledge_note :票据质押 noteReceivable_remove_pledge :票据解除质押 noteReceivable_note_cancle :票据通用撤销 queryNoteDetail_reply :查询待签收票据 currentAndFixed :活期定期转换 queryCurrentAndFixed :活期定期转换同步状态 updateCurAndFixedStatus :活期定期转换修改状态 withdrawFromNAcc :通知存款直接支取 |
| 4 | facctbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fpaybillid | 支付单据ID | int8 | 64 |  | √ | 0 | 支付单据ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpaybilltypeid | 支付单据类型 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fpayamt | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 9 | fbillnumber | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 10 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 11 | fbillorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbilltypeid | 单据类型 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_banklogentry_h |  | fentryid |

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

---

## 银企日志查询_归档-多语言表 t_bei_banklog_h_l

- **表名称：** 银企日志查询_归档-多语言表
- **表名：** t_bei_banklog_h_l

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
| 1 | idx_bei_banklog_h_l |  | fid,flocaleid,fcomment |
| 2 | pk_t_bei_banklog_h_l |  | fpkid |
