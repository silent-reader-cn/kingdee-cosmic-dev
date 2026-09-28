# 开票单-ar_invoice

## 关联子实体-子表 t_ar_invoice_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_invoice_lk

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
| 1 | idx_ar_invoice_lk_fk |  | fid |
| 2 | t_ar_invoice_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_ar_invoiceentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_invoiceentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frecamount | 价税合计_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 8 | frecamount_old | 价税合计_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_invoiceentry_lk_pkey |  | fpkid |
| 2 | idx_ar_invoiceentry_lk_fk |  | fentryid |

---

## 开票单-主表 t_ar_invoice

- **表名称：** 开票单-主表
- **表名：** t_ar_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 6 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 7 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 8 | fbuyername | 购买方名称 | varchar | 255 |  | √ | ' ' | 购买方名称 |
| 9 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fexpense | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 12 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_invoice :增值税发票 ar_finarbill :财务应收单 ar_busbill :暂估应收单 conm_salcontract :销售合同 |
| 13 | fbillstatus | 发票状态 | varchar | 5 |  | √ | ' ' | 发票状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fserialno | 开票流水号 | varchar | 50 |  | √ | ' ' | 开票流水号 |
| 15 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 16 | fimagenumber | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 17 | fbuyerid | 购买方名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: SP :专用发票(纸质) SE :专用发票(电子) GE :普通发票(纸质) ELE :普通发票(电子) OTHER :其他发票 |
| 19 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 20 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsrcbillno | 母单单号（拆票） | varchar | 50 |  | √ | ' ' | 母单单号（拆票） |
| 24 | finvoicestatus | 开票状态 | bpchar | 1 |  | √ | '0' | 开票状态,枚举: 0 :未开票 1 :已开票 2 :开票中 3 :已作废 4 :已红冲 5 :失控 6 :异常 7 :部分红冲 8 :全部红冲 9 :已拆分 |
| 25 | fpayer | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 26 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 27 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 28 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: SAL :销售 EXP :费用 |
| 29 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 32 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 33 | fsellername | 销售方名称 | varchar | 100 |  | √ | ' ' | 销售方名称 |
| 34 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 36 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 37 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 39 | fsellerid | 销售方名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 41 | fduedate | 最迟收款日期 | timestamp | 0 |  |  | null | 最迟收款日期 |
| 42 | fpaymode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 43 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 45 | frecorgid | 收款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fbizdate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 47 | fsourcebillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 48 | fchecker | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 49 | fvarianceamount | fvarianceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_invoice_fbillno |  | fbillno |
| 2 | t_ar_invoice_pkey |  | fid |
| 3 | idx_ar_invoice_forg |  | forgid,fbizdate |
| 4 | idx_ar_invoice_bizdate |  | fbizdate |

---

## 明细-子表 t_ar_invoiceentry

- **表名称：** 明细-子表
- **表名：** t_ar_invoiceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fverifiedwriteoffamt | 已红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已红冲金额 |
| 5 | frowtype | 行类型 | varchar | 30 |  | √ | ' ' | 行类型,枚举: 0 :正常行 1 :折扣行 2 :被折扣行 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 10 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 11 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本（作废） bd_materialversion |
| 14 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: order :销售订单 contract :销售合同 sm_salorder :销售订单 conm_salcontract :销售合同 |
| 15 | funverifiedwriteoffamt | 未红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未红冲金额 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 18 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 19 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 20 | facttaxunitprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 21 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 22 | finvresult | 开票结果 | varchar | 30 |  | √ | ' ' | 开票结果,枚举: 0 : 1 :成功 2 :失败 |
| 23 | ftaxclassid | 税收分类 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 24 | funverifiedwriteoffqty | 未红冲数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未红冲数量 |
| 25 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 26 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 28 | fverifiedwriteoffqty | 已红冲数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已红冲数量 |
| 29 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 32 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 33 | fconbillentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 34 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 35 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 36 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 38 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 39 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 40 | finvspectype | 开票规格型号 | varchar | 255 |  | √ | ' ' | 开票规格型号 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 43 | fquantity | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 44 | factunitprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 45 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 49 | fspectype | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 50 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 51 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0.0000000000 | 单位转换系数 |
| 52 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 53 | fassociatedamt | 关联金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联金额 |
| 54 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额(本位币) |
| 55 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 56 | fitemname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 57 | finvoiceunit | 开票单位 | varchar | 255 |  | √ | ' ' | 开票单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_ie_fid |  | fid |
| 2 | t_ar_invoiceentry_pkey |  | fentryid |

---

## 开票单-反写记录表 t_ar_invoice_wb

- **表名称：** 开票单-反写记录表
- **表名：** t_ar_invoice_wb

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
| 1 | t_ar_invoice_wb_pkey |  | fentryid |
| 2 | idx_ar_invoice_wb_fk |  | fid |

---

## 开票单-关联追踪表 t_ar_invoice_tc

- **表名称：** 开票单-关联追踪表
- **表名：** t_ar_invoice_tc

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
| 1 | t_ar_invoice_tc_pkey |  | fid |
| 2 | idx_ar_invoice_tc_tbill |  | ftbillid |
| 3 | idx_ar_invoice_tc_tid |  | ftid |

---

## 开票单-分表 t_ar_invoice_e

- **表名称：** 开票单-分表
- **表名：** t_ar_invoice_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyeraddr | 地址(买) | varchar | 100 |  | √ | ' ' | 地址(买) |
| 3 | fbuyertel | 电话(买) | varchar | 100 |  | √ | ' ' | 电话(买) |
| 4 | fbuyertin | 纳税人识别号(买) | varchar | 100 |  | √ | ' ' | 纳税人识别号(买) |
| 5 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 7 | fsplitormergeflag | 是否合并 | bpchar | 1 |  | √ | '0' | 是否合并 |
| 8 | fredflushblue | 重开发票 | bpchar | 1 |  | √ | '0' | 重开发票 |
| 9 | fblueinvoicecode | 蓝字发票代码 | varchar | 100 |  | √ | ' ' | 蓝字发票代码 |
| 10 | fisabandonreissue | 作废重开 | bpchar | 1 |  | √ | '0' | 作废重开 |
| 11 | finventoryflag | 带清单 | bpchar | 1 |  | √ | ' ' | 带清单 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 14 | fsellertin | 纳税人识别号(卖) | varchar | 100 |  | √ | ' ' | 纳税人识别号(卖) |
| 15 | fselleraddr | 地址(卖) | varchar | 100 |  | √ | ' ' | 地址(卖) |
| 16 | fsellertel | 电话(卖) | varchar | 100 |  | √ | ' ' | 电话(卖) |
| 17 | fbuyeracct | 账号(买) | varchar | 100 |  | √ | ' ' | 账号(买) |
| 18 | felepreviewurl | 电子发票预览地址 | varchar | 255 |  | √ | ' ' | 电子发票预览地址 |
| 19 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | ' ' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 |
| 20 | fblueinvoiceno | 蓝字发票号码 | varchar | 100 |  | √ | ' ' | 蓝字发票号码 |
| 21 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 22 | freopen | 重开状态 | varchar | 30 |  | √ | ' ' | 重开状态,枚举: 0 :未重开 1 :已重开 |
| 23 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 24 | fpdfurl | 电子发票下载地址 | varchar | 255 |  | √ | ' ' | 电子发票下载地址 |
| 25 | fsellerbank | 开户行(卖) | varchar | 255 |  | √ | ' ' | 开户行(卖) |
| 26 | fpaycond | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 27 | fisamount | 是否金额基准 | bpchar | 1 |  | √ | '0' | 是否金额基准 |
| 28 | fisincludetax | 录入价税合计 | bpchar | 1 |  | √ | '0' | 录入价税合计 |
| 29 | fselleracct | 账号(卖) | varchar | 100 |  | √ | ' ' | 账号(卖) |
| 30 | fbuyerbank | 开户行(买) | varchar | 255 |  | √ | ' ' | 开户行(买) |
| 31 | fcardbagurl | 卡包 | varchar | 255 |  | √ | ' ' | 卡包 |
| 32 | fredinfono | 红字信息表编号 | varchar | 100 |  | √ | ' ' | 红字信息表编号 |
| 33 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 34 | fassociatedamt | 关联金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联金额 |
| 35 | fredinvoice | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票 |
| 36 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 37 | fisoffline | 线下开票 | bpchar | 1 |  | √ | '0' | 线下开票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_invoice_e_pkey |  | fid |
| 2 | idx_ar_iex_applydate |  | fapplydate |
