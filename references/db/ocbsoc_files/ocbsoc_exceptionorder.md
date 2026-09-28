# 异常要货订单-ocbsoc_exceptionorder

## 商品明细-子表 t_ocbsoc_excepoentry

- **表名称：** 商品明细-子表
- **表名：** t_ocbsoc_excepoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovebaseqty | 批准基本数量 | numeric | 23 | 10 | √ | 0 | 批准基本数量 |
| 3 | fstandardprice | 标准价 | numeric | 23 | 10 | √ | 0 | 标准价 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fcombinationid | 组合商品 | int8 | 64 |  | √ | 0 | 组合商品 ocdbd_itemcombination |
| 13 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 15 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 16 | fpromotiondiscount | 促销折扣 | numeric | 23 | 10 | √ | 0 | 促销折扣 |
| 17 | forderlinetypeid | 订单行类型 | int8 | 64 |  | √ | 0 | 订单行类型 ocdbd_orderlinetype |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 20 | freqbaseqty | 要货基本数量 | numeric | 23 | 10 | √ | 0 | 要货基本数量 |
| 21 | fapproveqty | 批准数量 | numeric | 23 | 10 | √ | 0 | 批准数量 |
| 22 | fcloserecdiscount | 关闭退回分摊金额 | numeric | 23 | 10 | √ | 0 | 关闭退回分摊金额 |
| 23 | fentryclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :未关闭 B :已关闭 |
| 24 | fpricediscount | 单位价格折扣 | numeric | 23 | 10 | √ | 0 | 单位价格折扣 |
| 25 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 26 | fsrcbillentryid | 源订单商品明细行ID | int8 | 64 |  | √ | 0 | 源订单商品明细行ID |
| 27 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 28 | frecdiscount | 收款分摊折扣 | numeric | 23 | 10 | √ | 0 | 收款分摊折扣 |
| 29 | fstandardamount | 标准金额 | numeric | 23 | 10 | √ | 0 | 标准金额 |
| 30 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 31 | freqqty | 要货数量 | numeric | 23 | 10 | √ | 0 | 要货数量 |
| 32 | factualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 33 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | funitdiscount | 单位总折扣 | numeric | 23 | 10 | √ | 0 | 单位总折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_excepoentry_fid |  | fid |
| 2 | pk_ocbsoc_excepoentry |  | fentryid |
| 3 | idx_ocbsoc_excepoentry_item |  | fitemid |

---

## 收款信息-子表 t_ocbsoc_exceprecentry

- **表名称：** 收款信息-子表
- **表名：** t_ocbsoc_exceprecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factualusedamount | 实际使用金额 | numeric | 23 | 10 | √ | 0 | 实际使用金额 |
| 3 | ftipmsg | 提示信息 | varchar | 80 |  | √ | ' ' | 提示信息 |
| 4 | fisenough | 账户余额充足标识 | bpchar | 1 |  | √ | '0' | 账户余额充足标识 |
| 5 | fcloseusedamount | 关闭退回金额 | numeric | 23 | 10 | √ | 0 | 关闭退回金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcrecentryid | 源抵扣行ID | int8 | 64 |  | √ | 0 | 源抵扣行ID |
| 8 | frecremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fbillamount | 本单金额 | numeric | 23 | 10 | √ | 0 | 本单金额 |
| 10 | fautouserebateamount | 自动抵扣使用金额 | numeric | 23 | 10 | √ | 0 | 自动抵扣使用金额 |
| 11 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 12 | fusedamount | 本次使用金额 | numeric | 23 | 10 | √ | 0 | 本次使用金额 |
| 13 | freceiptoffsetid | 收款抵扣类型 | int8 | 64 |  | √ | 0 | 收款抵扣类型 ocdbd_receiptoffset |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_exceprecentry |  | fentryid |
| 2 | idx_ocbsoc_exceprecentry_eid |  | fid |

---

## 抵扣账户分摊明细表-子表 t_ocbsoc_excepdiscount

- **表名称：** 抵扣账户分摊明细表-子表
- **表名：** t_ocbsoc_excepdiscount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecdiscount | 抵扣金额 | numeric | 23 | 10 | √ | 0 | 抵扣金额 |
| 3 | fentrycloseusedamount | 关闭退回金额 | numeric | 23 | 10 | √ | 0 | 关闭退回金额 |
| 4 | faccounttypeid | 抵扣账户 | int8 | 64 |  | √ | 0 | 资金账户 ocdbd_incentiveaccount |
| 5 | funitrecdiscount | 单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 单位抵扣金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frecentryid | 源抵扣行ID | int8 | 64 |  | √ | 0 | 源抵扣行ID |
| 8 | fentryclosetime | 行关闭时间 | timestamp | 0 |  |  | null | 行关闭时间 |
| 9 | fitementryid | 源商品明细行ID | int8 | 64 |  | √ | 0 | 源商品明细行ID |
| 10 | fsrcdiscountentryid | 源分摊明细行ID | int8 | 64 |  | √ | 0 | 源分摊明细行ID |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fisshareoffset | 是否分摊折扣 | bpchar | 1 |  | √ | '1' | 是否分摊折扣 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_excepdiscount_eid |  | fid |
| 2 | pk_ocbsoc_excepdiscount |  | fentryid |

---

## 异常要货订单-主表 t_ocbsoc_exceporder

- **表名称：** 异常要货订单-主表
- **表名：** t_ocbsoc_exceporder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbalancecustmerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fupdatemoneytime | 扣除余额时点 | bpchar | 1 |  | √ | '2' | 扣除余额时点,枚举: 0 :提交 1 :审核 2 :无 |
| 4 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsumactualtaxamount | 实际价税合计 | numeric | 23 | 10 | √ | 0 | 实际价税合计 |
| 7 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | forderstatus | 订单状态 | bpchar | 1 |  | √ | 'A' | 订单状态,枚举: A :暂存 B :已提交 C :已审核 D :部分发货 E :已发货 F :已完成 |
| 10 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fsourceapply | 来源应用 | bpchar | 1 |  | √ | '1' | 来源应用,枚举: 1 :B2B订单中心 2 :经销商门户 3 :零售管理 4 :销售助手 |
| 12 | fbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fisvaletorder | 订单标识 | bpchar | 1 |  | √ | '1' | 订单标识,枚举: 0 :自助下单 1 :代客下单 2 :铺货下单 4 :车销订单 5 :访销订单 3 :其他 |
| 15 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 16 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 17 | fsrcbillid | 源订单ID | int8 | 64 |  | √ | 0 | 源订单ID |
| 18 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | 供货关系 ocdbd_channel_authorize |
| 20 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 21 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 22 | fsumclosetaxamount | 关闭退回价税合计 | numeric | 23 | 10 | √ | 0 | 关闭退回价税合计 |
| 23 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fexception | 订单异常原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 27 | fsourceplatform | 来源平台 | bpchar | 1 |  | √ | '1' | 来源平台,枚举: 1 :PC端 2 :移动端 |
| 28 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fbillrebateamount | 最大可使用激励金额 | numeric | 23 | 10 | √ | 0 | 最大可使用激励金额 |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_exceporder_bno |  | fbillno |
| 2 | pk_ocbsoc_exceporder |  | fid |
