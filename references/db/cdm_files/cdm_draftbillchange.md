# 换票记录单-cdm_draftbillchange

## 已换票据分录-子表 t_cdm_draftbill_havechg

- **表名称：** 已换票据分录-子表
- **表名：** t_cdm_draftbill_havechg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisneedsplit | 是否等分化数据 | bpchar | 1 |  | √ | '0' | 是否等分化数据 |
| 3 | foldelestatus | 操作前电票状态 | varchar | 80 |  | √ | ' ' | 操作前电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 payment :提示付款待签收 CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 4 | fbilltradelogid | 票据交易记录 | int8 | 64 |  | √ | 0 | 票据交易记录 |
| 5 | fs_billamount | 转让金额 | numeric | 19 | 6 | √ | 0 | 转让金额 |
| 6 | foldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 10 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_havechg |  | fentryid |
| 2 | idx_draftbill_havechg_fid |  | fid |

---

## 换票记录单-主表 t_cdm_draftbillchange

- **表名称：** 换票记录单-主表
- **表名：** t_cdm_draftbillchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbechangecount | 被换票据张数 | int4 | 32 |  | √ | 0 | 被换票据张数 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | ftradetype | 业务处理 | varchar | 30 |  | √ | ' ' | 业务处理,枚举: endorse :背书转让 discount :票据贴现 pledge :票据质押 rlspledge :质押解除 collect :票据托收 trusteeship :票据托管 retrieve :托管取回 refund :票据退票 payoff :票据解付 billsplit :票据拆分 payinterest :买方付息 |
| 8 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 9 | freason | 换票原因 | varchar | 600 |  | √ | ' ' | 换票原因 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | ftradebillno | 业务单据编号 | varchar | 80 |  | √ | ' ' | 业务单据编号 |
| 12 | fhavechangecount | 已换票据张数 | int4 | 32 |  | √ | 0 | 已换票据张数 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbechangeamount | 被换票据金额合计 | numeric | 19 | 6 | √ | 0 | 被换票据金额合计 |
| 16 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fhavechangeamount | 已换票据金额合计 | numeric | 19 | 6 | √ | 0 | 已换票据金额合计 |
| 18 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbillchange |  | fid |
| 2 | idx_draftbillchange_billno |  | fbillno |
| 3 | idx_draftbillchange_tbillno |  | ftradebillno |

---

## 被换票据分录-子表 t_cdm_draftbill_bechange

- **表名称：** 被换票据分录-子表
- **表名：** t_cdm_draftbill_bechange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisneedsplit | 是否等分化数据 | bpchar | 1 |  | √ | '0' | 是否等分化数据 |
| 3 | foldelestatus | 操作前电票状态 | varchar | 80 |  | √ | ' ' | 操作前电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 payment :提示付款待签收 CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 4 | fbilltradelogid | 票据交易记录 | int8 | 64 |  | √ | 0 | 票据交易记录 |
| 5 | fs_billamount | 转让金额 | numeric | 19 | 6 | √ | 0 | 转让金额 |
| 6 | foldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftradeentryid | 业务处理分录id | int8 | 64 |  | √ | 0 | 业务处理分录id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 11 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_draftbill_bechange_fid |  | fid |
| 2 | pk_t_cdm_draftbill_bechange |  | fentryid |
