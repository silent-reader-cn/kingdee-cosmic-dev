# 财务应收单-ar_finarbill

## 明细-子表 t_ar_finarbillentry

- **表名称：** 明细-子表
- **表名：** t_ar_finarbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_bj73_basedatafield | 物料分类 | int8 | 64 |  |  | null | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 9 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 10 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 12 | fsettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 13 | fdelivercustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 14 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 ec_incomeapply :请款单 pm_purorderbill :采购订单 im_transapply :调拨申请单 amccsa_custschdorder :销售计划协议 amccsa_custschdorder_init :期初销售计划协议 |
| 15 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 19 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 20 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 21 | facttaxunitprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 22 | funconfirmamt | 未确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未确认金额 |
| 23 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 24 | funsettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 25 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 26 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 27 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 28 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 31 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 32 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 35 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 36 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 37 | fsrcid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 38 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 39 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 40 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 41 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 42 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 43 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 44 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 45 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 46 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 47 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | funconfirmqty | 未确认数量 | numeric | 23 | 10 | √ | 0 | 未确认数量 |
| 51 | funverifyamt | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 52 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 54 | fsettledlocalamt | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 55 | fconfirmedqty | 已确认数量 | numeric | 23 | 10 | √ | 0 | 已确认数量 |
| 56 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 57 | funsettlelocalamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 58 | factunitprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 59 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 60 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 62 | fconfirmedamt | 已确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认金额 |
| 63 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 64 | fverifiedqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 65 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 66 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 67 | finvoicecustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 68 | fspectype | 规格型号 | varchar | 512 |  | √ | ' ' | 规格型号 |
| 69 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 70 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位转换系数 |
| 71 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 72 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 73 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 74 | fverifiedamt | 已勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_find_sourcebillid |  | fsrcid |
| 2 | idx_ar_find_pid |  | fid |
| 3 | idx_ar_fine_corebill |  | fcorebillno,fcorebillentryseq |
| 4 | t_ar_finarbillentry_pkey |  | fentryid |
| 5 | idx_ar_find_srcentryid |  | fsrcentryid |
| 6 | idx_ar_find_unsettle |  | funsettleamt |

---

## 预收信息-子表 t_ar_finarpreentry

- **表名称：** 预收信息-子表
- **表名：** t_ar_finarpreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillid | 预收款单id | int8 | 64 |  | √ | 0 | 预收款单id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillno | 预收款单 | varchar | 80 |  | √ | ' ' | 预收款单 |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: cas_recbill :收款单 ar_receivedbill :初始化预收单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_finarpreentry |  | fentryid |
| 2 | idx_ar_pre_pid |  | fid |
| 3 | idx_ar_pre_recid |  | fbillid |

---

## 关联子实体-子表 t_ar_finarbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_finarbill_lk

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
| 1 | idx_ar_finarbill_lk_fk |  | fid |
| 2 | t_ar_finarbill_lk_pkey |  | fpkid |

---

## 财务应收单-主表 t_ar_finarbill

- **表名称：** 财务应收单-主表
- **表名：** t_ar_finarbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsplitscheme | 拆分口径 | int8 | 64 |  | √ | 0 | [收款计划方案 ar_plansplit_scheme](../ar_files/ar_plansplit_scheme.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 9 | funsettleamount | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 10 | fbaddebtamt | 坏账金额 | numeric | 23 | 10 | √ | 0.0000000000 | 坏账金额 |
| 11 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 12 | fpaymentcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 13 | fsourcebillno | 源单编码（废弃） | varchar | 255 |  | √ | ' ' | 源单编码（废弃） |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_invoice :增值税发票 ar_finarbill :财务应收单 ap_finapbill :财务应付单 im_saloutbill :销售出库单 ar_busbill :暂估应收单 cas_paybill :付款单 cas_agentpaybill :代发单 conm_salcontract :销售合同 sm_salorder :销售订单 ism_arsettlebill :应收结算清单 mpm_projinvapply :项目开票申请单 fa_clearbill :资产清理单 im_mdc_exconsume :委外超耗单 plat_taxexpense :供应链费用单 ocmem_mc_reimburse :营销费用核销单 occpic_rebatestatement :返利结算单 mpm_projsaleconf :项目销售服务确认单 |
| 16 | fhadwrittenoff | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 20 | fistransfer | 转销生成 | bpchar | 1 |  | √ | '0' | 转销生成 |
| 21 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 22 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 26 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 27 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fiswrittenoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 32 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 33 | fsettlestatus | 核销状态 | varchar | 30 |  | √ | ' ' | 核销状态,枚举: unsettle :未核销 partsettle :部分核销 settled :全部核销 |
| 34 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 35 | fk_bj73_textfield2 | 考核大区 | varchar | 50 |  | √ | ' ' | 考核大区 |
| 36 | fk_bj73_textfield1 | 考核省区 | varchar | 50 |  | √ | ' ' | 考核省区 |
| 37 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 38 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 41 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | [应收款项性质 ar_payproperty](../ar_files/ar_payproperty.md) |
| 42 | fadjusttype | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: buckle :扣罚款 rebate :返利折扣 adjustinv :调整发票尾差 overdue :逾期利息 |
| 43 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 44 | fisbaddebt | 坏账 | bpchar | 1 |  | √ | '0' | 坏账 |
| 45 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 46 | funsettlelocalamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 47 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 48 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 53 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fpaycond | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 55 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 56 | fduedate | 最后到期日 | timestamp | 0 |  |  | null | 最后到期日 |
| 57 | fpaymode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 58 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 61 | frecorgid | 收款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 63 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 64 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 65 | fk_bj73_textareafield | 实际发票号 | varchar | 500 |  | √ | ' ' | 实际发票号 |
| 66 | fk_bj73_textfield | fk_bj73_textfield | varchar | 50 |  | √ | ' ' |  |
| 67 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 68 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 69 | fverifystatus | 勾稽状态 | varchar | 30 |  | √ | ' ' | 勾稽状态,枚举: unverify :未勾稽 partverify :部分勾稽 verified :全部勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_fin_bizdate_billno |  | fbizdate,fbillno |
| 2 | t_ar_finarbill_pkey |  | fid |
| 3 | idx_ar_fin_sourcebillid |  | fsourcebillid |
| 4 | idx_ar_fin_createtime |  | fcreatetime,fisvoucher |
| 5 | idx_ar_fin_bizdate |  | fbizdate |
| 6 | idx_ar_fin_asstact |  | fasstactid |
| 7 | idx_ar_fin_orgdate |  | forgid,fbizdate |
| 8 | idx_ar_fin_fbillno |  | fbillno |

---

## 关联子实体-子表 t_ar_finarplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_finarplanentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_finarplanentry_lk_fk |  | fentryid |
| 2 | pk_ar_finarplanentry_lk |  | fpkid |

---

## 子单据体-子表 t_ar_finarbilltaxsubentry

- **表名称：** 子单据体-子表
- **表名：** t_ar_finarbilltaxsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustmanually | 手工调整 | bpchar | 1 |  | √ | '0' | 手工调整 |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | ftaxloc | 税额（本位币） | numeric | 23 | 10 | √ | 0 | 税额（本位币） |
| 7 | ftaxcode | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 12 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_finarbilltaxsubentry |  | fdetailid |
| 2 | idx_ar_fintaxsub_entryid |  | fentryid |

---

## 收款计划-子表 t_ar_finarplanentry

- **表名称：** 收款计划-子表
- **表名：** t_ar_finarplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fplancorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 4 | fplanpricetaxlocal | 应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额(本位币) |
| 5 | fplanpricerate | 应收比例(%) | numeric | 23 | 10 | √ | 0 | 应收比例(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fplansettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsrcfinid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 11 | fplanbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | funplansettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fplancorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 ec_incomeapply :请款单 pm_purorderbill :采购订单 im_transapply :调拨申请单 amccsa_custschdorder :销售计划协议 amccsa_custschdorder_init :期初销售计划协议 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 17 | fplanremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fplancorebillentryseq | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 19 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 20 | fplanlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 21 | funplanlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 22 | fplanpricetax | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 23 | fplansettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 24 | fplansettledlocamt | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 25 | fsrcplanentryid | 源单收款计划id | int8 | 64 |  | √ | 0 | 源单收款计划id |
| 26 | fplanlockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 27 | fplancontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 28 | fplanmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 29 | funplansettlelocamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 30 | fplanproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fplanexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_finplan_duedate |  | fplanduedate |
| 2 | idx_ar_finplan_srcfinid |  | fsrcfinid |
| 3 | idx_ar_finplan_srcplanentryid |  | fsrcplanentryid |
| 4 | index_finar_plan |  | fid |
| 5 | t_ar_finarplanentry_pkey |  | fentryid |

---

## 明细-分表 t_ar_finarbillentry_e

- **表名称：** 明细-分表
- **表名：** t_ar_finarbillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | finvdifftax | 发票尾差税额 | numeric | 23 | 10 | √ | 0 | 发票尾差税额 |
| 5 | frectax | 收款时点税额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 收款时点税额(废弃) |
| 6 | fissueinvlocalamt | 已开票金额(不含税本位币) | numeric | 23 | 10 | √ | 0 | 已开票金额(不含税本位币) |
| 7 | finvoicedamt | 已关联销售发票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联销售发票价税合计 |
| 8 | fadjinvdiffamt | 已调整发票尾差金额 | numeric | 23 | 10 | √ | 0 | 已调整发票尾差金额 |
| 9 | funinvoicedamt | 未关联销售发票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联销售发票价税合计 |
| 10 | fisallverify | 完全勾稽 | bpchar | 1 |  | √ | '0' | 完全勾稽 |
| 11 | funconfirmbaseqty | 未确认基本数量 | numeric | 23 | 10 | √ | 0 | 未确认基本数量 |
| 12 | fwoffqty | 已冲回数量 | numeric | 23 | 10 | √ | 0 | 已冲回数量 |
| 13 | fissueinvtax | 已开票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票税额 |
| 14 | fsrcbillentryseq | 源单单据行号 | varchar | 2000 |  |  | ' ' | 源单单据行号 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | finvoicecode | 发票代码 | varchar | 2048 |  | √ | ' ' | 发票代码 |
| 17 | finvoicedlocalamt | 已关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联销售发票价税合计(本位币) |
| 18 | fissueinvqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 19 | funinvoicedqty | 未关联销售发票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联销售发票数量 |
| 20 | finvoiceno | 发票号码 | varchar | 2048 |  | √ | ' ' | 发票号码 |
| 21 | finvdifflocalamt | 发票尾差金额(本位币) | numeric | 23 | 10 | √ | 0 | 发票尾差金额(本位币) |
| 22 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  |  | ' ' | 尾差调整日志 |
| 23 | fwoffbaseqty | 已冲回基本数量 | numeric | 23 | 10 | √ | 0 | 已冲回基本数量 |
| 24 | fe_iv_saleid | 关联销售发票内码 | int8 | 64 |  | √ | 0 | 关联销售发票内码 |
| 25 | finvdiffamt | 发票尾差金额 | numeric | 23 | 10 | √ | 0 | 发票尾差金额 |
| 26 | fe_iv_sale_entryid | 关联发票分录ID | int8 | 64 |  | √ | 0 | 关联发票分录ID |
| 27 | fwofftotallocalamt | 已冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已冲回价税合计(本位币) |
| 28 | fissueinvamt | 已开票金额(不含税) | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额(不含税) |
| 29 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 3 :仅退款不退货 |
| 30 | finvoicedqty | 已关联销售发票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联销售发票数量 |
| 31 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 32 | fallbussettle | 完全暂估核销 | bpchar | 1 |  | √ | '0' | 完全暂估核销 |
| 33 | fconfirmedbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0 | 已确认基本数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fwofflocalamt | 已冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 已冲回金额(本位币) |
| 36 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 37 | fsrcbillno | 源单单据编号 | varchar | 2000 |  |  | ' ' | 源单单据编号 |
| 38 | fissueinvreclocalamt | 已开票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已开票价税合计(本位币) |
| 39 | fisinvoicefirst | 先开票 | bpchar | 1 |  | √ | '0' | 先开票 |
| 40 | fadjinvdifftaxlocamt | 已调整发票尾差税额(本位币) | numeric | 23 | 10 | √ | 0 | 已调整发票尾差税额(本位币) |
| 41 | fadjinvdifflocalamt | 已调整发票尾差金额(本位币) | numeric | 23 | 10 | √ | 0 | 已调整发票尾差金额(本位币) |
| 42 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 43 | fissueinvrecamt | 已开票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票价税合计 |
| 44 | funinvoicedlocalamt | 未关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联销售发票价税合计(本位币) |
| 45 | fwofftotalamt | 已冲回价税合计 | numeric | 23 | 10 | √ | 0 | 已冲回价税合计 |
| 46 | fe_invoicedbaseqty | 已关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 已关联销售发票基本数量 |
| 47 | fissueinvlocaltax | 已开票税额(本位币) | numeric | 23 | 10 | √ | 0 | 已开票税额(本位币) |
| 48 | fadjinvdifftax | 已调整发票尾差税额 | numeric | 23 | 10 | √ | 0 | 已调整发票尾差税额 |
| 49 | fe_uninvoicedbaseqty | 未关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 未关联销售发票基本数量 |
| 50 | finvdifftaxlocamt | 发票尾差税额(本位币) | numeric | 23 | 10 | √ | 0 | 发票尾差税额(本位币) |
| 51 | fvattax | 增值税(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 增值税(废弃) |
| 52 | fcostlocalamt | 成本金额(本位币) | numeric | 23 | 10 | √ | 0 | 成本金额(本位币) |
| 53 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 54 | fwoffamt | 已冲回金额 | numeric | 23 | 10 | √ | 0 | 已冲回金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_iv_enid |  | fe_iv_sale_entryid |
| 2 | idx_ar_finentry_e_fid |  | fid |
| 3 | t_ar_finarbillentry_e_pkey |  | fentryid |
| 4 | idx_ar_fin_vattax |  | fvattax |

---

## 财务应收单-分表 t_ar_finarbill_e

- **表名称：** 财务应收单-分表
- **表名：** t_ar_finarbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwritebackbill | 反写单据 | bpchar | 1 |  | √ | '0' | 反写单据 |
| 3 | fwoffsourcebilltype | 冲销源单类型(废弃) | varchar | 30 |  | √ | ' ' | 冲销源单类型(废弃),枚举: |
| 4 | fissueinvreclocalamt | 已开票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已开票价税合计(本位币) |
| 5 | fsrcasstactid | 源单往来单位（转销） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | finvoicedamt | 已关联销售发票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联销售发票价税合计 |
| 7 | fivsale_create_flag | 发票关联生成 | bpchar | 1 |  | √ | '0' | 发票关联生成 |
| 8 | fprojectnumid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 9 | fispremium | 是否质保金 | bpchar | 1 |  | √ | '0' | 是否质保金 |
| 10 | fsettlelocalamt | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 11 | funinvoicedamt | 未关联销售发票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联销售发票价税合计 |
| 12 | facctagecalcdate | 账龄起算日 | timestamp | 0 |  |  | null | 账龄起算日 |
| 13 | fissueinvrecamt | 已开票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票价税合计 |
| 14 | funinvoicedlocalamt | 未关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联销售发票价税合计(本位币) |
| 15 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 16 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 17 | finvoicecode | 发票代码 | varchar | 2048 |  | √ | ' ' | 发票代码 |
| 18 | finvoicedlocalamt | 已关联销售发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联销售发票价税合计(本位币) |
| 19 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 20 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 21 | finvctrlmode | 项目开票控制方式 | varchar | 30 |  | √ | ' ' | 项目开票控制方式,枚举: A :按数量控制 B :按金额控制 |
| 22 | fisscmcexpense | 供应链费用 | bpchar | 1 |  | √ | '0' | 供应链费用 |
| 23 | fsettleamount | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 24 | finvoiceno | 发票号码 | varchar | 2048 |  | √ | ' ' | 发票号码 |
| 25 | frelationpay | 关联交易 | bpchar | 1 |  | √ | ' ' | 关联交易 |
| 26 | fpremiumamt | 质保金金额 | numeric | 23 | 10 | √ | 0 | 质保金金额 |
| 27 | fnotsplitbycon | 合同编号非默认维度 | bpchar | 1 |  | √ | '0' | 合同编号非默认维度 |
| 28 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从总账引入 |
| 29 | fbaddebtcause | 坏账原因 | varchar | 30 |  | √ | ' ' | 坏账原因,枚举: overdue :逾期未还并明显超过规定账龄 bankrupt :债务人破产和死亡 other :其他原因 |
| 30 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 31 | fisintertax | 国际税(废弃) | bpchar | 1 |  | √ | '0' | 国际税(废弃) |
| 32 | fpremiumrate | 质保金比例(%) | numeric | 23 | 10 | √ | 0 | 质保金比例(%) |
| 33 | fsourcebiztype | 源单业务类型 | varchar | 255 |  | √ | ' ' | 源单业务类型 |
| 34 | fsettlerelations | 组织间结算 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 35 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 36 | fdepartmentid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | ftaxroundrule | 先舍入后汇总(废弃) | bpchar | 1 |  | √ | '0' | 先舍入后汇总(废弃) |
| 38 | fpremduedate | 质保金到期日 | timestamp | 0 |  |  | null | 质保金到期日 |
| 39 | ftransway | 转销版本 | varchar | 30 |  | √ | ' ' | 转销版本,枚举: normal :普通单据 trans_old :旧转销 trans_new :新转销 |
| 40 | finvoiceadjust | 发票云尾差生成调整单 | bpchar | 1 |  | √ | '0' | 发票云尾差生成调整单 |
| 41 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 42 | ftranstype | 转销单据类型 | varchar | 30 |  | √ | ' ' | 转销单据类型,枚举: normal :普通单据 trans_red :新转销生成的红单 trans_blue :新转销生成的蓝单 |
| 43 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 44 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 45 | fiswoffbyqty | 按数量冲回 | bpchar | 1 |  | √ | '0' | 按数量冲回 |
| 46 | fisplansplit | 计划按分组方案生成 | bpchar | 1 |  | √ | '1' | 计划按分组方案生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_finarbill_e_pkey |  | fid |
| 2 | idx_ar_fin_e_cause |  | fbaddebtcause |

---

## 财务应收单-关联追踪表 t_ar_finarbill_tc

- **表名称：** 财务应收单-关联追踪表
- **表名：** t_ar_finarbill_tc

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
| 1 | idx_ar_finarbill_tc_tid |  | ftid |
| 2 | t_ar_finarbill_tc_pkey |  | fid |
| 3 | idx_ar_finarbill_tc_tbill |  | ftbillid |

---

## 开票结果详情-子表 t_ar_finarbill_inv_entry

- **表名称：** 开票结果详情-子表
- **表名：** t_ar_finarbill_inv_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpre_blue_number | 原蓝字发票号码 | varchar | 80 |  | √ | ' ' | 原蓝字发票号码 |
| 3 | fred_blue | 红蓝字 | bpchar | 1 |  | √ | '0' | 红蓝字,枚举: 0 :蓝票 1 :红票 |
| 4 | finvoice_code | 发票代码 | varchar | 80 |  | √ | ' ' | 发票代码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | ffile_addr | 版式文件地址 | varchar | 255 |  | √ | ' ' | 版式文件地址 |
| 8 | finvoice_status | 发票状态 | varchar | 30 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 |
| 9 | finvoice_number | 发票号码 | varchar | 80 |  | √ | ' ' | 发票号码 |
| 10 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 11 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 12 | finvoiceid | finvoiceid | int8 | 64 |  | √ | 0 | id |
| 13 | fivdate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 14 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 15 | fidentification | 清单标识 | bpchar | 1 |  | √ | '1' | 清单标识,枚举: 1 :清单 0 :非清单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | finvoiceid | finvoiceid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_finarbill_inv_entry |  | finvoiceid |
| 2 | idx_inv_code_num_uni |  | fid,finvoice_code,finvoice_number |

---

## 子单据体-子表 t_ar_finarbilltaxentry

- **表名称：** 子单据体-子表
- **表名：** t_ar_finarbilltaxentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 2 | fincludediscount | 含折扣(废弃) | bpchar | 1 |  | √ | ' ' | 含折扣(废弃) |
| 3 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdiscountamt | fdiscountamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | ftaxbase | 税控金额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 税控金额(废弃) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaxassessamt | 评估计税金额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 评估计税金额(废弃) |
| 9 | ftaxbasetype | 税基类型(废弃) | bpchar | 1 |  | √ | ' ' | 税基类型(废弃),枚举: 1 :不含税金额 2 :含税金额 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fincludevat | 含增值税(废弃) | bpchar | 1 |  | √ | ' ' | 含增值税(废弃) |
| 12 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fisinpricetax | 价内税(废弃) | bpchar | 1 |  | √ | ' ' | 价内税(废弃) |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fisoffset | 抵消标识 | bpchar | 1 |  | √ | '0' | 抵消标识 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnondeductible | 不可抵扣额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 不可抵扣额(废弃) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fincludetail | 含尾款(废弃) | bpchar | 1 |  | √ | ' ' | 含尾款(废弃) |
| 21 | ftaxtime | 计税时点(废弃) | varchar | 255 |  | √ | ' ' | 计税时点(废弃),枚举: invoice :开票时点 receipt :收款时点 |
| 22 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fdeductible | 抵扣额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣额(废弃) |
| 25 | fdeductionrate | 抵扣率(%)(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣率(%)(废弃) |
| 26 | fisoutputtax | 销项税(废弃) | bpchar | 1 |  | √ | ' ' | 销项税(废弃) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fcandeductible | 可抵扣(废弃) | bpchar | 1 |  | √ | ' ' | 可抵扣(废弃) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_finarbilltaxentry_pkey |  | fdetailid |
| 2 | idx_ar_fintaxe_pid |  | fentryid |

---

## 财务应收单-反写记录表 t_ar_finarbill_wb

- **表名称：** 财务应收单-反写记录表
- **表名：** t_ar_finarbill_wb

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
| 1 | t_ar_finarbill_wb_pkey |  | fentryid |
| 2 | idx_ar_finarbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_ar_finarbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_finarbillentry_lk

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
| 1 | idx_ar_finarbillentry_lk_fk |  | fentryid |
| 2 | t_ar_finarbillentry_lk_pkey |  | fpkid |
