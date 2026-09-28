# 应付核销单-ap_settlebill

## 应付核销单-主表 t_ap_settlebill

- **表名称：** 应付核销单-主表
- **表名：** t_ap_settlebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0 | 汇兑损益 |
| 7 | fmainbillentity | 主方实体标识 | varchar | 50 |  | √ | ' ' | 主方实体标识 |
| 8 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 cas_paymentbilltype :付款类型 ar_payproperty :应收款项性质 cas_receivingbilltype :收款类型 |
| 10 | fsettlelogentryid | 核销日志分录id | int8 | 64 |  | √ | 0 | 核销日志分录id |
| 11 | freceivingtypeid | 主方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 14 | fmainbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 15 | fpaypropertyfield | 款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 18 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | fbillstatus | 核销单状态 | varchar | 30 |  | √ | ' ' | 核销单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 24 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsettleseq | 核销序号 | int4 | 32 |  | √ | 0 | 核销序号 |
| 27 | fautosettletype | 自动核销参数类型 | varchar | 30 |  | √ | '0' | 自动核销参数类型,枚举: 1 :BOTP自动核销 2 :核心单据号自动核销 3 :其它 4 :BOTP自动核销(断关系) |
| 28 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fmainbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 33 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 34 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 35 | fasstreceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 36 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 37 | fiswrittenoff | 是否红冲生成 | bpchar | 1 |  | √ | '0' | 是否红冲生成 |
| 38 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 39 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | flocaltotalsettleamt | 核销金额(本位币) | numeric | 23 | 10 | √ | 0 | 核销金额(本位币) |
| 41 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 42 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fpayableamt | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 45 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 46 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 manual :手工核销 match :方案匹配核销 import :引入核销 rpamatch :RPA方案核销 |
| 49 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 liqsettle :应付清理 paytrans :应付转销 payself :付款红蓝对冲 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 appaidsettle :采购期初预付 arapsettle :应收冲应付 recpaysettle :收款冲退款 arpaysettle :应收退款核销 payclearing :付款清理 payrefundclearing :付款退款清理 |
| 50 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fplanduedate | 计划到期日 | timestamp | 0 |  |  | null | 计划到期日 |
| 53 | ftotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 54 | fbilltypenewid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 55 | fsettlerecordid | 核销记录id | int8 | 64 |  | √ | 0 | 核销记录id |
| 56 | fasstactname | 往来单位名称 | varchar | 255 |  | √ | ' ' | 往来单位名称 |
| 57 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 58 | fmainbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 59 | fasstpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 60 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 61 | fmainasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 62 | fpaymenttypeid | 主方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 63 | fiscahsale | 现销现购 | bpchar | 1 |  | √ | ' ' | 现销现购 |
| 64 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 65 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 66 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_sb_asstact |  | fmainasstactid |
| 2 | idx_ap_sb_mainbillentryid |  | fmainbillentryid |
| 3 | idx_ap_sb_mainbillid |  | fmainbillid |
| 4 | idx_ap_sb_orgdateseq |  | forgid,fsettledate,fsettleseq |
| 5 | pk_t_ap_settlebill |  | fid |
| 6 | idx_ap_sb_settlerecordid |  | fsettlerecordid |
| 7 | idx_ap_sb_mainbillno |  | fmainbillno |
| 8 | idx_ap_sb_logentry |  | fsettlelogentryid |
| 9 | idx_ap_sb_billno |  | fbillno |

---

## 单据体-子表 t_ap_settlebillentry

- **表名称：** 单据体-子表
- **表名：** t_ap_settlebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurchaserid | 辅方采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | fexratetable | 辅方汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 4 | fmaterialid | 辅方物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fasstact | 辅方往来单位名称 | varchar | 255 |  | √ | ' ' | 辅方往来单位名称 |
| 6 | fsalesmanid | 辅方销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | fisdiffcurrencysettle | 异币别核销 | bpchar | 1 |  | √ | '0' | 异币别核销 |
| 8 | fswappl | 辅方汇兑损益 | numeric | 23 | 10 | √ | 0 | 辅方汇兑损益 |
| 9 | fsettlelocalamt | 辅方核销金额(本位币) | numeric | 23 | 10 | √ | 0 | 辅方核销金额(本位币) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fpurdepartmentid | 辅方采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fbilldate | 辅方业务日期 | timestamp | 0 |  |  | null | 辅方业务日期 |
| 13 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 14 | fsettleamt | 辅方本次核销金额 | numeric | 23 | 10 | √ | 0 | 辅方本次核销金额 |
| 15 | fpaypropertytype | 款项性质类型 | varchar | 30 |  | √ | ' ' | 款项性质类型,枚举: ap_payproperty :应付款项性质 ar_payproperty :应收款项性质 cas_receivingbilltype :收款类型 cas_paymentbilltype :付款类型 |
| 16 | fpurdeptid | 辅方采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 17 | fsettlerecordentryid | 核销记录明细id | int8 | 64 |  | √ | 0 | 核销记录明细id |
| 18 | freceivingtypeid | 辅方收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 19 | fcorebillno | 辅方核心单据号 | varchar | 255 |  | √ | ' ' | 辅方核心单据号 |
| 20 | fexchangerate | 辅方汇率 | numeric | 23 | 10 | √ | 0 | 辅方汇率 |
| 21 | fpaypropertyfield | 辅方款项性质值 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 22 | fquotation | 辅方换算方式 | varchar | 30 |  | √ | '0' | 辅方换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 23 | fbillnum | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 24 | fpayableamt | 辅方应付金额 | numeric | 23 | 10 | √ | 0 | 辅方应付金额 |
| 25 | fbiztypeid | 辅方业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 26 | fbillentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 27 | fexpenseitemid | 辅方费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 28 | fpurorgid | 辅方采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fhadwrittenoff | 已被红冲 | bpchar | 1 |  | √ | '0' | 已被红冲 |
| 30 | fprojectid | 辅方项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fmpmtasknoid | 辅方项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 32 | fsettleentry | 核销明细配置 | varchar | 30 |  | √ | ' ' | 核销明细配置,枚举: 1 :按物料行核销 2 :按计划行核销 |
| 33 | fsalesdeptid | 辅方销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fplanduedate | 辅方计划到期日 | timestamp | 0 |  |  | null | 辅方计划到期日 |
| 35 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | fbilltypenewid | 辅方单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 37 | fdescription | 摘要 | varchar | 512 |  | √ | ' ' | 摘要 |
| 38 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 39 | fpaymenttypeid | 辅方付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 40 | fsalesorgid | 辅方销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | fsalesgroupid | 辅方销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 45 | fisperiod | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_settlebillentry |  | fentryid |
| 2 | idx_ap_sbe_billnum |  | fbillnum |
| 3 | idx_ap_sbe_asstact |  | fasstactid |
| 4 | idx_ap_sbe_pid |  | fid |
| 5 | idx_ap_sbe_billid |  | fbillid |
