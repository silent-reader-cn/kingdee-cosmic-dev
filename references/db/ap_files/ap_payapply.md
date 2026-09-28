# 付款申请单-ap_payapply

## 付款申请单-主表 t_ap_applypaybill

- **表名称：** 付款申请单-主表
- **表名：** t_ap_applypaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplycause | 请款事由 | varchar | 512 |  |  | null | 请款事由 |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 4 | fapplyorg | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fappseleamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 6 | fpayorg | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fispushrefund | 是否直接退款 | bpchar | 1 |  | √ | '0' | 是否直接退款 |
| 9 | fprojectdataid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fpaystatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: Norequired :无需付款 Alreadypay :已付款 Unpaid :未付款 Inpayment :部分付款 |
| 12 | fbiztype | 业务类型(预留字段) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 13 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpurorg | fpurorg | int8 | 64 |  | √ | 0 |  |
| 16 | fpaycurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 |
| 20 | fpurdept | fpurdept | int8 | 64 |  | √ | 0 |  |
| 21 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_invoice :发票 ap_finapbill :财务应付单 ar_finarbill :财务应收单 im_purinbill :采购入库单 pm_purorderbill :采购订单 im_purreturnbill :采购退货单 conm_purcontract :采购合同 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 cas_recbill :收款单 |
| 22 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 23 | fsettlecurrency | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fapprovalamount | 预计付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 预计付款金额 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fapplyamount | 申请金额(作废) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(作废) |
| 29 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 31 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 32 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 33 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 partfreeze :部分冻结 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | faprseleamount | 核准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核准金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | apply_indexes |  | fapplydate,fapplyorg |
| 2 | idx_ap_apply_billno |  | fbillno |
| 3 | t_ap_applypaybill_pkey |  | fid |

---

## 付款申请单-反写记录表 t_payapply_wb

- **表名称：** 付款申请单-反写记录表
- **表名：** t_payapply_wb

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
| 1 | t_payapply_wb_pkey |  | fentryid |
| 2 | idx_payapply_wb_fk |  | fid |

---

## 关联子实体-子表 t_ap_applypaybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_applypaybillentry_lk

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
| 1 | idx_ap_applypaybillentry_lk_fk |  | fentryid |
| 2 | t_ap_applypaybillentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_payapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_payapply_lk

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
| 1 | t_payapply_lk_pkey |  | fpkid |
| 2 | idx_payapply_lk_fk |  | fid |

---

## 明细-子表 t_ap_applypaybillentry

- **表名称：** 明细-子表
- **表名：** t_ap_applypaybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsourcecurrency | 源单币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fsalesman | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 9 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 10 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 11 | fsettlementtype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 12 | frectunittype | 收款单位类型 | varchar | 80 |  | √ | ' ' | 收款单位类型,枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | fpaymenttype | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 15 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 sm_salorder :销售订单 conm_salcontract :销售合同 pm_om_purorderbill :简单委外订单 |
| 16 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 23 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 24 | frectunit | 收款单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | fapplyamount | 申请金额(作废) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(作废) |
| 26 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 27 | fpaidamt | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 28 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型(预留字段) | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 31 | fapprovedamt | 预计付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 预计付款金额 |
| 32 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 33 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 35 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 36 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 38 | fasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 39 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | fappseleamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 41 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 42 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 43 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 44 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fbebank | 对方账户开户行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 47 | fassacct | 对方银行账号 | varchar | 50 |  | √ | ' ' | 对方银行账号 |
| 48 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 53 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 54 | fassacctname | 对方账号名称 | varchar | 255 |  | √ | ' ' | 对方账号名称 |
| 55 | fapprovedseleamt | 核准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核准金额 |
| 56 | fexpaydate | 期望付款日 | timestamp | 0 |  |  | null | 期望付款日 |
| 57 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 58 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | applyentry_indexes |  | fid,fentryid |
| 2 | t_ap_applypaybillentry_pkey |  | fentryid |

---

## 付款申请单-关联追踪表 t_payapply_tc

- **表名称：** 付款申请单-关联追踪表
- **表名：** t_payapply_tc

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
| 1 | idx_payapply_tc_tbill |  | ftbillid |
| 2 | idx_payapply_tc_tid |  | ftid |
| 3 | t_payapply_tc_pkey |  | fid |
