# 采购发票单-iv_purchasebill

## 采购发票单-主表 t_iv_purchasebill

- **表名称：** 采购发票单-主表
- **表名：** t_iv_purchasebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fredorblue | 红蓝字 | varchar | 80 |  | √ | ' ' | 红蓝字,枚举: blue :蓝字 red :红字 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdiscountamt | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 8 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 9 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fscmbilltype | 供应链单据标识 | varchar | 30 |  | √ | ' ' | 供应链单据标识,枚举: pm_purorderbill :采购订单 im_purinbill :采购入库 conm_purcontract :采购合同 im_mdc_ominbill :简单委外入库单 im_mdc_omcmplinbill :委外完工入库单 pm_om_purorderbill :简单委外订单 sctm_scpo :委外采购订单 im_ospurinbill :委外采购入库单 pm_puracceptbill :采购验收单 sfc_processsettlebill :工序结算单 |
| 12 | fsourcebillno | 源单编码（废弃） | varchar | 255 |  | √ | ' ' | 源单编码（废弃） |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_finapbill :财务应付单 iv_purchasebill :采购发票单 pm_purorderbill :采购订单 im_purinbill :采购入库单 |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fdeliverycountry | 交货国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 19 | fdeliveryaddr | 交货地址 | varchar | 200 |  | √ | ' ' | 交货地址 |
| 20 | fpaycondition | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 21 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 24 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 25 | foperategroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | foperatemanid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 28 | fisinputtaxded | 进项税抵扣 | bpchar | 1 |  | √ | ' ' | 进项税抵扣 |
| 29 | fisinvoicediffmode | 发票差异模式 | bpchar | 1 |  | √ | '0' | 发票差异模式 |
| 30 | flinkedordernumber | 关联订单编码 | varchar | 50 |  | √ | ' ' | 关联订单编码 |
| 31 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 32 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 33 | fivtype | 发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 34 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 37 | fselleraddr | 销售方地址 | varchar | 2000 |  | √ | ' ' | 销售方地址 |
| 38 | fivcategory | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型 bd_invoicecategory](../basedata_files/bd_invoicecategory.md) |
| 39 | fremark | 开票备注 | varchar | 512 |  | √ | ' ' | 开票备注 |
| 40 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | '0' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从应付引入 5 :API生成 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | fdeliverydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 45 | fivcontext | 开票类型 | int8 | 64 |  | √ | 0 | [开票类型 bd_invoicecontext](../basedata_files/bd_invoicecontext.md) |
| 46 | fissueivstatus | 开票状态 | varchar | 50 |  | √ | ' ' | 开票状态,枚举: NOT_APPLIED :未申请 UNINVOICED :未开票 INVOICING :开票中 PART_SUCCESS :部分开票成功 ALL_SUCCESS :全部开票成功 ALL_FAILED :全部开票失败 |
| 47 | foperateorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 49 | fbasecurrencyid | 本位币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 51 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 52 | foperatedeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 54 | fsellerbankname | 销售方银行账户名称 | varchar | 255 |  | √ | ' ' | 销售方银行账户名称 |
| 55 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 56 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 57 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_pur_fbillno |  | fbillno |
| 2 | idx_iv_pur_bizdate |  | fbizdate |
| 3 | idx_iv_pur_orgdate |  | forgid,fbizdate |
| 4 | idx_iv_pur_sourcebillid |  | fsourcebillid |
| 5 | pk_t_iv_purchasebill |  | fid |
| 6 | idx_iv_pur_asstact |  | fasstactid |

---

## 采购发票单-反写记录表 t_iv_purchasebill_wb

- **表名称：** 采购发票单-反写记录表
- **表名：** t_iv_purchasebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iv_purchasebill_wb |  | fentryid |
| 2 | idx_iv_purchasebill_wb_fk |  | fid |

---

## 关联子实体-子表 t_iv_purchasebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_purchasebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iv_purchasebill_lk |  | fpkid |
| 2 | idx_iv_purchasebill_lk_fk |  | fid |

---

## 已开票信息-子表 t_iv_purchaseinvoicedinfo

- **表名称：** 已开票信息-子表
- **表名：** t_iv_purchaseinvoicedinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgpdfaddr | 板式文件地址(PDF) | varchar | 2000 |  | √ | ' ' | 板式文件地址(PDF) |
| 3 | fgtax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fgivnumber | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 5 | fgivdate | 发票开具日期 | timestamp | 0 |  |  | null | 发票开具日期 |
| 6 | fgorigivcode | 原发票代码 | varchar | 50 |  | √ | ' ' | 原发票代码 |
| 7 | fgorigivdate | 原发票日期 | timestamp | 0 |  |  | null | 原发票日期 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fgamt | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fgivcode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 11 | fgxmladdr | 板式文件地址(XML) | varchar | 2000 |  | √ | ' ' | 板式文件地址(XML) |
| 12 | fgivtype | 发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 13 | fgivstatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: NORMAL :正常 WRITE_OFF :红冲 VOIDED :作废 PENDING_VOID :作废中 |
| 14 | fgivcategory | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型 bd_invoicecategory](../basedata_files/bd_invoicecategory.md) |
| 15 | fgorigivnumber | 原发票号码 | varchar | 50 |  | √ | ' ' | 原发票号码 |
| 16 | fgamtlocal | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 17 | fgtaxpriceamt | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 18 | fgtaxlocal | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 19 | fgtaxpriceamtlocal | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_purinfo_pid |  | fid |
| 2 | pk_t_iv_purchaseinvoicedinfo |  | fentryid |

---

## 明细-子表 t_iv_purchasebillentry

- **表名称：** 明细-子表
- **表名：** t_iv_purchasebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 4 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 6 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fe_srcbillentityid | 源单分录内码ID | int8 | 64 |  | √ | 0 | 源单分录内码ID |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 11 | fsrcbillentryseq | 源单单据行号 | varchar | 2000 |  |  | ' ' | 源单单据行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | finvoicesupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fmaterialversionid | 物料/费用项目版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | fe_red_quantity | 关联红字发票数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票数量 |
| 17 | fe_red_basequantity | 关联红字发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票基本数量 |
| 18 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 conm_purcontract :采购合同 sm_salorder :销售订单 |
| 19 | fe_amount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 20 | fe_reclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 21 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 22 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  |  | ' ' | 尾差调整日志 |
| 23 | fexpenseitemid | 费用项目名称 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 24 | fscmentryid | 供应链单据分录ID | int8 | 64 |  | √ | 0 | 供应链单据分录ID |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 27 | fsrcbillid | 源单ID-废弃 | varchar | 255 |  | √ | ' ' | 源单ID-废弃 |
| 28 | ffarmproducts | 农产品 | bpchar | 1 |  | √ | '0' | 农产品 |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 30 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 31 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 32 | fsrcbillnoiv | 源单单据编号 | varchar | 2000 |  |  | ' ' | 源单单据编号 |
| 33 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 34 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 35 | fe_localamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 36 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fe_recamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 40 | fe_sourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_finapbill :财务应付单 iv_purchasebill :采购发票单 pm_purorderbill :采购订单 im_purinbill :采购入库单 |
| 41 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 42 | fsrcbillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 43 | fe_srcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 44 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 45 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 46 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 47 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 48 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 49 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 50 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 51 | fe_materialname | fe_materialname | varchar | 255 |  | √ | ' ' |  |
| 52 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 53 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 54 | fe_remark | 备注说明 | varchar | 512 |  | √ | ' ' | 备注说明 |
| 55 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 56 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 57 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 58 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 59 | fe_tax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 60 | fsrcbilltypenum | 源单单据类型编码 | varchar | 255 |  | √ | ' ' | 源单单据类型编码 |
| 61 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 62 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 63 | fspectype | 规格型号 | varchar | 512 |  | √ | ' ' | 规格型号 |
| 64 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0 | 单位转换系数 |
| 65 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 66 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 67 | fmeasureunitid | 开票单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 68 | fsrcbillentityid | 源单分录内码ID-废弃 | varchar | 255 |  | √ | ' ' | 源单分录内码ID-废弃 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_purentry_srcbiilid |  | fe_srcbillid |
| 2 | idx_iv_purentry_corebill |  | fcorebillno,fcorebillentryseq |
| 3 | idx_iv_purentry_srcentryid |  | fe_srcbillentityid |
| 4 | pk_t_iv_purchasebillentry |  | fentryid |
| 5 | idx_iv_purentry_pid |  | fid |
| 6 | idx_iv_purentry_sourcebillid |  | fsrcbillid |

---

## 关联子实体-子表 t_iv_purchasebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_purchasebillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fe_recamount_old | 价税合计_原始携带值 | numeric | 23 | 10 |  | null | 价税合计_原始携带值 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fquantity_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbaseunitqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 7 | fbaseunitqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 8 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 9 | fe_reclocalamt_old | 价税合计(本位币)_原始携带值 | numeric | 23 | 10 |  | null | 价税合计(本位币)_原始携带值 |
| 10 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 12 | fquantity | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 13 | fe_reclocalamt | 价税合计(本位币)_确认携带值 | numeric | 23 | 10 |  | null | 价税合计(本位币)_确认携带值 |
| 14 | fe_recamount | 价税合计_确认携带值 | numeric | 23 | 10 |  | null | 价税合计_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iv_purchasebillentry_lk |  | fpkid |
| 2 | idx_iv_purchasebillentry_lk_fk |  | fentryid |

---

## 采购发票单-关联追踪表 t_iv_purchasebill_tc

- **表名称：** 采购发票单-关联追踪表
- **表名：** t_iv_purchasebill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iv_purchasebill_tc |  | fid |
| 2 | idx_iv_purchasebill_tc_tid |  | ftid |
| 3 | idx_iv_purchasebill_tc_tbill |  | ftbillid |

---

## 采购发票单-多语言表 t_iv_purchasebill_l

- **表名称：** 采购发票单-多语言表
- **表名：** t_iv_purchasebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsellerbankname | 销售方银行账户名称 | varchar | 255 |  | √ | ' ' | 销售方银行账户名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fselleraddr | 销售方地址 | varchar | 2000 |  | √ | ' ' | 销售方地址 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iv_purchasebill_l |  | fpkid |
| 2 | idx_iv_purchasebill_l_locale |  | fid,flocaleid |

---

## 采购发票单-分表 t_iv_purchasebill_e

- **表名称：** 采购发票单-分表
- **表名：** t_iv_purchasebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsellertaxregnum | 销售方纳税人识别号 | varchar | 200 |  | √ | ' ' | 销售方纳税人识别号 |
| 3 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 4 | forigivcode | 原发票代码 | varchar | 50 |  | √ | ' ' | 原发票代码 |
| 5 | forigivdate | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 6 | fselleremail | 销售方电子邮箱 | varchar | 200 |  | √ | ' ' | 销售方电子邮箱 |
| 7 | fsellerbankaccount | 销售方银行账号 | varchar | 200 |  | √ | ' ' | 销售方银行账号 |
| 8 | fadjustreason | 调整原因 | varchar | 2000 |  | √ | ' ' | 调整原因 |
| 9 | forigivnumber | 原发票号码 | varchar | 50 |  | √ | ' ' | 原发票号码 |
| 10 | fsellercountry | 销售方国家和地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 11 | fsellerpostcode | 销售方邮编 | varchar | 50 |  | √ | ' ' | 销售方邮编 |
| 12 | fsellerphone | 销售方电话 | varchar | 50 |  | √ | ' ' | 销售方电话 |
| 13 | forigivtype | 原发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 14 | fselleradmindivision | 销售方行政区划 | varchar | 100 |  | √ | ' ' | 销售方行政区划 |
| 15 | fseller | 销售方名称 | varchar | 200 |  | √ | ' ' | 销售方名称 |
| 16 | fsellersettletype | 销售方结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 17 | fsellercontact | 销售方联系人 | varchar | 50 |  | √ | ' ' | 销售方联系人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iv_purchasebill_e |  | fid |

---

## 明细-分表 t_iv_purchasebillentry_e

- **表名称：** 明细-分表
- **表名：** t_iv_purchasebillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettleinvloctax | 已核销采购发票税额(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票税额(本位币) |
| 3 | fsettleinvlocamt | 已核销采购发票金额(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票金额(本位币) |
| 4 | fredpricetax | 关联红字发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联红字发票价税合计 |
| 5 | funsettleinvpricetax | 未核销采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 未核销采购发票价税合计 |
| 6 | funsettleinvlocpricetax | 未核销采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票价税合计(本位币) |
| 7 | fsettleinvpricetax | 已核销采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 已核销采购发票价税合计 |
| 8 | fsettleinvtax | 已核销采购发票税额 | numeric | 23 | 10 | √ | 0 | 已核销采购发票税额 |
| 9 | fsettleinvbaseqty | 已核销采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 已核销采购发票基本数量 |
| 10 | funsettleinvtax | 未核销采购发票税额 | numeric | 23 | 10 | √ | 0 | 未核销采购发票税额 |
| 11 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 12 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 13 | funsettleinvloctax | 未核销采购发票税额(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票税额(本位币) |
| 14 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 15 | funsettleinvbaseqty | 未核销采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 未核销采购发票基本数量 |
| 16 | funsettleinvlocamt | 未核销采购发票金额(本位币) | numeric | 23 | 10 | √ | 0 | 未核销采购发票金额(本位币) |
| 17 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | [应付款项性质 ap_payproperty](../ap_files/ap_payproperty.md) |
| 18 | fredpricetaxloc | 关联红字发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 关联红字发票价税合计(本位币) |
| 19 | fsettleinvamount | 已核销采购发票金额 | numeric | 23 | 10 | √ | 0 | 已核销采购发票金额 |
| 20 | fsettleinvlocpricetax | 已核销采购发票价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已核销采购发票价税合计(本位币) |
| 21 | ffullygetinvoice | 已完全到票 | bpchar | 1 |  | √ | '0' | 已完全到票 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | funsettleinvamount | 未核销采购发票金额 | numeric | 23 | 10 | √ | 0 | 未核销采购发票金额 |
| 24 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iv_purchasebillentry_e |  | fentryid |
| 2 | idx_iv_purentry_e_pid |  | fid |
