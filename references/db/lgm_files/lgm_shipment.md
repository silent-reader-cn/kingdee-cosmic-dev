# 运输单-lgm_shipment

## 订单明细-子表 t_lgm_shipmentsplitorder

- **表名称：** 订单明细-子表
- **表名：** t_lgm_shipmentsplitorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 3 | forderamountandtax | 订单价税合计 | numeric | 23 | 10 | √ | 0 | 订单价税合计 |
| 4 | fsrcbillid | 订单ID | int8 | 64 |  | √ | 0 | 订单ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsrcbill | 单据 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 7 | fsettlestatus | 结算状态 | varchar | 50 |  | √ | 'A' | 结算状态,枚举: A :未结算 B :已结算 |
| 8 | fexpensebillno | 关联供应链费用单 | varchar | 50 |  | √ | ' ' | 关联供应链费用单 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shipmentsplitorder_fid |  | fid |
| 2 | pk_t_lgm_shipmentsplitorder |  | fentryid |

---

## 费用明细-子表 t_lgm_shipmentexpense

- **表名称：** 费用明细-子表
- **表名：** t_lgm_shipmentexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0 | 数量 |
| 4 | ftaxamount | 实际税额 | numeric | 23 | 10 | √ | 0.0 | 实际税额 |
| 5 | fygamount | 预估费用金额 | numeric | 23 | 10 | √ | 0.0 | 预估费用金额 |
| 6 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0 | 税率(%) |
| 7 | fispricefromcontract | 运输协议取价 | varchar | 5 |  | √ | '0' | 运输协议取价 |
| 8 | fissplit | 已分摊 | varchar | 5 |  | √ | '0' | 已分摊 |
| 9 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | famountandtax | 实际费用价税合计 | numeric | 23 | 10 | √ | 0.0 | 实际费用价税合计 |
| 11 | fygtaxamount | 预估税额 | numeric | 23 | 10 | √ | 0.0 | 预估税额 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | famount | 实际费用金额 | numeric | 23 | 10 | √ | 0.0 | 实际费用金额 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0 | 单价 |
| 15 | fshipunittype | 运输单元类型 | int8 | 64 |  | √ | 0 | [运输单元类型 lgm_shipunittype](../lgm_files/lgm_shipunittype.md) |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fsettleorgid | 费用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcurrencyid | 费用币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0 | 含税单价 |
| 21 | fygamountandtax | 预估费用价税合计 | numeric | 23 | 10 | √ | 0.0 | 预估费用价税合计 |
| 22 | fexpcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipmentexpense |  | fentryid |
| 2 | idx_lgm_shipmentexpense_fid |  | fid |

---

## 运输单-关联追踪表 t_lgm_shipment_tc

- **表名称：** 运输单-关联追踪表
- **表名：** t_lgm_shipment_tc

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
| 1 | pk_lgm_shipment_tc |  | fid |
| 2 | idx_lgm_shipment_tc_tid |  | ftid |
| 3 | idx_lgm_shipment_tc_tbill |  | ftbillid |

---

## 物料明细-子表 t_lgm_shipmententry

- **表名称：** 物料明细-子表
- **表名：** t_lgm_shipmententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fimorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsupplierlot | 供应商批号 | varchar | 100 |  | √ | ' ' | 供应商批号 |
| 4 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 10 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | fdeliveraddress | 发货地点 | varchar | 50 |  | √ | ' ' | 发货地点 |
| 16 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fdeliveraddresstype | 发货类型和地点 | varchar | 50 |  | √ | ' ' | 发货类型和地点,枚举: A :生产现场-物料 C :生产现场-物资描述 B :仓库 |
| 18 | funitid | 装运单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fdeliverydate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 24 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 25 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 26 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 27 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipmententry |  | fentryid |
| 2 | idx_shipmententry_fid |  | fid |

---

## 运输阶段-多语言表 t_lgm_shipmentstages_l

- **表名称：** 运输阶段-多语言表
- **表名：** t_lgm_shipmentstages_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | froute | 途径名称 | varchar | 100 |  | √ | ' ' | 途径名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_shipmentstages_l_fentryid |  | fentryid |
| 2 | pk_t_lgm_shipmentstages_l |  | fpkid |

---

## 物料明细-分表 t_lgm_shipmententry_r

- **表名称：** 物料明细-分表
- **表名：** t_lgm_shipmententry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 4 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 8 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 9 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 15 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipmententry_r |  | fentryid |
| 2 | idx_shipmententry_r_fid |  | fid |

---

## 运输单-主表 t_lgm_shipment

- **表名称：** 运输单-主表
- **表名：** t_lgm_shipment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fforwarder | 货运代理 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | forgid | 运输组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 6 | fsettlestatus | 结算状态 | varchar | 5 |  | √ | 'A' | 结算状态,枚举: A :未结算 B :已结算 |
| 7 | fisenterexpense | 录入费用 | bpchar | 1 |  | √ | '0' | 录入费用 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftransroute | 运输路线 | int8 | 64 |  | √ | 0 | [运输路线 lgm_transportroute](../lgm_files/lgm_transportroute.md) |
| 10 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | flogisticsstatusid | 运输状态 | int8 | 64 |  | √ | 0 | [运输单关键节点 lgm_shippingnode](../lgm_files/lgm_shippingnode.md) |
| 13 | fshiptoolid | 运输工具档案 | int8 | 64 |  | √ | 0 | [运输工具档案 lgm_shiptool](../lgm_files/lgm_shiptool.md) |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftransmode | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 18 | ftraceid | 货代提单号 | varchar | 100 |  | √ | ' ' | 货代提单号 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ftoolnumber | 运输工具号 | varchar | 50 |  | √ | ' ' | 运输工具号 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :已关闭 |
| 25 | ftranspointb | 启运地 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 26 | ftranspoint | 目的地 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fexternalnum | 外部编号 | varchar | 100 |  | √ | ' ' | 外部编号 |
| 29 | ftransporttype | 运输类型 | varchar | 50 |  | √ | ' ' | 运输类型,枚举: seaship :海运 road :公路 railway :铁路 airlift :航空 delivery :快递 theother :其他 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipment |  | fid |
| 2 | idx_shipment_fbillstatus |  | fbillstatus |
| 3 | idx_lgm_shipment_date |  | fbizdate |

---

## 运输单-反写记录表 t_lgm_shipment_wb

- **表名称：** 运输单-反写记录表
- **表名：** t_lgm_shipment_wb

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
| 1 | idx_lgm_shipment_wb_fk |  | fid |
| 2 | pk_lgm_shipment_wb |  | fentryid |

---

## 物料明细-多语言表 t_lgm_shipmententry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_lgm_shipmententry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 2 | fdeliveraddress | 发货地点 | varchar | 50 |  | √ | ' ' | 发货地点 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shipmententry_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_lgm_shipmententry_l |  | fpkid |

---

## 运输单-多语言表 t_lgm_shipment_l

- **表名称：** 运输单-多语言表
- **表名：** t_lgm_shipment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | ftoolnumber | ftoolnumber | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipment_l |  | fpkid |
| 2 | idx_shipment_l_fid |  | fid |

---

## 关联子实体-子表 t_lgm_shipmententry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lgm_shipmententry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shipmententry_lk |  | fpkid |
| 2 | idx_lgm_shipmententry_lk_fk |  | fentryid |

---

## 包装信息-子表 t_lgm_shipmentwrap

- **表名称：** 包装信息-子表
- **表名：** t_lgm_shipmentwrap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvolumeunitid | 体积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fweightunitid | 重量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fwrapbillno | 运输单元编号 | varchar | 50 |  | √ | ' ' | 运输单元编号 |
| 5 | fwrapnum | 内部件数 | numeric | 23 | 10 | √ | 0.0 | 内部件数 |
| 6 | fwrapnetweight | 净重 | numeric | 23 | 10 | √ | 0.0 | 净重 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fwrapgrossweight | 毛重 | numeric | 23 | 10 | √ | 0.0 | 毛重 |
| 9 | fwrapmaxweight | 最大装载重量 | numeric | 23 | 10 | √ | 0.0 | 最大装载重量 |
| 10 | fwrapsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 11 | fwrapmaxvolume | 最大装载容积 | numeric | 23 | 10 | √ | 0.0 | 最大装载容积 |
| 12 | fwrapvolume | 体积 | numeric | 23 | 10 | √ | 0.0 | 体积 |
| 13 | fwrapshipunittype | 运输单元类型 | int8 | 64 |  | √ | 0 | [运输单元类型 lgm_shipunittype](../lgm_files/lgm_shipunittype.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fwrapsrcbillname | 来源单据名称 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 16 | fwrapstate | 状态 | varchar | 50 |  | √ | 'C' | 状态,枚举: P :P C :C D :D |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipmentwrap |  | fentryid |
| 2 | idx_lgm_shipmentwrap_fk |  | fid |

---

## 分摊费用-子表 t_lgm_shipmentsplitentry

- **表名称：** 分摊费用-子表
- **表名：** t_lgm_shipmentsplitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0 | 税额 |
| 3 | fsrcbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 4 | freferamount | 关联费用金额 | numeric | 23 | 10 | √ | 0.0 | 关联费用金额 |
| 5 | famountandtax | 费用价税合计 | numeric | 23 | 10 | √ | 0.0 | 费用价税合计 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fexpenseentryid | 运输费用分录id | int8 | 64 |  | √ | 0 | 运输费用分录id |
| 8 | fsettlestatus | 结算状态 | varchar | 5 |  | √ | 'A' | 结算状态,枚举: A :未结算 B :已结算 |
| 9 | fexpenseamount | 费用金额 | numeric | 23 | 10 | √ | 0.0 | 费用金额 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | freferamountandtax | 关联费用价税合计 | numeric | 23 | 10 | √ | 0.0 | 关联费用价税合计 |
| 12 | frefertaxamount | 关联税额 | numeric | 23 | 10 | √ | 0.0 | 关联税额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fcurrencyid | 分摊费用币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shipmentsplitentry_fentryid |  | fentryid |
| 2 | pk_t_lgm_shipmentsplitentry |  | fdetailid |

---

## 关键节点-子表 t_lgm_shipmentnodes

- **表名称：** 关键节点-子表
- **表名：** t_lgm_shipmentnodes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodeid | 节点 | int8 | 64 |  | √ | 0 | [运输单关键节点 lgm_shippingnode](../lgm_files/lgm_shippingnode.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fisconfirmed | 已执行 | bpchar | 1 |  | √ | ' ' | 已执行 |
| 5 | fnumber | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fexectime | 实际时间 | timestamp | 0 |  |  | null | 实际时间 |
| 8 | fcofirmeduser | 确认用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fconfirmedtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fplantime | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lgm_shipmentnodes |  | fentryid |
| 2 | idx_shipmentnodes_fid |  | fid |

---

## 费用明细-多语言表 t_lgm_shipmentexpense_l

- **表名称：** 费用明细-多语言表
- **表名：** t_lgm_shipmentexpense_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexpcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shipmentexpense_l_fentryid |  | fentryid |
| 2 | pk_lgm_shipmentexpense_l |  | fpkid |

---

## 运输阶段-子表 t_lgm_shipmentstages

- **表名称：** 运输阶段-子表
- **表名：** t_lgm_shipmentstages

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | froutetransmode | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 3 | fplantranend | 计划运输结束 | timestamp | 0 |  |  | null | 计划运输结束 |
| 4 | facttotdur | 实际总时长(天) | numeric | 23 | 2 | √ | 0 | 实际总时长(天) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | froute | 途径名称 | varchar | 50 |  | √ | ' ' | 途径名称 |
| 7 | facttranstart | 实际运输开始 | timestamp | 0 |  |  | null | 实际运输开始 |
| 8 | factloadend | 实际装货结束 | timestamp | 0 |  |  | null | 实际装货结束 |
| 9 | fplanloadstart | 计划装货开始 | timestamp | 0 |  |  | null | 计划装货开始 |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdistance | 距离(km) | numeric | 23 | 2 | √ | 0 | 距离(km) |
| 12 | fendpoint | 目的地 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 13 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fduration | 时长(天) | numeric | 23 | 2 | √ | 0 | 时长(天) |
| 15 | fplantotdur | 计划总时长(天) | numeric | 23 | 2 | √ | 0 | 计划总时长(天) |
| 16 | fplantranstart | 计划运输开始 | timestamp | 0 |  |  | null | 计划运输开始 |
| 17 | fplanloadend | 计划装货结束 | timestamp | 0 |  |  | null | 计划装货结束 |
| 18 | factloadstart | 实际装货开始 | timestamp | 0 |  |  | null | 实际装货开始 |
| 19 | fstartpoint | 启运点 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 20 | facttranend | 实际运输结束 | timestamp | 0 |  |  | null | 实际运输结束 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_shipmentstages_fid |  | fid |
| 2 | pk_t_lgm_shipmentstages |  | fentryid |
