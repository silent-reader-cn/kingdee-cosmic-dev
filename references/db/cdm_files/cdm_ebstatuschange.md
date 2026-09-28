# 操作状态变更单-cdm_ebstatuschange

## 操作状态变更单分录-子表 t_cdm_ebstatuschg_entity

- **表名称：** 操作状态变更单分录-子表
- **表名：** t_cdm_ebstatuschg_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafterticketstatus | 修改后电票状态 | varchar | 50 |  | √ | ' ' | 修改后电票状态,枚举: invoice :提示收票待签收 invoicesigned :提示收票已签收 recite :背书待签收 recitesigned :背书已签收 acceptance :提示承兑待签收 acceptancesigned :提示承兑已签收 registed :出票已登记 ensure :保证待签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 releaseofedgsigned :质押解除已签收 payment :提示付款待签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 |
| 3 | fafterebstatus | 修改后电票操作状态 | varchar | 50 |  | √ | ' ' | 修改后电票操作状态,枚举: BANK_SUCCESS :交易成功 BANK_FAIL :交易失败 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftradetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: noteendorse :背书 remitaccept :提示承兑 remitreceive :提示收票 notediscount :贴现 notesignin :签收 ticketguarantee :出票保证 remitregister :开票登记 remitrevocation :撤销出票 notesigninreject :拒收 notecancle :撤销 remitcancle :取消出票 pledgenote :质押 removepledge :质押解除 presentpayment :票据托收 remitconfirm :合同确认 |
| 6 | freason | 原因 | varchar | 255 |  | √ | ' ' | 原因 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fticketstatus | 电票状态 | varchar | 50 |  | √ | ' ' | 电票状态,枚举: invoice :提示收票待签收 invoicesigned :提示收票已签收 recite :背书待签收 recitesigned :背书已签收 acceptance :提示承兑待签收 acceptancesigned :提示承兑已签收 registed :出票已登记 ensure :保证待签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 releaseofedgsigned :质押解除已签收 payment :提示付款待签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 |
| 9 | fbankmsg | 银行返回信息 | varchar | 512 |  | √ | ' ' | 银行返回信息 |
| 10 | febstatus | 电票操作状态 | varchar | 50 |  | √ | ' ' | 电票操作状态,枚举: BANK_PROCESSING :银行处理中 BANK_SUCCESS :交易成功 BANK_FAIL :交易失败 BANK_EXCEPTION :交易未确认 EB_PROCESSING :银企处理中 BANK_UNKNOWN :交易未确认 |
| 11 | foperatestatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: success :写入成功 fail :写入失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_ebstatuschg_entity_fid |  | fid |
| 2 | pk_t_cdm_ebstatuschg_entity |  | fentryid |

---

## 操作状态变更单-主表 t_cdm_ebstatuschange

- **表名称：** 操作状态变更单-主表
- **表名：** t_cdm_ebstatuschange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdraftbillno | 票据号码 | varchar | 50 |  | √ | ' ' | 票据号码 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsourceid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsourcetype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型,枚举: cdm_electronic_pay_deal :在线出票处理 cdm_electronic_rec_deal :在手票据处理 cdm_electronic_sign_deal :待签收票据处理 |
| 11 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_ebstatuschange |  | fid |
| 2 | idx_cdm_ebstatuschange |  | fbillno |
