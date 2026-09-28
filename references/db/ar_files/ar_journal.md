# 应收流水-ar_journal

## 应收流水-主表 t_ar_journal

- **表名称：** 应收流水-主表
- **表名：** t_ar_journal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizdescription | 业务描述 | varchar | 30 |  | √ | ' ' | 业务描述,枚举: fin :应收款发生额 rec :收款额 received :预收款额 fin_woff :应收款冲抵额 received_woff :预收款冲抵额 rec_woff :收款冲抵额 bus :暂估款发生额 pay :付款额 pay_woff :付款冲抵额 refund_sale :退销售回款 refund_sale_woff :退销售回款冲抵额 refund_received :退预收 refund_received_woff :退预收冲抵额 |
| 3 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 4 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | flocalreceivableamt | 应收金额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额折本位币 |
| 7 | fsourcejournalid | 源流水id | int8 | 64 |  | √ | 0 | 源流水id |
| 8 | fiswrittenoff | 红冲流水 | bpchar | 1 |  | √ | '0' | 红冲流水 |
| 9 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 10 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 11 | freceivedamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 12 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型 |
| 15 | festimatedamt | 暂估金额 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估金额 |
| 16 | fbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_busbill :暂估应收单 ar_finarbill :财务应收单 ar_receivedbill :初始化预收单 ar_settlerecord :应收核销记录 cas_recbill :收款单 ap_settlerecord :应付核销记录 ar_adjustexchbill :调汇单 ap_paidbill :初始化预付单 cas_paybill :付款单 ar_settlebill :应收核销单 ap_settlebill :应付核销单 ar_baddebtlossbill :坏账损失单 |
| 19 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | freceivableamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 26 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 28 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 29 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 30 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | flocalestimatedamt | 暂估金额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 暂估金额折本位币 |
| 32 | flocalreceivedamt | 收款金额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额折本位币 |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 35 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 36 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_journal_pkey |  | fid |
| 2 | idx_ar_jou_srcid |  | fsourcebillid |
| 3 | idx_ar_jou_asstact |  | fasstactid |
| 4 | idx_ar_jou_org_date |  | forgid,fbizdate |
| 5 | idx_ar_journal_bizdescsrctype |  | fsourcebilltype,fbizdescription |

---

## 应收流水-关联追踪表 t_ar_journal_tc

- **表名称：** 应收流水-关联追踪表
- **表名：** t_ar_journal_tc

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
| 1 | t_ar_journal_tc_pkey |  | fid |
| 2 | idx_ar_journal_tc_tid |  | ftid |
| 3 | idx_ar_journal_tc_tbill |  | ftbillid |

---

## 应收流水-反写记录表 t_ar_journal_wb

- **表名称：** 应收流水-反写记录表
- **表名：** t_ar_journal_wb

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
| 1 | idx_ar_journal_wb_fk |  | fid |
| 2 | t_ar_journal_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_ar_journal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_journal_lk

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
| 1 | t_ar_journal_lk_pkey |  | fpkid |
| 2 | idx_ar_journal_lk_fk |  | fid |
