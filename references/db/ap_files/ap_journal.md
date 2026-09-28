# 应付流水-ap_journal

## 应付流水-主表 t_ap_journal

- **表名称：** 应付流水-主表
- **表名：** t_ap_journal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizdescription | 业务描述 | varchar | 30 |  | √ | ' ' | 业务描述,枚举: fin :应付款发生额 pay :付款额 paid :预付款额 fin_woff :应付款冲抵额 paid_woff :预付款冲抵额 pay_woff :付款冲抵额 bus :暂估款发生额 rec :收款额 rec_woff :收款冲抵额 refund_pur :退采购付款 refund_pur_woff :退采购付款冲抵额 refund_paid :退预付 refund_paid_woff :退预付冲抵额 |
| 3 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 5 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | flocalprepaidamt | 付款金额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额折本币 |
| 7 | fsourcejournalid | 源流水id | int8 | 64 |  | √ | 0 | 源流水id |
| 8 | fiswrittenoff | 红冲流水 | bpchar | 1 |  | √ | '0' | 红冲流水 |
| 9 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 10 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 12 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 13 | festimatedcostamt | 暂估成本金额 | numeric | 23 | 10 | √ | 0 | 暂估成本金额 |
| 14 | flocalestimatedcostamt | 暂估成本金额折本币 | numeric | 23 | 10 | √ | 0 | 暂估成本金额折本币 |
| 15 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型 |
| 18 | fprepaidamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 19 | fpayableamt | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 20 | fpaymenttype | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 21 | festimatedamt | 暂估金额 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估金额 |
| 22 | fbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_busbill :暂估应付单 ap_finapbill :财务应付单 ap_paidbill :初始化预付单 ap_settlerecord :应付核销记录 cas_paybill :付款单 ar_settlerecord :应收核销记录 ap_adjexchbill :调汇单 ar_receivedbill :初始化预收单 cas_recbill :收款单 ar_settlebill :应收核销单 ap_settlebill :应付核销单 |
| 26 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 27 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 28 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | flocalpayableamt | 应付金额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额折本币 |
| 32 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 34 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 35 | flocalestimatedamt | 暂估金额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估金额折本币 |
| 36 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 38 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_jou_asstact |  | fasstactid |
| 2 | idx_ap_jou_org_date |  | forgid,fbizdate |
| 3 | t_ap_journal_pkey |  | fid |
| 4 | idx_ap_jou_srcid |  | fsourcebillid |
| 5 | idx_ap_journal_bizdescsrctype |  | fsourcebilltype,fbizdescription |
