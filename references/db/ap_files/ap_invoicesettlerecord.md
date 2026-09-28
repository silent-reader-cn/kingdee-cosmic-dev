# 应付发票核销记录-ap_invoicesettlerecord

## 核销信息-分表 t_ap_invsettlerecordentry_e

- **表名称：** 核销信息-分表
- **表名：** t_ap_invsettlerecordentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fivbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 3 | fivcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 4 | fivconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fivsettlebaseunitqty | 本次核销基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销基本数量 |
| 6 | fivactpricetax | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 7 | fivbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 8 | fivtaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 9 | fivbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 10 | fivamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fivpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 12 | fivsettlepricetaxtotalbas | 本次核销价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销价税合计（本位币） |
| 13 | fiventryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 14 | fivprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fivbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fivcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 17 | fivcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 sm_salorder :销售订单 |
| 18 | fivsettlelocaltax | 本次核销税额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销税额（本位币） |
| 19 | fivlocaltotalsettleamt | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 20 | fivcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 21 | fivbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fivtaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 23 | fivsettletax | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 24 | fivamountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 25 | fivpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 26 | fivconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 27 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 28 | fivbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 29 | fivtax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 30 | fivpricetax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 31 | fivprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 32 | fivconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 33 | fivsettlepricetaxtotal | 本次核销价税合计 | numeric | 23 | 10 | √ | 0 | 本次核销价税合计 |
| 34 | fivactprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | fivtotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 37 | fivinvname | 开票名称 | varchar | 50 |  | √ | ' ' | 开票名称 |
| 38 | fiventryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_invsre_eid |  | fid |
| 2 | pk_t_ap_invsettlerecordentry_e |  | fentryid |
| 3 | idx_ap_invsre_eivbillnum |  | fivbillno |
| 4 | idx_ap_invsre_eivbillid |  | fivbillid |
| 5 | idx_ap_invsre_eiventryid |  | fiventryid |

---

## 核销信息-子表 t_ap_invsettlerecordentry

- **表名称：** 核销信息-子表
- **表名：** t_ap_invsettlerecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadamountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 3 | fapsettletax | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 4 | faptaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fadbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 7 | fapentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 8 | fapbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 9 | fadbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 10 | fadbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 11 | fadtax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 12 | fapconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fapcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_paymentapply :付款单申请单 sm_salorder :销售订单 |
| 15 | fapactprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 16 | fapsettlepricetaxtotalbas | 本次核销价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销价税合计（本位币） |
| 17 | fadamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 18 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 19 | fapprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 20 | fapamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 21 | fapisbasedonamt | 是否金额基准 | bpchar | 1 |  | √ | '0' | 是否金额基准 |
| 22 | fapsettlepricetaxtotal | 本次核销价税合计 | numeric | 23 | 10 | √ | 0 | 本次核销价税合计 |
| 23 | fapconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 24 | fapsettlelocaltax | 本次核销税额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销税额（本位币） |
| 25 | fadentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 26 | fapbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fapbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 28 | fapcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 29 | fapactpricetax | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fapcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 32 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 33 | fappricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 34 | fadtaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 35 | fapsettlebaseunitqty | 本次核销基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销基本数量 |
| 36 | fapprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 37 | fadbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fapcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 40 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 41 | fapbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 42 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 43 | fapamountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 44 | fadentryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 45 | fappricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 46 | fapbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 47 | fadpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 48 | fapentryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 49 | fassistantattr | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 50 | faptaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 51 | fapbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 52 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 53 | fappricetax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 54 | fadbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 55 | faptax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 56 | faplocaltotalsettleamt | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 57 | faptotalsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 58 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 59 | fapconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 60 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 61 | fadpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_invsre_adbillid |  | fadbillid |
| 2 | idx_ap_invsre_adbillnum |  | fadbillno |
| 3 | idx_ap_invsre_apbillid |  | fapbillid |
| 4 | idx_ap_invsre_id |  | fid |
| 5 | pk_t_ap_invsettlerecordentry |  | fentryid |
| 6 | idx_ap_invsre_apbillnum |  | fapbillno |
| 7 | idx_ap_invsre_apentryid |  | fapentryid |
| 8 | idx_ap_invsre_adentryid |  | fadentryid |

---

## 应付发票核销记录-主表 t_ap_invsettlerecord

- **表名称：** 应付发票核销记录-主表
- **表名：** t_ap_invsettlerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 |
| 4 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: apivsettle :应付发票核销 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsettleseq | 核销序号 | int4 | 32 |  | √ | 0 | 核销序号 |
| 11 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_invsr_orgdate |  | forgid,fsettledate |
| 2 | idx_ap_invsr_seq |  | fsettleseq |
| 3 | pk_t_ap_invsettlerecord |  | fid |
