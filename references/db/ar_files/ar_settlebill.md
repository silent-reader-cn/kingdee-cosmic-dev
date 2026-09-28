# 应收核销单-ar_settlebill

## 应收核销单-主表 t_ar_settlebill

- **表名称：** 应收核销单-主表
- **表名：** t_ar_settlebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | fisdiffcurrencysettle | 异币种核销 | bpchar | 1 |  | √ | '0' | 异币种核销 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0 | 汇兑损益 |
| 7 | fmainbillentity | 主方实体标识 | varchar | 50 |  | √ | ' ' | 主方实体标识 |
| 8 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ar_payproperty :应收款项性质 cas_receivingbilltype :收款用途 ap_payproperty :应付款项性质 cas_paymentbilltype :付款类型 |
| 10 | fsettlelogentryid | 核销日志分录id | int8 | 64 |  | √ | 0 | 核销日志分录id |
| 11 | freceivingtypeid | 主方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 14 | fmainbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 15 | fpaypropertyfield | 款项性质值 | int8 | 64 |  | √ | 0 | 应收款项性质 ar_payproperty |
| 16 | findepadjustexch | 独立调汇 | bpchar | 1 |  | √ | '0' | 独立调汇 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 19 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 23 | fbillstatus | 核销单状态 | varchar | 30 |  | √ | ' ' | 核销单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 25 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 28 | fsettleseq | 核销序号 | int4 | 32 |  | √ | 0 | 核销序号 |
| 29 | fautosettletype | 自动核销参数类型 | varchar | 30 |  | √ | '0' | 自动核销参数类型,枚举: 1 :BOTP自动核销 2 :核心单据号自动核销 3 :其它 4 :BOTP自动核销(断关系) 5 :付款退款 6 :收款退款 7 :按合同编号核销 |
| 30 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fmainbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 32 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 35 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 36 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 37 | fasstreceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 38 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fiswrittenoff | 是否红冲生成 | bpchar | 1 |  | √ | '0' | 是否红冲生成 |
| 40 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 41 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 42 | flocaltotalsettleamt | 本次核销金额(本位币) | numeric | 23 | 10 | √ | 0 | 本次核销金额(本位币) |
| 43 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 44 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fpayableamt | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 47 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 48 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 manual :手工核销 match :方案匹配核销 import :引入核销 rpamatch :RPA方案核销 |
| 51 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 recself :收款红蓝对冲 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 aparsettle :应付冲应收 payrecsettle :付款冲退款 aprecsettle :应付退款核销 recclearing :收款清理 recrefundclearing :收款退款清理 arpremium :应收质保金 |
| 52 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fplanduedate | 计划到期日 | timestamp | 0 |  |  | null | 计划到期日 |
| 55 | ftotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 56 | fbilltypenewid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 57 | fsettlerecordid | 核销记录id | int8 | 64 |  | √ | 0 | 核销记录id |
| 58 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | fmainbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 61 | fasstpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 62 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 63 | fmainasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 64 | fpaymenttypeid | 主方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 65 | fiscahsale | 现销现购 | bpchar | 1 |  | √ | ' ' | 现销现购 |
| 66 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 67 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 68 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 69 | fbilltype | 单据类型（旧） | varchar | 30 |  | √ | ' ' | 单据类型（旧）,枚举: purap :采购标准应付 feeap :费用采购应付 otherap :其他应付 borrowap :应付款项调整 purfeeap :费用应付 appay :采购付款 otherpay :其他付款 advpay :预付款 advrec :预收款 ApFin_service_BT_S :服务采购应付 SalesRec :销售收款 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 ap_finapbill_asset_BT_S :资产采购应付 ApFin_product_BT_S :产品委外应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_sb_mainbillid |  | fmainbillid |
| 2 | idx_ar_sb_billno |  | fbillno |
| 3 | idx_ar_sb_logentry |  | fsettlelogentryid |
| 4 | idx_ar_sb_orgdateseq |  | forgid,fsettledate,fsettleseq |
| 5 | idx_ar_sb_settlerecordid |  | fsettlerecordid |
| 6 | idx_ar_sb_mainbillentryid |  | fmainbillentryid |
| 7 | idx_ar_sb_asstact |  | fmainasstactid |
| 8 | idx_ar_sb_mainbillno |  | fmainbillno |
| 9 | pk_t_ar_settlebill |  | fid |

---

## 单据体-子表 t_ar_settlebillentry

- **表名称：** 单据体-子表
- **表名：** t_ar_settlebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 辅方汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fsalesmanid | 辅方销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | fisdiffcurrencysettle | 异币种核销 | bpchar | 1 |  | √ | '0' | 异币种核销 |
| 5 | fswappl | 辅方汇兑损益 | numeric | 23 | 10 | √ | 0 | 辅方汇兑损益 |
| 6 | fsettlelocalamt | 辅方本次核销金额(本位币) | numeric | 23 | 10 | √ | 0 | 辅方本次核销金额(本位币) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fpurdepartmentid | 辅方采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 ar_payproperty :应收款项性质 cas_receivingbilltype :收款用途 cas_paymentbilltype :付款类型 |
| 10 | fsettlerecordentryid | 核销记录明细id | int8 | 64 |  | √ | 0 | 核销记录明细id |
| 11 | freceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 12 | fexchangerate | 辅方汇率 | numeric | 23 | 10 | √ | 0 | 辅方汇率 |
| 13 | fconbillnumber | 辅方合同编号 | varchar | 255 |  | √ | ' ' | 辅方合同编号 |
| 14 | fpaypropertyfield | 辅方款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 15 | fbillentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 16 | fexpenseitemid | 辅方费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 17 | fpurorgid | 辅方采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 19 | fprojectid | 辅方项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | fmpmtasknoid | 辅方项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 21 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 22 | fdescription | 摘要 | varchar | 512 |  | √ | ' ' | 摘要 |
| 23 | fsalesorgid | 辅方销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 27 | flicenseno | 辅方许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 28 | fpurchaserid | 辅方采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fmaterialid | 辅方物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 30 | fasstact | 辅方往来单位名称 | varchar | 255 |  | √ | ' ' | 辅方往来单位名称 |
| 31 | fbilldate | 辅方业务日期 | timestamp | 0 |  |  | null | 辅方业务日期 |
| 32 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 33 | fsettleamt | 辅方本次核销金额 | numeric | 23 | 10 | √ | 0 | 辅方本次核销金额 |
| 34 | fpurdeptid | 辅方采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 35 | fbonded | 辅方保税 | bpchar | 1 |  | √ | '0' | 辅方保税 |
| 36 | fcorebillno | 辅方核心单据号 | varchar | 255 |  | √ | ' ' | 辅方核心单据号 |
| 37 | fquotation | 辅方换算方式 | varchar | 30 |  | √ | '0' | 辅方换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 38 | flocalsettletaxamt | 辅方本次核销税额(本位币) | numeric | 23 | 10 | √ | 0 | 辅方本次核销税额(本位币) |
| 39 | fbillnum | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 40 | fpayableamt | 辅方应收金额 | numeric | 23 | 10 | √ | 0 | 辅方应收金额 |
| 41 | fbiztypeid | 辅方业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 42 | fbillsubentryid | 单据匹配分录id | int8 | 64 |  | √ | 0 | 单据匹配分录id |
| 43 | fsalesdeptid | 辅方销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fplanduedate | 辅方计划到期日 | timestamp | 0 |  |  | null | 辅方计划到期日 |
| 45 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 46 | fbilltypenewid | 辅方单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 47 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 48 | fsettletaxamt | 辅方本次核销税额 | numeric | 23 | 10 | √ | 0 | 辅方本次核销税额 |
| 49 | fpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 50 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | fsalesgroupid | 辅方销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 52 | fbilltype | 辅方单据类型（旧） | varchar | 30 |  | √ | ' ' | 辅方单据类型（旧）,枚举: standard :标准销售应收 expense :销售费用财务应收 other :其他应收 SalesRec :销售收款 OtherRec :其他收款 receivedbill :期初预收 liquidation :清理单 purap :标准采购应付 feeap :费用采购应付 otherap :其他应付 borrowap :应收款项调整 borrowar :应收款项调整 head :按整单 entry :按分录 planEntry :按账龄 purfeeap :费用应付 appay :采购付款 otherpay :其他付款 advpay :预付款 advrec :预收款 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 paid :期初预付 ap_finapbill_asset_BT_S :资产采购应付 ApFin_product_BT_S :产品委外应付 ApFin_service_BT_S :服务采购应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_settlebillentry |  | fentryid |
| 2 | idx_ar_sbe_billnum |  | fbillnum |
| 3 | idx_ar_sbe_asstact |  | fasstactid |
| 4 | idx_ar_sbe_pid |  | fid |
| 5 | idx_ar_sbe_billid |  | fbillid |

---

## 应收核销单-分表 t_ar_settlebill_e

- **表名称：** 应收核销单-分表
- **表名：** t_ar_settlebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 3 | fisperiodrecord | 初始化记录 | bpchar | 1 |  | √ | '0' | 初始化记录 |
| 4 | flocalsettletaxamt | 本次核销税额(本位币) | numeric | 23 | 10 | √ | 0 | 本次核销税额(本位币) |
| 5 | fsettletaxamt | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 6 | fmainbillsubentryid | 单据匹配分录id | int8 | 64 |  | √ | 0 | 单据匹配分录id |
| 7 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 8 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_settlebill_e |  | fid |
