# 渠道调拨单-ococic_transbill

## 渠道调拨单-主表 t_ococic_transbill

- **表名称：** 渠道调拨单-主表
- **表名：** t_ococic_transbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransbilldriver | 调拨申请驱动 | bpchar | 1 |  | √ | 'A' | 调拨申请驱动,枚举: A :调出方申请 B :调入方申请 |
| 3 | fsumrecamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 4 | fcontactname | 联系人 | varchar | 30 |  | √ | ' ' | 联系人 |
| 5 | fsettlestatus | 结算状态 | bpchar | 1 |  | √ | '0' | 结算状态,枚举: 0 :未结算 1 :部分结算 2 :已结算 |
| 6 | fdeliveryaddressid | 调入地址 | int8 | 64 |  | √ | 0 | [渠道收货地址 ocdbd_channel_address](../ocdbd_files/ocdbd_channel_address.md) |
| 7 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fbizclose | 关闭状态 | bpchar | 1 |  | √ | 'N' | 关闭状态,枚举: N :未关闭 Y :已关闭 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsumamount | 金额合计 | numeric | 23 | 10 | √ | 0 | 金额合计 |
| 14 | ftransbillchannelid | 调拨申请渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 16 | fdetailaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | foutchannelid | 调出渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 19 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 20 | ftransbilltype | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: 0 :渠道内调拨 1 :跨渠道调拨 2 :渠道间调账 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftransmode | 调拨方式 | bpchar | 1 |  | √ | '0' | 调拨方式,枚举: 0 :一键调拨 1 :分步调拨 2 :分步调账 |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :打回 P :预提交 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | finvalidstatus | 作废状态 | bpchar | 1 |  | √ | 'N' | 作废状态,枚举: N :未作废 Y :已作废 |
| 26 | fordertaxamount | 借项销售价税合计 | numeric | 23 | 10 | √ | 0 | 借项销售价税合计 |
| 27 | freturntaxamount | 贷项退回价税合计 | numeric | 23 | 10 | √ | 0 | 贷项退回价税合计 |
| 28 | fdatasources | 数据来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fsumqty | 调拨数量 | numeric | 23 | 10 | √ | 0 | 调拨数量 |
| 32 | ftelephone | 联系电话 | varchar | 255 |  | √ | ' ' | 联系电话 |
| 33 | frtchannelid | 调出店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 34 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fadmindivisionid | 省/市/区 | varchar | 36 |  | √ | ' ' | 省/市/区 |
| 36 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 37 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | finchannelid | 调入渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 39 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 40 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 41 | fsumtax | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 42 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 46 | funsumtaxamount | 待收金额 | numeric | 23 | 10 | √ | 0 | 待收金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transbill_billno |  | fbillno |
| 2 | idx_ococic_transbill_channel |  | foutchannelid,finchannelid,fbizdate |
| 3 | pk_ococic_transbill |  | fid |

---

## 渠道调拨单-关联追踪表 t_ococic_transdirbill_tc

- **表名称：** 渠道调拨单-关联追踪表
- **表名：** t_ococic_transdirbill_tc

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
| 1 | idx_ococic_transdirbill_tc_tbill |  | ftbillid |
| 2 | pk_ococic_transdirbill_tc |  | fid |
| 3 | idx_ococic_transdirbill_tc_tid |  | ftid |

---

## 商品明细-分表 t_ococic_transentry_t

- **表名称：** 商品明细-分表
- **表名：** t_ococic_transentry_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finstockstatus | 调入库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 3 | foutownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 4 | finstocktype | 调入库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 5 | finprojectid | 调入项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 6 | foutstocktypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 7 | finlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 8 | foutstockstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 9 | foutkeepertype | 调出保管者类型 | varchar | 36 |  | √ | ' ' | 调出保管者类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 10 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 12 | finkeeperid | 调入保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 14 | finkeepertype | 调入保管者类型 | varchar | 36 |  | √ | ' ' | 调入保管者类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 15 | finownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | finownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 18 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 19 | foutprojectid | 调出项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 20 | foutkeeperid | 调出保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_transentry_t |  | fentryid |
| 2 | idx_ococic_transentry_t_fid |  | fid |

---

## 源单收款抵扣-子表 t_ococic_transrecentry

- **表名称：** 源单收款抵扣-子表
- **表名：** t_ococic_transrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcashpoolid | 源资金池id | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |
| 3 | fcashpoolsrcentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 4 | frecrollbackamount | 调货回滚金额 | numeric | 23 | 10 | √ | 0 | 调货回滚金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | frecsrcbillentryid | 分录来源单据行id | int8 | 64 |  | √ | 0 | 分录来源单据行id |
| 7 | fcashpoolsrcid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 8 | frecdiscountamount | 抵扣金额 | numeric | 23 | 10 | √ | 0 | 抵扣金额 |
| 9 | faccounttypeid | 源单抵扣账户 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 10 | freceiptoffsetid | 源单抵扣类型 | int8 | 64 |  | √ | 0 | [收款抵扣类型 ocdbd_receiptoffset](../ocbsoc_files/ocdbd_receiptoffset.md) |
| 11 | fcashpoolsrcentity | 源单类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | funitrecdiscount | 单位抵扣金额 | numeric | 23 | 10 | √ | 0 | 单位抵扣金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fcashpoolsrcnumber | 源单编码 | varchar | 80 |  | √ | ' ' | 源单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transrecentry_fid |  | fid |
| 2 | pk_ococic_transrecentry |  | fentryid |

---

## 商品明细-分表 t_ococic_transentry_f

- **表名称：** 商品明细-分表
- **表名：** t_ococic_transentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | fpromotiondiscount | 价后促销折扣 | numeric | 23 | 10 | √ | 0 | 价后促销折扣 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :单位折扣率％ B :单位折扣额 C :无 |
| 6 | fsumdiscount | 单位总折扣（率） | numeric | 23 | 10 | √ | 0 | 单位总折扣（率） |
| 7 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 8 | fispresent | 是否赠品 | bpchar | 1 |  | √ | '0' | 是否赠品 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 10 | fdiscount | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 11 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 14 | frecdiscount | 价后收款优惠分摊折扣 | numeric | 23 | 10 | √ | 0 | 价后收款优惠分摊折扣 |
| 15 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transentry_f_fid |  | fid |
| 2 | pk_ococic_transentry_f |  | fentryid |

---

## 商品明细-分表 t_ococic_transentry_r

- **表名称：** 商品明细-分表
- **表名：** t_ococic_transentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoinoutbaseqty | 已关联渠道出库基本数量 | numeric | 23 | 10 | √ | 0 | 已关联渠道出库基本数量 |
| 3 | fsrcdeliveryid | 源单发货明细行id | int8 | 64 |  | √ | 0 | 源单发货明细行id |
| 4 | fsrcprice | 源单单价 | numeric | 23 | 10 | √ | 0 | 源单单价 |
| 5 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 6 | fcredittax | 调货退回税额 | numeric | 23 | 10 | √ | 0 | 调货退回税额 |
| 7 | fsrcqty | 源单数量 | numeric | 23 | 10 | √ | 0 | 源单数量 |
| 8 | fsrcpricediscount | 源单单位价格折扣 | numeric | 23 | 10 | √ | 0 | 源单单位价格折扣 |
| 9 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fsrcdiscountamount | 源单折扣额 | numeric | 23 | 10 | √ | 0 | 源单折扣额 |
| 11 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 12 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 13 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fsrctaxprice | 源单含税单价 | numeric | 23 | 10 | √ | 0 | 源单含税单价 |
| 15 | fcredittaxamount | 调货退回价税合计 | numeric | 23 | 10 | √ | 0 | 调货退回价税合计 |
| 16 | ftotaloutbaseqty | 累计渠道出库基本数量 | numeric | 23 | 10 | √ | 0 | 累计渠道出库基本数量 |
| 17 | ftransrollbackamount | 调货退回分摊折扣 | numeric | 23 | 10 | √ | 0 | 调货退回分摊折扣 |
| 18 | fcorebillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 19 | fcreditamount | 调货退回不含税金额 | numeric | 23 | 10 | √ | 0 | 调货退回不含税金额 |
| 20 | fcorebillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsrcpmtdiscount | 源单促销折扣 | numeric | 23 | 10 | √ | 0 | 源单促销折扣 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fjoininbaseqty | 已关联渠道入库基本数量 | numeric | 23 | 10 | √ | 0 | 已关联渠道入库基本数量 |
| 24 | fcorebillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 25 | fsrcbasepmtdiscount | 源单基本单位促销折扣 | numeric | 23 | 10 | √ | 0 | 源单基本单位促销折扣 |
| 26 | fsrcrecdiscount | 源单抵扣分摊折扣 | numeric | 23 | 10 | √ | 0 | 源单抵扣分摊折扣 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fsrcunitdiscount | 源单单位总折扣 | numeric | 23 | 10 | √ | 0 | 源单单位总折扣 |
| 29 | fcorebillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 30 | ftotalinbaseqty | 累计渠道入库基本数量 | numeric | 23 | 10 | √ | 0 | 累计渠道入库基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transentry_r_fid |  | fid |
| 2 | pk_ococic_transentry_r |  | fentryid |

---

## 商品明细-子表 t_ococic_transentry

- **表名称：** 商品明细-子表
- **表名：** t_ococic_transentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapprovebaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 3 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fapproveqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 11 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 12 | fscmlotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 13 | fapproveassistqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 14 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 15 | flotid | 批号ID | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 16 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 17 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 18 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transentry_fid |  | fid |
| 2 | pk_ococic_transentry |  | fentryid |

---

## 序列号单体-子表 t_ococic_transserial

- **表名称：** 序列号单体-子表
- **表名：** t_ococic_transserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fserialid | 序列号 | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 6 | fserialcomment | 备注 | varchar | 500 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transserial_eid |  | fentryid |
| 2 | pk_ococic_transserial |  | fdetailid |

---

## 关联子实体-子表 t_ococic_transdirentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_transdirentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fapprovebaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 2 | fapprovebaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_transdirentry_lk_fk |  | fentryid |
| 2 | pk_ococic_transdirentry_lk |  | fpkid |

---

## 渠道调拨单-反写记录表 t_ococic_transdirbill_wb

- **表名称：** 渠道调拨单-反写记录表
- **表名：** t_ococic_transdirbill_wb

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
| 1 | pk_ococic_transdirbill_wb |  | fentryid |
| 2 | idx_ococic_transdirbill_wb_fk |  | fid |
