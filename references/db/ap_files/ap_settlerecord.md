# 应付付款核销记录-ap_settlerecord

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

## 应付付款核销记录-反写记录表 t_ap_settlerecord_wb

- **表名称：** 应付付款核销记录-反写记录表
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

## 应付付款核销记录-主表 t_ap_settlerecord

- **表名称：** 应付付款核销记录-主表
- **表名：** t_ap_settlerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fisdiffcurrencysettle | 异币种核销 | bpchar | 1 |  | √ | '0' | 异币种核销 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 6 | fmainbillentity | 主方实体标识 | varchar | 50 |  | √ | ' ' | 主方实体标识 |
| 7 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 cas_paymentbilltype :付款类型 ar_payproperty :应收款项性质 cas_receivingbilltype :收款类型 |
| 9 | fsettlelogentryid | 核销日志分录id | int8 | 64 |  | √ | 0 | 核销日志分录id |
| 10 | freceivingtypeid | 主方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fmainbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 14 | fpaypropertyfield | 款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 15 | findepadjustexch | 独立调汇 | bpchar | 1 |  | √ | '0' | 独立调汇 |
| 16 | fbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 19 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 23 | fbillstatus | 核销记录状态 | varchar | 30 |  | √ | ' ' | 核销记录状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 25 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 28 | fsettleseq | 核销序号 | int8 | 64 |  | √ | 0 | 核销序号 |
| 29 | fautosettletype | 自动核销参数类型 | varchar | 30 |  | √ | '0' | 自动核销参数类型,枚举: 1 :BOTP自动核销 2 :核心单据号自动核销 3 :其它 4 :BOTP自动核销(断关系) 5 :付款退款 6 :收款退款 7 :按合同编号核销 |
| 30 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fiscreatesettlebill | 生成核销单 | bpchar | 1 |  | √ | ' ' | 生成核销单 |
| 32 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 35 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 36 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 37 | fasstreceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 38 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fiswrittenoff | 是否红冲生成 | bpchar | 1 |  | √ | '0' | 是否红冲生成 |
| 40 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 41 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 42 | flocaltotalsettleamt | 本次核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次核销金额(本位币) |
| 43 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 44 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fpayableamt | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 47 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 48 | fsettlebillid | 核销单id | int8 | 64 |  | √ | 0 | 核销单id |
| 49 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 manual :手工核销 match :方案匹配核销 import :引入核销 rpamatch :RPA方案核销 |
| 52 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 liqsettle :应付清理 paytrans :应付转销 payself :付款红蓝对冲 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 appaidsettle :采购期初预付 arapsettle :应收冲应付 recpaysettle :收款冲退款 arpaysettle :应收退款核销 payclearing :付款清理 payrefundclearing :付款退款清理 |
| 53 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 55 | fplanduedate | 计划到期日 | timestamp | 0 |  |  | null | 计划到期日 |
| 56 | ftotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次核销金额 |
| 57 | fbilltypenewid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 58 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | fmainbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 61 | fasstpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 62 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 63 | fmainasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 64 | fsettlebillno | 核销单单据编号 | varchar | 80 |  | √ | ' ' | 核销单单据编号 |
| 65 | fpaymenttypeid | 主方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 66 | fiscahsale | 现销现购 | bpchar | 1 |  | √ | ' ' | 现销现购 |
| 67 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 68 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 69 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 70 | fbilltype | 单据类型（旧） | varchar | 30 |  | √ | ' ' | 单据类型（旧）,枚举: purap :采购标准应付 feeap :费用采购应付 otherap :其他应付 borrowap :应付款项调整 purfeeap :费用应付 appay :采购付款 otherpay :其他付款 advpay :预付款 advrec :预收款 ApFin_service_BT_S :服务采购应付 SalesRec :销售收款 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 ap_finapbill_asset_BT_S :资产采购应付 ApFin_product_BT_S :产品委外应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sr_seq |  | fsettleseq |
| 2 | idx_ap_sr_logentry |  | fsettlelogentryid |
| 3 | idx_ap_sr_settlebillid |  | fsettlebillid |
| 4 | idx_ap_sr_orgdate |  | forgid,fsettledate |
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
| 2 | fsalesmanid | 辅方销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fisdiffcurrencysettle | 异币种核销 | bpchar | 1 |  | √ | '0' | 异币种核销 |
| 4 | fswappl | 辅方汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方汇兑损益 |
| 5 | fsettlelocalamt | 辅方本次核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 辅方本次核销金额(本位币) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpurdepartmentid | 辅方采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 ar_payproperty :应收款项性质 cas_receivingbilltype :收款类型 cas_paymentbilltype :付款类型 |
| 9 | freceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 10 | fexchangerate | 辅方汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方汇率 |
| 11 | fconbillnumber | 辅方合同编号 | varchar | 255 |  | √ | ' ' | 辅方合同编号 |
| 12 | fpaypropertyfield | 辅方款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 13 | fbillentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 14 | fexpenseitemid | 辅方费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 15 | fcostcenterid | fcostcenterid | int8 | 64 |  | √ | 0 |  |
| 16 | fpurorgid | 辅方采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 18 | fprojectid | 辅方项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | fmpmtasknoid | 辅方项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 20 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 21 | fdescription | 摘要 | varchar | 512 |  |  | null | 摘要 |
| 22 | fsalesorgid | 辅方销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 26 | flicenseno | 辅方许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 27 | fpurchaserid | 辅方采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 28 | fasstact | 辅方往来单位名称 | varchar | 255 |  | √ | ' ' | 辅方往来单位名称 |
| 29 | fmaterialid | 辅方物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 30 | fbilldate | 辅方业务日期 | timestamp | 0 |  |  | null | 辅方业务日期 |
| 31 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 32 | fsettleamt | 辅方本次核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方本次核销金额 |
| 33 | fpurdeptid | 辅方采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 34 | fbonded | 辅方保税 | bpchar | 1 |  | √ | '0' | 辅方保税 |
| 35 | fcorebillno | 辅方核心单据号 | varchar | 255 |  | √ | ' ' | 辅方核心单据号 |
| 36 | fquotation | 辅方换算方式 | varchar | 30 |  | √ | '0' | 辅方换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 37 | flocalsettletaxamt | 辅方本次核销税额(本位币) | numeric | 23 | 10 | √ | 0 | 辅方本次核销税额(本位币) |
| 38 | fbillnum | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 39 | fpayableamt | 辅方应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 辅方应付金额 |
| 40 | fbiztypeid | 辅方业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 41 | fbillsubentryid | 单据匹配分录id | int8 | 64 |  | √ | 0 | 单据匹配分录id |
| 42 | fsalesdeptid | 辅方销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fplanduedate | 辅方计划到期日 | timestamp | 0 |  |  | null | 辅方计划到期日 |
| 44 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 45 | fbilltypenewid | 辅方单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 46 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 47 | fsettletaxamt | 辅方本次核销税额 | numeric | 23 | 10 | √ | 0 | 辅方本次核销税额 |
| 48 | fpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 49 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | fsalesgroupid | 辅方销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 51 | fbilltype | 辅方单据类型（旧） | varchar | 30 |  | √ | ' ' | 辅方单据类型（旧）,枚举: purap :标准采购应付 feeap :费用采购应付 otherap :其他应付 appay :采购付款 paid :期初预付 liquidation :清理单 transpay :转付财务应付单 otherpay :其他付款 standard :标准销售应收 expense :销售费用应收 other :其他应收 borrowap :应付款项调整 borrowar :应付款项调整 purfeeap :费用应付 advpay :预付款 SalesRec :销售收款 OtherRec :其他收款 receivedbill :期初预收 advrec :预收款 ApFin_service_BT_S :服务采购应付 arfin_salefee_BT_S :销售费用应收 arfin_sersal_BT_S :服务销售应收 ap_finapbill_asset_BT_S :资产采购应付 ApFin_product_BT_S :产品委外应付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sre_billnum |  | fbillnum |
| 2 | idx_ap_sre_asstact |  | fasstactid |
| 3 | t_ap_settlerecordentry_pkey |  | fentryid |
| 4 | idx_ap_sre_idbillid |  | fid,fbillid |
| 5 | idx_ap_sre_pid |  | fid |
| 6 | idx_ap_sre_billid |  | fbillid |

---

## 应付付款核销记录-关联追踪表 t_ap_settlerecord_tc

- **表名称：** 应付付款核销记录-关联追踪表
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

---

## 应付付款核销记录-分表 t_ap_settlerecord_e

- **表名称：** 应付付款核销记录-分表
- **表名：** t_ap_settlerecord_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 3 | fisperiodrecord | 初始化记录 | bpchar | 1 |  | √ | '0' | 初始化记录 |
| 4 | flocalsettletaxamt | 本次核销税额(本位币) | numeric | 23 | 10 | √ | 0 | 本次核销税额(本位币) |
| 5 | fsettletaxamt | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 6 | fmainbillsubentryid | 单据匹配分录id | int8 | 64 |  | √ | 0 | 单据匹配分录id |
| 7 | fiswrittenoffred | 冲销生成 | bpchar | 1 |  | √ | '0' | 冲销生成 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_settlerecord_e |  | fid |
