# 项目决算-pac_projectsettle

## 项目成本-子表 t_pac_settlecostentry

- **表名称：** 项目成本-子表
- **表名：** t_pac_settlecostentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fclosedcost | 已结转成本 | numeric | 23 | 10 | √ | 0 | 已结转成本 |
| 4 | fbudgetexerate | 预算执行率(%) | numeric | 23 | 10 | √ | 0 | 预算执行率(%) |
| 5 | favailablebudget | 可用预算 | numeric | 23 | 10 | √ | 0 | 可用预算 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbudgetexeratevalue | 预算执行率 | varchar | 50 |  | √ | ' ' | 预算执行率 |
| 8 | fcostelement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | factualcost | 项目成本 | numeric | 23 | 10 | √ | 0 | 项目成本 |
| 10 | fsubelement | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fbudgetcost | 项目预算 | numeric | 23 | 10 | √ | 0 | 项目预算 |
| 13 | funclosedcost | 未结转成本 | numeric | 23 | 10 | √ | 0 | 未结转成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosettle_ce_sub |  | fsubelement |
| 2 | pk_t_pac_settlecostentry |  | fentryid |

---

## 项目收入-子表 t_pac_settlereventry

- **表名称：** 项目收入-子表
- **表名：** t_pac_settlereventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlecurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fprojectamt | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |
| 4 | fprojectlocamt | 项目收入（本位币） | numeric | 23 | 10 | √ | 0 | 项目收入（本位币） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 7 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fsettlecustomer | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fprojectcostamt | 项目成本 | numeric | 23 | 10 | √ | 0 | 项目成本 |
| 11 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | frevconway | 项目收入确认方式 | varchar | 50 |  | √ | ' ' | 项目收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosettle_re_id |  | fid |
| 2 | idx_pac_prosettle_re_billno |  | fbillno |
| 3 | pk_t_pac_settlereventry |  | fentryid |

---

## 项目决算-主表 t_pac_projectsettle

- **表名称：** 项目决算-主表
- **表名：** t_pac_projectsettle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapprovaldate | 立项日期 | timestamp | 0 |  |  | null | 立项日期 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fprojectamt | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |
| 5 | fprojectgroup | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 6 | fsettlestatus | 决算状态 | varchar | 50 |  | √ | ' ' | 决算状态,枚举: init_settle :发起决算 begin_settle :开始决算 final_settle :决算完成 abandon_settle :废弃 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | finvoicecustomer | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 9 | fenddate | 项目完成日期 | timestamp | 0 |  |  | null | 项目完成日期 |
| 10 | fprojectmanager | 项目经理 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fsettledate | 决算日期 | timestamp | 0 |  |  | null | 决算日期 |
| 14 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fbegindate | 项目开始日期 | timestamp | 0 |  |  | null | 项目开始日期 |
| 19 | fprojectprofit | 项目毛利 | numeric | 23 | 10 | √ | 0 | 项目毛利 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fprojectcostamt | 项目成本 | numeric | 23 | 10 | √ | 0 | 项目成本 |
| 23 | fsettleuser | 决算人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsettledept | 决算部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fprojectpgm | 项目毛利率(%) | numeric | 23 | 10 | √ | 0 | 项目毛利率(%) |
| 26 | fprojectpgmvalue | 项目毛利率 | varchar | 50 |  | √ | ' ' | 项目毛利率 |
| 27 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pac_prosettle_billno |  | fbillno |
| 2 | idx_pac_prosettle_org |  | forgid |
| 3 | pk_t_pac_projectsettle |  | fid |
| 4 | idx_pac_prosettle_proid |  | fproject |

---

## 项目总览-子表 t_pac_settlesumentry

- **表名称：** 项目总览-子表
- **表名：** t_pac_settlesumentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalecontracttotal | 销售合同总额 | numeric | 23 | 10 | √ | 0 | 销售合同总额 |
| 3 | fbusaptotal | 暂估应付总额 | numeric | 23 | 10 | √ | 0 | 暂估应付总额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsalinvoiceamt | 销售发票（金额） | numeric | 23 | 10 | √ | 0 | 销售发票（金额） |
| 6 | fpurinvoiceamt | 采购发票（金额） | numeric | 23 | 10 | √ | 0 | 采购发票（金额） |
| 7 | fpurinvoicetotal | 采购发票（总额） | numeric | 23 | 10 | √ | 0 | 采购发票（总额） |
| 8 | fsalinvoicetotal | 销售发票（总额） | numeric | 23 | 10 | √ | 0 | 销售发票（总额） |
| 9 | ffinaptotal | 财务应付（总额） | numeric | 23 | 10 | √ | 0 | 财务应付（总额） |
| 10 | fpaytotal | 付款总额 | numeric | 23 | 10 | √ | 0 | 付款总额 |
| 11 | ffinaramt | 财务应收（金额） | numeric | 23 | 10 | √ | 0 | 财务应收（金额） |
| 12 | ffinapamt | 财务应付（金额） | numeric | 23 | 10 | √ | 0 | 财务应付（金额） |
| 13 | fbusartotal | 暂估应收总额 | numeric | 23 | 10 | √ | 0 | 暂估应收总额 |
| 14 | fpremiumamt | 项目质保金 | numeric | 23 | 10 | √ | 0 | 项目质保金 |
| 15 | fclosedcost | 已结转成本 | numeric | 23 | 10 | √ | 0 | 已结转成本 |
| 16 | fprojectprofit | 项目毛利 | numeric | 23 | 10 | √ | 0 | 项目毛利 |
| 17 | fpurinvoicetax | 采购发票（税额） | numeric | 23 | 10 | √ | 0 | 采购发票（税额） |
| 18 | fsalinvoicetax | 销售发票（税额） | numeric | 23 | 10 | √ | 0 | 销售发票（税额） |
| 19 | fprojectpgm | 项目毛利率(%) | numeric | 23 | 10 | √ | 0 | 项目毛利率(%) |
| 20 | fsaleordertotal | 销售订单总额 | numeric | 23 | 10 | √ | 0 | 销售订单总额 |
| 21 | fprojectpgmvalue | 项目毛利率 | varchar | 50 |  | √ | ' ' | 项目毛利率 |
| 22 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | fconfirmamt | 已确认收入 | numeric | 23 | 10 | √ | 0 | 已确认收入 |
| 24 | frectotal | 收款总额 | numeric | 23 | 10 | √ | 0 | 收款总额 |
| 25 | ffinaptax | 财务应付（税额） | numeric | 23 | 10 | √ | 0 | 财务应付（税额） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | finvestcost | 项目投入总成本 | numeric | 23 | 10 | √ | 0 | 项目投入总成本 |
| 28 | fbudgetcost | 项目预算总成本 | numeric | 23 | 10 | √ | 0 | 项目预算总成本 |
| 29 | ffinartax | 财务应收（税额） | numeric | 23 | 10 | √ | 0 | 财务应收（税额） |
| 30 | ffinartotal | 财务应收（总额） | numeric | 23 | 10 | √ | 0 | 财务应收（总额） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_prosettle_se_id |  | fid |
| 2 | idx_prosettle_se_proid |  | fproject |
| 3 | pk_t_pac_settlesumentry |  | fentryid |
