# 要货订单-ocbsoc_saleorder

## 要货订单-关联追踪表 t_ocbsoc_order_tc

- **表名称：** 要货订单-关联追踪表
- **表名：** t_ocbsoc_order_tc

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
| 1 | idx_ocbsoc_order_tc_tid |  | ftid |
| 2 | pk_ocbsoc_order_tc |  | fid |
| 3 | idx_ocbsoc_order_tc_tbill |  | ftbillid |

---

## 价格组成明细-子表 t_ocbsoc_ordersubprice

- **表名称：** 价格组成明细-子表
- **表名：** t_ocbsoc_ordersubprice

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
| 1 | pk_ocbsoc_ordersubprice |  | fdetailid |
| 2 | idx_ocbsoc_ordsp_eid |  | fentryid |

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

## 要货订单-反写记录表 t_ocbsoc_order_wb

- **表名称：** 要货订单-反写记录表
- **表名：** t_ocbsoc_order_wb

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
| 1 | idx_ocbsoc_order_wb_fk |  | fid |
| 2 | pk_ocbsoc_order_wb |  | fentryid |

---

## 要货订单-主表 t_ocbsoc_order

- **表名称：** 要货订单-主表
- **表名：** t_ocbsoc_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fclosetime | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | fhasbudget | 已计预算 | bpchar | 1 |  | √ | '0' | 已计预算 |
| 6 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货 E :已发货 F :已完成 P :预提交 |
| 7 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdeliveryway | 配送方式 | bpchar | 1 |  | √ | ' ' | 配送方式,枚举: A :物流发货 B :车辆配送 C :客户自提 |
| 9 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 10 | forderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 13 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | [供货关系 ocdbd_channel_authorize](../ocdbd_files/ocdbd_channel_authorize.md) |
| 14 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 16 | frtchannelid | 订货店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 17 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 19 | fconfirmtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 20 | fchangeversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 23 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 24 | fjoinreqstatus | 转要货状态 | bpchar | 1 |  | √ | '0' | 转要货状态 |
| 25 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | 'A' | 确认状态,枚举: A :无需确认 B :未确认 C :已确认 |
| 26 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 27 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fupdatemoneytime | 扣除余额时点 | bpchar | 1 |  | √ | '2' | 扣除余额时点,枚举: 0 :提交 1 :审核 2 :无 |
| 29 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 30 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 31 | fsalesyearid | 所属年份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 35 | fsignstatus | 签收状态 | bpchar | 1 |  | √ | 'A' | 签收状态,枚举: A :未发货 B :待签收 C :部分签收 D :签收完成 |
| 36 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 37 | fsourceapply | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :B2B订单中心 2 :渠道门户 3 :零售管理 4 :渠道管家 |
| 38 | fcumulatepromsettle | 结算累计促销赠品 | bpchar | 1 |  | √ | '0' | 结算累计促销赠品 |
| 39 | fsrcpursalemodel | 源单购销模式 | bpchar | 1 |  | √ | ' ' | 源单购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 F :内销同步结算 G :渠道直送 H :分步调拨 I :店铺采购 |
| 40 | fpursalemodel | 购销模式 | bpchar | 1 |  | √ | ' ' | 购销模式,枚举: A :普通外销 B :内销分步结算 C :内部调拨 D :寄售外销 E :渠道购销 F :内销同步结算 G :渠道直送 H :分步调拨 I :店铺采购 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fisvaletorder | 订单标识 | bpchar | 1 |  | √ | '1' | 订单标识,枚举: 0 :自助下单 1 :代客下单 2 :铺货下单 4 :车销订单 5 :访销订单 3 :其他 |
| 43 | fpromotionupatetime | 促销匹配更新时间 | timestamp | 0 |  |  | null | 促销匹配更新时间 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 49 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 50 | fbusinesschannelid | 业务归属渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 51 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 52 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 53 | fsalesmonthid | 所属月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 54 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 56 | fsourceplatform | 来源平台 | bpchar | 1 |  | √ | '1' | 来源平台,枚举: 1 :PC端 2 :移动端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_order |  | fid |
| 2 | idx_ocbsoc_order_odate |  | forderdate |
| 3 | idx_ocbsoc_order_schl |  | fsalechannelid |
| 4 | idx_ocbsoc_order_bno |  | fbillno |
| 5 | idx_ocbsoc_order_ochl |  | forderchannelid |
| 6 | idx_ocbsoc_order_saler |  | fsalerid |

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

## 关联子实体-子表 t_ocbsoc_ordersubentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_ordersubentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_ordersubentry_lk_fk |  | fdetailid |
| 2 | pk_ocbsoc_ordersubentry_lk |  | fpkid |

---

## 关联子实体-子表 t_ocbsoc_orderrecentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_orderrecentry_lk

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
| 1 | pk_ocbsoc_orderrecentry_lk |  | fpkid |
| 2 | idx_ocbsoc_orderrecentry_lk_fk |  | fentryid |

---

## 商品明细-子表 t_ocbsoc_orderentry

- **表名称：** 商品明细-子表
- **表名：** t_ocbsoc_orderentry

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
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | fcombineparentid | 子件父分录Id | int8 | 64 |  | √ | 0 | 子件父分录Id |
| 11 | finvoicechannelid | 开票渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fitemlotid | 商品批号主档 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 13 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 14 | foperationmodeid | 经营方式 | int8 | 64 |  | √ | 0 | [商品经营方式 ocdbd_item_businesstype](../ocdpm_files/ocdbd_item_businesstype.md) |
| 15 | fcombinationid | 组合商品 | int8 | 64 |  | √ | 0 | [组合商品 ocdbd_itemcombination](../ocdbd_files/ocdbd_itemcombination.md) |
| 16 | fsubitemqty | 组合商品子件数量 | numeric | 23 | 10 | √ | 0 | 组合商品子件数量 |
| 17 | fapproveassistqty | 辅助单位批准数量 | numeric | 23 | 10 | √ | 0 | 辅助单位批准数量 |
| 18 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 19 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 21 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | faccessoryitemid | 配件所属商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 23 | fitemtypeid | fitemtypeid | int8 | 64 |  | √ | 0 |  |
| 24 | fispromotion | 促销政策标识 | bpchar | 1 |  | √ | '0' | 促销政策标识 |
| 25 | fentryaddressid | 省/市/区 | varchar | 36 |  | √ | ' ' | 省/市/区 |
| 26 | forderlinetypeid | 订单行类型 | int8 | 64 |  | √ | 0 | [订单行类型 ocdbd_orderlinetype](../ocbsoc_files/ocdbd_orderlinetype.md) |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 29 | freqbaseqty | 要货基本数量 | numeric | 23 | 10 | √ | 0 | 要货基本数量 |
| 30 | fapproveqty | 批准数量 | numeric | 23 | 10 | √ | 0 | 批准数量 |
| 31 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 33 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 34 | fassistreqqty | 辅助单位要货数量 | numeric | 23 | 10 | √ | 0 | 辅助单位要货数量 |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | freqqty | 要货数量 | numeric | 23 | 10 | √ | 0 | 要货数量 |
| 37 | fchannelwarehouseid | 收货渠道仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 38 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 39 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 40 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 41 | fpricepercent | 子件价格百分比例 | numeric | 23 | 10 | √ | 0 | 子件价格百分比例 |
| 42 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_orderentry_fid |  | fid |
| 2 | idx_ocbsoc_orderentry_item |  | fitemid |
| 3 | pk_ocbsoc_orderentry |  | fentryid |

---

## 发货明细-子表 t_ocbsoc_delyrecentry

- **表名称：** 发货明细-子表
- **表名：** t_ocbsoc_delyrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdeliveryrecordno | 发货记录编码 | varchar | 80 |  | √ | ' ' | 发货记录编码 |
| 2 | fcurretbaseqty | 本次下推退货基本数量 | numeric | 23 | 10 | √ | 0 | 本次下推退货基本数量 |
| 3 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fdeliveryrecordentryid | 发货记录行Id | int8 | 64 |  | √ | 0 | 发货记录行Id |
| 5 | fjoinretbaseqty | 已关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 已关联退货基本数量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdeliverydate | 发货时间 | timestamp | 0 |  |  | null | 发货时间 |
| 8 | fdeliverbaseqty | 发货基本数量 | numeric | 23 | 10 | √ | 0 | 发货基本数量 |
| 9 | ftotalretbaseqty | 累计退货基本数量 | numeric | 23 | 10 | √ | 0 | 累计退货基本数量 |
| 10 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 11 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 12 | finvorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fscmlotid | 批号ID | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 14 | fdeliveryqty | 发货数量 | numeric | 23 | 10 | √ | 0 | 发货数量 |
| 15 | fflotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 16 | forderchannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 17 | fexpirydate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fociclotid | 商品批号 | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_delyrecentry_eid |  | fentryid |
| 2 | pk_ocbsoc_delyrecentry |  | fdetailid |

---

## 要货订单-分表 t_ocbsoc_order_f

- **表名称：** 要货订单-分表
- **表名：** t_ocbsoc_order_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoeicetaker | 收票人 | varchar | 255 |  | √ | ' ' | 收票人 |
| 3 | fsumlocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 4 | fsumrecamount | 已收金额 | numeric | 23 | 10 | √ | 0 | 已收金额 |
| 5 | forderplantype | 订货计划类型 | bpchar | 1 |  | √ | ' ' | 订货计划类型,枚举: A :计划内订货 B :计划外订货 |
| 6 | fsyncuserid | 同步人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsumactualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fsumunrecamount | 待收金额 | numeric | 23 | 10 | √ | 0 | 待收金额 |
| 11 | fsumitemamount | 商品总金额 | numeric | 23 | 10 | √ | 0 | 商品总金额 |
| 12 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fpromotelableid | 促销标识 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 15 | fdistributionconfirmdate | 配送确认时间 | timestamp | 0 |  |  | null | 配送确认时间 |
| 16 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 17 | fsalordernumber | 同步销售订单编号 | varchar | 80 |  | √ | ' ' | 同步销售订单编号 |
| 18 | fsumdiscountamount | 优惠金额 | numeric | 23 | 10 | √ | 0 | 优惠金额 |
| 19 | finvoicephone | 收票人联系方式 | varchar | 50 |  | √ | ' ' | 收票人联系方式 |
| 20 | fsumlocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 21 | finvoicetype | 发票信息 | bpchar | 1 |  | √ | ' ' | 发票信息,枚举: 0 :专用发票 1 :普通发票 2 :无需发票 3 :延期开票-平铺 |
| 22 | finvoeicetakerid | 收票人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fiscontrolorderqty | 订货数量是否可调配 | bpchar | 1 |  | √ | '0' | 订货数量是否可调配 |
| 24 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | faccountusemodel | 资金池抵扣模式 | bpchar | 1 |  | √ | 'A' | 资金池抵扣模式,枚举: A :按账户抵扣 B :按自定义维度抵扣 |
| 26 | fsyncdate | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 27 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | ftotalapprovedamt | 已使用核销金额 | numeric | 23 | 10 | √ | 0 | 已使用核销金额 |
| 29 | fsyncstatus | 同步状态 | bpchar | 1 |  | √ | 'A' | 同步状态,枚举: A :未同步 B :同步中 C :同步失败 D :同步完成 |
| 30 | fsynerrormsg | 同步异常信息 | varchar | 255 |  | √ | ' ' | 同步异常信息 |
| 31 | fdistributionchannelid | 配送渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 32 | fintegrationtype | 集成ERP | bpchar | 1 |  | √ | 'A' | 集成ERP,枚举: A :无 B :星空企业版 C :星瀚 D :其他ERP |
| 33 | frebateaccounttype | 资金池类别 | bpchar | 1 |  | √ | ' ' | 资金池类别,枚举: A :品牌商 B :渠道商 |
| 34 | fsumreceivableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 35 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 36 | frecsettleorgid | frecsettleorgid | int8 | 64 |  | √ | 0 |  |
| 37 | finvoiceaddress | 收票地址 | varchar | 255 |  | √ | ' ' | 收票地址 |
| 38 | fpaystatus | 收款状态 | bpchar | 1 |  | √ | 'A' | 收款状态,枚举: A :未收款 B :部分收款 C :已收款 D :无需关注 |
| 39 | fiscreditorder | 调货订单 | bpchar | 1 |  | √ | '0' | 调货订单 |
| 40 | fpickingstatus | 拣货状态 | bpchar | 1 |  | √ | 'A' | 拣货状态,枚举: A :未拣货 B :部分拣货 C :已拣货 D :拣货中 |
| 41 | fvehicleid | 配送车辆 | int8 | 64 |  | √ | 0 | [车辆信息 ocdbd_vehicle](../ococic_files/ocdbd_vehicle.md) |
| 42 | fpriorityscore | 优先级权重得分 | int4 | 32 |  | √ | 0 | 优先级权重得分 |
| 43 | fdistributionstatus | 配送状态 | varchar | 10 |  | √ | '0' | 配送状态,枚举: 0 :无 1 :待确认 2 :已确认 3 :已配送 |
| 44 | fsumpickingqty | 商品总拣货数量 | numeric | 23 | 10 | √ | 0 | 商品总拣货数量 |
| 45 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 46 | fsumqty | 商品总批准数量 | numeric | 23 | 10 | √ | 0 | 商品总批准数量 |
| 47 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | fuuid | 数据唯一ID | varchar | 36 |  | √ | ' ' | 数据唯一ID |
| 49 | fmemmonthid | 预算月份 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 50 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 51 | fsumclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 52 | fsmartauditstatus | 智能审单状态 | bpchar | 1 |  | √ | 'A' | 智能审单状态,枚举: A :未提交智审 B :待人工审核 C :人工审核成功 D :待智能审核 E :智能审核中 F :自动循环审单 G :转人工复核 S :智能审核成功 |
| 53 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 54 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 55 | fdistributionconfirmerid | 配送确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fmemyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 57 | fbillrebateamount | 最大可使用激励金额 | numeric | 23 | 10 | √ | 0 | 最大可使用激励金额 |
| 58 | freceiveaddressid | 收货地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_order_cur |  | fsettlecurrencyid,fbasecurrencyid |
| 2 | pk_ocbsoc_order_f |  | fid |

---

## 抵扣账户分摊明细表-子表 t_ocbsoc_orderecdiscount

- **表名称：** 抵扣账户分摊明细表-子表
- **表名：** t_ocbsoc_orderecdiscount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecdiscount | 抵扣金额 | numeric | 23 | 10 | √ | 0 | 抵扣金额 |
| 3 | frecitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 4 | fentrycloseusedamount | 关闭退回金额 | numeric | 23 | 10 | √ | 0 | 关闭退回金额 |
| 5 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 6 | funitrecdiscount | 基本单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 基本单位抵扣金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frecentryid | 抵扣行ID | int8 | 64 |  | √ | 0 | 抵扣行ID |
| 9 | fentryclosetime | 行关闭时间 | timestamp | 0 |  |  | null | 行关闭时间 |
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
| 1 | pk_ocbsoc_orderecdiscount |  | fentryid |
| 2 | idx_ocbsoc_orderecdiscount_eid |  | fid |

---

## 促销明细-子表 t_ocbsoc_promotionentry

- **表名称：** 促销明细-子表
- **表名：** t_ocbsoc_promotionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 折扣率（%） | numeric | 23 | 10 | √ | 0 | 折扣率（%） |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flimitbalid | 限量余额ID | int8 | 64 |  | √ | 0 | 限量余额ID |
| 6 | factualdeductamount | 实际扣减总额 | numeric | 23 | 10 | √ | 0 | 实际扣减总额 |
| 7 | fdiscountamt | 优惠金额 | numeric | 23 | 10 | √ | 0 | 优惠金额 |
| 8 | fpricediscountamount | 单位折扣额（含税） | numeric | 23 | 10 | √ | 0 | 单位折扣额（含税） |
| 9 | fpresentqty_p | 接口赠品数量 | numeric | 23 | 10 | √ | 0 | 接口赠品数量 |
| 10 | fexpensetypeid | 营销费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 11 | fcumulatebalid | 累计执行ID | int8 | 64 |  | √ | 0 | 累计执行ID |
| 12 | fpresentqty | 赠品/换赠品数量 | numeric | 23 | 10 | √ | 0 | 赠品/换赠品数量 |
| 13 | flastpromsettletime | 上次累计促销结算时间 | timestamp | 0 |  |  | null | 上次累计促销结算时间 |
| 14 | fexecgroup | 执行组号 | int4 | 32 |  | √ | 0 | 执行组号 |
| 15 | fpresentgroupid | 主产品组/赠品组号 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 16 | fenablelimit | 启用限量 | bpchar | 1 |  | √ | '0' | 启用限量 |
| 17 | fachievemultiqty | 达标份数 | numeric | 23 | 10 | √ | 0 | 达标份数 |
| 18 | fbilldiscountrate | 整单折扣率（%） | numeric | 23 | 10 | √ | 0 | 整单折扣率（%） |
| 19 | fpromotionpolicyid | 促销政策编码 | int8 | 64 |  | √ | 0 | [促销政策 ocdpm_promotepolicyf7](../ocdpm_files/ocdpm_promotepolicyf7.md) |
| 20 | fbdgitemid | 预算产品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fispresent | 是否赠品/换赠品 | bpchar | 1 |  | √ | '0' | 是否赠品/换赠品 |
| 23 | fcumulatemodifytime | 累计执行修改时间 | timestamp | 0 |  |  | null | 累计执行修改时间 |
| 24 | flimittypeid | 限量方式 | int8 | 64 |  | √ | 0 | [限量方式 ocdpm_limittype](../ocdpm_files/ocdpm_limittype.md) |
| 25 | fbdgregionid | 预算所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | factualpromdctamt | 实际优惠金额 | numeric | 23 | 10 | √ | 0 | 实际优惠金额 |
| 27 | fwblimitqty | 已更新限量余额数量 | numeric | 23 | 10 | √ | 0 | 已更新限量余额数量 |
| 28 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 29 | fresultseq | 促销结果组号 | int4 | 32 |  | √ | 0 | 促销结果组号 |
| 30 | fselectstatus | 选择状态 | bpchar | 1 |  | √ | '1' | 选择状态 |
| 31 | fwbhaspromqty | 已促销（数量/份数）/金额 | numeric | 23 | 10 | √ | 0 | 已促销（数量/份数）/金额 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpromotionprice | 促销单价（含税） | numeric | 23 | 10 | √ | 0 | 促销单价（含税） |
| 34 | fpromsettletime | 累计促销结算时间 | timestamp | 0 |  |  | null | 累计促销结算时间 |
| 35 | fplanedeductamount | 计划扣减总额 | numeric | 23 | 10 | √ | 0 | 计划扣减总额 |
| 36 | fwbunpromqty | 未促销（数量/份数）/金额 | numeric | 23 | 10 | √ | 0 | 未促销（数量/份数）/金额 |
| 37 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fprocessstatus | 执行状态 | varchar | 10 |  | √ | '0' | 执行状态,枚举: 0 :未执行 1 :已执行 2 :已放弃 |
| 39 | fpresentprice | 赠品单价 | numeric | 23 | 10 | √ | 0 | 赠品单价 |
| 40 | fdiscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 41 | fbetweengrouptypeid | 赠品组间执行方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 42 | fbdgchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 43 | fbillachieveqty | 整单达标数量 | numeric | 23 | 10 | √ | 0 | 整单达标数量 |
| 44 | fbillachieveamount | 整单达标金额 | numeric | 23 | 10 | √ | 0 | 整单达标金额 |
| 45 | forderentryid | 要货订单分录ID | int8 | 64 |  | √ | 0 | 要货订单分录ID |
| 46 | fselectpresent | 手工选择赠品 | bpchar | 1 |  | √ | '0' | 手工选择赠品 |
| 47 | fachieveamount | 达标金额 | numeric | 23 | 10 | √ | 0 | 达标金额 |
| 48 | fingrouptypeid | 赠品组内执行方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 49 | fwbmultiqty | 已更新限量余额份数 | numeric | 23 | 10 | √ | 0 | 已更新限量余额份数 |
| 50 | fpromotiongroupid | 促销组号 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 51 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 52 | fmutexgroup | 互斥组 | varchar | 50 |  | √ | ' ' | 互斥组 |
| 53 | fbdgdeptid | 预算承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fachieveqty | 达标数量 | numeric | 23 | 10 | √ | 0 | 达标数量 |
| 55 | fpresentsumamount | 赠品总价 | numeric | 23 | 10 | √ | 0 | 赠品总价 |
| 56 | fchannelclassid | 预算渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 57 | fitemclassid_p | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 58 | fcostresponsible | 费用承担方 | bpchar | 1 |  | √ | ' ' | 费用承担方,枚举: A :订单所属销售部门 B :所属省区 C :所属大区 |
| 59 | fclosereturnamt | 关闭退回优惠 | numeric | 23 | 10 | √ | 0 | 关闭退回优惠 |
| 60 | fbdgprovinceid | 预算所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_pe_cumupromid |  | fcumulatebalid |
| 2 | pk_ocbsoc_promotionentry |  | fentryid |
| 3 | idx_ocbsoc_pe_limitid |  | flimitbalid |
| 4 | idx_ocbsoc_promotione_itemid |  | fitemid |
| 5 | idx_ocbsoc_promotionentry_fid |  | fid |

---

## 商品明细-分表 t_ocbsoc_orderentry_r

- **表名称：** 商品明细-分表
- **表名：** t_ocbsoc_orderentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalorderbaseqty | 累计订单基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单基本单位数量 |
| 3 | fsalorderassistqty | 直接关联销售订单辅助数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单辅助数量 |
| 4 | fsalorderoutassistqty | 直接出库辅助数量 | numeric | 23 | 10 | √ | 0 | 直接出库辅助数量 |
| 5 | fmonthvalidqty | 本月实际数 | numeric | 23 | 10 | √ | 0 | 本月实际数 |
| 6 | ftotalreturnbaseqty | 累计退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货基本单位数量 |
| 7 | fjoinreturnbaseqty | 已关联退货基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货基本单位数量 |
| 8 | fjoinreqbaseqty | 转要货关联基本数量 | numeric | 23 | 10 | √ | 0 | 转要货关联基本数量 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmonthplanqty | 本月计划数 | numeric | 23 | 10 | √ | 0 | 本月计划数 |
| 11 | ftotaloutstockbaseqty | 累计出库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库基本单位数量 |
| 12 | ftotalsignedassistqty | 已签收辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已签收辅助单位数量 |
| 13 | ftotalreturnassistqty | 累计退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计退货辅助单位数量 |
| 14 | fsalorderoutqty | 直接出库数量 | numeric | 23 | 10 | √ | 0 | 直接出库数量 |
| 15 | ftotalsignedbaseqty | 已签收基本单位数量 | numeric | 23 | 10 | √ | 0 | 已签收基本单位数量 |
| 16 | favailableqty | 可用库存数量 | varchar | 50 |  | √ | ' ' | 可用库存数量 |
| 17 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fpickingstatus | 行拣货状态 | bpchar | 1 |  | √ | 'A' | 行拣货状态,枚举: A :未拣货 B :部分拣货 C :已拣货 D :拣货中 |
| 19 | ftotalpickingqty | 已拣货数量 | numeric | 23 | 10 | √ | 0 | 已拣货数量 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fjoinreqqty | 转要货关联数量 | numeric | 23 | 10 | √ | 0 | 转要货关联数量 |
| 22 | fsalorderoutbaseqty | 直接出库基本数量 | numeric | 23 | 10 | √ | 0 | 直接出库基本数量 |
| 23 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 24 | fjoinpickingqty | 已关联拣货数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货数量 |
| 25 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 26 | fsalorderqty | 直接关联销售订单数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单数量 |
| 27 | fjoinreturnassistqty | 已关联退货辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联退货辅助单位数量 |
| 28 | fentryclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :未关闭 B :已关闭 |
| 29 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 30 | fsalorderbaseqty | 直接关联销售订单基本数量 | numeric | 23 | 10 | √ | 0 | 直接关联销售订单基本数量 |
| 31 | fjoinorderassistqty | 已关联辅助单位数量 | numeric | 23 | 10 | √ | 0 | 已关联辅助单位数量 |
| 32 | ftotalorderassistqty | 累计订单辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计订单辅助单位数量 |
| 33 | ftotalinstockassistqty | 累计入库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库辅助单位数量 |
| 34 | ftotaloutstockassistqty | 累计出库辅助单位数量 | numeric | 23 | 10 | √ | 0 | 累计出库辅助单位数量 |
| 35 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 36 | ftotalinstockbaseqty | 累计入库基本单位数量 | numeric | 23 | 10 | √ | 0 | 累计入库基本单位数量 |
| 37 | ftotalpickingbaseqty | 已拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已拣货基本数量 |
| 38 | fjoinorderbaseqty | 已关联基本单位数量 | numeric | 23 | 10 | √ | 0 | 已关联基本单位数量 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | fjoinorderqty | 已关联单位数量 | numeric | 23 | 10 | √ | 0 | 已关联单位数量 |
| 41 | fjoinpickingbaseqty | 已关联拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已关联拣货基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_orderentry_r |  | fentryid |
| 2 | idx_ocbsoc_orderentryr_fid |  | fid |

---

## 交付计划子单体-子表 t_ocbsoc_ordersubentry

- **表名称：** 交付计划子单体-子表
- **表名：** t_ocbsoc_ordersubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fcontactname | 收货人 | varchar | 50 |  | √ | ' ' | 收货人 |
| 3 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fsaleattrid | 销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freceivechannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | faddressid | 省/市/区 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 8 | fwarehouseid | 发货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | frequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 10 | fsubremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 12 | ftelephone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 13 | fkneadtaxamount | 揉价后的价税合计 | numeric | 23 | 10 | √ | 0 | 揉价后的价税合计 |
| 14 | fdistributionmodeid | 配送模式 | int8 | 64 |  | √ | 0 | [配送模式 ocdbd_distributionmode](../ococic_files/ocdbd_distributionmode.md) |
| 15 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 19 | fassistqty | 辅助单位数量 | numeric | 23 | 10 | √ | 0 | 辅助单位数量 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 22 | fstockorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_ordersubentry_eid |  | fentryid |
| 2 | pk_ocbsoc_ordersubentry |  | fdetailid |

---

## 收款信息-子表 t_ocbsoc_orderrecentry

- **表名称：** 收款信息-子表
- **表名：** t_ocbsoc_orderrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcloseusedrealintamt | 本次关闭退回结息金额 | numeric | 23 | 10 | √ | 0 | 本次关闭退回结息金额 |
| 3 | factualusedamount | 实际使用金额 | numeric | 23 | 10 | √ | 0 | 实际使用金额 |
| 4 | fcashpoolsrcentryid | 资金池来源行ID | int8 | 64 |  | √ | 0 | 资金池来源行ID |
| 5 | fcashpoolid | 资金池ID | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 6 | ftipmsg | 提示信息 | varchar | 80 |  | √ | ' ' | 提示信息 |
| 7 | fcloseusedamount | 关闭退回金额 | numeric | 23 | 10 | √ | 0 | 关闭退回金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | frealintamt | 实时结息金额 | numeric | 23 | 10 | √ | 0 | 实时结息金额 |
| 10 | frecremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fcashpoolsrcid | 资金池来源单据ID | int8 | 64 |  | √ | 0 | 资金池来源单据ID |
| 12 | fautouserebateamount | 自动抵扣使用金额 | numeric | 23 | 10 | √ | 0 | 自动抵扣使用金额 |
| 13 | fcloserealintamt | 关闭退回结息金额 | numeric | 23 | 10 | √ | 0 | 关闭退回结息金额 |
| 14 | fusedamount | 本次使用金额 | numeric | 23 | 10 | √ | 0 | 本次使用金额 |
| 15 | fcashpoolsrcentity | 资金池来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fruleid | 资金使用规则Id | int8 | 64 |  | √ | 0 | 资金使用规则Id |
| 18 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |
| 19 | famountpercent | 使用比例 | numeric | 23 | 10 | √ | 0 | 使用比例 |
| 20 | fjoinamount | 已关联金额 | numeric | 23 | 10 | √ | 0 | 已关联金额 |
| 21 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 22 | fisenough | 账户余额充足标识 | bpchar | 1 |  | √ | '0' | 账户余额充足标识 |
| 23 | fbillamount | 行指定抵扣金额 | numeric | 23 | 10 | √ | 0 | 行指定抵扣金额 |
| 24 | frefundinterest | 退货退回利息 | numeric | 23 | 10 | √ | 0 | 退货退回利息 |
| 25 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 26 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | [收款抵扣类型 ocdbd_receiptoffset](../ocbsoc_files/ocdbd_receiptoffset.md) |
| 27 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 28 | fcloserefundamount | 本次关闭退回金额 | numeric | 23 | 10 | √ | 0 | 本次关闭退回金额 |
| 29 | fsharepercent | 是否共享使用比例 | bpchar | 1 |  | √ | '1' | 是否共享使用比例 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | fcashpoolsrcnumber | 资金池来源单据编码 | varchar | 80 |  | √ | ' ' | 资金池来源单据编码 |
| 32 | fapprovedamt | 已使用核销金额 | numeric | 23 | 10 | √ | 0 | 已使用核销金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_orderrecentry_eid |  | fid |
| 2 | pk_ocbsoc_orderrecentry |  | fentryid |

---

## 商品明细-分表 t_ocbsoc_orderentry_f

- **表名称：** 商品明细-分表
- **表名：** t_ocbsoc_orderentry_f

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
| 13 | fisjoinpromotion | 是否参与促销 | bpchar | 1 |  | √ | '0' | 是否参与促销 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fbeforetaxamount | 计促销金额 | numeric | 23 | 10 | √ | 0 | 计促销金额 |
| 16 | fkneadprice | 揉价价格 | numeric | 23 | 10 | √ | 0 | 揉价价格 |
| 17 | fbudgetamount | 计预算金额 | numeric | 23 | 10 | √ | 0 | 计预算金额 |
| 18 | fsaleamount | 计销量金额 | numeric | 23 | 10 | √ | 0 | 计销量金额 |
| 19 | fisspecifykneadprice | 指定价格揉价 | bpchar | 1 |  | √ | '0' | 指定价格揉价 |
| 20 | fclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 21 | fpriceentryid | 价格政策分录Id | int8 | 64 |  | √ | 0 | 价格政策分录Id |
| 22 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 23 | fisrebate | 计返利 | bpchar | 1 |  | √ | '0' | 计返利 |
| 24 | fpromotiondiscount | 促销折扣 | numeric | 23 | 10 | √ | 0 | 促销折扣 |
| 25 | flocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 26 | foldpricediscount | 旧单位价格折扣 | numeric | 23 | 10 | √ | 0 | 旧单位价格折扣 |
| 27 | fissale | 计销量 | bpchar | 1 |  | √ | '0' | 计销量 |
| 28 | foriginaltaxprice | 原始含税单价 | numeric | 23 | 10 | √ | 0 | 原始含税单价 |
| 29 | fpricepolicyid | 价格政策Id | int8 | 64 |  | √ | 0 | [渠道价格政策 ocdbd_pricepolicy](../ocdpm_files/ocdbd_pricepolicy.md) |
| 30 | fcloserecdiscount | 关闭退回分摊金额 | numeric | 23 | 10 | √ | 0 | 关闭退回分摊金额 |
| 31 | fpricediscount | 单位价格折扣 | numeric | 23 | 10 | √ | 0 | 单位价格折扣 |
| 32 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 33 | flowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 34 | frecdiscount | 收款分摊折扣 | numeric | 23 | 10 | √ | 0 | 收款分摊折扣 |
| 35 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 36 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 37 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 38 | factualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 39 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | funitdiscount | 单位总折扣 | numeric | 23 | 10 | √ | 0 | 单位总折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_orderentry_f |  | fentryid |
| 2 | idx_ocbsoc_orderentryf_fid |  | fid |

---

## 交付计划子单体-分表 t_ocbsoc_ordersubentry_r

- **表名称：** 交付计划子单体-分表
- **表名：** t_ocbsoc_ordersubentry_r

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
| 1 | pk_ocbsoc_ordersubentry_r |  | fdetailid |
| 2 | idx_ocbsoc_ordersubentryr_eid |  | fentryid |

---

## 关联子实体-子表 t_ocbsoc_orderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocbsoc_orderentry_lk

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
| 1 | pk_ocbsoc_orderentry_lk |  | fpkid |
| 2 | idx_ocbsoc_orderentry_lk_fk |  | fentryid |
