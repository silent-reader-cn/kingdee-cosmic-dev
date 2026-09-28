# 开票中（废弃）-mal_statement_invoicing

## 明细数据-子表 t_mal_statementdataentry

- **表名称：** 明细数据-子表
- **表名：** t_mal_statementdataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fsrcbillno | 收货/入库单号 | varchar | 80 |  | √ | ' ' | 收货/入库单号 |
| 6 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 7 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 14 | fdate | 收货/入库日期 | timestamp | 0 |  |  | null | 收货/入库日期 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fentryunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_stm_entry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_statementdataentry |  | fentryid |

---

## 开票中（废弃）-多语言表 t_mal_statementdata_l

- **表名称：** 开票中（废弃）-多语言表
- **表名：** t_mal_statementdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_statementdata_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_statementdata_l |  | fpkid |

---

## 开票中（废弃）-主表 t_mal_statementdata

- **表名称：** 开票中（废弃）-主表
- **表名：** t_mal_statementdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fecorderid | 电商子订单号 | varchar | 80 |  | √ | ' ' | 电商子订单号 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fecorderqty | 电商订单数量 | int4 | 32 |  | √ | 0 | 电商订单数量 |
| 5 | fpurcheckno | 关联对账单号 | varchar | 80 |  | √ | ' ' | 关联对账单号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freqpersonid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpurorderbillno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 9 | fsumamount | 收货/入库金额（不含税） | numeric | 23 | 10 | √ | 0 | 收货/入库金额（不含税） |
| 10 | finvoiceresult | 开票结果 | varchar | 255 |  | √ | ' ' | 开票结果 |
| 11 | fbillno | 对账数据编号 | varchar | 80 |  | √ | ' ' | 对账数据编号 |
| 12 | flocalecorderid | 子订单号 | varchar | 80 |  | √ | ' ' | 子订单号 |
| 13 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 15 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fmalorderid | 商城订单id | int8 | 64 |  | √ | 0 | 商城订单id |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fecreturnqty | 电商退货数量 | int4 | 32 |  | √ | 0 | 电商退货数量 |
| 20 | feccount | 电商结算数量 | int4 | 32 |  | √ | 0 | 电商结算数量 |
| 21 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 22 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 23 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fecreturntaxamount | 电商退货金额 | numeric | 23 | 10 | √ | 0 | 电商退货金额 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | finvoicestatus | 开票状态 | varchar | 10 |  | √ | ' ' | 开票状态,枚举: 1 :待申请 2 :待审核 3 :驳回 4 :部分开票成功 5 :待出票 6 :开票成功 7 :处理中 8 :开票失败 |
| 27 | fskuid | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 28 | fdeporgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fbilldate | 对账日期 | timestamp | 0 |  |  | null | 对账日期 |
| 30 | fdiffqty | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 31 | flocalecporderid | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fcheckresult | 对账结果 | varchar | 10 |  | √ | ' ' | 对账结果,枚举: 1 :无差异 2 :有差异 |
| 34 | faftersalestatus | 售后状态 | varchar | 10 |  | √ | ' ' | 售后状态,枚举: A :待确认 B :已确认 C :已打回 E :已取消 F :已完成 G :自动确认 N :无售后 |
| 35 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 36 | freceiptid | 收货人 | int8 | 64 |  | √ | 0 | [收货地址 mal_address](../mal_files/mal_address.md) |
| 37 | fectaxamount | 电商结算金额 | numeric | 23 | 10 | √ | 0 | 电商结算金额 |
| 38 | fecporderid | 电商父订单号 | varchar | 80 |  | √ | ' ' | 电商父订单号 |
| 39 | fskuname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 40 | ftaxtype | 计税类型 | varchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 41 | fpurinvoiceno | 关联开票单号 | varchar | 80 |  | √ | ' ' | 关联开票单号 |
| 42 | fecordertaxamount | 电商订单金额 | numeric | 23 | 10 | √ | 0 | 电商订单金额 |
| 43 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmalorderentryid | 商城订单分录id | int8 | 64 |  | √ | 0 | 商城订单分录id |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | finvtypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 50 | flocalprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 51 | flocaltaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 52 | fsumqty | 收货/入库数量 | numeric | 23 | 10 | √ | 0 | 收货/入库数量 |
| 53 | fordercreatorid | 订单创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fsumtaxamount | 收货/入库金额 | numeric | 23 | 10 | √ | 0 | 收货/入库金额 |
| 55 | fmalorderbillno | 商城订单号 | varchar | 80 |  | √ | ' ' | 商城订单号 |
| 56 | flocaltaxprice | 商品价格 | numeric | 23 | 10 | √ | 0 | 商品价格 |
| 57 | fsumtax | 收货/入库税额 | numeric | 23 | 10 | √ | 0 | 收货/入库税额 |
| 58 | fectaxprice | 电商商品价格 | numeric | 23 | 10 | √ | 0 | 电商商品价格 |
| 59 | fdifftaxamount | 差异金额 | numeric | 23 | 10 | √ | 0 | 差异金额 |
| 60 | fcheckstatus | 对账状态 | bpchar | 1 |  | √ | ' ' | 对账状态,枚举: C :已对账 B :未对账 A :对账中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_statementdata |  | fid |
| 2 | idx_mal_stmd_fskuid |  | fskuid |
| 3 | idx_mal_stmd_fecorderid |  | fecorderid |

---

## 开票中（废弃）-分表 t_mal_statementdata_a

- **表名称：** 开票中（废弃）-分表
- **表名：** t_mal_statementdata_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
