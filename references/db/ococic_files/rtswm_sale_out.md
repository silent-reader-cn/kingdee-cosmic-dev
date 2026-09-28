# 店铺销售出库单-rtswm_sale_out

## 商品明细-分表 t_rtswm_saleoutentry_f

- **表名称：** 商品明细-分表
- **表名：** t_rtswm_saleoutentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 2 | √ | 0 | 税率(%) |
| 4 | fdiscountrate | 折扣率(%) | numeric | 23 | 6 | √ | 0 | 折扣率(%) |
| 5 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 8 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fcostprice | 成本单价 | numeric | 23 | 10 | √ | 0 | 成本单价 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fcostamount | 成本金额 | numeric | 23 | 10 | √ | 0 | 成本金额 |
| 13 | famountloc | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 14 | famountandtaxloc | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 15 | ftaxamountloc | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fdiscountamountloc | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtswm_saleoutentry_f |  | fentryid |
| 2 | idx_rtswm_saleoutentry_fid |  | fid |

---

## 关联子实体-子表 t_rtswm_saleoutentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_rtswm_saleoutentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtswm_saleoutentry_lk |  | fpkid |
| 2 | idx_rtswm_saleoutentry_lk_fk |  | fentryid |

---

## 结算明细-子表 t_rtswm_saleoutsettle

- **表名称：** 结算明细-子表
- **表名：** t_rtswm_saleoutsettle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fcardno | 卡/券号 | varchar | 50 |  | √ | ' ' | 卡/券号 |
| 4 | flocsettleamt | 结算金额本位币 | numeric | 23 | 10 | √ | 0 | 结算金额本位币 |
| 5 | fsettleid | 结算方式 | int8 | 64 |  | √ | 0 | 支付通道 rtbd_paymode |
| 6 | fsettlecurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fintegralconsum | 消耗积分 | numeric | 23 | 10 | √ | 0 | 消耗积分 |
| 10 | fexcrateld | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtswm_saleoutsettle_id |  | fid |
| 2 | pk_rtswm_saleoutsettle |  | fentryid |

---

## 商品明细-子表 t_rtswm_saleoutentry

- **表名称：** 商品明细-子表
- **表名：** t_rtswm_saleoutentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsnqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 对应物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 ocdbd_channel :渠道 |
| 9 | foutownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fgoodsclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 11 | fbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 12 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | foutinvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | foutkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fsnunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | foutownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 ocdbd_channel :渠道 |
| 20 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 21 | fchannellocationid | 仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 22 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fauxunitqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 24 | fwarehouseid | ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | foutinvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 26 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 27 | flocationid | ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 28 | fchannelwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 29 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 30 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 31 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 32 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rtswm_saleoutentry_id |  | fid |
| 2 | pk_rtswm_saleoutentry |  | fentryid |

---

## 店铺销售出库单-关联追踪表 t_rtswm_saleout_tc

- **表名称：** 店铺销售出库单-关联追踪表
- **表名：** t_rtswm_saleout_tc

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
| 1 | pk_rtswm_saleout_tc |  | fid |
| 2 | idx_rtswm_saleout_tc_tbill |  | ftbillid |
| 3 | idx_rtswm_saleout_tc_tid |  | ftid |

---

## 店铺销售出库单-主表 t_rtswm_saleout

- **表名称：** 店铺销售出库单-主表
- **表名：** t_rtswm_saleout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisredbill | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 3 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbizoperatorid | 销售员 | int8 | 64 |  | √ | 0 | 店铺人员 rtbd_user |
| 6 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 7 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 11 | fdeliveroperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 15 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fsalechannel | 销售店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 21 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 22 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 25 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtswm_saleout |  | fid |
| 2 | idx__rtswm_saleout_no |  | fbillno |

---

## 序列号明细-子表 t_rtswm_saleoutserial

- **表名称：** 序列号明细-子表
- **表名：** t_rtswm_saleoutserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fserialid | 序列号ID | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fserialnumber | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 6 | fserialcomment | 备注 | varchar | 100 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtswm_saleoutserial |  | fdetailid |
| 2 | idx_rtswm_saleoutserial_id |  | fentryid |

---

## 商品明细-分表 t_rtswm_saleoutentry_r

- **表名称：** 商品明细-分表
- **表名：** t_rtswm_saleoutentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 3 | frelatebaseqty | ERP关联基本数量 | numeric | 23 | 10 | √ | 0 | ERP关联基本数量 |
| 4 | fsrcbilleid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | fdueqty | 关联应收数量 | numeric | 23 | 10 | √ | 0 | 关联应收数量 |
| 6 | fredqty | 已冲销数量 | numeric | 23 | 10 | √ | 0 | 已冲销数量 |
| 7 | fsrcorderbillentryid | 订单单据分录ID | int8 | 64 |  | √ | 0 | 订单单据分录ID |
| 8 | fduebaseqty | 关联应收基本数量 | numeric | 23 | 10 | √ | 0 | 关联应收基本数量 |
| 9 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 10 | fredbaseqty | 已冲销基本数量 | numeric | 23 | 10 | √ | 0 | 已冲销基本数量 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcorderbilleid | 订单单据ID | int8 | 64 |  | √ | 0 | 订单单据ID |
| 13 | fdueamount | 关联应收金额 | numeric | 23 | 10 | √ | 0 | 关联应收金额 |
| 14 | fsrcorderbillentity | 订单单据实体 | varchar | 50 |  | √ | ' ' | 订单单据实体 |
| 15 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 16 | fsrcorderbillentryseq | 订单单据分录序号 | int8 | 64 |  | √ | 0 | 订单单据分录序号 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fsrcorderbillno | 订单单据编号 | varchar | 50 |  | √ | ' ' | 订单单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__rtswm_saleoutentry_rid |  | fid |
| 2 | pk_rtswm_saleoutentry_r |  | fentryid |

---

## 店铺销售出库单-反写记录表 t_rtswm_saleout_wb

- **表名称：** 店铺销售出库单-反写记录表
- **表名：** t_rtswm_saleout_wb

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
| 1 | idx_rtswm_saleout_wb_fk |  | fid |
| 2 | pk_rtswm_saleout_wb |  | fentryid |

---

## 店铺销售出库单-分表 t_rtswm_saleout_f

- **表名称：** 店铺销售出库单-分表
- **表名：** t_rtswm_saleout_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalamountloc | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | ftotaldisamountloc | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 6 | ftotalallamountloc | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 7 | ftotaltaxamountloc | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | ftotaldisamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 11 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 12 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rtswm_saleout_f |  | fid |
