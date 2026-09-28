# 协同订单对账-scp_ordercheck

## 关联子实体-子表 t_pur_ordercheck_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_ordercheck_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsumcheckqty | 关联对账数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 关联对账数量_确认携带值 |
| 2 | fsumcheckqty_old | 关联对账数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 关联对账数量_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_ordercheck_lk_fk |  | fentryid |
| 2 | t_pur_ordercheck_lk_pkey |  | fpkid |

---

## 协同订单对账-主表 t_pur_order

- **表名称：** 协同订单对账-主表
- **表名：** t_pur_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdelidate | fdelidate | timestamp | 0 |  |  | null |  |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 7 | fsumpayableamt | fsumpayableamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 8 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 9 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0.000000 |  |
| 10 | fsumpayamt | fsumpayamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 11 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 12 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 E :变更中 |
| 14 | flogstatus | flogstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 16 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 17 | fissyn | fissyn | bpchar | 1 |  | √ | ' ' |  |
| 18 | fpersonid | fpersonid | int8 | 64 |  | √ | 0 |  |
| 19 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 21 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
| 22 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fprepayrate | fprepayrate | numeric | 23 | 6 | √ | 0.00 |  |
| 24 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 25 | fbilldate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fpayeesupid | fpayeesupid | int8 | 64 |  | √ | 0 |  |
| 27 | fpaystatus | fpaystatus | bpchar | 1 |  | √ | ' ' |  |
| 28 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 29 | fcentersettle | fcentersettle | bpchar | 1 |  | √ | ' ' |  |
| 30 | fsupgroupid | 供应商分组 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 31 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 32 | fdeliaddr | fdeliaddr | varchar | 255 |  | √ | ' ' |  |
| 33 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 34 | fsuminvoiceamt | fsuminvoiceamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 35 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 37 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 39 | finvoicesupid | finvoicesupid | int8 | 64 |  | √ | 0 |  |
| 40 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 41 | fdelisupid | fdelisupid | int8 | 64 |  | √ | 0 |  |
| 42 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0.000000 |  |
| 44 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 45 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 46 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 47 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 48 | fsumprepayamt | fsumprepayamt | numeric | 23 | 10 | √ | 0.000000 |  |
| 49 | fsumtaxamount | 订单金额 | numeric | 23 | 10 | √ | 0.000000 | 订单金额 |
| 50 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0.000000 |  |
| 51 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_pkey |  | fid |
| 2 | idx_pur_order_fbillno |  | fbillno |
| 3 | idx_pur_order_frcvorgid |  | frcvorgid |
| 4 | idx_pur_order_fsupplierid |  | fsupplierid |
| 5 | idx_pur_order_fbizpartnerid |  | fbilldate,fbizpartnerid |

---

## 协同订单对账-分表 t_pur_order_a

- **表名称：** 协同订单对账-分表
- **表名：** t_pur_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumsaloutamount | 发货/退回金额 | numeric | 23 | 10 | √ | 0.000000 | 发货/退回金额 |
| 3 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 4 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 5 | fbillversion | fbillversion | varchar | 50 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fchangestatus | fchangestatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 9 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | frejectdate | frejectdate | timestamp | 0 |  |  | null |  |
| 13 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 14 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 15 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | fsuggestion | fsuggestion | varchar | 255 |  | √ | ' ' |  |
| 19 | frejectreason | frejectreason | varchar | 512 |  |  | ' ' |  |
| 20 | frejecterid | frejecterid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 23 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 24 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fsubversion | fsubversion | varchar | 50 |  | √ | ' ' |  |
| 26 | fcloseid | fcloseid | int8 | 64 |  | √ | 0 |  |
| 27 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 28 | fsumdiffamount | 差异金额 | numeric | 23 | 10 | √ | 0.000000 | 差异金额 |
| 29 | fsrcbilltype | 源单类型 | bpchar | 1 |  | √ | ' ' | 源单类型,枚举: 1 :自建商城 2 :京东商城 3 :ERP系统 |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fsumsettleamount | 收货金额 | numeric | 23 | 10 | √ | 0.000000 | 收货金额 |
| 32 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | ' ' | 对账状态,枚举: B :有差异 C :无差异 D :已对账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_order_a_pkey |  | fid |
| 2 | idx_pur_order_a_fcreatetime |  | fcreatetime |

---

## 对账分录-子表 t_pur_ordercheck

- **表名称：** 对账分录-子表
- **表名：** t_pur_ordercheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumcheckqty | 关联对账数量 | numeric | 23 | 10 | √ | 0.000000 | 关联对账数量 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 4 | fsumorderqty | 订单数量 | numeric | 23 | 10 | √ | 0.000000 | 订单数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 7 | fsumrcvamt | 收货总额 | numeric | 23 | 10 | √ | 0.000000 | 收货总额 |
| 8 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 9 | fsendno | 发货/退回单号 | varchar | 255 |  | √ | ' ' | 发货/退回单号 |
| 10 | fsumorderamt | 订单金额 | numeric | 23 | 10 | √ | 0.000000 | 订单金额 |
| 11 | fmatchkey | 匹配标识 | varchar | 255 |  | √ | ' ' | 匹配标识 |
| 12 | fsendamt | 发货/退回金额 | numeric | 23 | 10 | √ | 0.000000 | 发货/退回金额 |
| 13 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 14 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 15 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fsumsendqty | 发货/退回总数 | numeric | 23 | 10 | √ | 0.000000 | 发货/退回总数 |
| 17 | fsumrcvqty | 收货总数 | numeric | 23 | 10 | √ | 0.000000 | 收货总数 |
| 18 | fsendqty | 发货/退回数量 | numeric | 23 | 10 | √ | 0.000000 | 发货/退回数量 |
| 19 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 20 | frcvdate | 收货日期 | timestamp | 0 |  |  | null | 收货日期 |
| 21 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 22 | fsenddate | 发货/退回日期 | timestamp | 0 |  |  | null | 发货/退回日期 |
| 23 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fsumsendamt | 发货/退回总额 | numeric | 23 | 10 | √ | 0.000000 | 发货/退回总额 |
| 27 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 28 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 29 | frcvno | 收货单号 | varchar | 80 |  | √ | ' ' | 收货单号 |
| 30 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | frcvamt | 收货金额 | numeric | 23 | 10 | √ | 0.000000 | 收货金额 |
| 33 | fdiffqty | 差异数量 | numeric | 23 | 10 | √ | 0.000000 | 差异数量 |
| 34 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 35 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 36 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 37 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未对账 B :有差异 C :无差异 D :已对账 E :对账中 |
| 38 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 39 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 40 | fpaycodeid | 付款识别码 | varchar | 80 |  | √ | ' ' | 付款识别码 |
| 41 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 42 | fdiffamt | 差异金额 | numeric | 23 | 10 | √ | 0.000000 | 差异金额 |
| 43 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fsumdiffqty | 差异总数 | numeric | 23 | 10 | √ | 0.000000 | 差异总数 |
| 45 | fjdchildorderid | 京东子订单号 | varchar | 80 |  | √ | ' ' | 京东子订单号 |
| 46 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 47 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 48 | fsumdiffamt | 差异总额 | numeric | 23 | 10 | √ | 0.000000 | 差异总额 |
| 49 | frcvqty | 收货数量 | numeric | 23 | 10 | √ | 0.000000 | 收货数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_ordercheck_pkey |  | fentryid |
| 2 | idx_pur_ordercheck_fid |  | fid,fseq |
| 3 | idx_pur_ordercheck_fpoentryid |  | fpoentryid |

---

## 协同订单对账-关联追踪表 t_pur_order_tc

- **表名称：** 协同订单对账-关联追踪表
- **表名：** t_pur_order_tc

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
| 1 | idx_pur_order_tc_tid |  | ftid |
| 2 | idx_pur_order_tc_tbill |  | ftbillid |
| 3 | t_pur_order_tc_pkey |  | fid |

---

## 协同订单对账-反写记录表 t_pur_order_wb

- **表名称：** 协同订单对账-反写记录表
- **表名：** t_pur_order_wb

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
| 1 | t_pur_order_wb_pkey |  | fentryid |
| 2 | idx_pur_order_wb_fid |  | fid |
