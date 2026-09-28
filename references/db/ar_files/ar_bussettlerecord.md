# 暂估应收核销记录-ar_bussettlerecord

## 核销信息-分表 t_ar_bussettlerecordentry_a

- **表名称：** 核销信息-分表
- **表名：** t_ar_bussettlerecordentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fasstbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | fasstcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 4 | fasstinrealcard | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 5 | fasstmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fasstcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fasstexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 9 | fasstwoffbillid | 冲回单ID | int8 | 64 |  | √ | 0 | 冲回单ID |
| 10 | fasstsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 11 | fasstentryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 12 | fasstcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 13 | fasstsettlelossqty | 本次核销采购损耗数量 | numeric | 23 | 10 | √ | 0 | 本次核销采购损耗数量 |
| 14 | fasstassistantattr | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fasstpricetaxtotallocal | 价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 价税合计（本位币） |
| 16 | fasstlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 17 | fasstsettlelossbaseqty | 本次核销采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销采购损耗基本数量 |
| 18 | fasstbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fasstwoffbillno | 冲回单单据编号 | varchar | 80 |  | √ | ' ' | 冲回单单据编号 |
| 20 | fasstentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 21 | fasstsettlebaseunitqty | 本次核销基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销基本数量 |
| 22 | fasstprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fasstsettletax | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 24 | fassttaxlocal | 税额（本位币） | numeric | 23 | 10 | √ | 0 | 税额（本位币） |
| 25 | fasstbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 26 | fasstbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fasstispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 28 | fasstsettleamtlocal | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 29 | fasstquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 30 | fasstsettletaxlocal | 本次核销税额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销税额（本位币） |
| 31 | fassttax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 32 | fasstbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 33 | fasstasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 34 | fasstsettlepricetaxlocal | 本次核销价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销价税合计（本位币） |
| 35 | fasstcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_out_contract_settle :支出合同结算 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 36 | fasstamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 37 | fasstmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fasstbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 39 | fasstsettlepricetaxtotal | 本次核销价税合计 | numeric | 23 | 10 | √ | 0 | 本次核销价税合计 |
| 40 | fasstbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 41 | fasstamountlocal | 金额（本位币） | numeric | 23 | 10 | √ | 0 | 金额（本位币） |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fasstmeasureunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 44 | fasstbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 45 | fasstasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 46 | fasstpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 47 | fasstsettleunitqty | 本次核销数量 | numeric | 23 | 10 | √ | 0 | 本次核销数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_bussetrec_e_a_billid |  | fasstbillid |
| 2 | idx_ar_bussetrec_e_a_woffno |  | fasstwoffbillno |
| 3 | idx_ar_bussetrec_e_a_id |  | fid |
| 4 | idx_ar_bussetrec_e_a_woffid |  | fasstwoffbillid |
| 5 | idx_ar_bussetrec_e_a_billno |  | fasstbillno |
| 6 | idx_ar_bussetrec_e_a_billeid |  | fasstentryid |
| 7 | pk_t_ar_bussettlerecordentry_a |  | fentryid |

---

## 暂估应收核销记录-主表 t_ar_bussettlerecord

- **表名称：** 暂估应收核销记录-主表
- **表名：** t_ar_bussettlerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsettletype | 核销类型 | varchar | 30 |  | √ | ' ' | 核销类型,枚举: auto :自动核销 manual :手工核销 match :方案核销 |
| 4 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: arbusfinsettle :应收暂估财务核销 arbusself :应收暂估红蓝核销 arbusspecialsettle :应收暂估特殊核销 |
| 5 | fissettlebase | 是否金额基准 | bpchar | 1 |  | √ | '0' | 是否金额基准 |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsettleseq | 核销序号 | int4 | 32 |  | √ | 0 | 核销序号 |
| 12 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fsettledate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_bussettle_sdq |  | fsettleseq |
| 2 | idx_ar_bussettle_billno |  | fbillno |
| 3 | idx_ar_bussettl_orgdate |  | forgid,fsettledate |
| 4 | pk_t_ar_bussettlerecord |  | fid |

---

## 核销信息-子表 t_ar_bussettlerecordentry

- **表名称：** 核销信息-子表
- **表名：** t_ar_bussettlerecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 3 | fmainwoffbillid | 冲回单ID | int8 | 64 |  | √ | 0 | 冲回单ID |
| 4 | fmaincorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 5 | fmainsettlepricetaxlocal | 本次核销价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销价税合计（本位币） |
| 6 | fmainpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 7 | fmainquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fmainbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 9 | fmainbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fmainsettlebaseunitqty | 本次核销基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销基本数量 |
| 11 | fmainprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 12 | fmaintaxlocal | 税额（本位币） | numeric | 23 | 10 | √ | 0 | 税额（本位币） |
| 13 | fmainsettleunitqty | 本次核销数量 | numeric | 23 | 10 | √ | 0 | 本次核销数量 |
| 14 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 15 | fmainassistantattr | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fmainasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 17 | fmainbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fmainsettlelossbaseqty | 本次核销采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 本次核销采购损耗基本数量 |
| 19 | fmainsettletax | 本次核销税额 | numeric | 23 | 10 | √ | 0 | 本次核销税额 |
| 20 | fmainmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fmainsettleamt | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 22 | fmainbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 23 | fmainsettleamtlocal | 本次核销金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销金额（本位币） |
| 24 | fmaininrealcard | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 25 | fmainsettletaxlocal | 本次核销税额（本位币） | numeric | 23 | 10 | √ | 0 | 本次核销税额（本位币） |
| 26 | fmainsettlelossqty | 本次核销采购损耗数量 | numeric | 23 | 10 | √ | 0 | 本次核销采购损耗数量 |
| 27 | fmaincurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fmainamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 29 | fmainbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 30 | fmainwoffbillno | 冲回单单据编号 | varchar | 80 |  | √ | ' ' | 冲回单单据编号 |
| 31 | fmainbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fmaincorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 ec_out_contract_settle :支出合同结算 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 sm_salorder :销售订单 im_transapply :调拨申请单 sfc_processplanbill :工序计划 |
| 33 | fmaintax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 34 | fmainexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 35 | fmainentryseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 36 | fmainasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 37 | fmainsettlepricetaxtotal | 本次核销价税合计 | numeric | 23 | 10 | √ | 0 | 本次核销价税合计 |
| 38 | fmainbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 39 | fmainlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 40 | fmainmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 41 | fmainpricetaxtotallocal | 价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 价税合计（本位币） |
| 42 | fmainamountlocal | 金额（本位币） | numeric | 23 | 10 | √ | 0 | 金额（本位币） |
| 43 | fmainbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fmainmeasureunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | fmainentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_bussettlerecordentry |  | fentryid |
| 2 | idx_ar_bussetrec_e_billno |  | fmainbillno |
| 3 | idx_ar_bussetrec_e_woffno |  | fmainwoffbillno |
| 4 | idx_ar_bussetrec_e_billid |  | fmainbillid |
| 5 | idx_ar_bussetrec_e_id |  | fid |
| 6 | idx_ar_bussetrec_e_billeid |  | fmainentryid |
| 7 | idx_ar_bussetrec_e_woffid |  | fmainwoffbillid |
