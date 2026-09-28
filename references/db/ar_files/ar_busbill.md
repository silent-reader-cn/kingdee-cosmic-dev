# 暂估应收单-ar_busbill

## 关联子实体-子表 t_ar_busbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_busbillentry_lk

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
| 1 | t_ar_busbillentry_lk_pkey |  | fpkid |
| 2 | idx_ar_busbillentry_lk_fk |  | fentryid |

---

## 明细-子表 t_ar_busbillentry

- **表名称：** 明细-子表
- **表名：** t_ar_busbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | finvoicedamt | 已关联财务应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应收金额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | funinvoicedamt | 未关联财务应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应收金额 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | ffinalrecamount | ffinalrecamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 11 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 12 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 14 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 15 | funinvoicedqty | 未关联财务数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务数量 |
| 16 | fdelivercustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 ec_in_contract_settle :收入合同结算 pm_purorderbill :采购订单 im_transapply :调拨申请单 amccsa_custschdorder :销售计划协议 amccsa_custschdorder_init :期初销售计划协议 |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 19 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 20 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 23 | funwoffnotaxamt | 未冲回金额 | numeric | 23 | 10 | √ | 0 | 未冲回金额 |
| 24 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 25 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 26 | facttaxunitprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 27 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 28 | finvoicedlocamt | 已关联财务应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应收金额(本位币) |
| 29 | fiswriteoff | 已冲回 | bpchar | 1 |  | √ | '0' | 已冲回 |
| 30 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 31 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 32 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 33 | finvoicedqty | 已关联财务数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务数量 |
| 34 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 35 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 36 | funwoffqty | 未冲回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回数量 |
| 37 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 38 | funinvoicedlocamt | 未关联财务应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应收金额(本位币) |
| 39 | funwofftax | 未冲回税额 | numeric | 23 | 10 | √ | 0 | 未冲回税额 |
| 40 | funwofftaxlocal | 未冲回税额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回税额(本位币) |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 43 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 44 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 45 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 46 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 47 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 48 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 49 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 50 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 51 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 52 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 53 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 54 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 55 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 56 | ffinalqty | ffinalqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | fmostsrcbusbillid | 源蓝字暂估单id | int8 | 64 |  | √ | 0 | 源蓝字暂估单id |
| 58 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 59 | funwoffnotaxlocamt | 未冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回金额(本位币) |
| 60 | funwoffamt | 未冲回价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计 |
| 61 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 62 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 63 | funwofflocamt | 未冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计(本位币) |
| 64 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 65 | factunitprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 66 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 67 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 70 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 71 | fmostsrcbusentryid | 源蓝字暂估单分录id | int8 | 64 |  | √ | 0 | 源蓝字暂估单分录id |
| 72 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 73 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 74 | finvoicecustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 75 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位转换系数 |
| 76 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 77 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 78 | ffinalreclocalamt | ffinalreclocalamt | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_buse_corebill |  | fcorebillno,fcorebillentryseq |
| 2 | idx_ar_buse_srcentryid |  | fsrcentryid |
| 3 | idx_ar_buse_pid |  | fid |
| 4 | idx_ar_busbillentry_srcbillid |  | fsrcbillid |
| 5 | t_ar_busbillentry_pkey |  | fentryid |
| 6 | idx_ar_buse_material |  | fmaterialid |

---

## 暂估应收单-关联追踪表 t_ar_busbill_tc

- **表名称：** 暂估应收单-关联追踪表
- **表名：** t_ar_busbill_tc

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
| 1 | t_ar_busbill_tc_pkey |  | fid |
| 2 | idx_ar_busbill_tc_tbill |  | ftbillid |
| 3 | idx_ar_busbill_tc_tid |  | ftid |

---

## 子单据体-子表 t_ar_busbilltaxentry

- **表名称：** 子单据体-子表
- **表名：** t_ar_busbilltaxentry

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
| 8 | ftaxassessamt | 评估计税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 评估计税金额 |
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
| 21 | ftaxtime | 计税时点 | varchar | 255 |  | √ | ' ' | 计税时点,枚举: invoice :开票时点 receipt :收款时点 |
| 22 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | 税码 bastax_taxcode |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fdeductible | 抵扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣额 |
| 25 | fdeductionrate | 抵扣率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣率(%) |
| 26 | fisoutputtax | 销项税 | bpchar | 1 |  | √ | ' ' | 销项税 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fcandeductible | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_busbilltaxentry_pkey |  | fdetailid |
| 2 | idx_ar_bustaxe_pid |  | fentryid |

---

## 暂估应收单-反写记录表 t_ar_busbill_wb

- **表名称：** 暂估应收单-反写记录表
- **表名：** t_ar_busbill_wb

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
| 1 | idx_ar_busbill_wb_fk |  | fid |
| 2 | t_ar_busbill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_ar_busbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_busbill_lk

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
| 1 | idx_ar_busbill_lk_fk |  | fid |
| 2 | t_ar_busbill_lk_pkey |  | fpkid |

---

## 收款计划-子表 t_ar_busplanentry

- **表名称：** 收款计划-子表
- **表名：** t_ar_busplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fplanduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 5 | finvoicedamt | 已开票应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票应收金额 |
| 6 | fplanremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fplanpricetaxlocal | 应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额(本位币) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | funinvoicedamt | 未开票应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未开票应收金额 |
| 10 | finvoicedlocamt | 已开票应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 已开票应收金额(本位币) |
| 11 | fplanpricetax | 应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应收金额 |
| 12 | ffinalrecamount | ffinalrecamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fplansettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | funinvoicedlocamt | 未开票应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未开票应收金额(本位币) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | ffinalreclocalamt | ffinalreclocalamt | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_busplan_duedate |  | fplanduedate |
| 2 | idx_ar_busplan_fid |  | fid |
| 3 | t_ar_busplanentry_pkey |  | fentryid |

---

## 暂估应收单-分表 t_ar_busbill_e

- **表名称：** 暂估应收单-分表
- **表名：** t_ar_busbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从总账引入 |
| 3 | fisverifybusiness | 核销业务 | bpchar | 1 |  | √ | '0' | 核销业务 |
| 4 | fwriteoffbusiness | 冲销业务 | bpchar | 1 |  | √ | '0' | 冲销业务 |
| 5 | fisintertax | 国际税 | bpchar | 1 |  | √ | '0' | 国际税 |
| 6 | ftaxroundrule | 先舍入后汇总 | bpchar | 1 |  | √ | '0' | 先舍入后汇总 |
| 7 | fisselfwoff | 手工冲回标记 | bpchar | 1 |  | √ | '0' | 手工冲回标记 |
| 8 | funverifyamount | 未勾稽金额 | numeric | 23 | 10 | √ | 0 | 未勾稽金额 |
| 9 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 10 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 11 | fisarchive | 是否归档 | bpchar | 1 |  | √ | ' ' | 是否归档 |
| 12 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 14 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 16 | fverifystatus | 勾稽状态 | varchar | 30 |  | √ | ' ' | 勾稽状态,枚举: unverify :未勾稽 partverify :部分勾稽 verified :全部勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_busbill_e_pkey |  | fid |
| 2 | idx_ar_bus_exratedate |  | fexratedate |

---

## 明细-分表 t_ar_busbillentry_e

- **表名称：** 明细-分表
- **表名：** t_ar_busbillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | funinvnotaxamt | 未关联财务金额 | numeric | 23 | 10 | √ | 0 | 未关联财务金额 |
| 4 | frectax | 收款时点税额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款时点税额 |
| 5 | funconfirmamt | 未确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未确认金额 |
| 6 | fconfirmedamt | 已确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已确认金额 |
| 7 | fisallverify | 完全勾稽 | bpchar | 1 |  | √ | '0' | 完全勾稽 |
| 8 | funconfirmbaseqty | 未确认基本数量 | numeric | 23 | 10 | √ | 0 | 未确认基本数量 |
| 9 | fvattax | 增值税 | numeric | 23 | 10 | √ | 0.0000000000 | 增值税 |
| 10 | fverifiedqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0 | 已勾稽数量 |
| 11 | finvnotaxlocalamt | 已关联财务金额(本位币) | numeric | 23 | 10 | √ | 0 | 已关联财务金额(本位币) |
| 12 | funconfirmqty | 未确认数量 | numeric | 23 | 10 | √ | 0 | 未确认数量 |
| 13 | finvoicednotaxamt | 已关联财务金额 | numeric | 23 | 10 | √ | 0 | 已关联财务金额 |
| 14 | funverifyamt | 未勾稽金额 | numeric | 23 | 10 | √ | 0 | 未勾稽金额 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 16 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0 | 未勾稽数量 |
| 17 | fconfirmedqty | 已确认数量 | numeric | 23 | 10 | √ | 0 | 已确认数量 |
| 18 | fconfirmedbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0 | 已确认基本数量 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fverifiedamt | 已勾稽金额 | numeric | 23 | 10 | √ | 0 | 已勾稽金额 |
| 21 | funinvnotaxlocalamt | 未关联财务金额(本位币) | numeric | 23 | 10 | √ | 0 | 未关联财务金额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_busbillentry_e_pkey |  | fentryid |
| 2 | idx_ar_busentry_e_pid |  | fid |
| 3 | idx_ar_bus_vattax |  | fvattax |

---

## 暂估应收单-主表 t_ar_busbill

- **表名称：** 暂估应收单-主表
- **表名：** t_ar_busbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finvoicedamt | 已关联财务应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应收金额 |
| 6 | funinvoicedamt | 未关联财务应收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应收金额 |
| 7 | ffinalrecamount | ffinalrecamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 11 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 12 | fpaymentcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_invoice :增值税发票 ar_finarbill :财务应收单 sm_salorder :销售订单 im_saloutbill :销售出库单 ar_busbill :暂估应收单 conm_salcontract :销售合同 ism_arsettlebill :应收结算清单 |
| 16 | fsrcbizdate | 源暂估单日期 | timestamp | 0 |  |  | null | 源暂估单日期 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | funwoffnotaxamt | 未冲回金额 | numeric | 23 | 10 | √ | 0 | 未冲回金额 |
| 19 | finvoicedlocamt | 已关联财务应收金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已关联财务应收金额（本位币） |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fiswriteoff | fiswriteoff | bpchar | 1 |  | √ | ' ' |  |
| 22 | fsrcfinbillid | 财务源单ID | int8 | 64 |  | √ | 0 | 财务源单ID |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 26 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 27 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 28 | funinvoicedlocamt | 未关联财务应收金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未关联财务应收金额(本位币) |
| 29 | funwofftax | 未冲回税额 | numeric | 23 | 10 | √ | 0 | 未冲回税额 |
| 30 | funwofftaxlocal | 未冲回税额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回税额(本位币) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 33 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 34 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 35 | fmostsrcbusbillid | 源蓝字暂估单id | int8 | 64 |  | √ | 0 | 源蓝字暂估单id |
| 36 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 37 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | funwoffnotaxlocamt | 未冲回金额(本位币) | numeric | 23 | 10 | √ | 0 | 未冲回金额(本位币) |
| 40 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 41 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应收款项性质 ar_payproperty |
| 42 | funwoffamt | 未冲回价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计 |
| 43 | fisadjust | 冲回单 | bpchar | 1 |  | √ | '0' | 冲回单 |
| 44 | funwofflocamt | 未冲回价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未冲回价税合计(本位币) |
| 45 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 46 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fisfullinvoice | 完全开票 | bpchar | 1 |  | √ | '0' | 完全开票 |
| 50 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 53 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fpaycond | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 55 | fdepartmentid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 57 | fduedate | 最后到期日 | timestamp | 0 |  |  | null | 最后到期日 |
| 58 | fpaymode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 59 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 60 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 61 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 62 | frecorgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 63 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 64 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 65 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 66 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 67 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 68 | ffinalreclocalamt | ffinalreclocalamt | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_busbill_pkey |  | fid |
| 2 | idx_ar_bus_fbillno |  | fbillno |
| 3 | idx_ar_busbill_fsrcfinbillid |  | fsrcfinbillid |
| 4 | idx_ar_bus_dateorg |  | fbizdate,forgid |
| 5 | idx_ar_busbill_asstact |  | fasstactid |
| 6 | idx_ar_bus_org |  | forgid |
| 7 | idx_ar_busbill_sourcebillid |  | fsourcebillid |
