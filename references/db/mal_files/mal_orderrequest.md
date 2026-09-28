# 商城采购申请-mal_orderrequest

## 商城采购申请-多语言表 t_mal_orderrequest_l

- **表名称：** 商城采购申请-多语言表
- **表名：** t_mal_orderrequest_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 申请事由 | varchar | 255 |  | √ | ' ' | 申请事由 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orderrequest_fid_flocaleid |  | fid,flocaleid |
| 2 | pk_mal_orderrequest_l |  | fpkid |

---

## 商城采购申请-主表 t_mal_orderrequest

- **表名称：** 商城采购申请-主表
- **表名：** t_mal_orderrequest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | freceiptinfo | 详细地址 | varchar | 1000 |  | √ | ' ' | 详细地址 |
| 4 | fdeporgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbilldate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freqpersonid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsumamount | 申请下单金额 | numeric | 23 | 10 | √ | 0 | 申请下单金额 |
| 10 | freceiptid | 收货信息 | int8 | 64 |  | √ | 0 | [收货地址 mal_address](../mal_files/mal_address.md) |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fcostprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 13 | fremark | 申请事由 | varchar | 255 |  | √ | ' ' | 申请事由 |
| 14 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fcostorgid | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: mal_newshopcart :购物车 mal_purchase :商城选购 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | finvoiceorgid | 开票单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fexpenseorgid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 27 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 28 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_orderrequest |  | fid |
| 2 | idx_mal_orderrequest_fbillno |  | fbillno |
| 3 | idx_mal_orderrequest_fcreator |  | fcreatorid |
| 4 | idx_mal_orderrequest_fbilldate |  | fbilldate |

---

## 单据体-子表 t_mal_orderrequestentry

- **表名称：** 单据体-子表
- **表名：** t_mal_orderrequestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsimg | 图片字段 | varchar | 510 |  | √ | ' ' | 图片字段 |
| 3 | fsrcentryid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 4 | funtaxgoodsprice | 未税商品价格 | numeric | 23 | 10 | √ | 0 | 未税商品价格 |
| 5 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fprotocolsourceentryid | 协议分录ID | int8 | 64 |  | √ | 0 | 协议分录ID |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含费价格 | numeric | 23 | 10 | √ | 0 | 含费价格 |
| 11 | fentrycostprojectid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 12 | famount | 未税含费金额 | numeric | 23 | 10 | √ | 0 | 未税含费金额 |
| 13 | favgfreight | 分摊运费 | numeric | 23 | 10 | √ | 0 | 分摊运费 |
| 14 | fprice | 未税含费价格 | numeric | 23 | 10 | √ | 0 | 未税含费价格 |
| 15 | funtaxgoodsamount | 未税商品金额 | numeric | 23 | 10 | √ | 0 | 未税商品金额 |
| 16 | fextamount |  | numeric | 23 | 10 | √ | 0 |  |
| 17 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 18 | fcompareid | 比价标识 | varchar | 80 |  | √ | ' ' | 比价标识 |
| 19 | fmalpaytypeid | 支付方式 | int8 | 64 |  | √ | 0 | [商城支付方式 pbd_paytype](../pbd_files/pbd_paytype.md) |
| 20 | fminorderqty | 0 | numeric | 23 | 10 | √ | 0 | 0 |
| 21 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 22 | fplatform | 电商平台 | varchar | 10 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 23 | fcompareremark | 比价说明 | varchar | 255 |  | √ | ' ' | 比价说明 |
| 24 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fsuppilerid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 26 | fgoodsprice | 商品含税价格 | numeric | 23 | 10 | √ | 0 | 商品含税价格 |
| 27 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 28 | ftaxamount | 含费金额 | numeric | 23 | 10 | √ | 0 | 含费金额 |
| 29 | fmalorderentryid | 商城订单分录ID | int8 | 64 |  | √ | 0 | 商城订单分录ID |
| 30 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 31 | fgoodsamount | 商品金额 | numeric | 23 | 10 | √ | 0 | 商品金额 |
| 32 | fsrcbillid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 33 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fmalorderid | 商城订单ID | int8 | 64 |  | √ | 0 | 商城订单ID |
| 35 | fcompareresult | 比价结果 | bpchar | 1 |  | √ | 'A' | 比价结果,枚举: A :未比价 B :最低价 C :非最低价 |
| 36 | ftax | 含费税额 | numeric | 23 | 10 | √ | 0 | 含费税额 |
| 37 | fprotocolsourceid | 协议单据ID | int8 | 64 |  | √ | 0 | 协议单据ID |
| 38 | fmalorderbillno | 商城订单号 | varchar | 50 |  | √ | ' ' | 商城订单号 |
| 39 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 40 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 44 | fprotocolno |  | varchar | 255 |  | √ | ' ' |  |
| 45 | fgoodsuseid | 商品用途 | int8 | 64 |  | √ | 0 | [商品用途 pmm_goods_use](../pmm_files/pmm_goods_use.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_orderrequestentry |  | fentryid |
| 2 | idx_orderrequestentry_fid |  | fid |
