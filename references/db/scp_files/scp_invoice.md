# 开票单-scp_invoice

## 发票明细-子表 t_pur_invoicedetail

- **表名称：** 发票明细-子表
- **表名：** t_pur_invoicedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 3 | finvsource | 发票来源 | varchar | 1 |  | √ | '1' | 发票来源,枚举: 1 :手工创建 2 :发票云 |
| 4 | finvno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 5 | finvserialnum | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finvcompany | 开票公司 | varchar | 255 |  | √ | ' ' | 开票公司 |
| 8 | finvamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 9 | finvtax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 10 | finvid | 发票校验码 | varchar | 255 |  | √ | ' ' | 发票校验码 |
| 11 | finvcode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 12 | finvdate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 13 | finvremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | finvoiceamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 15 | finvcheckstatus | 查验通过 | varchar | 1 |  | √ | '3' | 查验通过,枚举: 1 :通过 2 :不通过 3 :未查验 |
| 16 | finvaddr | 发票下载地址 | varchar | 511 |  | √ | ' ' | 发票下载地址 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | freccompany | 收票公司 | varchar | 255 |  | √ | ' ' | 收票公司 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_invoicedetail |  | fentryid |
| 2 | idx_t_pur_invoicedetail_fid |  | fid,fseq |

---

## 开票明细-分表 t_pur_invoicentry2_a

- **表名称：** 开票明细-分表
- **表名：** t_pur_invoicentry2_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fmalstatdataid | fmalstatdataid | int8 | 64 |  | √ | 0 |  |
| 5 | fmalorderno | 商城订单号 | varchar | 80 |  | √ | ' ' | 商城订单号 |
| 6 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 7 | fecorder | fecorder | varchar | 50 |  | √ | ' ' |  |
| 8 | fafterdeductdiscounttype | 折扣方式（抵扣后） | varchar | 5 |  | √ | 'NULL' | 折扣方式（抵扣后）,枚举: A :折扣率(%) B :单位折扣额 C :折扣额 NULL :无 |
| 9 | fentrypaytype | 下游单据类型 | bpchar | 1 |  | √ | ' ' | 下游单据类型,枚举: 1 :应付单 2 :对公报销单 |
| 10 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 11 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fafterdeductamount | 本次开票金额（抵扣后） | numeric | 23 | 10 | √ | 0 | 本次开票金额（抵扣后） |
| 13 | fentryloccurr | 本位币 | int8 | 64 |  | √ | 1 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 16 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 17 | fsumpayamt | 关联收款金额 | numeric | 23 | 10 | √ | 0.000000 | 关联收款金额 |
| 18 | fmalorderentryid | 商城订单行ID | int8 | 64 |  | √ | 0 | 商城订单行ID |
| 19 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 20 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 21 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 22 | fafterdeducttaxamount | 本次开票价税合计（抵扣后） | numeric | 23 | 10 | √ | 0 | 本次开票价税合计（抵扣后） |
| 23 | fmalorderid | 商城订单ID | int8 | 64 |  | √ | 0 | 商城订单ID |
| 24 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 25 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 26 | fdeductamount | 扣款价税合计 | numeric | 23 | 10 | √ | 0 | 扣款价税合计 |
| 27 | fecorderno | fecorderno | varchar | 80 |  | √ | ' ' |  |
| 28 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 29 | fafterdeductdctamount | 本次开票折扣额（抵扣后） | numeric | 23 | 10 | √ | 0 | 本次开票折扣额（抵扣后） |
| 30 | fentrypaybillno | 下游单据号 | varchar | 80 |  | √ | ' ' | 下游单据号 |
| 31 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 32 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 33 | fisentrypay | 生成下游单据 | bpchar | 1 |  | √ | ' ' | 生成下游单据,枚举: 1 :已生成 2 :未生成 |
| 34 | fentryexchrate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 35 | fmalstatdatano | fmalstatdatano | varchar | 80 |  | √ | ' ' |  |
| 36 | fcheckbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 37 | fafterdeductdctrate | 单位折扣（%）（抵扣后） | numeric | 23 | 10 | √ | 0 | 单位折扣（%）（抵扣后） |
| 38 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 39 | fafterdeducttax | 本次开票税额（抵扣后） | numeric | 23 | 10 | √ | 0 | 本次开票税额（抵扣后） |
| 40 | fentryjdorderid | fentryjdorderid | int8 | 64 |  | √ | 0 |  |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 42 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 43 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry2_a_fid |  | fid |
| 2 | t_pur_invoicentry2_a_pkey |  | fentryid |
| 3 | idx_pur_invoicentry2_a_fsrceid |  | fsrcentryid |
| 4 | idx_pur_invoicentry2_a_fpoid |  | fpoentryid |
| 5 | idx_pur_invoicentry2_a_fsrcid |  | fsrcbillid |

---

## 开票明细-子表 t_pur_invoicentry2

- **表名称：** 开票明细-子表
- **表名：** t_pur_invoicentry2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxprefpolicy | 优惠政策 | varchar | 255 |  | √ | ' ' | 优惠政策 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 5 | factcheckamount | 本次开票金额 | numeric | 23 | 10 | √ | 0 | 本次开票金额 |
| 6 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | finbillno | 源单单号 | varchar | 80 |  | √ | ' ' | 源单单号 |
| 10 | fistaxpref | 税收优惠 | bpchar | 1 |  | √ | ' ' | 税收优惠 |
| 11 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 12 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 13 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 14 | fdeductiontax | 抵扣税额 | numeric | 23 | 10 | √ | 0.000000 | 抵扣税额 |
| 15 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | factchecktaxamount | 本次开票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次开票价税合计 |
| 17 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 20 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 21 | ftaxcode | 税收编码 | varchar | 50 |  | √ | ' ' | 税收编码 |
| 22 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 23 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 24 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 25 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 26 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 27 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 33 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 34 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 35 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 36 | factcheckprice | 本次开票单价 | numeric | 23 | 10 | √ | 0 | 本次开票单价 |
| 37 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 38 | factchecktaxprice | 本次开票含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 本次开票含税单价 |
| 39 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 40 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 41 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 43 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :折扣额 NULL :无 |
| 44 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fsourcebill | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 46 | fdeductiondate | 抵扣日期 | timestamp | 0 |  |  | null | 抵扣日期 |
| 47 | fcostid | fcostid | int8 | 64 |  | √ | 0 |  |
| 48 | finbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 49 | factchecktax | 本次开票税额 | numeric | 23 | 10 | √ | 0 | 本次开票税额 |
| 50 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_invoicentry2_pkey |  | fentryid |
| 2 | idx_pur_invoicentry2_fid_fseq |  | fid,fseq |
| 3 | idx_pur_invoicentry2_fmatid |  | fmaterialid |

---

## 附件-附件表 t_pur_invrejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_invrejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invrejectatt_fbasedataid |  | fbasedataid |
| 2 | pk_t_pur_invrejectreasonatt |  | fpkid |

---

## 发票附件-附件表 t_pur_invoicedetail_att

- **表名称：** 发票附件-附件表
- **表名：** t_pur_invoicedetail_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_invoicedetail_att |  | fpkid |
| 2 | pk_pur_invoicedetail_att_feid |  | fentryid |
| 3 | pk_pur_invoicedetail_att_fbdid |  | fbasedataid |

---

## 开票单-关联追踪表 t_pur_invoice_tc

- **表名称：** 开票单-关联追踪表
- **表名：** t_pur_invoice_tc

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
| 1 | idx_pur_invoice_tc_tid |  | ftid |
| 2 | idx_pur_invoice_tc_tbill |  | ftbillid |
| 3 | t_pur_invoice_tc_pkey |  | fid |

---

## 发货明细(作废)-分表 t_pur_invoicentry_a

- **表名称：** 发货明细(作废)-分表
- **表名：** t_pur_invoicentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 7 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 11 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 12 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 13 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 14 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 16 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 17 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 18 | fsumpayamt | 关联收款金额 | numeric | 23 | 10 | √ | 0.000000 | 关联收款金额 |
| 19 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 22 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_invoicentry_a_pkey |  | fentryid |
| 2 | idx_pur_invoicentry_a_fid |  | fid |
| 3 | idx_pur_invoicentry_a_fpoid |  | fpoentryid |

---

## 开票单-多语言表 t_pur_invoice_l

- **表名称：** 开票单-多语言表
- **表名：** t_pur_invoice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_invoice_l_pkey |  | fpkid |
| 2 | idx_pur_invoice_l_fid |  | fid,flocaleid |

---

## 开票单-分表 t_pur_invoice_a

- **表名称：** 开票单-分表
- **表名：** t_pur_invoice_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fecinvoicestate | fecinvoicestate | varchar | 10 |  | √ | ' ' |  |
| 3 | finvaddress | 发票下载地址 | varchar | 1000 |  | √ | ' ' | 发票下载地址 |
| 4 | frevname | 收票人 | varchar | 255 |  | √ | ' ' | 收票人 |
| 5 | finvdetail | 开票要求 | bpchar | 1 |  | √ | ' ' | 开票要求,枚举: 1 :按大类开票 2 :按明细开票 |
| 6 | ftaxrate | 汇总开票税率(%) | numeric | 23 | 10 | √ | 0.000000 | 汇总开票税率(%) |
| 7 | fmarkid | fmarkid | varchar | 255 |  | √ | ' ' |  |
| 8 | frevphone | 联系方式 | varchar | 255 |  | √ | ' ' | 联系方式 |
| 9 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 10 | fwishinvdate | fwishinvdate | timestamp | 0 |  |  | null |  |
| 11 | fecorderqty | fecorderqty | int4 | 32 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 14 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :企业 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fispay | fispay | bpchar | 1 |  | √ | ' ' |  |
| 17 | fecinvoiceresult | fecinvoiceresult | varchar | 512 |  | √ | ' ' |  |
| 18 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 |
| 19 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 20 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 21 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 22 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 23 | fpayableamt | 客户应付金额 | numeric | 23 | 10 | √ | 0.000000 | 客户应付金额 |
| 24 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 25 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | frevaddress | 收票地址 | varchar | 255 |  | √ | ' ' | 收票地址 |
| 28 | finvtypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | femail | femail | varchar | 80 |  | √ | ' ' |  |
| 31 | ftaxcode | 汇总开票税收编码 | varchar | 50 |  | √ | ' ' | 汇总开票税收编码 |
| 32 | fpayableno | 客户应付单号 | varchar | 80 |  | √ | ' ' | 客户应付单号 |
| 33 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 34 | frejectreason | 打回原因 | varchar | 512 |  |  | ' ' | 打回原因 |
| 35 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 37 | fjdorder | fjdorder | int8 | 64 |  | √ | 0 |  |
| 38 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fsrcinvtype | 开票来源 | bpchar | 1 |  | √ | ' ' | 开票来源,枚举: 1 :电商对账 2 :协同对账 3 :协同收货/入库 4 :电商对账（旧） |
| 40 | fadmindivisionid | fadmindivisionid | varchar | 50 |  | √ | ' ' |  |
| 41 | fcfmnote | 发票签收情况 | varchar | 255 |  | √ | ' ' | 发票签收情况 |
| 42 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 43 | fserialnum | 发票序列号 | varchar | 50 |  | √ | ' ' | 发票序列号 |
| 44 | fcheckbillno | 对账单号(废弃) | varchar | 80 |  | √ | ' ' | 对账单号(废弃) |
| 45 | fitemname | 汇总开票项目名称 | varchar | 255 |  | √ | ' ' | 汇总开票项目名称 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoice_a_fcreatetime |  | fcreatetime |
| 2 | t_pur_invoice_a_pkey |  | fid |

---

## 发货明细(作废)-子表 t_pur_invoicentry

- **表名称：** 发货明细(作废)-子表
- **表名：** t_pur_invoicentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxprefpolicy | 优惠政策 | varchar | 255 |  | √ | ' ' | 优惠政策 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 7 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | foutbilldate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 14 | foutbillno | 发货单号 | varchar | 80 |  | √ | ' ' | 发货单号 |
| 15 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fistaxpref | 税收优惠 | bpchar | 1 |  | √ | ' ' | 税收优惠 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 19 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 20 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 22 | fdeductiontax | 抵扣税额 | numeric | 23 | 10 | √ | 0.000000 | 抵扣税额 |
| 23 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 24 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 29 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 30 | ftaxcode | 税收编码 | varchar | 50 |  | √ | ' ' | 税收编码 |
| 31 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 33 | fdeductiondate | 抵扣日期 | timestamp | 0 |  |  | null | 抵扣日期 |
| 34 | fcostid | fcostid | int8 | 64 |  | √ | 0 |  |
| 35 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 36 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 37 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 38 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 39 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 43 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_invoicentry_fmatid |  | fmaterialid |
| 3 | t_pur_invoicentry_pkey |  | fentryid |

---

## 物流信息-子表 t_pur_invoice_log

- **表名称：** 物流信息-子表
- **表名：** t_pur_invoice_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogdate | 寄出日期 | timestamp | 0 |  |  | null | 寄出日期 |
| 3 | fdelidate | 预计到达日期 | timestamp | 0 |  |  | null | 预计到达日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flogbillno | 物流单号 | varchar | 80 |  | √ | ' ' | 物流单号 |
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | [物流公司 pur_logsupplier](../pbd_files/pur_logsupplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_invoice_log_pkey |  | fentryid |
| 2 | idx_pur_invoice_log_fid |  | fid |
| 3 | idx_pur_invoice_log_flogbillno |  | flogbillno |

---

## 开票单-主表 t_pur_invoice

- **表名称：** 开票单-主表
- **表名：** t_pur_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | fwriteoffflag | fwriteoffflag | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 11 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 12 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 13 | fdeductsumtaxamount | 扣款价税合计 | numeric | 23 | 10 | √ | 0 | 扣款价税合计 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | finsumtaxamount | 入库/收货价税合计 | numeric | 23 | 10 | √ | 0 | 入库/收货价税合计 |
| 18 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已开票 D :已关闭 Z :已作废 |
| 22 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 23 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 25 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 33 | fcfmstatus | 签收状态 | bpchar | 1 |  | √ | ' ' | 签收状态,枚举: A :待签收 B :已签收 C :已打回 |
| 34 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 35 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 36 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 37 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 38 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |
| 39 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoice_fbilldate |  | fbilldate |
| 2 | idx_pur_invoice_fbizpartnerid |  | fbizpartnerid |
| 3 | t_pur_invoice_pkey |  | fid |
| 4 | idx_pur_invoice_fbillno |  | fbillno |

---

## 扣款明细-子表 t_pur_invoicedeductentry

- **表名称：** 扣款明细-子表
- **表名：** t_pur_invoicedeductentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainbillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnote | 扣款说明 | varchar | 512 |  | √ | ' ' | 扣款说明 |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 11 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 12 | fdeducttaxamount | 扣款价税合计 | numeric | 23 | 10 | √ | 0 | 扣款价税合计 |
| 13 | fbillno | 源单单号 | varchar | 80 |  | √ | ' ' | 源单单号 |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 16 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 17 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 20 | fsourcebill | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 22 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 25 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invdeentry_fid |  | fid,fseq |
| 2 | idx_idx_pur_invdeentry_srcenid |  | fsrcbillentryid |
| 3 | pk_pur_invoicedeductentry |  | fentryid |
| 4 | idx_idx_pur_invdeentry_srcid |  | fsrcbillid |

---

## 关联子实体-子表 t_pur_invoicentry2_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_invoicentry2_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 2 | ftaxamount | 价税合计_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_确认携带值 |
| 3 | ftaxamount_old | 价税合计_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计_原始携带值 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 7 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry2_lk_fk |  | fentryid |
| 2 | t_pur_invoicentry2_lk_pkey |  | fpkid |

---

## 开票单-反写记录表 t_pur_invoice_wb

- **表名称：** 开票单-反写记录表
- **表名：** t_pur_invoice_wb

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
| 1 | t_pur_invoice_wb_pkey |  | fentryid |
