# 收票单-ap_invoice

## 收票单-反写记录表 t_ap_invoice_wb

- **表名称：** 收票单-反写记录表
- **表名：** t_ap_invoice_wb

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
| 1 | idx_t_ap_invoice_wb_fid |  | fid |
| 2 | t_ap_invoice_wb_pkey |  | fentryid |

---

## 收票单-分表 t_ap_invoice_e

- **表名称：** 收票单-分表
- **表名：** t_ap_invoice_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyeraddr | 地址(买) | varchar | 100 |  | √ | ' ' | 地址(买) |
| 3 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | fbuyertel | 电话(买) | varchar | 100 |  | √ | ' ' | 电话(买) |
| 5 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 6 | fbuyertin | 纳税人识别号(买) | varchar | 100 |  | √ | ' ' | 纳税人识别号(买) |
| 7 | freceivedate | 收票日期 | timestamp | 0 |  |  | null | 收票日期 |
| 8 | fsellerbank | 开户行(卖) | varchar | 255 |  | √ | ' ' | 开户行(卖) |
| 9 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 10 | fpaycond | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 11 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 12 | fisincludetax | 录入价税合计 | bpchar | 1 |  | √ | '0' | 录入价税合计 |
| 13 | fselleracct | 账号(卖) | varchar | 100 |  | √ | ' ' | 账号(卖) |
| 14 | fbuyerbank | 开户行(买) | varchar | 255 |  | √ | ' ' | 开户行(买) |
| 15 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fsellertin | 纳税人识别号(卖) | varchar | 100 |  | √ | ' ' | 纳税人识别号(卖) |
| 18 | fselleraddr | 地址(卖) | varchar | 100 |  | √ | ' ' | 地址(卖) |
| 19 | fbuyeracct | 账号(买) | varchar | 100 |  | √ | ' ' | 账号(买) |
| 20 | fsellertel | 电话(卖) | varchar | 100 |  | √ | ' ' | 电话(卖) |
| 21 | fcheckstatus | 查验状态 | varchar | 5 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_iex_acct |  | fselleracct |
| 2 | t_ap_invoice_e_pkey |  | fid |

---

## 收票单-关联追踪表 t_ap_invoice_tc

- **表名称：** 收票单-关联追踪表
- **表名：** t_ap_invoice_tc

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
| 1 | idx_ap_invoice_tc_tbill |  | ftbillid |
| 2 | idx_ap_invoice_tc_tid |  | ftid |
| 3 | t_ap_invoice_tc_pkey |  | fid |

---

## 财务应付单分录-子表 t_ap_invoicefinentry

- **表名称：** 财务应付单分录-子表
- **表名：** t_ap_invoicefinentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fusedamt | 使用金额 | numeric | 23 | 10 | √ | 0.0000000000 | 使用金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffinid | 财务应付单ID | int8 | 64 |  | √ | 0 | 财务应付单ID |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_invoicefin_pid |  | fid |
| 2 | t_ap_invoicefinentry_pkey |  | fentryid |

---

## 收票单-主表 t_ap_invoice

- **表名称：** 收票单-主表
- **表名：** t_ap_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 3 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fistaxdeduction | 进项税抵扣 | bpchar | 1 |  | √ | '0' | 进项税抵扣 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 10 | fpaymenttype | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 11 | fbuyername | 购买方名称 | varchar | 100 |  | √ | ' ' | 购买方名称 |
| 12 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 13 | fsourcebillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fexpense | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | freceivablesacct | 收款账号 | varchar | 50 |  | √ | ' ' | 收款账号 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_invoice :发票 ap_busbill :暂估应付单 conm_purcontract :采购合同 |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fserialno | 发票流水号 | varchar | 80 |  | √ | ' ' | 发票流水号 |
| 21 | funmatchamt | 未匹配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未匹配金额 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fissuedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 24 | flastpaydate | 最迟付款日期 | timestamp | 0 |  |  | null | 最迟付款日期 |
| 25 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 26 | fbuyerid | 购买方名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: ELE :普通发票(电子) SE :专用发票(电子) GE :普通发票(纸质) SP :专用发票(纸质) PAPER :普通纸质卷票 MACH :通用机打发票 TAXI :的士票发票 TRAIN :火车票发票 PLANE :飞机票发票 OTHERCLOUD :其他发票 MOTOR :机动车销售发票 USERCAR :二手车发票 QUOTA :定额发票 TOLL :通行费电子发票 PASSENGER :客运发票 BRIDGE :过路过桥费发票 CARBOAT :车船税发票（专票） PAID :完税证明发票 STEAMER :轮船票发票 OTHER :其他发票 NORMPE :通用机打电子发票 FINE :财政电子发票 NOELETIC :全电普票 MAELETIC :全电专票 PAYLETTER :海关进口增值税专用缴款书 |
| 28 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 29 | funrelatedamt | 未关联金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联金额 |
| 30 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 31 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fsynstatus | 同步至发票云 | varchar | 30 |  | √ | ' ' | 同步至发票云,枚举: notsynchro :无需同步 waitsynchro :待同步 hassynchro :已同步 |
| 34 | foriginalgraphurl | 电子发票预览地址 | varchar | 255 |  | √ | ' ' | 电子发票预览地址 |
| 35 | fpurchaserid | fpurchaserid | int8 | 64 |  | √ | 0 |  |
| 36 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 37 | finvoicestatus | 发票状态 | varchar | 5 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 |
| 38 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 39 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 40 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 41 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: PUR :采购 FEE :费用 |
| 42 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fchangesynstatustime | 同步发票云更改时间 | timestamp | 0 |  |  | null | 同步发票云更改时间 |
| 45 | fisarchive | 是否归档 | bpchar | 1 |  | √ | ' ' | 是否归档 |
| 46 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fasstactid | 销售方名称 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 51 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 53 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 55 | fasstactname | 销售方名称 | varchar | 255 |  | √ | ' ' | 销售方名称 |
| 56 | fmatchrule | 匹配规则 | varchar | 30 |  | √ | ' ' | 匹配规则,枚举: ORDER :匹配订单 REC :匹配接收 IN :匹配验收 |
| 57 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 59 | fchecker | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 60 | freceivablessuppid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 61 | fisreffin | 应付采集 | bpchar | 1 |  | √ | ' ' | 应付采集 |
| 62 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_invoice_orgdate |  | forgid,fissuedate |
| 2 | idx_ap_invoice_billno |  | fbillno |
| 3 | idx_ap_invoice_issuedate |  | fissuedate |
| 4 | t_ap_invoice_pkey |  | fid |

---

## 关联子实体-子表 t_ap_invoiceentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_invoiceentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fquantity_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fprice_old | fprice_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 9 | fquantity | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 10 | fpricetaxtotal | 价税合计_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_确认携带值 |
| 11 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fpricetaxtotal_old | 价税合计_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_invoiceentry_lk_pkey |  | fpkid |

---

## 明细-子表 t_ap_invoiceentry

- **表名称：** 明细-子表
- **表名：** t_ap_invoiceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdiscountamt | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 8 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 10 | funmatchqty | 未匹配数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未匹配数量 |
| 11 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 |
| 12 | factpricetax | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 13 | frelatedamt | 关联金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联金额 |
| 14 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 15 | fsourcebillentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 16 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 17 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 18 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 19 | funmatchamt | 未匹配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未匹配金额 |
| 20 | ftaxclassid | 税收分类 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 21 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 22 | fdisposeqty | fdisposeqty | varchar | 50 |  | √ | ' ' |  |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | funrelatedamt | 未关联金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未关联金额 |
| 25 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 26 | famountbase | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fpricetaxtotal | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 29 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 30 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 31 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 32 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 33 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 34 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 35 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 NULL :无 |
| 36 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 37 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 38 | finvspectype | 票面规格型号 | varchar | 80 |  | √ | ' ' | 票面规格型号 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 41 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 42 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 43 | finvunit | 票面单位 | varchar | 50 |  | √ | ' ' | 票面单位 |
| 44 | fpricetaxtotalbase | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fmatchrule | 匹配规则 | varchar | 30 |  | √ | ' ' | 匹配规则,枚举: ORDER :匹配订单 REC :匹配接收 IN :匹配验收 |
| 48 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 49 | fsourcebillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 50 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 51 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_invoiceentry_pkey |  | fentryid |
| 2 | idx_ap_ie_fid |  | fid |

---

## 关联子实体-子表 t_ap_invoice_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_invoice_lk

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
| 1 | t_ap_invoice_lk_pkey |  | fpkid |
| 2 | idx_ap_invoice_lk_fk |  | fid |
