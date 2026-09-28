# 财务应付单-ap_finapbill

## 明细-分表 t_ap_finapbilldetailentry_f

- **表名称：** 明细-分表
- **表名：** t_ap_finapbilldetailentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutreturnbillid | 委外完工退库单 | varchar | 2000 |  | √ | ' ' | 委外完工退库单 |
| 3 | fprocureinventorybillid | 采购库存单据号 | varchar | 2000 |  | √ | ' ' | 采购库存单据号 |
| 4 | foutinventorybillid | 委外完工入库单 | varchar | 2000 |  | √ | ' ' | 委外完工入库单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fsaleinventorybillid | 销售库存单据号 | varchar | 2000 |  | √ | ' ' | 销售库存单据号 |

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
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | fpaytax | 付款时点税额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 付款时点税额(废弃) |
| 4 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | finvoicedamt | 已收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 已收票价税合计（废弃） |
| 6 | funinvoicedamt | 未收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 未收票价税合计（废弃） |
| 7 | fpurinbillno | fpurinbillno | varchar | 50 |  | √ | ' ' |  |
| 8 | fisallverify | 完全勾稽 | bpchar | 1 |  | √ | '0' | 完全勾稽 |
| 9 | finvbiztype | 关联业务单据业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 10 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fwofftotalamt | 已冲回价税合计原币 | numeric | 23 | 10 | √ | 0 | 已冲回价税合计原币 |
| 12 | fpurreceivebillentryid | fpurreceivebillentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fe_uninvoicedlocamt | 未关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计(本位币) |
| 14 | fworkn | 生产工单号 | varchar | 50 |  | √ | ' ' | 生产工单号 |
| 15 | fe_iv_create_qty | 发票关联生成数量 | numeric | 23 | 10 | √ | 0 | 发票关联生成数量 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 17 | fe_uninvoicedamount | 未关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计 |
| 18 | fe_invoicedbaseqty | 已关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 已关联采购发票基本数量 |
| 19 | fisgetinvoice | 先到票 | bpchar | 1 |  | √ | '0' | 先到票 |
| 20 | fscmentryid | 供应链单据分录ID | int8 | 64 |  | √ | 0 | 供应链单据分录ID |
| 21 | fe_iv_purid | 关联采购发票内码 | int8 | 64 |  | √ | 0 | 关联采购发票内码 |
| 22 | fe_invoicedamount | 已关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计 |
| 23 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 24 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 25 | fpurreceivebillentryseq | fpurreceivebillentryseq | int8 | 64 |  | √ | 0 |  |
| 26 | fe_uninvoicedbaseqty | 未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 未关联采购发票基本数量 |
| 27 | fpurinbillentryseqid | fpurinbillentryseqid | int8 | 64 |  | √ | 0 |  |
| 28 | fvattax | 增值税(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 增值税(废弃) |
| 29 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 30 | fworkrown | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 31 | fpurreceivebillno | fpurreceivebillno | varchar | 50 |  | √ | ' ' |  |
| 32 | fpurinbillid | fpurinbillid | int8 | 64 |  | √ | 0 |  |
| 33 | fversion_a | 数据版本号 | int4 | 32 |  | √ | 0 | 数据版本号 |
| 34 | fmatchrule | fmatchrule | varchar | 30 |  | √ | ' ' |  |
| 35 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 36 | fe_iv_pur_entryid | 关联采购分录ID | int8 | 64 |  | √ | 0 | 关联采购分录ID |
| 37 | fpurinbillentryseq | fpurinbillentryseq | int8 | 64 |  | √ | 0 |  |
| 38 | fe_uninvoiceqty | 未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 未关联采购发票数量 |
| 39 | fpurreceivebillid | fpurreceivebillid | int8 | 64 |  | √ | 0 |  |
| 40 | fe_invoicedlocamt | 已关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计(本位币) |
| 41 | fe_invoiceqty | 已关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 已关联采购发票数量 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fwoffamt | 已冲回金额原币 | numeric | 23 | 10 | √ | 0 | 已冲回金额原币 |

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

## 付款计划-子表 t_ap_finapplanentry

- **表名称：** 付款计划-子表
- **表名：** t_ap_finapplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fplancorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 4 | fplanpricetaxlocal | 应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额(本位币) |
| 5 | fplanpricerate | 应付比例(%) | numeric | 23 | 10 | √ | 0 | 应付比例(%) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | funplanlocklocamt | funplanlocklocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fplansettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsrcfinid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 12 | funplansettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fplancorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 17 | fplanremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 18 | fplancorebillentryseq | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 19 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 20 | funplanlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 21 | fplanpricetax | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 22 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fplansettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 24 | fplansettledlocamt | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 25 | fsrcplanentryid | 源单付款计划id | int8 | 64 |  | √ | 0 | 源单付款计划id |
| 26 | fplanlockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 27 | fplancostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 28 | fplancontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 29 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 |
| 30 | fplanmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 31 | funplansettlelocamt | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 32 | fplanproject | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fplanexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 35 | fplanlockedlocamt | fplanlockedlocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsplitscheme | 拆分口径 | int8 | 64 |  | √ | 0 | 付款计划方案 ap_plansplit_scheme |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fistaxdeduction | 税额不计入成本 | bpchar | 1 |  | √ | '0' | 税额不计入成本 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | funsettleamount | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 10 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 11 | fpurmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 12 | freceivingsupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fisinvoicematch | 是否匹配生成 | bpchar | 1 |  | √ | ' ' | 是否匹配生成 |
| 14 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | frelationpay | 关联交易 | bpchar | 1 |  | √ | ' ' | 关联交易 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_invoice :收票单 ap_finapbill :财务应付单 ar_finarbill :财务应收单 im_purinbill :采购入库单 pm_purorderbill :采购订单 im_purreturnbill :采购退货单 ap_busbill :暂估应付单 im_purreceivebill :收料通知单 conm_purcontract :采购合同 pm_om_purorderbill :简单委外订单 im_mdc_omcmplinbill :委外完工入库单 pm_puracceptbill :采购验收单 im_mdc_ominbill :简单委外入库单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 ism_apsettlebill :应付结算清单 sfc_processsettlebill :工序结算单 |
| 19 | fhadwrittenoff | 已被冲销 | bpchar | 1 |  | √ | ' ' | 已被冲销 |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 23 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 24 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 25 | finvoicebiztypeid | 发票类别 | int8 | 64 |  | √ | 0 | 发票业务类别 bd_invoicebiztype |
| 26 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 28 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 29 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fisperiod | 是否期初 | bpchar | 1 |  | √ | ' ' | 是否期初 |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 33 | fpurchaserid | fpurchaserid | int8 | 64 |  | √ | 0 |  |
| 34 | fiswrittenoff | 冲销单据 | bpchar | 1 |  | √ | ' ' | 冲销单据 |
| 35 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 36 | fsettlestatus | 核销状态 | varchar | 30 |  | √ | ' ' | 核销状态,枚举: unsettle :未核销 partsettle :部分核销 settled :全部核销 |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 38 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 39 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 40 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 43 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 44 | fadjusttype | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: buckle :扣罚款 rebate :返利折扣 adjustinv :调整发票尾差 overdue :逾期利息 |
| 45 | fisarchive | 是否归档 | bpchar | 1 |  | √ | ' ' | 是否归档 |
| 46 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 47 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 48 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 53 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fdepartmentid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 57 | fduedate | 最后到期日 | timestamp | 0 |  |  | null | 最后到期日 |
| 58 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 59 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 60 | funsettleamountbase | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 61 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 62 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 63 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 64 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 65 | fistanspay | 是否转销 | bpchar | 1 |  | √ | ' ' | 是否转销 |
| 66 | fverifystatus | 勾稽状态 | varchar | 30 |  | √ | ' ' | 勾稽状态,枚举: 10 :未勾稽 20 :部分勾稽 30 :全部勾稽 |

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
| 4 | idx_ap_fin_bizdate |  | fbizdate |
| 5 | t_ap_finapbill_pkey |  | fid |
| 6 | idx_ap_fin_billno |  | fbillno |

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

## 费用分摊-子表 t_ap_finapbillallocentry

- **表名称：** 费用分摊-子表
- **表名：** t_ap_finapbillallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fsrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 6 | fallocationamt | 分配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分配金额 |
| 7 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 1 | idx_ap_fin_entrypur_fentryid |  | fentryid |
| 2 | pk_t_ap_finapbillentrypur |  | fdetailid |

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
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 5 | fintercostamt | 计成本金额 | numeric | 23 | 10 | √ | 0 | 计成本金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | funitconvertrate | 单位换算系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位换算系数 |
| 8 | fwoffqty | 已冲回数量 | numeric | 23 | 10 | √ | 0 | 已冲回数量 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 11 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 12 | fsettledamt | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 13 | finvoicesupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 16 | factpricetax | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 17 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 18 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 19 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fsourcebillentryid | 源分录ID | varchar | 50 |  | √ | ' ' | 源分录ID |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 23 | funlockamt | 未锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未锁定金额 |
| 24 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 25 | fpremiumrate | 质保金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 质保金比例(%) |
| 26 | fcardid | fcardid | int8 | 64 |  | √ | 0 |  |
| 27 | fwofftotallocalamt | 已冲回价税合计本位币 | numeric | 23 | 10 | √ | 0 | 已冲回价税合计本位币 |
| 28 | finventorycostsharing | 存货费用分摊 | varchar | 30 |  | √ | ' ' | 存货费用分摊,枚举: procure_cost_sharing :采购费用分摊 sale_cost_sharing :销售费用分摊 entrustout_cost_sharing :委外费用分摊 no_cost_sharing :不分摊 |
| 29 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 30 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 31 | funsettleamt | 未核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额 |
| 32 | fverifyamount | 已勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽金额 |
| 33 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 34 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 35 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 36 | fverifyquantity | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 37 | fadjustamount | 抵消金额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额 |
| 38 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 39 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 40 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 41 | fpricetax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 42 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 43 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 44 | funverifyquantity | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 47 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 48 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 49 | fwofflocalamt | 已冲回金额本位币 | numeric | 23 | 10 | √ | 0 | 已冲回金额本位币 |
| 50 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 51 | funsettleamtbase | 未核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未核销金额(本位币) |
| 52 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 53 | fprepayrate | 预付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 预付比例(%) |
| 54 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 55 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 56 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 57 | fisallocate | 已分摊存货费用 | bpchar | 1 |  | √ | '0' | 已分摊存货费用 |
| 58 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 59 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 60 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 61 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 62 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 63 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 64 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 65 | fe_loss_baseunitqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 66 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 67 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 68 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 69 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 70 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 71 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 72 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 73 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 74 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 75 | fe_loss_quantity | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 76 | fadjustlocalamt | 抵消金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 抵消金额(本位币) |
| 77 | fsourcebillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 78 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 79 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 80 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 81 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 82 | fsettledamtbase | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |

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
| 4 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 5 | fpaytax | 付款时点税额(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 付款时点税额(废弃) |
| 6 | finvoicedamt | 已关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计 |
| 7 | fprojectnumid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 8 | fisintax | 按价税合计分配 | bpchar | 1 |  | √ | '0' | 按价税合计分配 |
| 9 | funinvoicedamt | 未收票价税合计（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 未收票价税合计（废弃） |
| 10 | fiswholealloc | 按整单分摊 | bpchar | 1 |  | √ | '1' | 按整单分摊 |
| 11 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 12 | finvoicedlocalamt | 已关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已关联采购发票价税合计(本位币) |
| 13 | fscmbilltype | 供应链单据标识 | varchar | 30 |  | √ | ' ' | 供应链单据标识,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 sfc_processsettlebill :工序结算单 |
| 14 | fivpur_create_flag | 发票关联生成 | bpchar | 1 |  | √ | '0' | 发票关联生成 |
| 15 | fpremiumamt | 质保金金额 | numeric | 23 | 10 | √ | 0.0000000000 | 质保金金额 |
| 16 | fisintertax | 国际税(废弃) | bpchar | 1 |  | √ | '0' | 国际税(废弃) |
| 17 | fpremiumrate | 质保金比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 质保金比例(%) |
| 18 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 19 | ftermsdate | 赎期起算日 | timestamp | 0 |  |  | null | 赎期起算日 |
| 20 | fpremduedate | 质保金到期日 | timestamp | 0 |  |  | null | 质保金到期日 |
| 21 | ftaxroundrule | 先舍入后汇总 | bpchar | 1 |  | √ | '0' | 先舍入后汇总 |
| 22 | ftransway | 转销版本 | varchar | 30 |  | √ | ' ' | 转销版本,枚举: normal :普通单据 trans_old :旧转销 trans_new :新转销 |
| 23 | ftranstype | 转销单据类型 | varchar | 30 |  | √ | ' ' | 转销单据类型,枚举: normal :普通单据 trans_red :新转销生成的红单 trans_blue :新转销生成的蓝单 |
| 24 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 25 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 partfreeze :部分冻结 |
| 26 | fsrcbilltypeid | 源单单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 28 | fwritebackbill | 反写单据 | bpchar | 1 |  | √ | '0' | 反写单据 |
| 29 | fsrcasstactid | 源单往来单位（转销） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | fispremium | 是否质保金 | bpchar | 1 |  | √ | '0' | 是否质保金 |
| 31 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 32 | fiv_lossqty_handle | 是否处理损耗 | bpchar | 1 |  | √ | '0' | 是否处理损耗 |
| 33 | fisexpensealloc | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 34 | funinvoicedlocalamt | 未关联采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计(本位币) |
| 35 | funinvoicedamt_iv | 未关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未关联采购发票价税合计 |
| 36 | fbebank | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 37 | fisadjust | 是否借贷调整 | bpchar | 1 |  | √ | '0' | 是否借贷调整 |
| 38 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 39 | fisrefinv | 关联发票 | bpchar | 1 |  | √ | '0' | 关联发票 |
| 40 | fsettleamount | 已核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额 |
| 41 | fpaymentcurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 42 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从总账引入 shr_xzfp :s-HR传入 |
| 43 | fpayeebanknum | 收款账号 | varchar | 50 |  | √ | ' ' | 收款账号 |
| 44 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 45 | fsettlerelations | 组织间结算 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 46 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | ' ' | 录入含税单价 |
| 47 | fsettleamountbase | 已核销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已核销金额(本位币) |
| 48 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 49 | fisplansplit | 计划按分组方案生成 | bpchar | 1 |  | √ | '1' | 计划按分组方案生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_finapbill_e_pkey |  | fid |
| 2 | idx_ap_fabe_acct |  | fpayeebanknum |

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
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fincludevat | 含增值税 | bpchar | 1 |  | √ | ' ' | 含增值税 |
| 12 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fisinpricetax | 价内税 | bpchar | 1 |  | √ | ' ' | 价内税 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fisoffset | 抵消标识 | bpchar | 1 |  | √ | '0' | 抵消标识 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fnondeductible | 不可抵扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 不可抵扣额 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fincludetail | 含尾款 | bpchar | 1 |  | √ | ' ' | 含尾款 |
| 21 | ftaxtime | 计税时点 | varchar | 255 |  | √ | ' ' | 计税时点,枚举: invoice :开票时点 pay :付款时点 |
| 22 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
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
