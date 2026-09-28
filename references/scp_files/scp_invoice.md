# 开票单-scp_invoice

## 发票明细-子表 t_pur_invoicedetail

- **表名称：** 发票明细-子表
- **表名：** t_pur_invoicedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
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
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
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

## 入库明细-分表 t_pur_invoicentry2_a

- **表名称：** 入库明细-分表
- **表名：** t_pur_invoicentry2_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 5 | fecorder | fecorder | varchar | 50 |  | √ | ' ' |  |
| 6 | fentrypaytype | 下游单据类型 | bpchar | 1 |  | √ | ' ' | 下游单据类型,枚举: 1 :应付单 2 :对公报销单 |
| 7 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 8 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fentryloccurr | 本位币 | int8 | 64 |  | √ | 1 | 币种 bd_currency |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 13 | fsumpayamt | 关联收款金额 | numeric | 19 | 6 | √ | 0.000000 | 关联收款金额 |
| 14 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 15 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 16 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 17 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 18 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 19 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 20 | fentrypaybillno | 下游单据号 | varchar | 80 |  | √ | ' ' | 下游单据号 |
| 21 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 22 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 23 | fisentrypay | 生成下游单据 | bpchar | 1 |  | √ | ' ' | 生成下游单据,枚举: 1 :已生成 2 :未生成 |
| 24 | fentryexchrate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 25 | fcheckbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 26 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 27 | fentryjdorderid | fentryjdorderid | int8 | 64 |  | √ | 0 |  |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 30 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry2_a_fid |  | fid |
| 2 | t_pur_invoicentry2_a_pkey |  | fentryid |
| 3 | idx_pur_invoicentry2_a_fpoid |  | fpoentryid |

---

## 入库明细-子表 t_pur_invoicentry2

- **表名称：** 入库明细-子表
- **表名：** t_pur_invoicentry2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxprefpolicy | 优惠政策 | varchar | 255 |  | √ | ' ' | 优惠政策 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | factcheckamount | 本次开票金额 | numeric | 23 | 10 | √ | 0 | 本次开票金额 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 12 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 13 | factcheckprice | 本次开票单价 | numeric | 23 | 10 | √ | 0 | 本次开票单价 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | finbillno | 入库/收货单号 | varchar | 80 |  | √ | ' ' | 入库/收货单号 |
| 16 | factchecktaxprice | 本次开票含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 本次开票含税单价 |
| 17 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 18 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 19 | fistaxpref | 税收优惠 | bpchar | 1 |  | √ | ' ' | 税收优惠 |
| 20 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 21 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 22 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 24 | fdeductiontax | 抵扣税额 | numeric | 19 | 6 | √ | 0.000000 | 抵扣税额 |
| 25 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 26 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | factchecktaxamount | 本次开票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次开票价税合计 |
| 28 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 29 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 32 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 33 | ftaxcode | 税收编码 | varchar | 50 |  | √ | ' ' | 税收编码 |
| 34 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 36 | fdeductiondate | 抵扣日期 | timestamp | 0 |  |  | null | 抵扣日期 |
| 37 | fcostid | fcostid | int8 | 64 |  | √ | 0 |  |
| 38 | finbilldate | 入库/收货日期 | timestamp | 0 |  |  | null | 入库/收货日期 |
| 39 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 40 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 41 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 42 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 46 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry2_fid_fseq |  | fid,fseq |
| 2 | t_pur_invoicentry2_pkey |  | fentryid |
| 3 | idx_pur_invoicentry2_fmatid |  | fmaterialid |

---

## 附件-附件表 t_pur_invrejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_invrejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
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
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 7 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 11 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 12 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 13 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 14 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 16 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 17 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 18 | fsumpayamt | 关联收款金额 | numeric | 19 | 6 | √ | 0.000000 | 关联收款金额 |
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
| 2 | finvaddress | 发票下载地址 | varchar | 1000 |  | √ | ' ' | 发票下载地址 |
| 3 | frevname | frevname | varchar | 255 |  | √ | ' ' |  |
| 4 | finvdetail | 开票要求 | bpchar | 1 |  | √ | ' ' | 开票要求,枚举: 1 :汇总开具 2 :按明细开具 |
| 5 | ftaxrate | 汇总开票税率(%) | numeric | 19 | 6 | √ | 0.000000 | 汇总开票税率(%) |
| 6 | frevphone | frevphone | varchar | 255 |  | √ | ' ' |  |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :企业 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fispay | fispay | bpchar | 1 |  | √ | ' ' |  |
| 13 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 |
| 14 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 15 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 16 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 17 | fpayableamt | 客户应付金额 | numeric | 19 | 6 | √ | 0.000000 | 客户应付金额 |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 19 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | frevaddress | frevaddress | varchar | 255 |  | √ | ' ' |  |
| 22 | finvtypeid | 发票种类 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | ftaxcode | 汇总开票税收编码 | varchar | 50 |  | √ | ' ' | 汇总开票税收编码 |
| 25 | fpayableno | 客户应付单号 | varchar | 80 |  | √ | ' ' | 客户应付单号 |
| 26 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 27 | frejectreason | 打回原因 | varchar | 512 |  |  | ' ' | 打回原因 |
| 28 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fjdorder | fjdorder | int8 | 64 |  | √ | 0 |  |
| 31 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fcfmnote | 发票签收情况 | varchar | 255 |  | √ | ' ' | 发票签收情况 |
| 33 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 34 | fserialnum | 发票序列号 | varchar | 50 |  | √ | ' ' | 发票序列号 |
| 35 | fcheckbillno | 对账单号(废弃) | varchar | 80 |  | √ | ' ' | 对账单号(废弃) |
| 36 | fitemname | 汇总开票项目名称 | varchar | 255 |  | √ | ' ' | 汇总开票项目名称 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 10 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | foutbilldate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 13 | foutbillno | 发货单号 | varchar | 80 |  | √ | ' ' | 发货单号 |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | fistaxpref | 税收优惠 | bpchar | 1 |  | √ | ' ' | 税收优惠 |
| 17 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 18 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 19 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 21 | fdeductiontax | 抵扣税额 | numeric | 19 | 6 | √ | 0.000000 | 抵扣税额 |
| 22 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 23 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 29 | ftaxcode | 税收编码 | varchar | 50 |  | √ | ' ' | 税收编码 |
| 30 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 32 | fdeductiondate | 抵扣日期 | timestamp | 0 |  |  | null | 抵扣日期 |
| 33 | fcostid | fcostid | int8 | 64 |  | √ | 0 |  |
| 34 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 35 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 36 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 37 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 41 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoicentry_fmatid |  | fmaterialid |
| 2 | idx_pur_invoicentry_fid_fseq |  | fid,fseq |
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
| 8 | fsupplierid | 物流公司 | int8 | 64 |  | √ | 0 | 物流公司 pur_logsupplier |

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
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | fwriteoffflag | fwriteoffflag | bpchar | 1 |  | √ | '0' |  |
| 6 | forgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 11 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 16 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已开票 D :已关闭 Z :已作废 |
| 19 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 21 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 25 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 29 | fcfmstatus | 签收状态 | bpchar | 1 |  | √ | ' ' | 签收状态,枚举: A :待签收 B :已签收 C :已打回 |
| 30 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 31 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 32 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 33 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 34 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 35 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 36 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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
| 1 | t_pur_invoicentry2_lk_pkey |  | fpkid |

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
