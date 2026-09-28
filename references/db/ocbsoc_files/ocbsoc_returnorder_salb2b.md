# 下游退货申请单(已作废)-ocbsoc_returnorder_salb2b

## 下游退货申请单(已作废)-关联追踪表 t_ocbsoc_returnorder_tc

- **表名称：** 下游退货申请单(已作废)-关联追踪表
- **表名：** t_ocbsoc_returnorder_tc

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
| 1 | pk_ocbsoc_returnorder_tc |  | fid |
| 2 | idx_ocbsoc_returnorder_tc_tbill |  | ftbillid |
| 3 | idx_ocbsoc_returnorder_tc_tid |  | ftid |

---

## 下游退货申请单(已作废)-主表 t_ocbsoc_rorder

- **表名称：** 下游退货申请单(已作废)-主表
- **表名：** t_ocbsoc_rorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconsigneename | 退货人 | varchar | 80 |  | √ | ' ' | 退货人 |
| 3 | frebateaccounttype | 资金池类别 | bpchar | 1 |  | √ | ' ' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 4 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 5 | ftradetype | 购销模式 | bpchar | 1 |  | √ | ' ' | 购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 G :渠道直送 H :分步调拨 I :店铺采购 |
| 6 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsalereturnstatus | 退货入库状态 | bpchar | 1 |  | √ | 'A' | 退货入库状态,枚举: A :未入库 D :部分入库 E :已入库 |
| 10 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 11 | fconsigneephone | 退货人电话 | varchar | 80 |  | √ | ' ' | 退货人电话 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fiscreditorder | 调货退货 | bpchar | 1 |  | √ | '0' | 调货退货 |
| 14 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 16 | freturnreasonid | 退货原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fconsigneeid | 退货地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |
| 19 | fdetailaddress | 退货详细地址 | varchar | 255 |  | √ | ' ' | 退货详细地址 |
| 20 | fbillno | 申请编号 | varchar | 80 |  | √ | ' ' | 申请编号 |
| 21 | foutchannelid | 退库渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 22 | fvehicleid | 退货车辆 | int8 | 64 |  | √ | 0 | [车辆信息 ocdbd_vehicle](../ococic_files/ocdbd_vehicle.md) |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | freturnchannelid | 退货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 P :预提交 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | [供货关系 ocdbd_channel_authorize](../ocdbd_files/ocdbd_channel_authorize.md) |
| 33 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 34 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 35 | fbusinesschannelid | 业务归属渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 36 | fpurreturnstatus | 退货出库状态 | bpchar | 1 |  | √ | 'A' | 退货出库状态,枚举: A :未出库 D :部分出库 E :已出库 |
| 37 | frtchannelid | 退货店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 38 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 39 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 40 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 41 | fpushstatus | 下推状态 | bpchar | 1 |  | √ | ' ' | 下推状态,枚举: A :已下推发货单 B :已下推销售出库/采购入库单 |
| 42 | fconsigneefixedtel | 固定电话 | varchar | 80 |  | √ | ' ' | 固定电话 |
| 43 | fareaid | 省市区 | varchar | 36 |  | √ | ' ' | 省市区 |
| 44 | faccountusemodel | 资金池抵扣模式 | bpchar | 1 |  | √ | 'A' | 资金池抵扣模式,枚举: A :按账户抵扣 B :按自定义维度抵扣 |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 47 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_rorder_bdt |  | fbilldate |
| 2 | idx_ocbsoc_rorder_bno |  | fbillno |
| 3 | pk_ocbsoc_rorder |  | fid |

---

## 商品分录-子表 t_ocbsoc_rorderentry

- **表名称：** 商品分录-子表
- **表名：** t_ocbsoc_rorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 6 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foperationmodeid | 经营方式 | int8 | 64 |  | √ | 0 | [商品经营方式 ocdbd_item_businesstype](../ocdpm_files/ocdbd_item_businesstype.md) |
| 9 | fscmlotid | 批号ID | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 10 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fociclotid | 商品批号 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 14 | fqty | 退货数量 | numeric | 23 | 10 | √ | 0 | 退货数量 |
| 15 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | freturnverify | 企业版退货校验 | bpchar | 1 |  | √ | '0' | 企业版退货校验 |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 20 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 22 | foutwarehouseid | 退库仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 23 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 24 | fbaseqty | 基本退货数量 | numeric | 23 | 10 | √ | 0 | 基本退货数量 |
| 25 | fassistqty | 辅助退货数量 | numeric | 23 | 10 | √ | 0 | 辅助退货数量 |
| 26 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_rorderentry |  | fentryid |
| 2 | idx_ocbsoc_rorderentry_id |  | fid |

---

## 关联子实体-子表 t_ocbsoc_rorder_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_rorder_entry_lk

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
| 1 | idx_ocbsoc_rorder_entry_lk_fk |  | fentryid |
| 2 | pk_ocbsoc_rorder_entry_lk |  | fpkid |

---

## 下游退货申请单(已作废)-反写记录表 t_ocbsoc_returnorder_wb

- **表名称：** 下游退货申请单(已作废)-反写记录表
- **表名：** t_ocbsoc_returnorder_wb

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
| 1 | idx_ocbsoc_returnorder_wb_fk |  | fid |
| 2 | pk_ocbsoc_returnorder_wb |  | fentryid |

---

## 下游退货申请单(已作废)-分表 t_ocbsoc_rorder_f

- **表名称：** 下游退货申请单(已作废)-分表
- **表名：** t_ocbsoc_rorder_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumlocaltax | 税额合计本位币 | numeric | 23 | 10 | √ | 0 | 税额合计本位币 |
| 3 | fintegrationtype | 集成ERP | bpchar | 1 |  | √ | 'A' | 集成ERP,枚举: A :无 B :星空企业版 C :星瀚 D :其他ERP |
| 4 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 5 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 6 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 7 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fsumlocalamount | 不含税金额合计本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额合计本位币 |
| 11 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 12 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 13 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 14 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 17 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fsyncbillno | 同步退货通知单编号 | varchar | 80 |  | √ | ' ' | 同步退货通知单编号 |
| 19 | fsyncstatus | 同步状态 | bpchar | 1 |  | √ | 'A' | 同步状态,枚举: A :未同步 B :同步中 C :同步失败 D :同步完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_rorderf_sbid |  | fsettlecurrencyid,fbasecurrencyid |
| 2 | pk_ocbsoc_rorder_f |  | fid |

---

## 退款抵扣信息-子表 t_ocbsoc_rorderrecentry

- **表名称：** 退款抵扣信息-子表
- **表名：** t_ocbsoc_rorderrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcashpoolsrcentryid | 资金池来源行ID | int8 | 64 |  | √ | 0 | 资金池来源行ID |
| 3 | fcashpoolid | 资金池ID | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 4 | frealrefundinterest | 本次退回利息 | numeric | 23 | 10 | √ | 0 | 本次退回利息 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcrecentryid | 来源收款抵扣行ID | int8 | 64 |  | √ | 0 | 来源收款抵扣行ID |
| 7 | frecremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fbillamount | fbillamount | numeric | 23 | 10 | √ | 0 |  |
| 9 | fcashpoolsrcid | 资金池来源单据ID | int8 | 64 |  | √ | 0 | 资金池来源单据ID |
| 10 | frefundinterest | 退回利息 | numeric | 23 | 10 | √ | 0 | 退回利息 |
| 11 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 12 | fusedamount | 本次回退金额 | numeric | 23 | 10 | √ | 0 | 本次回退金额 |
| 13 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | [收款抵扣类型 ocdbd_receiptoffset](../ocbsoc_files/ocdbd_receiptoffset.md) |
| 14 | fcashpoolsrcentity | 资金池来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fisreturn | 是否返还抵扣 | bpchar | 1 |  | √ | '0' | 是否返还抵扣 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fcashpoolsrcnumber | 资金池来源单据编码 | varchar | 80 |  | √ | ' ' | 资金池来源单据编码 |
| 18 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_rorderrecentry |  | fentryid |
| 2 | idx_ocbsoc_rorderrecentry_id |  | fid |

---

## 抵扣账户分摊明细表-子表 t_ocbsoc_rorderrecdisc

- **表名称：** 抵扣账户分摊明细表-子表
- **表名：** t_ocbsoc_rorderrecdisc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitrecdiscount | 单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 单位抵扣金额 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | frecentryid | 抵扣行ID | int8 | 64 |  | √ | 0 | 抵扣行ID |
| 5 | fitementryid | 商品明细行ID | int8 | 64 |  | √ | 0 | 商品明细行ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_rorderrecdisc_eid |  | fid |
| 2 | pk_ocbsoc_rorderrecdisc |  | fentryid |

---

## 商品分录-分表 t_ocbsoc_rorderentry_f

- **表名称：** 商品分录-分表
- **表名：** t_ocbsoc_rorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | flocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 4 | flocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 5 | fpromotiondiscount | 促销折扣 | numeric | 23 | 10 | √ | 0 | 促销折扣 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 7 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :单位折扣率％ B :单位折扣额 NULL :无 |
| 8 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 9 | funitpromotiondiscount | 基本单位促销折扣 | numeric | 23 | 10 | √ | 0 | 基本单位促销折扣 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 11 | fdiscount | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 12 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | frebateamount | 计返利金额 | numeric | 23 | 10 | √ | 0 | 计返利金额 |
| 15 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 16 | frecdiscount | 抵扣分摊折扣 | numeric | 23 | 10 | √ | 0 | 抵扣分摊折扣 |
| 17 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 18 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 19 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 20 | fbudgetamount | 计预算金额 | numeric | 23 | 10 | √ | 0 | 计预算金额 |
| 21 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 22 | fsaleamount | 计销量金额 | numeric | 23 | 10 | √ | 0 | 计销量金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | funitdiscount | 单位总折扣（率） | numeric | 23 | 10 | √ | 0 | 单位总折扣（率） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_rorderentry_f |  | fentryid |
| 2 | idx_ocbsoc_rorderentryf_id |  | fid |

---

## 序列号-子表 t_ocbsoc_rordersndetail

- **表名称：** 序列号-子表
- **表名：** t_ocbsoc_rordersndetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 5 | fscmserialid | 供应链序列号 | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 6 | focicserialid | 商品序列号 | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_rordersndetail |  | fdetailid |
| 2 | idx_ocbsoc_rordersndetail_eid |  | fentryid |

---

## 商品分录-分表 t_ocbsoc_rorderentry_x

- **表名称：** 商品分录-分表
- **表名：** t_ocbsoc_rorderentry_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainbillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 3 | fsumsalereturnassistqty | 累计退货入库辅助数量 | numeric | 23 | 10 | √ | 0 | 累计退货入库辅助数量 |
| 4 | fsumrefundassistqty | 累计换补货辅助数量 | numeric | 23 | 10 | √ | 0 | 累计换补货辅助数量 |
| 5 | fjoindelireturnassistqty | 关联发货退货辅助数量 | numeric | 23 | 10 | √ | 0 | 关联发货退货辅助数量 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 7 | fjoinrefundassistqty | 关联换补货辅助数量 | numeric | 23 | 10 | √ | 0 | 关联换补货辅助数量 |
| 8 | fsumdelireturnbaseqty | 累计发货退货基本数量 | numeric | 23 | 10 | √ | 0 | 累计发货退货基本数量 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 11 | fjoinsalereturnassistqty | 关联退货入库辅助数量 | numeric | 23 | 10 | √ | 0 | 关联退货入库辅助数量 |
| 12 | fjoinretrunbaseqty | 关联申请基本数量 | numeric | 23 | 10 | √ | 0 | 关联申请基本数量 |
| 13 | fsumretrunbaseqty | 累计申请基本数量 | numeric | 23 | 10 | √ | 0 | 累计申请基本数量 |
| 14 | fjoindelireturnbaseqty | 关联发货退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联发货退货基本数量 |
| 15 | fjoinrefundbaseqty | 关联换补货基本数量 | numeric | 23 | 10 | √ | 0 | 关联换补货基本数量 |
| 16 | fjoinsalereturnbaseqty | 关联退货入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联退货入库基本数量 |
| 17 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 18 | fsumrefundbaseqty | 累计换补货基本数量 | numeric | 23 | 10 | √ | 0 | 累计换补货基本数量 |
| 19 | fsumdelireturnassistqty | 累计发货退货辅助数量 | numeric | 23 | 10 | √ | 0 | 累计发货退货辅助数量 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fsumpurreturnassistqty | 累计退货出库辅助数量 | numeric | 23 | 10 | √ | 0 | 累计退货出库辅助数量 |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | fsumsalereturnbaseqty | 累计退货入库基本数量 | numeric | 23 | 10 | √ | 0 | 累计退货入库基本数量 |
| 25 | fsumpurreturnbaseqty | 累计退货出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计退货出库基本数量 |
| 26 | fsrcitementryid | 来源商品行ID | int8 | 64 |  | √ | 0 | 来源商品行ID |
| 27 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 28 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 29 | fjoinpurreturnbaseqty | 关联退货出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联退货出库基本数量 |
| 30 | fjoinpurreturnassistqty | 关联退货出库辅助数量 | numeric | 23 | 10 | √ | 0 | 关联退货出库辅助数量 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_rorderentry_x |  | fentryid |
| 2 | idx_ocbsoc_rorderentryx_id |  | fid |
