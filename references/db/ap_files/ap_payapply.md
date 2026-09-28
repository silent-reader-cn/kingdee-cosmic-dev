# 付款申请单-ap_payapply

## 付款申请单-主表 t_ap_applypaybill

- **表名称：** 付款申请单-主表
- **表名：** t_ap_applypaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplycause | 请款事由 | varchar | 512 |  |  | null | 请款事由 |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 4 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 5 | fapprover | 当前处理人 | varchar | 80 |  | √ | ' ' | 当前处理人 |
| 6 | fapplyorg | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fappseleamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 8 | fpayorg | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fscheuser | 排款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fispushrefund | 是否直接退款 | bpchar | 1 |  | √ | '0' | 是否直接退款 |
| 12 | fprojectdataid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fpaystatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: Norequired :无需付款 Alreadypay :已付款 Unpaid :未付款 Inpayment :部分付款 |
| 15 | fbiztype | 业务类型(预留字段) | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 17 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fschestatus | 排款状态 | varchar | 30 |  | √ | ' ' | 排款状态,枚举: 0 :未排款 1 :已排款 |
| 19 | fpurorg | fpurorg | int8 | 64 |  | √ | 0 |  |
| 20 | fpaycurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 |
| 24 | fpurdept | fpurdept | int8 | 64 |  | √ | 0 |  |
| 25 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_invoice :发票 ap_finapbill :财务应付单 ar_finarbill :财务应收单 im_purinbill :采购入库单 pm_purorderbill :采购订单 im_purreturnbill :采购退货单 conm_purcontract :采购合同 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 cas_recbill :收款单 |
| 26 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 27 | fsettlecurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 29 | fsuretybiztype | 保证金业务类型 | varchar | 50 |  | √ | ' ' | 保证金业务类型,枚举: suretyrefund :保证金退款 suretypay :保证金付款 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 32 | fapprovalamount | 预计付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 预计付款金额 |
| 33 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 34 | fapplyamount | 申请金额(作废) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(作废) |
| 35 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fisexceedallowpay | 超允付金额付款 | bpchar | 1 |  | √ | '0' | 超允付金额付款 |
| 37 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 38 | fschetime | 排款时间 | timestamp | 0 |  |  | null | 排款时间 |
| 39 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 40 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 41 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 partfreeze :部分冻结 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 44 | faprseleamount | 核准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核准金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_apply_billno |  | fbillno |
| 2 | apply_indexes |  | fapplydate,fapplyorg |
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

---

## 明细匹配记录-子表 t_ap_applyentrymatch

- **表名称：** 明细匹配记录-子表
- **表名：** t_ap_applyentrymatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 2 | fsprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fssettlecurid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fmatchbillno | 匹配编号 | varchar | 100 |  | √ | ' ' | 匹配编号 |
| 5 | fslicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 8 | fscorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 9 | fslockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0 | 已锁定金额 |
| 10 | fscorebilltype | 核心单据类型 | varchar | 50 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 sm_salorder :销售订单 conm_salcontract :销售合同 |
| 11 | fscorebillentryseq | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 12 | fmatchbillid | 匹配记录id | int8 | 64 |  | √ | 0 | 匹配记录id |
| 13 | fspaidamt | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 14 | fscorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 15 | fsappseleamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 16 | fscorebillno | 核心单据号 | varchar | 100 |  | √ | ' ' | 核心单据号 |
| 17 | fsapprovedseleamt | 核准金额 | numeric | 23 | 10 | √ | 0 | 核准金额 |
| 18 | fsourcesubentryid | 源子单据体id | int8 | 64 |  | √ | 0 | 源子单据体id |
| 19 | fspayamount | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 20 | fmatchstatus | 匹配状态 | varchar | 50 |  | √ | ' ' | 匹配状态,枚举: 0 :未匹配 1 :已匹配 |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ap_applyentrymatch |  | fdetailid |
| 2 | idx_ap_applyentrymatch |  | fentryid |

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
| 3 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsourcecurrency | 源单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fsalesman | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 7 | fk_bj73_amountfield1 | 剩余应付金额 | numeric | 23 | 10 |  | null | 剩余应付金额 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 10 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 12 | fsettlementtype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 13 | frectunittype | 收款单位类型 | varchar | 80 |  | √ | ' ' | 收款单位类型,枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 14 | fasstactbalance | 往来单位余额 | numeric | 23 | 10 | √ | 0 | 往来单位余额 |
| 15 | frefundamt | 退款金额 | numeric | 23 | 10 | √ | 0 | 退款金额 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fisscmcexpense | 供应链费用 | bpchar | 1 |  | √ | '0' | 供应链费用 |
| 18 | fpaymenttype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 19 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 sm_salorder :销售订单 conm_salcontract :销售合同 pm_om_purorderbill :简单委外订单 |
| 20 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 22 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 24 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 27 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 28 | fismatch | 已匹配 | bpchar | 1 |  | √ | '0' | 已匹配 |
| 29 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 30 | frectunit | 收款单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fapplyamount | 申请金额(作废) | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额(作废) |
| 32 | fk_bj73_amountfield | 剩余金额 | numeric | 23 | 10 |  | null | 剩余金额 |
| 33 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 34 | fpaidamt | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 35 | fk_bj73_unitfield | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | ffreezestate | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: unfreeze :未冻结 allfreeze :已冻结 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型(预留字段) | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fapprovedamt | 预计付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 预计付款金额 |
| 40 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 41 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 43 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 44 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 45 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 46 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 47 | fasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 48 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 49 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 50 | flinkallowpayamt | 联动付款允付金额 | numeric | 23 | 10 | √ | 0 | 联动付款允付金额 |
| 51 | fk_bj73_qtyfield | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 52 | fappseleamount | 申请金额 | numeric | 23 | 10 | √ | 0.0000000000 | 申请金额 |
| 53 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 54 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bos_user :人员 bos_org :公司 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 55 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 56 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 57 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 58 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 59 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | fesourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 61 | fislinkpay | 联动付款 | bpchar | 1 |  | √ | '0' | 联动付款 |
| 62 | fbebank | 对方账户开户行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 63 | fassacct | 对方银行账号 | varchar | 50 |  | √ | ' ' | 对方银行账号 |
| 64 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 65 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 67 | fbalanceupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 68 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 70 | fpayeraccbank | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 71 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 72 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 73 | fassacctname | 对方账号名称 | varchar | 255 |  | √ | ' ' | 对方账号名称 |
| 74 | fk_bj73_pricefield | 单价 | numeric | 23 | 10 |  | null | 单价 |
| 75 | fk_bj73_textfield | 财务应付单据编号 | varchar | 50 |  | √ | ' ' | 财务应付单据编号 |
| 76 | fapprovedseleamt | 核准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核准金额 |
| 77 | fexpaydate | 期望付款日 | timestamp | 0 |  |  | null | 期望付款日 |
| 78 | flockedamt | 已锁定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已锁定金额 |
| 79 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

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

## 关联子实体-子表 t_ap_applyentrymatch_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_applyentrymatch_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ap_applyentrymatch_lk |  | fpkid |
| 2 | idx_ap_applyentrymatch_lk |  | fdetailid |
