# 暂估应付单-ap_busbill

## 费用分摊-子表 t_ap_busbillallocentry

- **表名称：** 费用分摊-子表
- **表名：** t_ap_busbillallocentry

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
| 1 | idx_ap_busalloc_fid |  | fid |
| 2 | t_ap_busbillallocentry_pkey |  | fentryid |

---

## 存货费用分摊采购单据信息-子表 t_ap_busbillentrypur

- **表名称：** 存货费用分摊采购单据信息-子表
- **表名：** t_ap_busbillentrypur

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
| 1 | pk_t_ap_busbillentrypur |  | fdetailid |
| 2 | idx_ap_bus_entrypur_fentryid |  | fentryid |

---

## 子单据体-子表 t_ap_busbilltaxentry

- **表名称：** 子单据体-子表
- **表名：** t_ap_busbilltaxentry

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
| 1 | t_ap_busbilltaxentry_pkey |  | fdetailid |
| 2 | idx_ap_bustaxe_pid |  | fentryid |

---

## 明细-分表 t_ap_busbillentry_e

- **表名称：** 明细-分表
- **表名：** t_ap_busbillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | frelationid | 先到票关联财务应付分录id | int8 | 64 |  | √ | 0 | 先到票关联财务应付分录id |
| 4 | funinvnotaxamt | 未关联财务金额 | numeric | 23 | 10 | √ | 0 | 未关联财务金额 |
| 5 | ffinsrcwofftotalamt | 财务源单明细冲回价税合计 | numeric | 23 | 10 | √ | 0 | 财务源单明细冲回价税合计 |
| 6 | finvbiztype | 关联业务单据业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 7 | ffinsrcwoffamt | 财务源单明细冲回金额 | numeric | 23 | 10 | √ | 0 | 财务源单明细冲回金额 |
| 8 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcostdiffamt | 成本金额差异 | numeric | 23 | 10 | √ | 0 | 成本金额差异 |
| 10 | finvoicednotaxamt | 已关联财务金额 | numeric | 23 | 10 | √ | 0 | 已关联财务金额 |
| 11 | fworkn | 生产工单号 | varchar | 50 |  | √ | ' ' | 生产工单号 |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | fisgetinvoice | 先到票 | bpchar | 1 |  | √ | '0' | 先到票 |
| 14 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 15 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 16 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 17 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 18 | fworkrown | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 19 | fversion_a | 数据版本a | int4 | 32 |  | √ | 0 | 数据版本a |
| 20 | finvnotaxlocalamt | 已关联财务金额(本位币) | numeric | 23 | 10 | √ | 0 | 已关联财务金额(本位币) |
| 21 | fversion_b | 数据版本b | int4 | 32 |  | √ | 0 | 数据版本b |
| 22 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 23 | fversion_c | 数据版本c | int4 | 32 |  | √ | 0 | 数据版本c |
| 24 | fversion_d | 数据版本d | int4 | 32 |  | √ | 0 | 数据版本d |
| 25 | fversion_e | 数据版本e(反写应付结算清单数据升级) | int4 | 32 |  | √ | 0 | 数据版本e(反写应付结算清单数据升级) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | funinvnotaxlocalamt | 未关联财务金额(本位币) | numeric | 23 | 10 | √ | 0 | 未关联财务金额(本位币) |
| 28 | ftotaldiffamt | 价税合计差异 | numeric | 23 | 10 | √ | 0 | 价税合计差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_buseentry_e_pid |  | fid |
| 2 | idx_ar_bus_materialversion |  | fmaterialversionid |
| 3 | t_ap_busbillentry_e_pkey |  | fentryid |

---

## 明细-分表 t_ap_busbillentry_f

- **表名称：** 明细-分表
- **表名：** t_ap_busbillentry_f

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
| 1 | pk_t_ap_busbillentry_f |  | fentryid |
| 2 | idx_ap_bus_entryf_fid |  | fid |

---

## 关联子实体-子表 t_ap_busbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_busbill_lk

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
| 1 | t_ap_busbill_lk_pkey |  | fpkid |
| 2 | idx_ap_busbill_lk_fk |  | fid |

---

## 存货费用分摊销售单据信息-子表 t_ap_busbillentrysale

- **表名称：** 存货费用分摊销售单据信息-子表
- **表名：** t_ap_busbillentrysale

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
| 1 | idx_ap_bus_entrysale_fentryid |  | fentryid |
| 2 | pk_t_ap_busbillentrysale |  | fdetailid |

---

## 暂估应付单-关联追踪表 t_ap_busbill_tc

- **表名称：** 暂估应付单-关联追踪表
- **表名：** t_ap_busbill_tc

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
| 1 | t_ap_busbill_tc_pkey |  | fid |
| 2 | idx_ap_busbill_tc_tbill |  | ftbillid |
| 3 | idx_ap_busbill_tc_tid |  | ftid |

---

## 付款计划-子表 t_ap_busplanentry

- **表名称：** 付款计划-子表
- **表名：** t_ap_busplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fnoinvoiceamt | fnoinvoiceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 6 | finvoicedamt | 已开票应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票应付金额 |
| 7 | fplanremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | fplanpricetaxlocal | 应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额(本位币) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | funinvoicedamt | 未开票应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未开票应付金额 |
| 11 | finvoicedlocamt | 已开票应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已开票应付金额(本位币) |
| 12 | fplanpricetax | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 13 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fplansettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fnoinvoicelocamt | fnoinvoicelocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | funinvoicedlocamt | 未开票应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未开票应付金额(本位币) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_busplanentry_pkey |  | fentryid |
| 2 | idx_ap_busplan_duedate |  | fplanduedate |
| 3 | idx_ap_busplan_fid |  | fid |

---

## 明细-子表 t_ap_busbillentry

- **表名称：** 明细-子表
- **表名：** t_ap_busbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpaytax | 付款时点税额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款时点税额 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fintercostamt | 计成本金额 | numeric | 23 | 10 | √ | 0 | 计成本金额 |
| 7 | finvoicedamt | 已关联财务应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应付金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | funinvoicedamt | 未关联财务应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应付金额 |
| 10 | fcostdifflocalamt | 成本金额差异本位币 | numeric | 23 | 10 | √ | 0 | 成本金额差异本位币 |
| 11 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 14 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 15 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 16 | finvoicesupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 17 | finvoicecode | 发票代码 | varchar | 30 |  | √ | ' ' | 发票代码 |
| 18 | ffinsrcwofflocalamt | 财务源单明细冲回金额本位币 | numeric | 23 | 10 | √ | 0 | 财务源单明细冲回金额本位币 |
| 19 | funinvoicedqty | 未关联财务数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务数量 |
| 20 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_out_contract_settle :支出合同结算 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 21 | finvoiceno | 发票号码 | varchar | 30 |  | √ | ' ' | 发票号码 |
| 22 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 23 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 24 | fscmentryid | 供应链单据分录ID | int8 | 64 |  | √ | 0 | 供应链单据分录ID |
| 25 | ffinsrcwoffqty | 财务源单明细冲回数量 | numeric | 23 | 10 | √ | 0 | 财务源单明细冲回数量 |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 27 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 28 | funwoffnotaxamt | 未冲回金额 | numeric | 23 | 10 | √ | 0 | 未冲回金额 |
| 29 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 30 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 31 | finventorycostsharing | 存货费用分摊 | varchar | 30 |  | √ | ' ' | 存货费用分摊,枚举: procure_cost_sharing :采购费用分摊 sale_cost_sharing :销售费用分摊 entrustout_cost_sharing :委外费用分摊 no_cost_sharing :不分摊 |
| 32 | facttaxunitprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 33 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 34 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 35 | finvoicedlocamt | 已关联财务应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应付金额(本位币) |
| 36 | ffinsrcentryid | 财务源单明细ID | int8 | 64 |  | √ | 0 | 财务源单明细ID |
| 37 | fiswriteoff | 已冲回 | bpchar | 1 |  | √ | '0' | 已冲回 |
| 38 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 39 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 40 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 41 | finvoicedqty | 已关联财务数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务数量 |
| 42 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 43 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 44 | funwoffqty | 未冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回数量 |
| 45 | ftotaldifflocalamt | 价税合计差异本位币 | numeric | 23 | 10 | √ | 0 | 价税合计差异本位币 |
| 46 | funinvoicedlocamt | 未关联财务应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应付金额(本位币) |
| 47 | funwofftax | 未冲回税额 | numeric | 23 | 10 | √ | 0 | 未冲回税额 |
| 48 | funwofftaxlocal | 未冲回税额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回税额(本位币) |
| 49 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 50 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 51 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 52 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 53 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 54 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 55 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 56 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 57 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 58 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 59 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 60 | fisallocate | 已分摊存货费用 | bpchar | 1 |  | √ | '0' | 已分摊存货费用 |
| 61 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 62 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 63 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 64 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 65 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 66 | fmostsrcbusbillid | 源蓝字暂估单id | int8 | 64 |  | √ | 0 | 源蓝字暂估单id |
| 67 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 68 | funwoffnotaxlocamt | 未冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回金额(本位币) |
| 69 | funwoffamt | 未冲回价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计 |
| 70 | fe_loss_baseunitqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 71 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 72 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 73 | funwofflocamt | 未冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计(本位币) |
| 74 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 75 | factunitprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 76 | ffinsrcwofftotallocalamt | 财务源单明细冲回价税合计本位币 | numeric | 23 | 10 | √ | 0 | 财务源单明细冲回价税合计本位币 |
| 77 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 78 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 79 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 80 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 81 | fvattax | 增值税 | numeric | 23 | 10 | √ | 0.0000000000 | 增值税 |
| 82 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 83 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 84 | fmostsrcbusentryid | 源蓝字暂估单分录id | int8 | 64 |  | √ | 0 | 源蓝字暂估单分录id |
| 85 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 86 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 87 | fe_loss_quantity | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 88 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位转换系数 |
| 89 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 90 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 91 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_buse_material |  | fmaterialid |
| 2 | idx_ap_buse_scmentryid |  | fscmentryid |
| 3 | idx_ap_buse_srcentryid |  | fsrcentryid |
| 4 | idx_ap_buse_pid |  | fid |
| 5 | idx_ap_busbillentry_srcbillid |  | fsrcbillid |
| 6 | t_ap_busbillentry_pkey |  | fentryid |
| 7 | idx_ap_buse_corebill |  | fcorebillno,fcorebillentryseq |

---

## 存货费用分摊委外退库单据信息-子表 t_ap_busbillentryreturn

- **表名称：** 存货费用分摊委外退库单据信息-子表
- **表名：** t_ap_busbillentryreturn

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
| 1 | pk_t_ap_busbillentryreturn |  | fdetailid |
| 2 | idx_ap_bus_entryretu_fentryid |  | fentryid |

---

## 关联子实体-子表 t_ap_busbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_busbillentry_lk

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
| 1 | t_ap_busbillentry_lk_pkey |  | fpkid |
| 2 | idx_ap_busentry_lk_pentryid |  | fentryid |
| 3 | idx_ap_busbillentry_lk_fk |  | fentryid |

---

## 暂估应付单-主表 t_ap_busbill

- **表名称：** 暂估应付单-主表
- **表名：** t_ap_busbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | finvoicedamt | 已关联财务应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应付金额 |
| 5 | funinvoicedamt | 未关联财务应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应付金额 |
| 6 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fistaxdeduction | 税额不计入成本 | bpchar | 1 |  | √ | '1' | 税额不计入成本 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 11 | fpurmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 12 | freceivingsupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fscmbilltype | 供应链单据标识 | varchar | 30 |  | √ | ' ' | 供应链单据标识,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 sfc_processsettlebill :工序结算单 |
| 14 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 ap_busbill :暂估应付单 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 ism_apsettlebill :应付结算清单 im_purreceivebill :收料通知单 sfc_processsettlebill :工序结算单 |
| 18 | fsrcbizdate | 源暂估单日期 | timestamp | 0 |  |  | null | 源暂估单日期 |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | funwoffnotaxamt | 未冲回金额 | numeric | 23 | 10 | √ | 0 | 未冲回金额 |
| 21 | frevaluasrcbusbillid | 重估源单ID | int8 | 64 |  | √ | 0 | 重估源单ID |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | finvoicedlocamt | 已关联财务应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应付金额(本位币) |
| 24 | fiswriteoff | fiswriteoff | bpchar | 1 |  | √ | '0' |  |
| 25 | fsrcfinbillid | 财务源单ID | int8 | 64 |  | √ | 0 | 财务源单ID |
| 26 | finvoicebiztypeid | 发票类别 | int8 | 64 |  | √ | 0 | 发票业务类别 bd_invoicebiztype |
| 27 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 28 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fhadrevaluation | 已重估 | bpchar | 1 |  | √ | '0' | 已重估 |
| 31 | funinvoicedlocamt | 未关联财务应付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应付金额(本位币) |
| 32 | funwofftax | 未冲回税额 | numeric | 23 | 10 | √ | 0 | 未冲回税额 |
| 33 | funwofftaxlocal | 未冲回税额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回税额(本位币) |
| 34 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 37 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 38 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 39 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 40 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 41 | frevaluasrcbusbillno | 重估源单编码 | varchar | 80 |  | √ | ' ' | 重估源单编码 |
| 42 | fmostsrcbusbillid | 源蓝字暂估单id | int8 | 64 |  | √ | 0 | 源蓝字暂估单id |
| 43 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 44 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | funwoffnotaxlocamt | 未冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回金额(本位币) |
| 47 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 48 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 49 | funwoffamt | 未冲回价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计 |
| 50 | fisadjust | 冲回单 | bpchar | 1 |  | √ | '0' | 冲回单 |
| 51 | funwofflocamt | 未冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计(本位币) |
| 52 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 53 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 54 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 57 | fisfullinvoice | 完全开票 | bpchar | 1 |  | √ | '0' | 完全开票 |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 60 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 61 | fpaycond | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 62 | fdepartmentid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 63 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 65 | fduedate | 最后到期日 | timestamp | 0 |  |  | null | 最后到期日 |
| 66 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 67 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 68 | fisrevaluation | 重估业务 | bpchar | 1 |  | √ | '0' | 重估业务 |
| 69 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 70 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 71 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 72 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 73 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_bus_fbillno |  | fbillno |
| 2 | idx_ap_busbill_sourcebillid |  | fsourcebillid |
| 3 | idx_ap_busbill_dateorg |  | fbizdate,forgid |
| 4 | idx_ap_bus_dateorgstate |  | fbizdate,forgid,fbillstatus |
| 5 | idx_ap_busbill_fsrcfinbillid |  | fsrcfinbillid |
| 6 | idx_ap_busbill_asstact |  | fasstactid |
| 7 | t_ap_busbill_pkey |  | fid |

---

## 存货费用分摊委外入库单据信息-子表 t_ap_busbillentryout

- **表名称：** 存货费用分摊委外入库单据信息-子表
- **表名：** t_ap_busbillentryout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillid | 委外库存单据号 | int8 | 64 |  | √ | 0 | 委外完工入库单 im_mdc_omprdinbill |
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
| 1 | pk_t_ap_busbillentryout |  | fdetailid |
| 2 | idx_ap_bus_entryout_fentryid |  | fentryid |

---

## 暂估应付单-分表 t_ap_busbill_e

- **表名称：** 暂估应付单-分表
- **表名：** t_ap_busbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从总账引入 |
| 3 | fisallocbyper | 是否按比例分摊 | bpchar | 1 |  | √ | '1' | 是否按比例分摊 |
| 4 | fisverifybusiness | 核销业务 | bpchar | 1 |  | √ | '0' | 核销业务 |
| 5 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 6 | fwriteoffbusiness | 冲销业务 | bpchar | 1 |  | √ | '0' | 冲销业务 |
| 7 | fisintertax | 国际税 | bpchar | 1 |  | √ | '0' | 国际税 |
| 8 | fprojectnumid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 9 | fgenerationtype | 生成方式 | bpchar | 1 |  | √ | '0' | 生成方式,枚举: 0 :其它 1 :采购入库单审核触发(先到票) 2 :财务应付单审核触发(先到票) |
| 10 | fiswholealloc | 按整单分摊 | bpchar | 1 |  | √ | '1' | 按整单分摊 |
| 11 | ftaxroundrule | 先舍入后汇总 | bpchar | 1 |  | √ | '0' | 先舍入后汇总 |
| 12 | fisselfwoff | 手工冲回标记 | bpchar | 1 |  | √ | '0' | 手工冲回标记 |
| 13 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 14 | fisexpensealloc | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 15 | frelationfinapbillid | 先到票关联财务单Id | int8 | 64 |  | √ | 0 | 先到票关联财务单Id |
| 16 | fisarchive | 是否归档 | bpchar | 1 |  | √ | ' ' | 是否归档 |
| 17 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 18 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 19 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_bus_exratedate |  | fexratedate |
| 2 | t_ap_busbill_e_pkey |  | fid |
| 3 | idx_ap_bus_relationid |  | frelationfinapbillid |

---

## 暂估应付单-反写记录表 t_ap_busbill_wb

- **表名称：** 暂估应付单-反写记录表
- **表名：** t_ap_busbill_wb

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
| 1 | idx_ap_busbill_wb_fk |  | fid |
| 2 | t_ap_busbill_wb_pkey |  | fentryid |
