# 采购金额明细查询-pmm_puramountdetail

## 采购金额明细查询-反写记录表 t_mal_order_wb

- **表名称：** 采购金额明细查询-反写记录表
- **表名：** t_mal_order_wb

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
| 1 | idx_mal_order_wb_fk |  | fid |
| 2 | t_mal_order_wb_pkey |  | fentryid |

---

## 采购金额明细查询-多语言表 t_mal_order_l

- **表名称：** 采购金额明细查询-多语言表
- **表名：** t_mal_order_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 申请事由 | varchar | 512 |  | √ | ' ' | 申请事由 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_order_l_pkey |  | fpkid |
| 2 | idx_mal_order_l_fid |  | fid,flocaleid |

---

## 采购金额明细查询-主表 t_mal_order

- **表名称：** 采购金额明细查询-主表
- **表名：** t_mal_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmalpaytype | 支付方式 | int8 | 64 |  | √ | 0 | [商城支付方式 pbd_paytype](../pbd_files/pbd_paytype.md) |
| 3 | fdelidate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 4 | finvdetail | 开票要求 | varchar | 2 |  | √ | ' ' | 开票要求,枚举: 1 :按明细开票 2 :汇总开票 22 :办公用品 3 :电脑配件 19 :耗材 |
| 5 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdeporgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbilldate | 订货日期 | timestamp | 0 |  |  | null | 订货日期 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 10 | freqpersonid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbiztype | 业务类型（废弃） | bpchar | 1 |  | √ | ' ' | 业务类型（废弃）,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 12 | fmalinvtype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 13 | finvtype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: 1 :普通发票 2 :增值税专用发票 3 :增值税电子普通发票 |
| 14 | fsumamount | 合计金额 | numeric | 19 | 6 | √ | 0.000000 | 合计金额 |
| 15 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建供应商 Z :电商供应商 |
| 16 | freceiptid | 收货人 | int8 | 64 |  | √ | 0 | [收货地址 mal_address](../mal_files/mal_address.md) |
| 17 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 18 | fbillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 19 | fcostprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fcostorgid | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ffreight | 运费 | numeric | 19 | 6 | √ | 0.000000 | 运费 |
| 23 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 25 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 pur_paycond](../basedata_files/pur_paycond.md) |
| 26 | finvway | 开票方式 | bpchar | 1 |  | √ | ' ' | 开票方式,枚举: 1 :随货开票 2 :集中开票 |
| 27 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fpaytype | 支付方式 | varchar | 3 |  | √ | ' ' | 支付方式,枚举: 1 :货到付款 4 :预存款 101 :账期支付 5 :公司转账 |
| 29 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 31 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 34 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 35 | finvoiceorgid | 开票单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fexpenseorgid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 38 | fsumtaxamount | 订单金额 | numeric | 19 | 6 | √ | 0.000000 | 订单金额 |
| 39 | fsettleorgid | 核算公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fsumtax | 合计税额 | numeric | 19 | 6 | √ | 0.000000 | 合计税额 |
| 41 | ftalentid | ftalentid | varchar | 80 |  | √ | ' ' |  |
| 42 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 43 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 44 | fitemname | 汇总开票项目名称 | varchar | 255 |  | √ | ' ' | 汇总开票项目名称 |
| 45 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
| 46 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_order_fbilldate |  | fbilldate |
| 2 | idx_mal_order_fbillno |  | fbillno |
| 3 | idx_mal_order_fbizpartnerid |  | fbizpartnerid |
| 4 | t_mal_order_pkey |  | fid |

---

## 采购金额明细查询-分表 t_mal_order_a

- **表名称：** 采购金额明细查询-分表
- **表名：** t_mal_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fecorderid | 电商订单号 | int8 | 64 |  | √ | 0 | 京东订单 pbd_jdorder |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjdorderstatus | 电商订单状态 | varchar | 255 |  | √ | ' ' | 电商订单状态 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fecsource | 电商平台类型 | varchar | 80 |  | √ | ' ' | 电商平台类型,枚举: pbd_jdorder :京东订单 pbd_order_sn :电商订单_SN pbd_order_xy :电商订单_西域 pbd_order_cg :电商订单_晨光 pbd_order_dl :电商订单_得力 pbd_order_xfs :电商订单_鑫方盛 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 12 | fjdorderid | 电商订单号 | varchar | 80 |  | √ | ' ' | 电商订单号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fasyncstatus | 下游单据状态 | bpchar | 1 |  | √ | ' ' | 下游单据状态,枚举: A :未完成 B :已完成 |
| 15 | fecorderstatus | 电商订单状态 | bpchar | 1 |  | √ | ' ' | 电商订单状态,枚举: 1 :已生成 2 :已确认 3 :已取消 4 :已失效 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_order_a_pkey |  | fid |
| 2 | idx_mal_order_a_fcreatetime |  | fcreatetime |
| 3 | idx_mal_order_a_fcreatorid |  | fcreatorid |

---

## 商品分录-子表 t_mal_orderentry

- **表名称：** 商品分录-子表
- **表名：** t_mal_orderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddvalue | 增值保障 | bpchar | 1 |  | √ | ' ' | 增值保障,枚举: 1 :碎屏保 2 :无理由 3 :意外保 4 :碎屏换新 5 :延长保 6 :换新 |
| 3 | fcommentfirststatus | fcommentfirststatus | bpchar | 1 |  | √ | 'A' |  |
| 4 | fgoodsimg | 图片 | varchar | 255 |  |  | ' ' | 图片 |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 6 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 7 | fmaterialid | ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 E :变更中 |
| 9 | fsumorderqty | 关联订单数量 | numeric | 19 | 6 | √ | 0.000000 | 关联订单数量 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | ftaxprice | 商品价格 | numeric | 23 | 10 | √ | 0.0000000000 | 商品价格 |
| 13 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 14 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 15 | fentrycostprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 17 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 18 | fcommentfollowstatus | fcommentfollowstatus | bpchar | 1 |  | √ | 'A' |  |
| 19 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 20 | fcompareid | 比价标识 | varchar | 80 |  | √ | ' ' | 比价标识 |
| 21 | fsumreceiptqty | 关联收货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联收货数量 |
| 22 | fsumreturnreqqty | 关联退货申请数量 | numeric | 19 | 6 | √ | 0.000000 | 关联退货申请数量 |
| 23 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 24 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 25 | fcompareremark | 比价说明 | varchar | 255 |  | √ | ' ' | 比价说明 |
| 26 | fsumpayamt | 关联付款金额 | numeric | 19 | 6 | √ | 0.000000 | 关联付款金额 |
| 27 | fsuppilerid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 28 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 29 | ftaxamount | 商品金额 | numeric | 19 | 6 | √ | 0.000000 | 商品金额 |
| 30 | ferpbillstatus | 采购订单状态 | bpchar | 1 |  | √ | ' ' | 采购订单状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 31 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 32 | fcategory | 配置ID | varchar | 80 |  | √ | ' ' | 配置ID |
| 33 | flogstatus | 订单物流状态 | bpchar | 1 |  | √ | ' ' | 订单物流状态,枚举: H :待确认 I :已确认 J :已打回 A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 34 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fjdorderstatus | fjdorderstatus | varchar | 255 |  | √ | ' ' |  |
| 36 | fispresent | fispresent | bpchar | 1 |  | √ | ' ' |  |
| 37 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 38 | ferpbillnumber | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 39 | fsumrequestqty | 关联申请数量 | numeric | 19 | 6 | √ | 0.000000 | 关联申请数量 |
| 40 | fsumoutstockqty | 关联发货数量 | numeric | 19 | 6 | √ | 0.000000 | 关联发货数量 |
| 41 | fsuminstockqty | 关联入库数量 | numeric | 19 | 6 | √ | 0.000000 | 关联入库数量 |
| 42 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 43 | fcompareresult | 比价情况 | bpchar | 1 |  | √ | ' ' | 比价情况,枚举: A :未比价 B :最低价 C :非最低价 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 46 | fsuminvamt | 关联开票金额 | numeric | 19 | 6 | √ | 0.000000 | 关联开票金额 |
| 47 | fgoodsuseid | 商品用途 | int8 | 64 |  | √ | 0 | [商品用途 pmm_goods_use](../pmm_files/pmm_goods_use.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_orderentry_pkey |  | fentryid |
| 2 | idx_mal_orderentry_fid_fseq |  | fid,fseq |
| 3 | idx_mal_orderentry_fmaterialid |  | fmaterialid |

---

## 商品分录-分表 t_mal_orderentry_a

- **表名称：** 商品分录-分表
- **表名：** t_mal_orderentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchildorderid | fchildorderid | varchar | 100 |  | √ | ' ' |  |
| 3 | fprosourceentryid | 协议分录ID | varchar | 255 |  | √ | ' ' | 协议分录ID |
| 4 | freturnamount | 电商退货金额 | numeric | 19 | 6 | √ | 0.000000 | 电商退货金额 |
| 5 | fjdorder | 京东单 | int8 | 64 |  | √ | 0 | [京东订单 pbd_jdorder](../pbd_files/pbd_jdorder.md) |
| 6 | ferpsourceid | 来源单据ID | varchar | 255 |  | √ | ' ' | 来源单据ID |
| 7 | fordersource | fordersource | varchar | 80 |  | √ | ' ' |  |
| 8 | ferpsourceentryid | 来源单据分录ID | varchar | 255 |  | √ | ' ' | 来源单据分录ID |
| 9 | ferpsourcebilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 10 | forder | 电商子订单 | int8 | 64 |  | √ | 0 | 京东订单 pbd_jdorder |
| 11 | fprotocolsourceid | 协议单据ID | varchar | 255 |  | √ | ' ' | 协议单据ID |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fprotocolno | 协议编码 | varchar | 80 |  | √ | ' ' | 协议编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_orderentry_a_fid |  | fid |
| 2 | t_mal_orderentry_a_pkey |  | fentryid |

---

## 采购金额明细查询-关联追踪表 t_mal_order_tc

- **表名称：** 采购金额明细查询-关联追踪表
- **表名：** t_mal_order_tc

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
| 1 | t_mal_order_tc_pkey |  | fid |
| 2 | idx_mal_order_tc_tid |  | ftid |
| 3 | idx_mal_order_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_mal_orderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mal_orderentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsumorderqty_old | 关联订单数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 关联订单数量_原始携带值 |
| 4 | fsumorderqty | 关联订单数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 关联订单数量_确认携带值 |
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
| 1 | idx_mal_orderentry_lk_fk |  | fentryid |
| 2 | t_mal_orderentry_lk_pkey |  | fpkid |
