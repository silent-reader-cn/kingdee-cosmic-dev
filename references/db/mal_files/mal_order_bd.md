# 商城订单-mal_order_bd

## 商城订单-分表 t_mal_order_a

- **表名称：** 商城订单-分表
- **表名：** t_mal_order_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fecorderid | fecorderid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fjdorderstatus | fjdorderstatus | varchar | 255 |  | √ | ' ' |  |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | fecsource | fecsource | varchar | 80 |  | √ | ' ' |  |
| 8 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 9 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 12 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fasyncstatus | 下游单据状态 | bpchar | 1 |  | √ | ' ' | 下游单据状态,枚举: A :未完成 B :已完成 |
| 15 | fecorderstatus | fecorderstatus | bpchar | 1 |  | √ | ' ' |  |
| 16 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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

## 单据体-子表 t_mal_orderentry

- **表名称：** 单据体-子表
- **表名：** t_mal_orderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddvalue | faddvalue | bpchar | 1 |  | √ | ' ' |  |
| 3 | fcommentfirststatus | fcommentfirststatus | bpchar | 1 |  | √ | 'A' |  |
| 4 | fgoodsimg | fgoodsimg | varchar | 255 |  |  | ' ' |  |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 6 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 8 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fsumorderqty | fsumorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 12 | ftaxprice | 商品价格 | numeric | 23 | 10 | √ | 0.0000000000 | 商品价格 |
| 13 | fcostitemid | fcostitemid | int8 | 64 |  | √ | 0 |  |
| 14 | famount | famount | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | fentrycostprojectid | fentrycostprojectid | int8 | 64 |  | √ | 0 |  |
| 16 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 18 | fcommentfollowstatus | fcommentfollowstatus | bpchar | 1 |  | √ | 'A' |  |
| 19 | fjdorderid | fjdorderid | varchar | 80 |  | √ | ' ' |  |
| 20 | fcompareid | fcompareid | varchar | 80 |  | √ | ' ' |  |
| 21 | fsumreceiptqty | fsumreceiptqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 22 | fsumreturnreqqty | fsumreturnreqqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fdctamount | fdctamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 24 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 25 | fcompareremark | fcompareremark | varchar | 255 |  | √ | ' ' |  |
| 26 | fsumpayamt | fsumpayamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 27 | fsuppilerid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 28 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 29 | ftaxamount | 商品金额 | numeric | 19 | 6 | √ | 0.000000 | 商品金额 |
| 30 | ferpbillstatus | ferpbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 31 | fdctrate | fdctrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 32 | fcategory | fcategory | varchar | 80 |  | √ | ' ' |  |
| 33 | flogstatus | flogstatus | bpchar | 1 |  | √ | ' ' |  |
| 34 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fjdorderstatus | fjdorderstatus | varchar | 255 |  | √ | ' ' |  |
| 36 | fispresent | fispresent | bpchar | 1 |  | √ | ' ' |  |
| 37 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 38 | ferpbillnumber | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 39 | fsumrequestqty | fsumrequestqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 40 | fsumoutstockqty | fsumoutstockqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 41 | fsuminstockqty | fsuminstockqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 42 | ftax | ftax | numeric | 19 | 6 | √ | 0.000000 |  |
| 43 | fcompareresult | fcompareresult | bpchar | 1 |  | √ | ' ' |  |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fsuminvamt | fsuminvamt | numeric | 19 | 6 | √ | 0.000000 |  |
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

## 商城订单-主表 t_mal_order

- **表名称：** 商城订单-主表
- **表名：** t_mal_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmalpaytype | 支付方式 | int8 | 64 |  | √ | 0 | [商城支付方式 pbd_paytype](../pbd_files/pbd_paytype.md) |
| 3 | fdelidate | fdelidate | timestamp | 0 |  |  | null |  |
| 4 | finvdetail | finvdetail | varchar | 2 |  | √ | ' ' |  |
| 5 | floccurrid | floccurrid | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdeporgid | fdeporgid | int8 | 64 |  | √ | 0 |  |
| 8 | fbilldate | 订货日期 | timestamp | 0 |  |  | null | 订货日期 |
| 9 | fexchtypeid | fexchtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 11 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 12 | fmalinvtype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 13 | finvtype | finvtype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | fsumamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 16 | freceiptid | 收货人 | int8 | 64 |  | √ | 0 | [收货信息 pbd_receiptinfo](../pbd_files/pbd_receiptinfo.md) |
| 17 | ftaxtype | ftaxtype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | 商城订单号 | varchar | 80 |  | √ | ' ' | 商城订单号 |
| 19 | fcostprojectid | fcostprojectid | int8 | 64 |  | √ | 0 |  |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fcostorgid | fcostorgid | int8 | 64 |  | √ | 0 |  |
| 22 | ffreight | ffreight | numeric | 19 | 6 | √ | 0.000000 |  |
| 23 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 25 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 26 | finvway | finvway | bpchar | 1 |  | √ | ' ' |  |
| 27 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 28 | fpaytype | fpaytype | varchar | 3 |  | √ | ' ' |  |
| 29 | fsumqty | fsumqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 31 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 32 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 33 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 34 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 35 | finvoiceorgid | finvoiceorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fexpenseorgid | fexpenseorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fpersonid | fpersonid | int8 | 64 |  | √ | 0 |  |
| 38 | fsumtaxamount | fsumtaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 39 | fsettleorgid | 核算公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fsumtax | fsumtax | numeric | 19 | 6 | √ | 0.000000 |  |
| 41 | ftalentid | ftalentid | varchar | 80 |  | √ | ' ' |  |
| 42 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 43 | fexchrate | fexchrate | numeric | 19 | 6 | √ | 1.000000 |  |
| 44 | fitemname | fitemname | varchar | 255 |  | √ | ' ' |  |
| 45 | fcontacterid | fcontacterid | int8 | 64 |  | √ | 0 |  |
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
