# 销售发票单-iv_salebill

## 销售发票单-主表 t_iv_salebill

- **表名称：** 销售发票单-主表
- **表名：** t_iv_salebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购买方地址 | varchar | 2000 |  | √ | ' ' | 购买方地址 |
| 3 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fredorblue | 红蓝字 | varchar | 80 |  | √ | ' ' | 红蓝字,枚举: blue :蓝字 red :红字 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fdiscountamt | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | frecamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 9 | fispricetotal | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 10 | fisinclusivetax | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | finvctrlmode | 项目开票控制方式 | varchar | 30 |  | √ | ' ' | 项目开票控制方式,枚举: A :按数量控制 B :按金额控制 |
| 13 | fsourcebillno | 源单编码（废弃） | varchar | 255 |  | √ | ' ' | 源单编码（废弃） |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_finarbill :财务应收单 im_saloutbill :销售出库单 sm_salorder :销售订单 iv_salebill :销售发票单 mpm_projinvapply :项目开票申请单 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fisvmark | 发票云调用标识 | bpchar | 1 |  | √ | '0' | 发票云调用标识 |
| 18 | fdeliverycountry | 交货国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 19 | fbuyerbankname | 购买方银行账户名称 | varchar | 255 |  | √ | ' ' | 购买方银行账户名称 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 22 | fdeliveryaddr | 交货地址 | varchar | 200 |  | √ | ' ' | 交货地址 |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 26 | freclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 27 | foperategroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | foperatemanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 30 | flinkedordernumber | 关联订单编码 | varchar | 50 |  | √ | ' ' | 关联订单编码 |
| 31 | fasstacttype | 往来单位类型 | varchar | 30 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 32 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 33 | fivtype | 发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 34 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | ftaxlocamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 37 | fivcategory | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型 bd_invoicecategory](../basedata_files/bd_invoicecategory.md) |
| 38 | fremark | 开票备注 | varchar | 512 |  | √ | ' ' | 开票备注 |
| 39 | fbillsrctype | 单据来源类型 | varchar | 30 |  | √ | '0' | 单据来源类型,枚举: 0 :手工新增 1 :导入生成 2 :后台生成 3 :从应收引入 5 :API生成 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 43 | fdeliverydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 44 | fivcontext | 开票类型 | int8 | 64 |  | √ | 0 | [开票类型 bd_invoicecontext](../basedata_files/bd_invoicecontext.md) |
| 45 | freccondition | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 46 | fissueivstatus | 开票状态 | varchar | 50 |  | √ | ' ' | 开票状态,枚举: NOT_APPLIED :未申请 UNINVOICED :未开票 INVOICING :开票中 PART_SUCCESS :部分开票成功 ALL_SUCCESS :全部开票成功 ALL_FAILED :全部开票失败 |
| 47 | foperateorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 49 | fbasecurrencyid | 本位币币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | flocalamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 51 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 52 | foperatedeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fsourcebillid | 源单ID | varchar | 255 |  | √ | ' ' | 源单ID |
| 54 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 55 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 56 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 57 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_salebill_sourcebillid |  | fsourcebillid |
| 2 | pk_t_iv_salebill |  | fid |
| 3 | idx_iv_salebill_bizdate |  | fbizdate |
| 4 | idx_iv_salebill_fbillno |  | fbillno |
| 5 | idx_iv_salebill_orgdate |  | forgid,fbizdate |
| 6 | idx_iv_salebill_asstact |  | fasstactid |

---

## 关联子实体-子表 t_iv_salebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_salebillentry_lk

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
| 1 | pk_iv_salebillentry_lk |  | fpkid |
| 2 | idx_iv_salebillentry_lk_fk |  | fentryid |

---

## 明细-分表 t_iv_salebillentry_e

- **表名称：** 明细-分表
- **表名：** t_iv_salebillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvdifftax | 发票尾差税额 | numeric | 23 | 10 | √ | 0 | 发票尾差税额 |
| 3 | finvdiffamt | 发票尾差金额 | numeric | 23 | 10 | √ | 0 | 发票尾差金额 |
| 4 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 5 | finvdifftaxlocamt | 发票尾差税额(本位币) | numeric | 23 | 10 | √ | 0 | 发票尾差税额(本位币) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | finvdifflocalamt | 发票尾差金额(本位币) | numeric | 23 | 10 | √ | 0 | 发票尾差金额(本位币) |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_iv_salebillentry_e_pid |  | fid |
| 2 | pk_t_iv_salebillentry_e |  | fentryid |

---

## 销售发票单-分表 t_iv_salebill_e

- **表名称：** 销售发票单-分表
- **表名：** t_iv_salebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyerbankaccount | 购买方银行账号 | varchar | 200 |  | √ | ' ' | 购买方银行账号 |
| 3 | fbuyercountry | 购买方国家和地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 4 | fbuyer | 购买方名称 | varchar | 200 |  | √ | ' ' | 购买方名称 |
| 5 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 6 | forigivcode | 原发票代码 | varchar | 50 |  | √ | ' ' | 原发票代码 |
| 7 | forigivdate | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 8 | fbuyerphone | 购买方电话 | varchar | 50 |  | √ | ' ' | 购买方电话 |
| 9 | fadjustreason | 调整原因 | varchar | 2000 |  | √ | ' ' | 调整原因 |
| 10 | fbuyersettletype | 购买方结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 11 | fbuyerpostcode | 购买方邮编 | varchar | 50 |  | √ | ' ' | 购买方邮编 |
| 12 | forigivnumber | 原发票号码 | varchar | 50 |  | √ | ' ' | 原发票号码 |
| 13 | fbuyertaxregnum | 购买方纳税人识别号 | varchar | 200 |  | √ | ' ' | 购买方纳税人识别号 |
| 14 | fbuyeradmindivision | 购买方行政区划 | varchar | 100 |  | √ | ' ' | 购买方行政区划 |
| 15 | fbuyercontact | 购买方联系人 | varchar | 50 |  | √ | ' ' | 购买方联系人 |
| 16 | forigivtype | 原发票种类 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 17 | fbuyeremail | 购买方电子邮箱 | varchar | 200 |  | √ | ' ' | 购买方电子邮箱 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iv_salebill_e |  | fid |

---

## 销售发票单-关联追踪表 t_iv_salebill_tc

- **表名称：** 销售发票单-关联追踪表
- **表名：** t_iv_salebill_tc

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
| 1 | pk_iv_salebill_tc |  | fid |
| 2 | idx_iv_salebill_tc_tbill |  | ftbillid |
| 3 | idx_iv_salebill_tc_tid |  | ftid |

---

## 已开票信息-子表 t_iv_saleinvoicedinfo

- **表名称：** 已开票信息-子表
- **表名：** t_iv_saleinvoicedinfo

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
| 1 | idx_iv_saleinfo_pid |  | fid |
| 2 | pk_t_iv_saleinvoicedinfo |  | fentryid |

---

## 关联子实体-子表 t_iv_salebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_iv_salebill_lk

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
| 1 | idx_iv_salebill_lk_fk |  | fid |
| 2 | pk_iv_salebill_lk |  | fpkid |

---

## 销售发票单-多语言表 t_iv_salebill_l

- **表名称：** 销售发票单-多语言表
- **表名：** t_iv_salebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyeraddr | 购买方地址 | varchar | 2000 |  | √ | ' ' | 购买方地址 |
| 3 | fbuyerbankname | 购买方银行账户名称 | varchar | 255 |  | √ | ' ' | 购买方银行账户名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iv_salebill_l_locale |  | fid,flocaleid |
| 2 | pk_iv_salebill_l |  | fpkid |

---

## 销售发票单-反写记录表 t_iv_salebill_wb

- **表名称：** 销售发票单-反写记录表
- **表名：** t_iv_salebill_wb

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
| 1 | idx_iv_salebill_wb_fk |  | fid |
| 2 | pk_iv_salebill_wb |  | fentryid |

---

## 明细-子表 t_iv_salebillentry

- **表名称：** 明细-子表
- **表名：** t_iv_salebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同 | varchar | 255 |  | √ | ' ' | 合同 |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fe_srcbillentityid | 源单分录内码ID | int8 | 64 |  | √ | 0 | 源单分录内码ID |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 10 | fsrcbillentryseq | 源单单据行号 | varchar | 2000 |  |  | ' ' | 源单单据行号 |
| 11 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 12 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | fmaterialversionid | 物料/费用项目版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fe_red_quantity | 关联红字发票数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票数量 |
| 15 | fdelivercustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 16 | fe_red_basequantity | 关联红字发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联红字发票基本数量 |
| 17 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: sm_salorder :销售订单 conm_salcontract :销售合同 pm_purorderbill :采购订单 |
| 18 | fe_amount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 19 | fe_reclocalamt | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 20 | ftaxlocalamt | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 21 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  |  | ' ' | 尾差调整日志 |
| 22 | fexpenseitemid | 费用项目名称 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 25 | fsrcbillid | 源单ID-废弃 | varchar | 255 |  | √ | ' ' | 源单ID-废弃 |
| 26 | facttaxunitprice | 实际含税单价-废弃 | numeric | 23 | 10 | √ | 0 | 实际含税单价-废弃 |
| 27 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 28 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 29 | fsrcbillnoiv | 源单单据编号 | varchar | 2000 |  |  | ' ' | 源单单据编号 |
| 30 | ftaxcodeid | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 31 | fbaseunitqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 32 | fe_localamt | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 33 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 36 | fe_recamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 37 | fe_sourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ar_finarbill :财务应收单 im_saloutbill :销售出库单 sm_salorder :销售订单 iv_salebill :销售发票单 mpm_projinvapply :项目开票申请单 |
| 38 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 39 | fsrcbillno | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 40 | fe_srcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 41 | fassistantattrid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 42 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 43 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 44 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 45 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 46 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 47 | fdiscountmode | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: NULL :无 PERCENT :折扣率(%) PERUNIT :单位折扣额 TOTAL :固定折扣额 |
| 48 | fe_materialname | fe_materialname | varchar | 255 |  | √ | ' ' |  |
| 49 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 50 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 51 | fe_remark | 备注说明 | varchar | 512 |  | √ | ' ' | 备注说明 |
| 52 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 53 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 54 | finvname | 开票名称 | varchar | 255 |  | √ | ' ' | 开票名称 |
| 55 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 56 | factunitprice | 实际单价-废弃 | numeric | 23 | 10 | √ | 0 | 实际单价-废弃 |
| 57 | fe_tax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 58 | fsrcbilltypenum | 源单单据类型编码 | varchar | 255 |  | √ | ' ' | 源单单据类型编码 |
| 59 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 60 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 61 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 62 | finvoicecustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 63 | fspectype | 规格型号 | varchar | 512 |  | √ | ' ' | 规格型号 |
| 64 | funitcoefficient | 单位转换系数 | numeric | 23 | 10 | √ | 0 | 单位转换系数 |
| 65 | fdiscountlocalamt | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 66 | fmeasureunitid | 开票单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 67 | fsrcbillentityid | 源单分录内码ID-废弃 | varchar | 255 |  | √ | ' ' | 源单分录内码ID-废弃 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iv_salebillentry |  | fentryid |
| 2 | idx_iv_saleentry_corebill |  | fcorebillno,fcorebillentryseq |
| 3 | idx_iv_saleentry_srcbiilid |  | fe_srcbillid |
| 4 | idx_iv_saleentry_srcentryid |  | fe_srcbillentityid |
| 5 | idx_iv_saleentry_pid |  | fid |
| 6 | idx_iv_saleentry_sbillid |  | fsrcbillid |
