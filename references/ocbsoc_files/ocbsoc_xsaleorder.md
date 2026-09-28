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
| 2 | fsourcebilltypeid | 源单据类型id | int8 | 64 |  | √ | 0 | 源单据类型id |
| 3 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | 'A' | 确认状态,枚举: A :无需确认 B :未确认 C :已确认 |
| 4 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 5 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 11 | fclosetime | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货 E :已发货 F :已完成 P :预提交 |
| 16 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未发货 B :待签收 C :部分签收 D :签收完成 |
| 17 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 18 | fsourceapply | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :B2B订单中心 2 :经销商门户 3 :零售管理 4 :销售助手 |
| 19 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdeliveryway | 配送方式 | bpchar | 1 |  | √ | ' ' | 配送方式,枚举: A :物流发货 B :车辆配送 C :客户自提 |
| 21 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 22 | forderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fisvaletorder | 订单标识 | bpchar | 1 |  | √ | '1' | 订单标识,枚举: 0 :自助下单 1 :代客下单 2 :铺货下单 4 :车销订单 5 :访销订单 3 :其他 |
| 25 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | 渠道价格类型 ocdbd_price_type |
| 31 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | 供货关系 ocdbd_channel_authorize |
| 32 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 33 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 34 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 35 | fbusinesschannelid | 业务归属渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 36 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 37 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 38 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 41 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 42 | fconfirmtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 43 | fsourceplatform | 来源平台 | bpchar | 1 |  | √ | '1' | 来源平台,枚举: 1 :PC端 2 :移动端 |
| 44 | fchangeversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 47 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

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
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | freserveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 10 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 12 | fdetailid | 交付计划行Id | int8 | 64 |  | √ | 0 | 交付计划行Id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

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
| 4 | frecitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 5 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 6 | fdiscountentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 7 | funitrecdiscount | 单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 单位抵扣金额 |
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
| 4 | fsumrecamount | 已收金额 | numeric | 23 | 10 | √ | 0 | 已收金额 |
| 5 | frebateaccounttype | 资金池类别 | bpchar | 1 |  | √ | ' ' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 6 | fsumreceivableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 7 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | frecsettleorgid | frecsettleorgid | int8 | 64 |  | √ | 0 |  |
| 9 | finvoiceaddress | 收票地址 | varchar | 255 |  | √ | ' ' | 收票地址 |
| 10 | fsumactualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fsumunrecamount | 待收金额 | numeric | 23 | 10 | √ | 0 | 待收金额 |
| 14 | fpaystatus | 收款状态 | bpchar | 1 |  | √ | 'A' | 收款状态,枚举: A :未收款 B :部分收款 C :已收款 D :无需关注 |
| 15 | fiscreditorder | 调货订单 | bpchar | 1 |  | √ | '0' | 调货订单 |
| 16 | fsumitemamount | 商品总金额 | numeric | 23 | 10 | √ | 0 | 商品总金额 |
| 17 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 18 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 19 | fpickingstatus | 拣货状态 | bpchar | 1 |  | √ | 'A' | 拣货状态,枚举: A :未拣货 B :部分拣货 C :已拣货 D :拣货中 |
| 20 | fvehicleid | 配送车辆 | int8 | 64 |  | √ | 0 | 车辆信息 ocdbd_vehicle |
| 21 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 22 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 23 | fsumqty | 商品总批准数量 | numeric | 23 | 10 | √ | 0 | 商品总批准数量 |
| 24 | fsumdiscountamount | 优惠金额 | numeric | 23 | 10 | √ | 0 | 优惠金额 |
| 25 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | finvoicephone | 收票人联系方式 | varchar | 50 |  | √ | ' ' | 收票人联系方式 |
| 27 | fsumlocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 28 | finvoicetype | 发票信息 | bpchar | 1 |  | √ | ' ' | 发票信息,枚举: 0 :专用发票 1 :普通发票 2 :无需发票 3 :延期开票-平铺 |
| 29 | finvoeicetakerid | 收票人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fiscontrolorderqty | 订货数量是否可调配 | bpchar | 1 |  | √ | '0' | 订货数量是否可调配 |
| 31 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 32 | fsumclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 33 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 34 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 36 | faccountusemodel | 资金池抵扣模式 | bpchar | 1 |  | √ | 'A' | 资金池抵扣模式,枚举: A :按账户抵扣 B :按自定义维度抵扣 |
| 37 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fbillrebateamount | 最大可使用激励金额 | numeric | 23 | 10 | √ | 0 | 最大可使用激励金额 |
| 39 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | 渠道收货地址 ocdbd_channel_address |

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

## 商品明细-子表 t_ocbsoc_xorderentry

- **表名称：** 商品明细-子表
- **表名：** t_ocbsoc_xorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovebaseqty | 批准基本数量 | numeric | 23 | 10 | √ | 0 | 批准基本数量 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fcontactname | 收货人 | varchar | 50 |  | √ | ' ' | 收货人 |
| 6 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fbillentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fcombineparentid | 子件父分录Id | int8 | 64 |  | √ | 0 | 子件父分录Id |
| 12 | finvoicechannelid | 开票渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fitemlotid | 商品批号主档 | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 14 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 15 | foperationmodeid | 经营方式 | int8 | 64 |  | √ | 0 | 商品经营方式 ocdbd_item_businesstype |
| 16 | fcombinationid | 组合商品 | int8 | 64 |  | √ | 0 | 组合商品 ocdbd_itemcombination |
| 17 | fsubitemqty | 组合商品子件数量 | numeric | 23 | 10 | √ | 0 | 组合商品子件数量 |
| 18 | fapproveassistqty | 辅助单位批准数量 | numeric | 23 | 10 | √ | 0 | 辅助单位批准数量 |
| 19 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 20 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 22 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | faccessoryitemid | 配件所属商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 24 | fitemtypeid | fitemtypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fentryaddressid | 省/市/区 | varchar | 36 |  | √ | ' ' | 省/市/区 |
| 26 | forderlinetypeid | 订单行类型 | int8 | 64 |  | √ | 0 | 订单行类型 ocdbd_orderlinetype |
| 27 | fbillentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 30 | freqbaseqty | 要货基本数量 | numeric | 23 | 10 | √ | 0 | 要货基本数量 |
| 31 | fapproveqty | 批准数量 | numeric | 23 | 10 | √ | 0 | 批准数量 |
| 32 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 33 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 34 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 35 | fassistreqqty | 辅助单位要货数量 | numeric | 23 | 10 | √ | 0 | 辅助单位要货数量 |
| 36 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 37 | freqqty | 要货数量 | numeric | 23 | 10 | √ | 0 | 要货数量 |
| 38 | fchannelwarehouseid | 收货渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 39 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 42 | fpricepercent | 子件价格百分比例 | numeric | 23 | 10 | √ | 0 | 子件价格百分比例 |
| 43 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | 渠道收货地址 ocdbd_channel_address |

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
| 2 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | faddressid | 省/市/区 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 6 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 7 | fsubremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fkneadtaxamount | 揉价后的价税合计 | numeric | 23 | 10 | √ | 0 | 揉价后的价税合计 |
| 9 | fdistributionmodeid | 配送模式 | int8 | 64 |  | √ | 0 | 配送模式 ocdbd_distributionmode |
| 10 | fplanentrysrcid | 源单行id | int8 | 64 |  | √ | 0 | 源单行id |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 14 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fplanentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 19 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 20 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 21 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 22 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 23 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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
| 6 | fcashpoolid | 资金池ID | int8 | 64 |  | √ | 0 | 资金池余额 ocdbd_rebateaccount |
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
| 19 | fcashpoolsrcentity | 资金池来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 20 | fruleid | 资金使用规则Id | int8 | 64 |  | √ | 0 | 资金使用规则Id |
| 21 | fdiffuseamount | 变更差额 | numeric | 23 | 10 | √ | 0 | 变更差额 |
| 22 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |
| 23 | famountpercent | 使用比例 | numeric | 23 | 10 | √ | 0 | 使用比例 |
| 24 | fjoinamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 25 | fisenough | 账户余额充足标识 | bpchar | 1 |  | √ | '0' | 账户余额充足标识 |
| 26 | fbillamount | 行指定抵扣金额 | numeric | 23 | 10 | √ | 0 | 行指定抵扣金额 |
| 27 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 28 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | 收款抵扣类型 ocdbd_receiptoffset |
| 29 | fcloserefundamount | fcloserefundamount | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsharepercent | 是否共享使用比例 | bpchar | 1 |  | √ | '1' | 是否共享使用比例 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fcashpoolsrcnumber | 资金池来源单据编码 | varchar | 80 |  | √ | ' ' | 资金池来源单据编码 |

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
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fchangebillno | 变更单据编号 | varchar | 80 |  | √ | ' ' | 变更单据编号 |
| 4 | fchangecanceldate | 变更单作废日期 | timestamp | 0 |  |  | null | 变更单作废日期 |
| 5 | fsourcebillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 6 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | 'A' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 7 | fchangereason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 8 | fchangecancelerid | 变更单作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 13 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | ftotalpickingqty | 已拣货数量 | numeric | 23 | 10 | √ | 0 | 已拣货数量 |
| 15 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 16 | fsalorderoutbaseqty | 直接出库基本数量 | numeric | 23 | 10 | √ | 0 | 直接出库基本数量 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | fjoinpickingqty | 已关联拣货数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货数量 |
| 19 | fsalorderqty | 直接关联销售订单数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单数量 |
| 20 | fjoinreturnassistqty | 已关联退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货辅助单位数量 |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsalorderbaseqty | 直接关联销售订单基本数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单基本数量 |
| 23 | fjoinorderassistqty | 已关联辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联辅助单位数量 |
| 24 | ftotalorderassistqty | 累计订单辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单辅助单位数量 |
| 25 | ftotalinstockassistqty | 累计入库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库辅助单位数量 |
| 26 | ftotaloutstockassistqty | 累计出库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库辅助单位数量 |
| 27 | ftotalinstockbaseqty | 累计入库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库基本单位数量 |
| 28 | ftotalpickingbaseqty | 已拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已拣货基本数量 |
| 29 | fjoinorderbaseqty | 已关联基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联基本单位数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fjoinorderqty | 已关联单位数量 | numeric | 23 | 10 | √ | 0 | 已关联单位数量 |
| 32 | fjoinpickingbaseqty | 已关联拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货基本数量 |

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
| 10 | fkneadtaxamount | 揉价后价税合计 | numeric | 23 | 10 | √ | 0 | 揉价后价税合计 |
| 11 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 12 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 13 | fbeforetaxamount | 原价税合计 | numeric | 23 | 10 | √ | 0 | 原价税合计 |
| 14 | fkneadprice | 揉价价格 | numeric | 23 | 10 | √ | 0 | 揉价价格 |
| 15 | fisspecifykneadprice | 指定价格揉价 | bpchar | 1 |  | √ | '0' | 指定价格揉价 |
| 16 | fclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 17 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 18 | fisrebate | 计返利 | bpchar | 1 |  | √ | '0' | 计返利 |
| 19 | fpromotiondiscount | 促销折扣 | numeric | 23 | 10 | √ | 0 | 促销折扣 |
| 20 | flocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 21 | fissale | 计销量 | bpchar | 1 |  | √ | '0' | 计销量 |
| 22 | fcloserecdiscount | 关闭退回分摊金额 | numeric | 23 | 10 | √ | 0 | 关闭退回分摊金额 |
| 23 | fpricediscount | 单位价格折扣 | numeric | 23 | 10 | √ | 0 | 单位价格折扣 |
| 24 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 25 | flowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 26 | frecdiscount | 收款分摊折扣 | numeric | 23 | 10 | √ | 0 | 收款分摊折扣 |
| 27 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 28 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 29 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 30 | factualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 31 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | funitdiscount | 单位总折扣 | numeric | 23 | 10 | √ | 0 | 单位总折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_xorderentry_f |  | fentryid |
| 2 | idx_ocbsoc_xorderentryf_fid |  | fid |
