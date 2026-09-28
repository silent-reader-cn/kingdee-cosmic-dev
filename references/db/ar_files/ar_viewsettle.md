# 查询核销记录-ar_viewsettle

## 关联子实体-子表 t_ap_settlerecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_settlerecord_lk

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
| 1 | t_ap_settlerecord_lk_pkey |  | fpkid |
| 2 | idx_ap_settlerecord_lk_fk |  | fid |

---

## 查询核销记录-反写记录表 t_ap_settlerecord_wb

- **表名称：** 查询核销记录-反写记录表
- **表名：** t_ap_settlerecord_wb

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
| 1 | t_ap_settlerecord_wb_pkey |  | fentryid |
| 2 | idx_ap_settlerecord_wb_fk |  | fid |

---

## 查询核销记录-主表 t_ap_settlerecord

- **表名称：** 查询核销记录-主表
- **表名：** t_ap_settlerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 6 | fmainbillentity | 主方实体标识 | varchar | 50 |  | √ | ' ' | 主方实体标识 |
| 7 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ar_payproperty :应收款项性质 cas_receivingbilltype :收款用途 ap_payproperty :应付款项性质 cas_paymentbilltype :付款类型 |
| 9 | fsettlelogentryid | 核销日志分录id | int8 | 64 |  | √ | 0 | 核销日志分录id |
| 10 | freceivingtypeid | 主方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fmainbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 14 | fpaypropertyfield | 款项性质值 | int8 | 64 |  | √ | 0 | 应收款项性质 ar_payproperty |
| 15 | fbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 18 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | fbillstatus | 核销记录状态 | varchar | 30 |  | √ | ' ' | 核销记录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 24 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fsettleseq | 核销序号 | int8 | 64 |  | √ | 0 | 核销序号 |
| 27 | fautosettletype | 自动核销参数类型 | varchar | 30 |  | √ | '0' | 自动核销参数类型,枚举: 1 :BOTP自动核销 2 :核心单据号自动核销 3 :其它 4 :BOTP自动核销(断关系) 5 :付款退款 6 :收款退款 |
| 28 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fiscreatesettlebill | 生成核销单 | bpchar | 1 |  | √ | ' ' | 生成核销单 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 33 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 34 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 35 | fasstreceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 36 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 37 | fiswrittenoff | 是否红冲生成 | bpchar | 1 |  | √ | '0' | 是否红冲生成 |
| 38 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 39 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | flocaltotalsettleamt | 核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额(本位币) |
| 41 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 42 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fpayableamt | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 45 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 46 | fsettlebillid | 核销单id | int8 | 64 |  | √ | 0 | 核销单id |
| 47 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 manual :手工核销 match :方案匹配核销 import :引入核销 rpamatch :RPA方案核销 |
| 50 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 recself :收款红蓝对冲 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 aparsettle :应付冲应收 payrecsettle :付款冲退款 aprecsettle :应付退款核销 recclearing :收款清理 recrefundclearing :收款退款清理 |
| 51 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | fplanduedate | 计划到期日 | timestamp | 0 |  |  | null | 计划到期日 |
| 54 | ftotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次核销金额 |
| 55 | fbilltypenewid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 56 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 57 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 58 | fmainbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 59 | fasstpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 60 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 61 | fmainasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 62 | fsettlebillno | 核销单单据编号 | varchar | 80 |  | √ | ' ' | 核销单单据编号 |
| 63 | fpaymenttypeid | 主方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 64 | fiscahsale | 现销现购 | bpchar | 1 |  | √ | ' ' | 现销现购 |
| 65 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 66 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 67 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 68 | fbilltype | 单据类型（旧） | varchar | 30 |  | √ | ' ' | 单据类型（旧）,枚举: standard :标准销售应收 expense :费用销售应收 other :其他应收 borrowar :应收款项调整 SalesRec :销售收款 OtherRec :其他收款 advrec :预收款 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 receivedbill :期初预收 head :按整单 entry :按分录 planEntry :按账龄 appay :采购付款 advpay :预付款 ap_finapbill_asset_BT_S :资产采购应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sr_logentry |  | fsettlelogentryid |
| 2 | idx_ap_sr_seq |  | fsettleseq |
| 3 | idx_ap_sr_orgdate |  | forgid,fsettledate |
| 4 | idx_ap_sr_settlebillid |  | fsettlebillid |
| 5 | idx_ap_sr_asstact |  | fmainasstactid |
| 6 | t_ap_settlerecord_pkey |  | fid |
| 7 | idx_ap_sr_billno |  | fbillno |
| 8 | idx_ap_sr_mainbillid |  | fmainbillid |

---

## 单据体-子表 t_ap_settlerecordentry

- **表名称：** 单据体-子表
- **表名：** t_ap_settlerecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurchaserid | 辅方采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | fasstact | 辅方往来单位名称 | varchar | 255 |  | √ | ' ' | 辅方往来单位名称 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fsalesmanid | 辅方销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 7 | fswappl | 辅方汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方汇兑损益 |
| 8 | fsettlelocalamt | 辅方核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 辅方核销金额(本位币) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fpurdepartmentid | 辅方采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbilldate | 辅方业务日期 | timestamp | 0 |  |  | null | 辅方业务日期 |
| 12 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 13 | fsettleamt | 辅方本次核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方本次核销金额 |
| 14 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 ar_payproperty :应收款项性质 cas_receivingbilltype :收款用途 cas_paymentbilltype :付款类型 |
| 15 | fpurdeptid | 辅方采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 16 | freceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 17 | fcorebillno | 辅方核心单据号 | varchar | 255 |  | √ | ' ' | 辅方核心单据号 |
| 18 | fexchangerate | 辅方汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方汇率 |
| 19 | fpaypropertyfield | 辅方款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 20 | fquotation | 辅方换算方式 | varchar | 30 |  | √ | '0' | 辅方换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 21 | fbillnum | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 22 | fpayableamt | 辅方应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方应收金额 |
| 23 | fbiztypeid | 辅方业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 24 | fbillentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 25 | fexpenseitemid | 辅方费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 27 | fpurorgid | 辅方采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 29 | fprojectid | 辅方项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fmpmtasknoid | 辅方项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 31 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 32 | fsalesdeptid | 辅方销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fplanduedate | 辅方计划到期日 | timestamp | 0 |  |  | null | 辅方计划到期日 |
| 34 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 35 | fbilltypenewid | 辅方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | fdescription | 摘要 | varchar | 512 |  |  | null | 摘要 |
| 37 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 38 | fpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 39 | fsalesorgid | 辅方销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 43 | fsalesgroupid | 辅方销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 44 | fbilltype | 辅方单据类型（旧） | varchar | 30 |  | √ | ' ' | 辅方单据类型（旧）,枚举: standard :标准销售应收 expense :销售费用财务应收 other :其他应收 SalesRec :销售收款 OtherRec :其他收款 receivedbill :期初预收 liquidation :清理单 purap :标准采购应付 feeap :费用采购应付 otherap :其他应付 borrowap :应收款项调整 borrowar :应收款项调整 head :按整单 entry :按分录 planEntry :按账龄 purfeeap :费用应付 appay :采购付款 otherpay :其他付款 advpay :预付款 advrec :预收款 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 paid :期初预付 ap_finapbill_asset_BT_S :资产采购应付 ApFin_product_BT_S :产品委外应付 ApFin_service_BT_S :服务采购应付 |
| 45 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sre_billnum |  | fbillnum |
| 2 | t_ap_settlerecordentry_pkey |  | fentryid |
| 3 | idx_ap_sre_asstact |  | fasstactid |
| 4 | idx_ap_sre_idbillid |  | fid,fbillid |
| 5 | idx_ap_sre_pid |  | fid |
| 6 | idx_ap_sre_billid |  | fbillid |

---

## 查询核销记录-关联追踪表 t_ap_settlerecord_tc

- **表名称：** 查询核销记录-关联追踪表
- **表名：** t_ap_settlerecord_tc

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
| 1 | idx_ap_settlerecord_tc_tid |  | ftid |
| 2 | t_ap_settlerecord_tc_pkey |  | fid |
| 3 | idx_ap_settlerecord_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_ap_settlerecordentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_settlerecordentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settlerecordentry_lk_pkey |  | fpkid |
| 2 | idx_ap_settlerecordentry_lk_fk |  | fentryid |
