# 财务应付单-ap_finapbill

## 关联子实体-子表 t_ap_finapbilldetailentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_finapbilldetailentry_lk

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
| 1 | t_ap_finapbilldetailentry_lk_pkey |  | fpkid |
| 2 | idx_ap_finapbillentry_lk_fk |  | fentryid |
| 3 | idx_finentry_lk_fentryid |  | fentryid |

---

## 财务应付单-反写记录表 t_ap_finapbill_wb

- **表名称：** 财务应付单-反写记录表
- **表名：** t_ap_finapbill_wb

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
| 1 | t_ap_finapbill_wb_pkey |  | fentryid |
| 2 | idx_ap_finapbill_wb_fk |  | fid |

---

## 预付信息-子表 t_ap_finappreentry

- **表名称：** 预付信息-子表
- **表名：** t_ap_finappreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillid | 预付款单id | int8 | 64 |  | √ | 0 | 预付款单id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbillno | 预付款单 | varchar | 80 |  | √ | ' ' | 预付款单 |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: cas_paybill :付款单 ap_paidbill :初始化预付单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_finappreentry |  | fentryid |
| 2 | idx_ap_pre_pid |  | fid |
| 3 | idx_ap_pre_payid |  | fbillid |

---

## 财务应付单-主表 t_ap_finapbill

- **表名称：** 财务应付单-主表
- **表名：** t_ap_finapbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsplitscheme | 拆分口径 | int8 | 64 |  | √ | 0 | [付款计划方案 ap_plansplit_scheme](../ap_files/ap_plansplit_scheme.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fistaxdeduction | 税额不计入成本 | bpchar | 1 |  | √ | '0' | 税额不计入成本 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | funsettleamount | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 10 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 11 | fpurmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 12 | freceivingsupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fisinvoicematch | 是否匹配生成 | bpchar | 1 |  | √ | ' ' | 是否匹配生成 |
| 14 | fsourcebillno | 源单编码（废弃） | varchar | 255 |  | √ | ' ' | 源单编码（废弃） |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | frelationpay | 关联交易 | bpchar | 1 |  | √ | ' ' | 关联交易 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_invoice :收票单 ap_finapbill :财务应付单 ar_finarbill :财务应收单 im_purinbill :采购入库单 pm_purorderbill :采购订单 im_purreturnbill :采购退货单 ap_busbill :暂估应付单 im_purreceivebill :收料通知单 conm_purcontract :采购合同 pm_om_purorderbill :简单委外订单 im_mdc_omcmplinbill :委外完工入库单 pm_puracceptbill :采购验收单 im_mdc_ominbill :简单委外入库单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 ism_apsettlebill :应付结算清单 sfc_processsettlebill :工序结算单 mpm_projpurchaseconf :项目采购服务确认单 plat_taxexpense :供应链费用单 occpic_supbgt :采购返利结算单 er_publicreimbursebill :对公报销单 |
| 19 | fhadwrittenoff | 已被冲销 | bpchar | 1 |  | √ | ' ' | 已被冲销 |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 23 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 24 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 25 | finvoicebiztypeid | 发票类别 | int8 | 64 |  | √ | 0 | [发票业务类别 bd_invoicebiztype](../basedata_files/bd_invoicebiztype.md) |
| 26 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 28 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 29 | fk_bj73_assistantfield | 其他应付类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 30 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fisperiod | 是否期初 | bpchar | 1 |  | √ | ' ' | 是否期初 |
| 33 | fk_bj73_fyxm | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 35 | fpurchaserid | fpurchaserid | int8 | 64 |  | √ | 0 |  |
| 36 | fiswrittenoff | 冲销单据 | bpchar | 1 |  | √ | ' ' | 冲销单据 |
| 37 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 38 | fsettlestatus | 核销状态 | varchar | 30 |  | √ | ' ' | 核销状态,枚举: unsettle :未核销 partsettle :部分核销 settled :全部核销 |
| 39 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 40 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 41 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 42 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 45 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | [应付款项性质 ap_payproperty](../ap_files/ap_payproperty.md) |
| 46 | fadjusttype | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: buckle :扣罚款 rebate :返利折扣 adjustinv :调整发票尾差 overdue :逾期利息 invdiff :发票差异 |
| 47 | fisarchive | 是否归档 | bpchar | 1 |  | √ | ' ' | 是否归档 |
| 48 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 49 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 50 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 55 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fdepartmentid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 59 | fduedate | 最后到期日 | timestamp | 0 |  |  | null | 最后到期日 |
| 60 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 61 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 62 | funsettleamountbase | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 63 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 64 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 65 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 66 | fk_bj73_textareafield | 实际发票号码 | varchar | 500 |  | √ | ' ' | 实际发票号码 |
| 67 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 68 | fistanspay | 转销生成 | bpchar | 1 |  | √ | ' ' | 转销生成 |
| 69 | fverifystatus | 勾稽状态 | varchar | 30 |  | √ | ' ' | 勾稽状态,枚举: 10 :未勾稽 20 :部分勾稽 30 :全部勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fin_asstact |  | fasstactid |
| 2 | idx_ap_fin_orgdate |  | forgid,fbizdate |
| 3 | idx_ap_fin_sourcebillid |  | fsourcebillid |
| 4 | t_ap_finapbill_pkey |  | fid |
| 5 | idx_ap_fin_bizdate_billno |  | fbizdate,fbillno |
| 6 | idx_ap_fin_bizdate |  | fbizdate |
| 7 | idx_ap_fin_billno |  | fbillno |

---

## 费用分摊-子表 t_ap_finapbillallocentry

- **表名称：** 费用分摊-子表
- **表名：** t_ap_finapbillallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 6 | fallocationamt | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 7 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fallocationper | 分配比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 分配比例(%) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_finapbillallocentry_pkey |  | fentryid |
| 2 | idx_ap_finalloc_fid |  | fid |

---

## 财务应付单-关联追踪表 t_ap_finapbill_tc

- **表名称：** 财务应付单-关联追踪表
- **表名：** t_ap_finapbill_tc

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
| 1 | t_ap_finapbill_tc_pkey |  | fid |
| 2 | idx_ap_finapbill_tc_tbill |  | ftbillid |
| 3 | idx_ap_finapbill_tc_tid |  | ftid |

---

## 资产采购费用分摊卡片信息-子表 t_ap_finapbillentryasset

- **表名称：** 资产采购费用分摊卡片信息-子表
- **表名：** t_ap_finapbillentryasset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fassetcardid | 资产卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_finapbillentryasset |  | fdetailid |
| 2 | idx_ap_finapbillentryasset_entryid |  | fentryid |

---

## 子单据体-子表 t_ap_finapbilltaxentry

- **表名称：** 子单据体-子表
- **表名：** t_ap_finapbilltaxentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 2 | fincludediscount | 含折扣 | bpchar | 1 |  | √ | ' ' | 含折扣 |
| 3 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdiscountamt | fdiscountamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | ftaxbase | 税控金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税控金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftaxassessamt | 计税评估金额 | numeric | 23 | 10 | √ | 0.0000000000 | 计税评估金额 |
| 9 | ftaxbasetype | 税基类型 | bpchar | 1 |  | √ | ' ' | 税基类型,枚举: 1 :不含税金额 2 :含税金额 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fincludevat | 含增值税 | bpchar | 1 |  | √ | ' ' | 含增值税 |
| 12 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fisinpricetax | 价内税 | bpchar | 1 |  | √ | ' ' | 价内税 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fisoffset | 抵消标识 | bpchar | 1 |  | √ | '0' | 抵消标识 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fnondeductible | 不可抵扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 不可抵扣额 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fincludetail | 含尾款 | bpchar | 1 |  | √ | ' ' | 含尾款 |
| 21 | ftaxtime | 计税时点 | varchar | 255 |  | √ | ' ' | 计税时点,枚举: invoice :开票时点 pay :付款时点 |
| 22 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fdeductible | 抵扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣额 |
| 25 | fisinputtax | 进项税 | bpchar | 1 |  | √ | ' ' | 进项税 |
| 26 | fdeductionrate | 抵扣率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣率(%) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fcandeductible | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_finapbilltaxentry_pkey |  | fdetailid |
| 2 | idx_ar_finaptaxe_pid |  | fentryid |

---

## 明细-分表 t_ap_finapbilldetailentry_f

- **表名称：** 明细-分表
- **表名：** t_ap_finapbilldetailentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallocatedlocalamt | 存货已分摊金额(本位币) | numeric | 23 | 10 | √ | 0 | 存货已分摊金额(本位币) |
| 3 | funittax | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 4 | fallocatedtotal | 存货已分摊价税合计 | numeric | 23 | 10 | √ | 0 | 存货已分摊价税合计 |
| 5 | flinktaxrateid | 环节税税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 6 | fprocureinventorybillid | 采购库存单据号 | varchar | 2000 |  | √ | ' ' | 采购库存单据号 |
| 7 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0 | 未勾稽基本数量 |
| 8 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0 | 已勾稽基本数量 |
| 9 | fundertaketype | 承担类型 | varchar | 30 |  | √ | ' ' | 承担类型,枚举: 1 :企业承担 2 :企业代垫 3 :客户承担 |
| 10 | funallocatedlocalamt | funallocatedlocalamt | numeric | 23 | 10 | √ | 0 |  |
| 11 | ftaxunitid | 计税单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | ftaxqty | 计税数量 | numeric | 23 | 10 | √ | 0 | 计税数量 |
| 13 | fdutypaidamout | 完税价格 | numeric | 23 | 10 | √ | 0 | 完税价格 |
| 14 | fallocatedamt | 存货已分摊金额 | numeric | 23 | 10 | √ | 0 | 存货已分摊金额 |
| 15 | foutreturnbillid | 委外完工退库单 | varchar | 2000 |  | √ | ' ' | 委外完工退库单 |
| 16 | fallocatedlocaltotal | 存货已分摊价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 存货已分摊价税合计(本位币) |
| 17 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 18 | fbaseunittax | 基本单位税额 | numeric | 23 | 10 | √ | 0 | 基本单位税额 |
| 19 | flinktaxrate | 环节税税率(%) | numeric | 23 | 10 | √ | 0 | 环节税税率(%) |
| 20 | foutinventorybillid | 委外完工入库单 | varchar | 2000 |  | √ | ' ' | 委外完工入库单 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fsaleinventorybillid | 销售库存单据号 | varchar | 2000 |  | √ | ' ' | 销售库存单据号 |
| 23 | fwoffbaseqty | 已冲回基本数量 | numeric | 23 | 10 | √ | 0 | 已冲回基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_finapbilldetailentry_f |  | fentryid |
| 2 | idx_ap_fin_entryf_fid |  | fid |

---

## 明细-分表 t_ap_finapbilldetailentry_e

- **表名称：** 明细-分表
- **表名：** t_ap_finapbilldetailentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettleinvloctax | 已核销采购发票税额(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票税额(本位币) |
| 3 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 4 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 5 | fpaytax | 付款时点税额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 付款时点税额(废弃) |
| 6 | funsettleinvpricetax | 未核销采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未核销采购发票价税合计 |
| 7 | funsettleinvlocpricetax | 未核销采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票价税合计(本位币) |
| 8 | finvoicedamt | 已收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 已收票价税合计（废弃） |
| 9 | funinvoicedamt | 未收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 未收票价税合计（废弃） |
| 10 | fpurinbillno | fpurinbillno | varchar | 50 |  | √ | ' ' |  |
| 11 | funsettleinvtax | 未核销采购发票税额 | numeric | 23 | 10 | √ | 0 | 未核销采购发票税额 |
| 12 | fisallverify | 完全勾稽 | bpchar | 1 |  | √ | '0' | 完全勾稽 |
| 13 | finvbiztype | 关联业务单据业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | funsettleinvloctax | 未核销采购发票税额(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票税额(本位币) |
| 15 | fsrcbillentryseq | 源单单据行号 | varchar | 2000 |  |  | ' ' | 源单单据行号 |
| 16 | funsettleinvbaseqty | 未核销采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 未核销采购发票基本数量 |
| 17 | fpurreceivebillentryid | fpurreceivebillentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fworkn | 生产工单号（废弃） | varchar | 50 |  | √ | ' ' | 生产工单号（废弃） |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fe_uninvoicedamount | 未关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计 |
| 21 | fisgetinvoice | 先到票 | bpchar | 1 |  | √ | '0' | 先到票 |
| 22 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  |  | ' ' | 尾差调整日志 |
| 23 | fscmentryid | 供应链单据分录ID | int8 | 64 |  | √ | 0 | 供应链单据分录ID |
| 24 | fe_iv_purid | 关联采购发票内码 | int8 | 64 |  | √ | 0 | 关联采购发票内码 |
| 25 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 26 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 27 | fsettleinvlocamt | 已核销采购发票金额(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票金额(本位币) |
| 28 | fworkrown | 工单行号（废弃） | int8 | 64 |  | √ | 0 | 工单行号（废弃） |
| 29 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 30 | funsettleinvlocamt | 未核销采购发票金额(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票金额(本位币) |
| 31 | fe_uninvoiceqty | 未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 未关联采购发票数量 |
| 32 | fpurreceivebillid | fpurreceivebillid | int8 | 64 |  | √ | 0 |  |
| 33 | fsettleinvlocpricetax | 已核销采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票价税合计(本位币) |
| 34 | fallbussettle | 完全暂估核销 | bpchar | 1 |  | √ | '0' | 完全暂估核销 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | funsettleinvamount | 未核销采购发票金额 | numeric | 23 | 10 | √ | 0 | 未核销采购发票金额 |
| 37 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 38 | fsrcbillno | 源单单据编号 | varchar | 2000 |  |  | ' ' | 源单单据编号 |
| 39 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 40 | fsettleinvtax | 已核销采购发票税额 | numeric | 23 | 10 | √ | 0 | 已核销采购发票税额 |
| 41 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 42 | fdepartid | 生产车间（废弃） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fwofftotalamt | 已冲回价税合计 | numeric | 23 | 10 | √ | 0 | 已冲回价税合计 |
| 44 | fe_uninvoicedlocamt | 未关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计(本位币) |
| 45 | fsettleinvamount | 已核销采购发票金额 | numeric | 23 | 10 | √ | 0 | 已核销采购发票金额 |
| 46 | fe_iv_create_qty | 发票关联生成数量 | numeric | 23 | 10 | √ | 0 | 发票关联生成数量 |
| 47 | fe_invoicedbaseqty | 已关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 已关联采购发票基本数量 |
| 48 | fe_invoicedamount | 已关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计 |
| 49 | fpurreceivebillentryseq | fpurreceivebillentryseq | int8 | 64 |  | √ | 0 |  |
| 50 | fe_uninvoicedbaseqty | 未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 未关联采购发票基本数量 |
| 51 | fsettleinvpricetax | 已核销采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已核销采购发票价税合计 |
| 52 | fpurinbillentryseqid | fpurinbillentryseqid | int8 | 64 |  | √ | 0 |  |
| 53 | fsettleinvbaseqty | 已核销采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 已核销采购发票基本数量 |
| 54 | fvattax | 增值税(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 增值税(废弃) |
| 55 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 56 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 57 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 58 | fpurreceivebillno | fpurreceivebillno | varchar | 50 |  | √ | ' ' |  |
| 59 | fpurinbillid | fpurinbillid | int8 | 64 |  | √ | 0 |  |
| 60 | fversion_a | 数据版本号 | int4 | 32 |  | √ | 0 | 数据版本号 |
| 61 | fmatchrule | fmatchrule | varchar | 30 |  | √ | ' ' |  |
| 62 | fe_iv_pur_entryid | 关联采购分录ID | int8 | 64 |  | √ | 0 | 关联采购分录ID |
| 63 | fpurinbillentryseq | fpurinbillentryseq | int8 | 64 |  | √ | 0 |  |
| 64 | fe_invoicedlocamt | 已关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计(本位币) |
| 65 | fe_invoiceqty | 已关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 已关联采购发票数量 |
| 66 | fwoffamt | 已冲回金额 | numeric | 23 | 10 | √ | 0 | 已冲回金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_finentry_e_fid |  | fid |
| 2 | idx_ap_iv_enid |  | fe_iv_pur_entryid |
| 3 | t_ap_finapbilldetailentry_e_pkey |  | fentryid |
| 4 | idx_ap_fin_vattax |  | fvattax |

---

## 付款计划-子表 t_ap_finapplanentry

- **表名称：** 付款计划-子表
- **表名：** t_ap_finapplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fplancorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 4 | fplanpricetaxlocal | 应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额(本位币) |
| 5 | fk_bj73_qtyfield | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 6 | fplanpricerate | 应付比例(%) | numeric | 23 | 10 | √ | 0 | 应付比例(%) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | funplanlocklocamt | funplanlocklocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fplansettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsrcfinid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 13 | fplanbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | funplansettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fplancorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 19 | fplanremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 20 | fplancorebillentryseq | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 21 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 22 | fplanlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 23 | funplanlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 24 | fplanpricetax | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 25 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fplansettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 27 | fplansettledlocamt | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 28 | fsrcplanentryid | 源单付款计划id | int8 | 64 |  | √ | 0 | 源单付款计划id |
| 29 | fplanlockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 30 | fk_bj73_pricefield | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 31 | fplancostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 32 | fplancontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 33 | fk_bj73_unitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 |
| 35 | fplanmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 36 | funplansettlelocamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 37 | fplanproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fplanexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 40 | fplanlockedlocamt | fplanlockedlocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_applan_srcfinid |  | fsrcfinid |
| 2 | t_ap_finapplanentry_pkey |  | fentryid |
| 3 | idx_ap_applan_fduedate |  | fplanduedate |
| 4 | idx_ap_applan_srcplanentryid |  | fsrcplanentryid |
| 5 | index_finap_plan |  | fid |

---

## 存货费用分摊委外退库单据信息-子表 t_ap_finapbillentryreturn

- **表名称：** 存货费用分摊委外退库单据信息-子表
- **表名：** t_ap_finapbillentryreturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillid | 委外完工退库库存单据号 | int8 | 64 |  | √ | 0 | 委外完工退库单 im_mdc_omprdoutbill |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fin_entryretu_fentryid |  | fentryid |
| 2 | pk_t_ap_finapbillentryreturn |  | fdetailid |

---

## 存货费用分摊销售单据信息-子表 t_ap_finapbillentrysale

- **表名称：** 存货费用分摊销售单据信息-子表
- **表名：** t_ap_finapbillentrysale

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillid | 销售库存单据号 | int8 | 64 |  | √ | 0 | 销售出库单 im_saloutbill |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fin_entrysale_fentryid |  | fentryid |
| 2 | pk_t_ap_finapbillentrysale |  | fdetailid |

---

## 资产卡片-多选基础资料表 t_ap_finapbillassetcard

- **表名称：** 资产卡片-多选基础资料表
- **表名：** t_ap_finapbillassetcard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 50 |  | √ | ' ' | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_finapbillassetcard_fid |  | fentryid |
| 2 | idx_ap_finapbillassetcard_all |  | fentryid,fpkid |
| 3 | pk_t_ap_finapbillassetcard |  | fpkid |

---

## 存货费用分摊委外入库单据信息-子表 t_ap_finapbillentryout

- **表名称：** 存货费用分摊委外入库单据信息-子表
- **表名：** t_ap_finapbillentryout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillid | 委外完工入库库存单据号 | int8 | 64 |  | √ | 0 | 委外完工入库单 im_mdc_omprdinbill |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fin_entryout_fentryid |  | fentryid |
| 2 | pk_t_ap_finapbillentryout |  | fdetailid |

---

## 关联子实体-子表 t_ap_finapbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_finapbill_lk

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
| 1 | t_ap_finapbill_lk_pkey |  | fpkid |
| 2 | idx_ap_finapbill_lk_fk |  | fid |

---

## 关联子实体-子表 t_ap_finapplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_finapplanentry_lk

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
| 1 | pk_ap_finapplanentry_lk |  | fpkid |
| 2 | idx_ap_finapplanentry_lk_fk |  | fentryid |

---

## 子单据体-子表 t_ap_finapbilltaxsubentry

- **表名称：** 子单据体-子表
- **表名：** t_ap_finapbilltaxsubentry

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
| 1 | idx_ap_fintaxsub_entryid |  | fentryid |
| 2 | pk_t_ap_finapbilltaxsubentry |  | fdetailid |

---

## 存货费用分摊采购单据信息-子表 t_ap_finapbillentrypur

- **表名称：** 存货费用分摊采购单据信息-子表
- **表名：** t_ap_finapbillentrypur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillid | 采购库存单据号 | int8 | 64 |  | √ | 0 | 采购入库单 im_purinbill |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_finapbillentrypur |  | fdetailid |
| 2 | idx_ap_fin_entrypur_fentryid |  | fentryid |

---

## 发票分录-子表 t_ap_finapbillinventry

- **表名称：** 发票分录-子表
- **表名：** t_ap_finapbillinventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fistaxdeduction | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fissupplement | 后补发票 | varchar | 30 |  | √ | ' ' | 后补发票,枚举: 0 :否 1 :是 |
| 9 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 10 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 11 | fbuyername | 收票公司 | varchar | 255 |  | √ | ' ' | 收票公司 |
| 12 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 13 | fbillno | 收票单 | varchar | 80 |  | √ | ' ' | 收票单 |
| 14 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 16 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 17 | fserialno | 发票流水号 | varchar | 80 |  | √ | ' ' | 发票流水号 |
| 18 | fusedamt | 本次占用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次占用金额 |
| 19 | fsrctype | 行来源 | varchar | 30 |  | √ | ' ' | 行来源,枚举: 1 :发票采集 2 :发票下推 3 :应付指定发票 4 :发票指定应付 |
| 20 | finvid | 发票ID | int8 | 64 |  | √ | 0 | 发票ID |
| 21 | fasstactname | 开票公司 | varchar | 255 |  | √ | ' ' | 开票公司 |
| 22 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: ELE :普通发票(电子) SE :专用发票(电子) GE :普通发票(纸质) SP :专用发票(纸质) PAPER :普通纸质卷票 MACH :通用机打发票 TAXI :的士票发票 TRAIN :火车票发票 PLANE :飞机票发票 OTHERCLOUD :其他发票 MOTOR :机动车销售发票 USERCAR :二手车发票 QUOTA :定额发票 TOLL :通行费电子发票 PASSENGER :客运发票 BRIDGE :过路过桥费发票 CARBOAT :车船税发票（专票） PAID :完税证明发票 STEAMER :轮船票发票 OTHER :其他发票 NORMPE :通用机打电子发票 FINE :财政电子发票 NOELETIC :全电普票 MAELETIC :全电专票 PAYLETTER :海关进口增值税专用缴款书 |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_finapbillinventry_pkey |  | fentryid |
| 2 | idx_ap_fininve_fid |  | fid |

---

## 明细-子表 t_ap_finapbilldetailentry

- **表名称：** 明细-子表
- **表名：** t_ap_finapbilldetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fisassetpurlocate | 资产采购费用分摊 | bpchar | 1 |  | √ | '0' | 资产采购费用分摊 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fintercostamt | 计成本金额 | numeric | 23 | 10 | √ | 0 | 计成本金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | funitconvertrate | 单位换算系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位换算系数 |
| 9 | fwoffqty | 已冲回数量 | numeric | 23 | 10 | √ | 0 | 已冲回数量 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fsettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 14 | finvoicesupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 17 | factpricetax | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 18 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 19 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fsourcebillentryid | 源分录ID | varchar | 50 |  | √ | ' ' | 源分录ID |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 24 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 25 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 26 | fpremiumrate | 质保金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 质保金比例(%) |
| 27 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 28 | fwofftotallocalamt | 已冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已冲回价税合计(本位币) |
| 29 | finventorycostsharing | 存货费用分摊 | varchar | 30 |  | √ | ' ' | 存货费用分摊,枚举: procure_cost_sharing :采购费用分摊 sale_cost_sharing :销售费用分摊 entrustout_cost_sharing :委外费用分摊 no_cost_sharing :不分摊 |
| 30 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 31 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 32 | funsettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 33 | fverifyamount | 已勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽金额 |
| 34 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 35 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 36 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 37 | fverifyquantity | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 38 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 39 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 40 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 41 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 42 | fpricetax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 43 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 44 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 45 | funverifyquantity | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 48 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 49 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 50 | fwofflocalamt | 已冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 已冲回金额(本位币) |
| 51 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 52 | funsettleamtbase | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 53 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 54 | fprepayrate | 预付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 预付比例(%) |
| 55 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 56 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 57 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 58 | fisallocate | 已分摊存货费用 | bpchar | 1 |  | √ | '0' | 已分摊存货费用 |
| 59 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 60 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 61 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 62 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 63 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 64 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 65 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fe_loss_baseunitqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 67 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 68 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 69 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 70 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 71 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 72 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 73 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 74 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fspectype | 规格型号 | varchar | 512 |  | √ | ' ' | 规格型号 |
| 76 | fe_loss_quantity | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 77 | fassetcard | fassetcard | int8 | 64 |  | √ | 0 |  |
| 78 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 79 | fsourcebillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 80 | fk_bj73_textfield | requid | varchar | 50 |  | √ | ' ' | requid |
| 81 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 82 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 83 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 84 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 85 | fsettledamtbase | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_fine_unsettle |  | funsettleamt |
| 2 | t_ap_finapbilldetailentry_pkey |  | fentryid |
| 3 | idx_ap_fine_pid |  | fid |
| 4 | idx_ap_fine_sourcebillentryid |  | fsourcebillentryid |
| 5 | idx_ap_fine_corebill |  | fcorebillno,fcorebillentryseq |
| 6 | idx_ap_fine_sourcebillid |  | fsourcebillid |

---

## 财务应付单-分表 t_ap_finapbill_e

- **表名称：** 财务应付单-分表
- **表名：** t_ap_finapbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwoffsourcebilltype | 冲销源单类型(废弃) | varchar | 30 |  | √ | ' ' | 冲销源单类型(废弃),枚举: |
| 3 | fisallocbyper | 按比例分配 | bpchar | 1 |  | √ | '1' | 按比例分配 |
| 4 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 5 | fpaytax | 付款时点税额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 付款时点税额(废弃) |
| 6 | finvoicedamt | 已关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计 |
| 7 | fprojectnumid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 8 | fisintax | 按价税合计分配 | bpchar | 1 |  | √ | '0' | 按价税合计分配 |
| 9 | funinvoicedamt | 未收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 未收票价税合计（废弃） |
| 10 | fiswholealloc | 按整单分摊 | bpchar | 1 |  | √ | '1' | 按整单分摊 |
| 11 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 12 | finvoicedlocalamt | 已关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计(本位币) |
| 13 | fisscmcexpense | 供应链费用 | bpchar | 1 |  | √ | '0' | 供应链费用 |
| 14 | fscmbilltype | 供应链单据标识 | varchar | 30 |  | √ | ' ' | 供应链单据标识,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 sfc_processsettlebill :工序结算单 ism_apsettlebill :应付结算清单 |
| 15 | fivpur_create_flag | 发票关联生成 | bpchar | 1 |  | √ | '0' | 发票关联生成 |
| 16 | fpremiumamt | 质保金金额 | numeric | 23 | 10 | √ | 0.0000000000 | 质保金金额 |
| 17 | fisintertax | 国际税(废弃) | bpchar | 1 |  | √ | '0' | 国际税(废弃) |
| 18 | fpremiumrate | 质保金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 质保金比例(%) |
| 19 | ftrdbillno | 第三方业务编码 | varchar | 80 |  | √ | ' ' | 第三方业务编码 |
| 20 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 21 | ftermsdate | 赎期起算日 | timestamp | 0 |  |  | null | 赎期起算日 |
| 22 | fsourcebiztype | 源单业务类型 | varchar | 255 |  | √ | ' ' | 源单业务类型 |
| 23 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 24 | fpremduedate | 质保金到期日 | timestamp | 0 |  |  | null | 质保金到期日 |
| 25 | ftaxroundrule | 先舍入后汇总 | bpchar | 1 |  | √ | '0' | 先舍入后汇总 |
| 26 | ftransway | 转销版本 | varchar | 30 |  | √ | ' ' | 转销版本,枚举: normal :普通单据 trans_old :旧转销 trans_new :新转销 |
| 27 | ftranstype | 转销单据类型 | varchar | 30 |  | √ | ' ' | 转销单据类型,枚举: normal :普通单据 trans_red :新转销生成的红单 trans_blue :新转销生成的蓝单 |
| 28 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 29 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 partfreeze :部分冻结 |
| 30 | fiswoffbyqty | 按数量冲回 | bpchar | 1 |  | √ | '0' | 按数量冲回 |
| 31 | fsrcbilltypeid | 源单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 32 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 33 | fwritebackbill | 反写单据 | bpchar | 1 |  | √ | '0' | 反写单据 |
| 34 | fsrcasstactid | 源单往来单位（转销） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 35 | fisinvoicediffmode | 发票差异模式 | bpchar | 1 |  | √ | '0' | 发票差异模式 |
| 36 | fispremium | 是否质保金 | bpchar | 1 |  | √ | '0' | 是否质保金 |
| 37 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 38 | fiv_lossqty_handle | 是否处理损耗 | bpchar | 1 |  | √ | '0' | 是否处理损耗 |
| 39 | fisimpexptax | 进出口环节税费 | bpchar | 1 |  | √ | '0' | 进出口环节税费 |
| 40 | fisexpensealloc | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 41 | funinvoicedlocalamt | 未关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计(本位币) |
| 42 | funinvoicedamt_iv | 未关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计 |
| 43 | fbebank | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 44 | fisadjust | 是否借贷调整 | bpchar | 1 |  | √ | '0' | 是否借贷调整 |
| 45 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 46 | fisrefinv | 关联发票 | bpchar | 1 |  | √ | '0' | 关联发票 |
| 47 | fsettleamount | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 48 | fpaymentcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | fnotsplitbycon | 合同编号非默认维度 | bpchar | 1 |  | √ | '0' | 合同编号非默认维度 |
| 50 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从总账引入 shr_xzfp :s-HR传入 |
| 51 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 52 | fpayeebanknum | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 53 | fsettlerelations | 组织间结算 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 54 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | ' ' | 录入含税单价 |
| 55 | fsettleamountbase | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 56 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 57 | fisplansplit | 计划按分组方案生成 | bpchar | 1 |  | √ | '1' | 计划按分组方案生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_finapbill_e_pkey |  | fid |
| 2 | idx_ap_fabe_acct |  | fpayeebanknum |
