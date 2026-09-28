# 商城订单-ent_order

## 商城订单-分表 t_mal_order_a

- **表名称：** 商城订单-分表
- **表名：** t_mal_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fecorderid | fecorderid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjdorderstatus | fjdorderstatus | varchar | 255 |  | √ | ' ' |  |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fecsource | fecsource | varchar | 80 |  | √ | ' ' |  |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 12 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fecorderstatus | fecorderstatus | bpchar | 1 |  | √ | ' ' |  |
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
| 4 | fgoodsimg | fgoodsimg | varchar | 255 |  |  | ' ' |  |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 6 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 7 | fmaterialid | 对应ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fsumorderqty | fsumorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 12 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 13 | fcostitemid | 费用类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 14 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 15 | fentrycostprojectid | fentrycostprojectid | int8 | 64 |  | √ | 0 |  |
| 16 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 17 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 18 | fcommentfollowstatus | fcommentfollowstatus | bpchar | 1 |  | √ | 'A' |  |
| 19 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 20 | fcompareid | fcompareid | varchar | 80 |  | √ | ' ' |  |
| 21 | fsumreceiptqty | 收货数量 | numeric | 19 | 6 | √ | 0.000000 | 收货数量 |
| 22 | fsumreturnreqqty | fsumreturnreqqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 24 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 25 | fcompareremark | fcompareremark | varchar | 255 |  | √ | ' ' |  |
| 26 | fsumpayamt | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 27 | fsuppilerid | fsuppilerid | int8 | 64 |  | √ | 0 |  |
| 28 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 29 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 30 | ferpbillstatus | ferpbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 31 | fdctrate | 折扣率(%) | numeric | 19 | 6 | √ | 0.000000 | 折扣率(%) |
| 32 | fcategory | fcategory | varchar | 80 |  | √ | ' ' |  |
| 33 | flogstatus | flogstatus | bpchar | 1 |  | √ | ' ' |  |
| 34 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fjdorderstatus | fjdorderstatus | varchar | 255 |  | √ | ' ' |  |
| 36 | fispresent | fispresent | bpchar | 1 |  | √ | ' ' |  |
| 37 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 38 | ferpbillnumber | ferpbillnumber | varchar | 80 |  | √ | ' ' |  |
| 39 | fsumrequestqty | fsumrequestqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 40 | fsumoutstockqty | 发货数量 | numeric | 19 | 6 | √ | 0.000000 | 发货数量 |
| 41 | fsuminstockqty | 入库数量 | numeric | 19 | 6 | √ | 0.000000 | 入库数量 |
| 42 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 43 | fcompareresult | fcompareresult | bpchar | 1 |  | √ | ' ' |  |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fsuminvamt | 开票金额 | numeric | 19 | 6 | √ | 0.000000 | 开票金额 |
| 47 | fgoodsuseid | fgoodsuseid | int8 | 64 |  | √ | 0 |  |

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

## 商城订单-多语言表 t_mal_order_l

- **表名称：** 商城订单-多语言表
- **表名：** t_mal_order_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 订单备注 | varchar | 512 |  | √ | ' ' | 订单备注 |
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

## 商城订单-主表 t_mal_order

- **表名称：** 商城订单-主表
- **表名：** t_mal_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmalpaytype | fmalpaytype | int8 | 64 |  | √ | 0 |  |
| 3 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 4 | finvdetail | 开票要求 | varchar | 2 |  | √ | ' ' | 开票要求,枚举: 1 :汇总开具 2 :按明细开具 |
| 5 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | forgid | 结算客户 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdeporgid | fdeporgid | int8 | 64 |  | √ | 0 |  |
| 8 | fbilldate | 订货日期 | timestamp | 0 |  |  | null | 订货日期 |
| 9 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 10 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 11 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 12 | fmalinvtype | fmalinvtype | int8 | 64 |  | √ | 0 |  |
| 13 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 |
| 14 | fsumamount | 合计金额 | numeric | 19 | 6 | √ | 0.000000 | 合计金额 |
| 15 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 16 | freceiptid | 收货人 | int8 | 64 |  | √ | 0 | [收货信息 pbd_receiptinfo](../pbd_files/pbd_receiptinfo.md) |
| 17 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 18 | fbillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 19 | fcostprojectid | fcostprojectid | int8 | 64 |  | √ | 0 |  |
| 20 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 21 | fcostorgid | fcostorgid | int8 | 64 |  | √ | 0 |  |
| 22 | ffreight | ffreight | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 25 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 pur_paycond](../basedata_files/pur_paycond.md) |
| 26 | finvway | 开票方式 | bpchar | 1 |  | √ | ' ' | 开票方式,枚举: 1 :集中开票 2 :随货开票 |
| 27 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 28 | fpaytype | fpaytype | varchar | 3 |  | √ | ' ' |  |
| 29 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 31 | fsupplierid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 33 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 34 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 35 | finvoiceorgid | finvoiceorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fexpenseorgid | fexpenseorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fpersonid | fpersonid | int8 | 64 |  | √ | 0 |  |
| 38 | fsumtaxamount | 订单金额 | numeric | 19 | 6 | √ | 0.000000 | 订单金额 |
| 39 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 40 | fsumtax | 合计税额 | numeric | 19 | 6 | √ | 0.000000 | 合计税额 |
| 41 | ftalentid | ftalentid | varchar | 80 |  | √ | ' ' |  |
| 42 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 43 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 44 | fitemname | 汇总开票项目名称 | varchar | 255 |  | √ | ' ' | 汇总开票项目名称 |
| 45 | fcontacterid | 商家联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 46 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

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
