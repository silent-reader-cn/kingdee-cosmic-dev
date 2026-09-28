# 收入成本确认单-ar_revcfmbill

## 明细-子表 t_ar_revcfmbillentry

- **表名称：** 明细-子表
- **表名：** t_ar_revcfmbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fconfirmqty | 确认数量 | numeric | 23 | 10 | √ | 0.0000000000 | 确认数量 |
| 5 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0 | 未勾稽基本数量 |
| 6 | fisallverify | 完全勾稽 | bpchar | 1 |  | √ | '0' | 完全勾稽 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 10 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | fdelivercustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 14 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 salout :销售出库 im_transapply :调拨申请单 amccsa_custschdorder :销售计划协议 amccsa_custschdorder_init :期初销售计划协议 |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 16 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 19 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 20 | fconfirmrate | 收入确认比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收入确认比例(%) |
| 21 | facttaxunitprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 22 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 23 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0 | 已勾稽基本数量 |
| 24 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 25 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 26 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 27 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 28 | fconfirmamt | 确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 确认金额 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 31 | fmaterialname | 物料名称(预留字段) | varchar | 255 |  | √ | ' ' | 物料名称(预留字段) |
| 32 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 33 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 34 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 35 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 36 | fcurtaxsettlamt | 含税结算额(本位币) | numeric | 23 | 10 | √ | 0 | 含税结算额(本位币) |
| 37 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 38 | fprojectamt | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |
| 39 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 40 | fisinvoicefirst | 先开票 | bpchar | 1 |  | √ | '0' | 先开票 |
| 41 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 42 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 43 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 44 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 45 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | funverifyamt | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 49 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 50 | factunitprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 51 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 52 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 54 | fprojectlocamt | 项目收入(本位币) | numeric | 23 | 10 | √ | 0 | 项目收入(本位币) |
| 55 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 56 | frelationidstr | 先开票关联出库单明细id | text | 0 |  |  | ' ' | 先开票关联出库单明细id |
| 57 | fverifiedqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 58 | fconfirmbaseqty | 确认基本数量 | numeric | 23 | 10 | √ | 0 | 确认基本数量 |
| 59 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 60 | finvoicecustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 61 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位转换系数 |
| 62 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 63 | finventorycost | 存货成本 | numeric | 23 | 10 | √ | 0.0000000000 | 存货成本 |
| 64 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 65 | ftaxsettleamt | 含税结算额 | numeric | 23 | 10 | √ | 0 | 含税结算额 |
| 66 | fverifiedamt | 已勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_revcfmbillentry_fid |  | fid |
| 2 | idx_ar_revcfmbillentry_srcbillid |  | fsourcebillid |
| 3 | t_ar_revcfmbillentry_pkey |  | fentryid |
| 4 | idx_ar_revcfmbillentry_srcentryid |  | fsourcebillentryid |

---

## 收入成本确认单-主表 t_ar_revcfmbill

- **表名称：** 收入成本确认单-主表
- **表名：** t_ar_revcfmbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fprojectnumid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 6 | fgenerationtype | 生成方式 | bpchar | 1 |  | √ | '0' | 生成方式,枚举: 0 :其它 1 :销售出库单审核触发(先开票) 2 :财务应收单审核触发(先开票) 3 :财务应收单手工下推触发(先开票) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | frevconrate | 项目收入确认比例(%) | numeric | 23 | 10 | √ | 0 | 项目收入确认比例(%) |
| 10 | frevconway | 项目收入确认方式 | varchar | 30 |  | √ | ' ' | 项目收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 12 | fpaymentcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 13 | fsourcebillno | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_invoice :增值税发票 ar_finarbill :财务应收单 ap_finapbill :财务应付单 im_saloutbill :销售出库单 ar_busbill :暂估应收单 sm_salorder :销售订单 conm_salcontract :销售合同 ar_revcfmbill :收入成本确认单 mpm_projsaleconf :项目销售服务确认单 ar_revcfmplanbill :收入计划单 |
| 16 | fhadwrittenoff | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fconfirmrate | 收入确认比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收入确认比例(%) |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fconfirmlocamt | 确认金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 确认金额(本位币) |
| 21 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 22 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fconfirmamt | 确认金额 | numeric | 23 | 10 | √ | 0.0000000000 | 确认金额 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | fconfirmway | 确认方式 | varchar | 30 |  | √ | ' ' | 确认方式,枚举: RATE :按比例 AMOUNT :按金额 |
| 30 | fiswrittenoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 31 | fprojectamt | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |
| 32 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 33 | famount | 总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 总金额 |
| 34 | fgetcosttime | 获取成本更新时间 | timestamp | 0 |  |  | null | 获取成本更新时间 |
| 35 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 36 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应收款项性质 ar_payproperty |
| 39 | funverifyamt | 未勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽金额 |
| 40 | fbiztypeid | 业务类型(废弃) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 41 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 42 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 |
| 45 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fprojectlocamt | 项目收入(本位币) | numeric | 23 | 10 | √ | 0 | 项目收入(本位币) |
| 48 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 49 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 51 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | frevconfirmnode | 收入确认时点 | varchar | 30 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 53 | flocalamt | 总金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 总金额(本位币) |
| 54 | fprojectcostamt | 项目成本 | numeric | 23 | 10 | √ | 0 | 项目成本 |
| 55 | frecorgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 57 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 58 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 59 | finventorycost | 存货成本 | numeric | 23 | 10 | √ | 0.0000000000 | 存货成本 |
| 60 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 61 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 62 | fverifystatus | 勾稽状态 | varchar | 30 |  | √ | ' ' | 勾稽状态,枚举: unverify :未勾稽 partverify :部分勾稽 verified :全部勾稽 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_revcfmbill_bizdate |  | fbizdate |
| 2 | idx_ar_revcfmbill_org |  | forgid |
| 3 | t_ar_revcfmbill_pkey |  | fid |
| 4 | idx_ar_revcfmbill_billno |  | fbillno |
| 5 | idx_ar_revcfmbill_sourcebill |  | fsourcebillid |

---

## 收入成本确认单-关联追踪表 t_ar_revcfmbill_tc

- **表名称：** 收入成本确认单-关联追踪表
- **表名：** t_ar_revcfmbill_tc

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
| 1 | idx_ar_revcfmbill_tc_tbill |  | ftbillid |
| 2 | idx_ar_revcfmbill_tc_tid |  | ftid |
| 3 | t_ar_revcfmbill_tc_pkey |  | fid |

---

## 收入成本确认单-反写记录表 t_ar_revcfmbill_wb

- **表名称：** 收入成本确认单-反写记录表
- **表名：** t_ar_revcfmbill_wb

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
| 1 | t_ar_revcfmbill_wb_pkey |  | fentryid |
| 2 | idx_ar_revcfmbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_ar_revcfmbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_revcfmbillentry_lk

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
| 1 | idx_ar_revcfmbillentry_lk_fk |  | fentryid |
| 2 | t_ar_revcfmbillentry_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_ar_revcfmbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_revcfmbill_lk

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
| 1 | idx_ar_revcfmbill_lk_fk |  | fid |
| 2 | t_ar_revcfmbill_lk_pkey |  | fpkid |

---

## 项目成本-子表 t_ar_revcfmbillproentry

- **表名称：** 项目成本-子表
- **表名：** t_ar_revcfmbillproentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fcarriedcost | 已结转成本 | numeric | 23 | 10 | √ | 0 | 已结转成本 |
| 4 | fprobudgetcost | 项目预算成本 | numeric | 23 | 10 | √ | 0 | 项目预算成本 |
| 5 | fprojectnum | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: handleinput :手工录入 procostimport :项目成本引入 procostcalculate :项目成本计算 probudgetimport :项目预算引入 |
| 8 | fcarryratio | 结转比例(%) | numeric | 23 | 10 | √ | 0 | 结转比例(%) |
| 9 | fprojectcosttype | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 10 | famount | 本次结转成本 | numeric | 23 | 10 | √ | 0 | 本次结转成本 |
| 11 | fprojecttaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_revcfmbillproentry_fid |  | fid |
| 2 | pk_t_ar_revcfmbillproentry |  | fentryid |
