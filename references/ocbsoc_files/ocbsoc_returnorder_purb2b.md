# 我的退货申请单(已作废)-ocbsoc_returnorder_purb2b

## 我的退货申请单(已作废)-关联追踪表 t_ocbsoc_returnorder_tc

- **表名称：** 我的退货申请单(已作废)-关联追踪表
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

## 我的退货申请单(已作废)-主表 t_ocbsoc_rorder

- **表名称：** 我的退货申请单(已作废)-主表
- **表名：** t_ocbsoc_rorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconsigneename | 退货人 | varchar | 80 |  | √ | ' ' | 退货人 |
| 3 | frebateaccounttype | 资金池类别 | bpchar | 1 |  | √ | ' ' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 4 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 5 | ftradetype | 购销模式 | bpchar | 1 |  | √ | ' ' | 购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 G :渠道直送 |
| 6 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsalereturnstatus | 退货入库状态 | bpchar | 1 |  | √ | 'A' | 退货入库状态,枚举: A :未入库 D :部分入库 E :已入库 |
| 10 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 11 | fconsigneephone | 退货人电话 | varchar | 80 |  | √ | ' ' | 退货人电话 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fiscreditorder | 调货退货 | bpchar | 1 |  | √ | '0' | 调货退货 |
| 14 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | freturnreasonid | 退货原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 18 | fconsigneeid | 退货地址 | int8 | 64 |  | √ | 0 | 渠道收货地址 ocdbd_channel_address |
| 19 | fdetailaddress | 退货详细地址 | varchar | 255 |  | √ | ' ' | 退货详细地址 |
| 20 | fbillno | 申请编号 | varchar | 80 |  | √ | ' ' | 申请编号 |
| 21 | foutchannelid | 退库渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 22 | fvehicleid | 退货车辆 | int8 | 64 |  | √ | 0 | 车辆信息 ocdbd_vehicle |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | freturnchannelid | 退货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 P :预提交 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | 供货关系 ocdbd_channel_authorize |
| 33 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 34 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 35 | fbusinesschannelid | 业务归属渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 36 | fpurreturnstatus | 退货出库状态 | bpchar | 1 |  | √ | 'A' | 退货出库状态,枚举: A :未出库 D :部分出库 E :已出库 |
| 37 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 38 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 39 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 40 | fpushstatus | 下推状态 | bpchar | 1 |  | √ | ' ' | 下推状态,枚举: A :已下推发货单 B :已下推销售出库/采购入库单 |
| 41 | fconsigneefixedtel | 固定电话 | varchar | 80 |  | √ | ' ' | 固定电话 |
| 42 | fareaid | 省市区 | varchar | 36 |  | √ | ' ' | 省市区 |
| 43 | faccountusemodel | 资金池抵扣模式 | bpchar | 1 |  | √ | 'A' | 资金池抵扣模式,枚举: A :按账户抵扣 B :按自定义维度抵扣 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 46 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

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
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 6 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foperationmodeid | 经营方式 | int8 | 64 |  | √ | 0 | 商品经营方式 ocdbd_item_businesstype |
| 9 | fscmlotid | 批号ID | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 10 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fociclotid | 商品批号 | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 14 | fqty | 退货数量 | numeric | 23 | 10 | √ | 0 | 退货数量 |
| 15 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 19 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 20 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 21 | foutwarehouseid | 退库仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 22 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 23 | fbaseqty | 基本退货数量 | numeric | 23 | 10 | √ | 0 | 基本退货数量 |
| 24 | fassistqty | 辅助退货数量 | numeric | 23 | 10 | √ | 0 | 辅助退货数量 |
| 25 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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

## 我的退货申请单(已作废)-反写记录表 t_ocbsoc_returnorder_wb

- **表名称：** 我的退货申请单(已作废)-反写记录表
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

## 我的退货申请单(已作废)-分表 t_ocbsoc_rorder_f

- **表名称：** 我的退货申请单(已作废)-分表
- **表名：** t_ocbsoc_rorder_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsumlocaltax | 税额合计本位币 | numeric | 23 | 10 | √ | 0 | 税额合计本位币 |
| 3 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 4 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 5 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | 渠道价格类型 ocdbd_price_type |
| 6 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fsumlocalamount | 不含税金额合计本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额合计本位币 |
| 10 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 11 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 12 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 13 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 16 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 3 | fcashpoolid | 资金池ID | int8 | 64 |  | √ | 0 | 资金池余额 ocdbd_rebateaccount |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcrecentryid | 来源收款抵扣行ID | int8 | 64 |  | √ | 0 | 来源收款抵扣行ID |
| 6 | frecremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fbillamount | fbillamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | fcashpoolsrcid | 资金池来源单据ID | int8 | 64 |  | √ | 0 | 资金池来源单据ID |
| 9 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 10 | fusedamount | 本次回退金额 | numeric | 23 | 10 | √ | 0 | 本次回退金额 |
| 11 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | 收款抵扣类型 ocdbd_receiptoffset |
| 12 | fcashpoolsrcentity | 资金池来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fisreturn | 是否返还抵扣 | bpchar | 1 |  | √ | '0' | 是否返还抵扣 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcashpoolsrcnumber | 资金池来源单据编码 | varchar | 80 |  | √ | ' ' | 资金池来源单据编码 |
| 16 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

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
| 14 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 15 | frecdiscount | 抵扣分摊折扣 | numeric | 23 | 10 | √ | 0 | 抵扣分摊折扣 |
| 16 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 17 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 18 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 19 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | funitdiscount | 单位总折扣（率） | numeric | 23 | 10 | √ | 0 | 单位总折扣（率） |

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
| 5 | fscmserialid | 供应链序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |
| 6 | focicserialid | 商品序列号 | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |

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
