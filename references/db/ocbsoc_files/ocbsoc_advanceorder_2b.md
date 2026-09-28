# 代客下预订单-ocbsoc_advanceorder_2b

## 代客下预订单-主表 t_ocbsoc_advanceorder

- **表名称：** 代客下预订单-主表
- **表名：** t_ocbsoc_advanceorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumlocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 3 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 4 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fsumamount | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | forderremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 21 | fsumlocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 22 | fpaytype | 付款方式 | bpchar | 1 |  | √ | '2' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 23 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 26 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 27 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :已关闭 |
| 28 | fsupplyrelation | 供货关系 | bpchar | 1 |  | √ | ' ' | 供货关系,枚举: A :组织直供 B :渠道供货 |
| 29 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | fsumlocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 31 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 32 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 33 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 35 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 38 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_advanceorder |  | fid |
| 2 | idx_ocbsoc_advanceorder_bno |  | fbillno |

---

## 代客下预订单-分表 t_ocbsoc_advanceorder_x

- **表名称：** 代客下预订单-分表
- **表名：** t_ocbsoc_advanceorder_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderdescription_tag | 订单说明_详情 | text | 0 |  |  | null | 订单说明_详情 |
| 3 | forderdescription | 订单说明 | varchar | 255 |  | √ | ' ' | 订单说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_advanceorder_x |  | fid |
| 2 | idx_ocbsoc_advanceorderx |  | forderdescription |

---

## 商品明细-子表 t_ocbsoc_advanceentry

- **表名称：** 商品明细-子表
- **表名：** t_ocbsoc_advanceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaltaxamount | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 3 | fapprovebaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | frowclosestatus | 行关闭状态 | bpchar | 1 |  | √ | 'A' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fentryorderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 8 | fpushfailmessage | 自动生成失败原因 | varchar | 500 |  | √ | ' ' | 自动生成失败原因 |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 11 | fentrystatus | 生成状态 | bpchar | 1 |  | √ | 'N' | 生成状态,枚举: N :未生成 Y :已生成 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 14 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 15 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 16 | fweek | 星期 | bpchar | 1 |  | √ | ' ' | 星期,枚举: 2 :星期一 3 :星期二 4 :星期三 5 :星期四 6 :星期五 7 :星期六 1 :星期日 |
| 17 | fapproveassistqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 18 | flocaltax | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 19 | fentryrequestdate | 期望到货日期 | timestamp | 0 |  |  | null | 期望到货日期 |
| 20 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 21 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | flocalamount | 不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 不含税金额本位币 |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 27 | fapproveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 28 | fpricediscount | 单位折扣 | numeric | 23 | 10 | √ | 0 | 单位折扣 |
| 29 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 30 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 31 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 32 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocbsoc_advanceentry |  | fentryid |
| 2 | idx_ocbsoc_advanceentry_fid |  | fid |
