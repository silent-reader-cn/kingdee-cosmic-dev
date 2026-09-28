# 要货订单变更-ocbsoc_xsaleorder

## 交付计划子单体-分表 t_ocbsoc_xordersentry_r

- **表名称：** 交付计划子单体-分表
- **表名：** t_ocbsoc_xordersentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftotalorderbaseqty | 累计订单基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单基本单位数量 |
| 2 | fjoinpickingqty | 已关联拣货数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货数量 |
| 3 | fsignedbaseqty | 已签收基本单位数量 | numeric | 23 | 10 | √ | 0 | 已签收基本单位数量 |
| 4 | fjoinreturnassistqty | 已关联退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货辅助单位数量 |
| 5 | fjoinreturnbaseqty | 已关联退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货基本单位数量 |
| 6 | ftotalreturnbaseqty | 累计退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货基本单位数量 |
| 7 | ftotaloutstockbaseqty | 累计出库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库基本单位数量 |
| 8 | fjoinorderassistqty | 已关联辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联辅助单位数量 |
| 9 | ftotalorderassistqty | 累计订单辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单辅助单位数量 |
| 10 | ftotalinstockassistqty | 累计入库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库辅助单位数量 |
| 11 | ftotalreturnassistqty | 累计退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货辅助单位数量 |
| 12 | ftotaloutstockassistqty | 累计出库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库辅助单位数量 |
| 13 | ftotalinstockbaseqty | 累计入库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库基本单位数量 |
| 14 | ftotalpickingbaseqty | 已拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已拣货基本数量 |
| 15 | fjoinorderbaseqty | 已关联基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联基本单位数量 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 17 | fsignedassistqty | 已签收辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已签收辅助单位数量 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fjoinpickingbaseqty | 已关联拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货基本数量 |
| 20 | ftotalpickingqty | 已拣货数量 | numeric | 23 | 10 | √ | 0 | 已拣货数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xordersentryr_eid |  | fentryid |
| 2 | pk_ocbsoc_xordersentry_r |  | fdetailid |

---

## 要货订单变更-主表 t_ocbsoc_xorder

- **表名称：** 要货订单变更-主表
- **表名：** t_ocbsoc_xorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fclosetime | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货 E :已发货 F :已完成 P :预提交 |
| 6 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdeliveryway | 配送方式 | bpchar | 1 |  | √ | ' ' | 配送方式,枚举: A :物流发货 B :车辆配送 C :客户自提 |
| 8 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 9 | forderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 11 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | [供货关系 ocdbd_channel_authorize](../ocdbd_files/ocdbd_channel_authorize.md) |
| 12 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 13 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 14 | frtchannelid | 订货店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 15 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fconfirmtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 18 | fchangeversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 21 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 22 | fsourcebilltypeid | 源单据类型id | int8 | 64 |  | √ | 0 | 源单据类型id |
| 23 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | 'A' | 确认状态,枚举: A :无需确认 B :未确认 C :已确认 |
| 24 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 25 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 27 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 28 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 29 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 32 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未发货 B :待签收 C :部分签收 D :签收完成 |
| 33 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 34 | fsourceapply | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :B2B订单中心 2 :渠道门户 3 :零售管理 4 :渠道管家 |
| 35 | fcumulatepromsettle | 结算累计促销赠品 | bpchar | 1 |  | √ | '0' | 结算累计促销赠品 |
| 36 | fsrcpursalemodel | 源单购销模式 | bpchar | 1 |  | √ | ' ' | 源单购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 F :内销同步结算 G :渠道直送 H :分步调拨 I :店铺采购 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fisvaletorder | 订单标识 | bpchar | 1 |  | √ | '1' | 订单标识,枚举: 0 :自助下单 1 :代客下单 2 :铺货下单 4 :车销订单 5 :访销订单 3 :其他 |
| 39 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 44 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 45 | fbusinesschannelid | 业务归属渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 46 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 47 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 48 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 50 | fsourceplatform | 来源平台 | bpchar | 1 |  | √ | '1' | 来源平台,枚举: 1 :PC端 2 :移动端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xorder |  | fid |
| 2 | idx_ocbsoc_xorder_odate |  | forderdate |
| 3 | idx_ocbsoc_xorder_schl |  | fsalechannelid |
| 4 | idx_ocbsoc_xorder_ochl |  | forderchannelid |
| 5 | idx_ocbsoc_xorder_saler |  | fsalerid |
| 6 | idx_ocbsoc_xorder_bno |  | fbillno |

---

## 预留明细-子表 t_ocbsoc_reserveentry

- **表名称：** 预留明细-子表
- **表名：** t_ocbsoc_reserveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freservebaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | freserveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 10 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 12 | fdetailid | 交付计划行Id | int8 | 64 |  | √ | 0 | 交付计划行Id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_reserveentry_fid |  | fid |
| 2 | idx_ocbsoc_reserveentry_fdid |  | fdetailid |
| 3 | pk_ocbsoc_reserveentry |  | fentryid |

---

## 抵扣账户分摊明细表-子表 t_ocbsoc_xorecdiscount

- **表名称：** 抵扣账户分摊明细表-子表
- **表名：** t_ocbsoc_xorecdiscount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 3 | frecdiscount | 抵扣金额 | numeric | 23 | 10 | √ | 0 | 抵扣金额 |
| 4 | frecitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 5 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 6 | fdiscountentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 7 | funitrecdiscount | 基本单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 基本单位抵扣金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | frecentryid | 抵扣行ID | int8 | 64 |  | √ | 0 | 抵扣行ID |
| 10 | fitementryid | 商品明细行ID | int8 | 64 |  | √ | 0 | 商品明细行ID |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xorecdiscount_eid |  | fid |
| 2 | pk_ocbsoc_xorecdiscount |  | fentryid |

---

## 要货订单变更-分表 t_ocbsoc_xorder_f

- **表名称：** 要货订单变更-分表
- **表名：** t_ocbsoc_xorder_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoeicetaker | 收票人 | varchar | 255 |  | √ | ' ' | 收票人 |
| 3 | fsumlocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 4 | fintegrationtype | 集成ERP | bpchar | 1 |  | √ | 'A' | 集成ERP,枚举: A :无 B :星空企业版 C :星瀚 D :其他ERP |
| 5 | fsumrecamount | 已收金额 | numeric | 23 | 10 | √ | 0 | 已收金额 |
| 6 | frebateaccounttype | 资金池类别 | bpchar | 1 |  | √ | ' ' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 7 | fsumreceivableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 8 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | frecsettleorgid | frecsettleorgid | int8 | 64 |  | √ | 0 |  |
| 10 | finvoiceaddress | 收票地址 | varchar | 255 |  | √ | ' ' | 收票地址 |
| 11 | fsumactualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 12 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 14 | fsumunrecamount | 待收金额 | numeric | 23 | 10 | √ | 0 | 待收金额 |
| 15 | fpaystatus | 收款状态 | bpchar | 1 |  | √ | 'A' | 收款状态,枚举: A :未收款 B :部分收款 C :已收款 D :无需关注 |
| 16 | fiscreditorder | 调货订单 | bpchar | 1 |  | √ | '0' | 调货订单 |
| 17 | fsumitemamount | 商品总金额 | numeric | 23 | 10 | √ | 0 | 商品总金额 |
| 18 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 19 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 20 | fpickingstatus | 拣货状态 | bpchar | 1 |  | √ | 'A' | 拣货状态,枚举: A :未拣货 B :部分拣货 C :已拣货 D :拣货中 |
| 21 | fvehicleid | 配送车辆 | int8 | 64 |  | √ | 0 | [车辆信息 ocdbd_vehicle](../ococic_files/ocdbd_vehicle.md) |
| 22 | fpromotelableid | 促销标识 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 23 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 24 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 25 | fsalordernumber | 同步销售订单编号 | varchar | 80 |  | √ | ' ' | 同步销售订单编号 |
| 26 | fsumqty | 商品总批准数量 | numeric | 23 | 10 | √ | 0 | 商品总批准数量 |
| 27 | fsumdiscountamount | 优惠金额 | numeric | 23 | 10 | √ | 0 | 优惠金额 |
| 28 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | finvoicephone | 收票人联系方式 | varchar | 50 |  | √ | ' ' | 收票人联系方式 |
| 30 | fsumlocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 31 | finvoicetype | 发票信息 | bpchar | 1 |  | √ | ' ' | 发票信息,枚举: 0 :专用发票 1 :普通发票 2 :无需发票 3 :延期开票-平铺 |
| 32 | finvoeicetakerid | 收票人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 34 | fiscontrolorderqty | 订货数量是否可调配 | bpchar | 1 |  | √ | '0' | 订货数量是否可调配 |
| 35 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 36 | fsumclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 37 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 38 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 40 | faccountusemodel | 资金池抵扣模式 | bpchar | 1 |  | √ | 'A' | 资金池抵扣模式,枚举: A :按账户抵扣 B :按自定义维度抵扣 |
| 41 | fmemyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 42 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 43 | fbillrebateamount | 最大可使用激励金额 | numeric | 23 | 10 | √ | 0 | 最大可使用激励金额 |
| 44 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xorderf_cur |  | fsettlecurrencyid,fbasecurrencyid |
| 2 | pk_ocbsoc_xorder_f |  | fid |

---

## 智能审单明细-子表 t_ocbsoc_ordersa_res

- **表名称：** 智能审单明细-子表
- **表名：** t_ocbsoc_ordersa_res

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 3 | fcontentdetail_tag | 规则结果描述_详情 | text | 0 |  |  | null | 规则结果描述_详情 |
| 4 | fcheckruleresult | fcheckruleresult | varchar | 255 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcheckrulestatus | 规则是否通过 | bpchar | 1 |  | √ | ' ' | 规则是否通过,枚举: F :失败 T :通过 |
| 7 | fcheckitemname | 检查项名称 | varchar | 255 |  | √ | ' ' | 检查项名称 |
| 8 | fcheckitemid | 检查项ID | varchar | 50 |  | √ | ' ' | 检查项ID |
| 9 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcontentdetail | 规则结果描述 | text | 0 |  |  | null | 规则结果描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_ordersa_res |  | fentryid |
| 2 | idx_ocbsoc_ordersa_res_id |  | fid |

---

## 商品明细-子表 t_ocbsoc_xorderentry

- **表名称：** 商品明细-子表
- **表名：** t_ocbsoc_xorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovebaseqty | 批准基本数量 | numeric | 23 | 10 | √ | 0 | 批准基本数量 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fcontactname | 收货人 | varchar | 50 |  | √ | ' ' | 收货人 |
| 6 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fbillentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | fcombineparentid | 子件父分录Id | int8 | 64 |  | √ | 0 | 子件父分录Id |
| 12 | finvoicechannelid | 开票渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 13 | fitemlotid | 商品批号主档 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 14 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 15 | foperationmodeid | 经营方式 | int8 | 64 |  | √ | 0 | [商品经营方式 ocdbd_item_businesstype](../ocdpm_files/ocdbd_item_businesstype.md) |
| 16 | fcombinationid | 组合商品 | int8 | 64 |  | √ | 0 | [组合商品 ocdbd_itemcombination](../ocdbd_files/ocdbd_itemcombination.md) |
| 17 | fsubitemqty | 组合商品子件数量 | numeric | 23 | 10 | √ | 0 | 组合商品子件数量 |
| 18 | fapproveassistqty | 辅助单位批准数量 | numeric | 23 | 10 | √ | 0 | 辅助单位批准数量 |
| 19 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 20 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 22 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | faccessoryitemid | 配件所属商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 24 | fitemtypeid | fitemtypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fentryaddressid | 省/市/区 | varchar | 36 |  | √ | ' ' | 省/市/区 |
| 26 | forderlinetypeid | 订单行类型 | int8 | 64 |  | √ | 0 | [订单行类型 ocdbd_orderlinetype](../ocbsoc_files/ocdbd_orderlinetype.md) |
| 27 | fbillentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 30 | freqbaseqty | 要货基本数量 | numeric | 23 | 10 | √ | 0 | 要货基本数量 |
| 31 | fapproveqty | 批准数量 | numeric | 23 | 10 | √ | 0 | 批准数量 |
| 32 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 33 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 34 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 35 | fassistreqqty | 辅助单位要货数量 | numeric | 23 | 10 | √ | 0 | 辅助单位要货数量 |
| 36 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 37 | freqqty | 要货数量 | numeric | 23 | 10 | √ | 0 | 要货数量 |
| 38 | fchannelwarehouseid | 收货渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 39 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 42 | fpricepercent | 子件价格百分比例 | numeric | 23 | 10 | √ | 0 | 子件价格百分比例 |
| 43 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xorderentry_fid |  | fid |
| 2 | pk_ocbsoc_xorderentry |  | fentryid |
| 3 | idx_ocbsoc_xorderentry_item |  | fitemid |

---

## 交付计划子单体-子表 t_ocbsoc_xordersentry

- **表名称：** 交付计划子单体-子表
- **表名：** t_ocbsoc_xordersentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcontactname | 收货人 | varchar | 50 |  | √ | ' ' | 收货人 |
| 2 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 5 | faddressid | 省/市/区 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 6 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 7 | fsubremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fkneadtaxamount | 揉价后的价税合计 | numeric | 23 | 10 | √ | 0 | 揉价后的价税合计 |
| 9 | fdistributionmodeid | 配送模式 | int8 | 64 |  | √ | 0 | [配送模式 ocdbd_distributionmode](../ococic_files/ocdbd_distributionmode.md) |
| 10 | fplanentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 14 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fplanentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 19 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 20 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 21 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 22 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 23 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xordersentry |  | fdetailid |
| 2 | idx_ocbsoc_xordersentry_eid |  | fentryid |

---

## 收款信息-子表 t_ocbsoc_xorderrecentry

- **表名称：** 收款信息-子表
- **表名：** t_ocbsoc_xorderrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcloseusedrealintamt | 本次关闭退回结息金额 | numeric | 23 | 10 | √ | 0 | 本次关闭退回结息金额 |
| 3 | frecentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | factualusedamount | 实际使用金额 | numeric | 23 | 10 | √ | 0 | 实际使用金额 |
| 5 | fcashpoolsrcentryid | 资金池来源行ID | int8 | 64 |  | √ | 0 | 资金池来源行ID |
| 6 | fcashpoolid | 资金池ID | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 7 | frecentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 8 | ftipmsg | 提示信息 | varchar | 80 |  | √ | ' ' | 提示信息 |
| 9 | fcloseusedamount | 关闭退回金额 | numeric | 23 | 10 | √ | 0 | 关闭退回金额 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | frealintamt | 实时结息金额 | numeric | 23 | 10 | √ | 0 | 实时结息金额 |
| 12 | frecremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fcashpoolsrcid | 资金池来源单据ID | int8 | 64 |  | √ | 0 | 资金池来源单据ID |
| 14 | fdiffrealintamt | 变更结息差额 | numeric | 23 | 10 | √ | 0 | 变更结息差额 |
| 15 | fautouserebateamount | 自动抵扣使用金额 | numeric | 23 | 10 | √ | 0 | 自动抵扣使用金额 |
| 16 | fcloserealintamt | 关闭退回结息金额 | numeric | 23 | 10 | √ | 0 | 关闭退回结息金额 |
| 17 | foldusedamount | 旧本次使用金额 | numeric | 23 | 10 | √ | 0 | 旧本次使用金额 |
| 18 | fusedamount | 本次使用金额 | numeric | 23 | 10 | √ | 0 | 本次使用金额 |
| 19 | fcashpoolsrcentity | 资金池来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 21 | fruleid | 资金使用规则Id | int8 | 64 |  | √ | 0 | 资金使用规则Id |
| 22 | fdiffuseamount | 变更差额 | numeric | 23 | 10 | √ | 0 | 变更差额 |
| 23 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |
| 24 | famountpercent | 使用比例 | numeric | 23 | 10 | √ | 0 | 使用比例 |
| 25 | fjoinamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 26 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 27 | fisenough | 账户余额充足标识 | bpchar | 1 |  | √ | '0' | 账户余额充足标识 |
| 28 | fbillamount | 行指定抵扣金额 | numeric | 23 | 10 | √ | 0 | 行指定抵扣金额 |
| 29 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 30 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | [收款抵扣类型 ocdbd_receiptoffset](../ocbsoc_files/ocdbd_receiptoffset.md) |
| 31 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 32 | fcloserefundamount | fcloserefundamount | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsharepercent | 是否共享使用比例 | bpchar | 1 |  | √ | '1' | 是否共享使用比例 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcashpoolsrcnumber | 资金池来源单据编码 | varchar | 80 |  | √ | ' ' | 资金池来源单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xorderrecentry |  | fentryid |
| 2 | idx_ocbsoc_xorderrecentry_fid |  | fid |

---

## 要货订单变更-分表 t_ocbsoc_xorder_x

- **表名称：** 要货订单变更-分表
- **表名：** t_ocbsoc_xorder_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fchangebillno | 变更单据编号 | varchar | 80 |  | √ | ' ' | 变更单据编号 |
| 4 | fchangecanceldate | 变更单作废日期 | timestamp | 0 |  |  | null | 变更单作废日期 |
| 5 | fsourcebillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 6 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | 'A' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 7 | fchangereason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 8 | fchangecancelerid | 变更单作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 10 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 12 | fchangecancelstatus | 变更单作废状态 | bpchar | 1 |  | √ | 'A' | 变更单作废状态,枚举: A :正常 B :已作废 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xorder_x |  | fid |
| 2 | idx_ocbsoc_xorderx_num |  | fchangebillno |

---

## 商品明细-分表 t_ocbsoc_xorderentry_r

- **表名称：** 商品明细-分表
- **表名：** t_ocbsoc_xorderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalorderbaseqty | 累计订单基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单基本单位数量 |
| 3 | fsalorderassistqty | 直接关联销售订单辅助数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单辅助数量 |
| 4 | fsalorderoutassistqty | 直接出库辅助数量 | numeric | 23 | 10 | √ | 0 | 直接出库辅助数量 |
| 5 | ftotalreturnbaseqty | 累计退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货基本单位数量 |
| 6 | fjoinreturnbaseqty | 已关联退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货基本单位数量 |
| 7 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 8 | ftotaloutstockbaseqty | 累计出库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库基本单位数量 |
| 9 | ftotalsignedassistqty | 已签收辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已签收辅助单位数量 |
| 10 | ftotalreturnassistqty | 累计退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货辅助单位数量 |
| 11 | fsalorderoutqty | 直接出库数量 | numeric | 23 | 10 | √ | 0 | 直接出库数量 |
| 12 | ftotalsignedbaseqty | 已签收基本单位数量 | numeric | 23 | 10 | √ | 0 | 已签收基本单位数量 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | ftotalpickingqty | 已拣货数量 | numeric | 23 | 10 | √ | 0 | 已拣货数量 |
| 15 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 16 | fsalorderoutbaseqty | 直接出库基本数量 | numeric | 23 | 10 | √ | 0 | 直接出库基本数量 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | fjoinpickingqty | 已关联拣货数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货数量 |
| 19 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 20 | fsalorderqty | 直接关联销售订单数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单数量 |
| 21 | fjoinreturnassistqty | 已关联退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货辅助单位数量 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fsalorderbaseqty | 直接关联销售订单基本数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单基本数量 |
| 24 | fjoinorderassistqty | 已关联辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联辅助单位数量 |
| 25 | ftotalorderassistqty | 累计订单辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单辅助单位数量 |
| 26 | ftotalinstockassistqty | 累计入库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库辅助单位数量 |
| 27 | ftotaloutstockassistqty | 累计出库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库辅助单位数量 |
| 28 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 29 | ftotalinstockbaseqty | 累计入库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库基本单位数量 |
| 30 | ftotalpickingbaseqty | 已拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已拣货基本数量 |
| 31 | fjoinorderbaseqty | 已关联基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联基本单位数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fjoinorderqty | 已关联单位数量 | numeric | 23 | 10 | √ | 0 | 已关联单位数量 |
| 34 | fjoinpickingbaseqty | 已关联拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xorderentry_r |  | fentryid |
| 2 | idx_ocbsoc_xorderentryr_fid |  | fid |

---

## 商品明细-分表 t_ocbsoc_xorderentry_f

- **表名称：** 商品明细-分表
- **表名：** t_ocbsoc_xorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 3 | fstandardprice | 标准价 | numeric | 23 | 10 | √ | 0 | 标准价 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 7 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 8 | fiskneadprice | 参与揉价 | bpchar | 1 |  | √ | '0' | 参与揉价 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | frebateamount | 计返利金额 | numeric | 23 | 10 | √ | 0 | 计返利金额 |
| 11 | fkneadtaxamount | 揉价后价税合计 | numeric | 23 | 10 | √ | 0 | 揉价后价税合计 |
| 12 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fbeforetaxamount | 计促销金额 | numeric | 23 | 10 | √ | 0 | 计促销金额 |
| 15 | fkneadprice | 揉价价格 | numeric | 23 | 10 | √ | 0 | 揉价价格 |
| 16 | fbudgetamount | 计预算金额 | numeric | 23 | 10 | √ | 0 | 计预算金额 |
| 17 | fsaleamount | 计销量金额 | numeric | 23 | 10 | √ | 0 | 计销量金额 |
| 18 | fisspecifykneadprice | 指定价格揉价 | bpchar | 1 |  | √ | '0' | 指定价格揉价 |
| 19 | fclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 20 | fpriceentryid | 价格政策分录Id | int8 | 64 |  | √ | 0 | 价格政策分录Id |
| 21 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 22 | fisrebate | 计返利 | bpchar | 1 |  | √ | '0' | 计返利 |
| 23 | fpromotiondiscount | 促销折扣 | numeric | 23 | 10 | √ | 0 | 促销折扣 |
| 24 | flocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 25 | fissale | 计销量 | bpchar | 1 |  | √ | '0' | 计销量 |
| 26 | foriginaltaxprice | 原始含税单价 | numeric | 23 | 10 | √ | 0 | 原始含税单价 |
| 27 | fpricepolicyid | 价格政策Id | int8 | 64 |  | √ | 0 | [渠道价格政策 ocdbd_pricepolicy](../ocdpm_files/ocdbd_pricepolicy.md) |
| 28 | fcloserecdiscount | 关闭退回分摊金额 | numeric | 23 | 10 | √ | 0 | 关闭退回分摊金额 |
| 29 | fpricediscount | 单位价格折扣 | numeric | 23 | 10 | √ | 0 | 单位价格折扣 |
| 30 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 31 | flowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 32 | frecdiscount | 收款分摊折扣 | numeric | 23 | 10 | √ | 0 | 收款分摊折扣 |
| 33 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 34 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 35 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 36 | factualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 37 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | funitdiscount | 单位总折扣 | numeric | 23 | 10 | √ | 0 | 单位总折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xorderentryf_fid |  | fid |
| 2 | pk_ocbsoc_xorderentry_f |  | fentryid |

---

## 价格组成明细-子表 t_ocbsoc_xordersubprice

- **表名称：** 价格组成明细-子表
- **表名：** t_ocbsoc_xordersubprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 2 | fpriceitemid | 价格组成项 | int8 | 64 |  | √ | 0 | [价格组成项 ocdbd_price_combitem](../ocdpm_files/ocdbd_price_combitem.md) |
| 3 | fexpensetypeid | 营销费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 4 | fdetailprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 5 | fowndepid | 归属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_xordsp_eid |  | fentryid |
| 2 | pk_ocbsoc_xordersubprice |  | fdetailid |
