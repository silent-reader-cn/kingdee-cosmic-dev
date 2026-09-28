# 采购转固单-fa_purchasebill

## 采购转固单-反写记录表 t_fa_purchasebill_wb

- **表名称：** 采购转固单-反写记录表
- **表名：** t_fa_purchasebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_purchasebill_wb_pkey |  | fentryid |
| 2 | idx_fa_purchasebill_wb_fk |  | fid |

---

## 采购转固单-主表 t_fa_purchasebill

- **表名称：** 采购转固单-主表
- **表名：** t_fa_purchasebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexchangetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fpurchasedate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fhasvoucher | 凭证 | bpchar | 1 |  | √ | '0' | 凭证 |
| 6 | fexchangeratetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 9 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbuildway | 建卡方式 | varchar | 50 |  | √ | ' ' | 建卡方式,枚举: 1 :按表体分录行建卡 2 :按数量拆分建卡 3 :按整单建卡 |
| 12 | fhandleorgid | 经办部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsourcebillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsourcebillsign | 来源单据标识 | varchar | 30 |  | √ | ' ' | 来源单据标识,枚举: im_materialreqoutbill :领料出库单 im_purreceivebill :采购收货单 im_publicreimbursebill :对公报销单 im_otheroutbill :其他出库单 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fhandlerid | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fpurchasecurrencyid | 采购币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fisincludetax | 录入含税单价 | bpchar | 1 |  | √ | '0' | 录入含税单价 |
| 24 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fqtycreate | 整单建卡可生成数量(废弃) | int4 | 32 |  | √ | 0 | 整单建卡可生成数量(废弃) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_purchasebill_pkey |  | fid |
| 2 | idx_fa_purbil_fbillno |  | fbillno |

---

## 资产信息-子表 t_fa_purchasebillentry

- **表名称：** 资产信息-子表
- **表名：** t_fa_purchasebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodel | 规格型号 | varchar | 255 |  |  | ' ' | 规格型号 |
| 3 | frealaccountdate | 开始使用日期 | timestamp | 0 |  |  | null | 开始使用日期 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | ftotalamount | 价税合计（本位币） | numeric | 19 | 6 | √ | 0.000000 | 价税合计（本位币） |
| 7 | fsourceentryid | 来源分录id | int8 | 64 |  | √ | 0 | 来源分录id |
| 8 | fassetqtyleft | 可生成数量(废弃) | numeric | 19 | 6 | √ | 0 | 可生成数量(废弃) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fprice | 单价 | numeric | 19 | 6 | √ | 0 | 单价 |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fisdeductiontax | 是否专票 | bpchar | 1 |  | √ | ' ' | 是否专票 |
| 13 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 14 | funitprice | 单价（作废） | numeric | 19 | 6 | √ | 0.000000 | 单价（作废） |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | finvoicecode | finvoicecode | varchar | 50 |  | √ | ' ' |  |
| 17 | foriginunitprice | foriginunitprice | numeric | 19 | 6 | √ | 0 |  |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | ftaxamount | 税额（本位币） | numeric | 19 | 6 | √ | 0.000000 | 税额（本位币） |
| 20 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 21 | fname | 资产名称 | varchar | 300 |  |  | ' ' | 资产名称 |
| 22 | fbaseassetqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 23 | forigintotalamount | 价税合计 | numeric | 19 | 6 | √ | 0 | 价税合计 |
| 24 | fnotaxamount | 金额（本位币） | numeric | 19 | 6 | √ | 0.000000 | 金额（本位币） |
| 25 | fnewunitprice | 含税单价 | numeric | 19 | 6 | √ | 0 | 含税单价 |
| 26 | forigintaxamount | 税额 | numeric | 19 | 6 | √ | 0 | 税额 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 29 | fassetqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 30 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | ftaxunitprice | 含税单价（作废） | numeric | 19 | 6 | √ | 0.000000 | 含税单价（作废） |
| 33 | foriginnotaxamount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 34 | fismainline | 主信息行 | bpchar | 1 |  | √ | '0' | 主信息行 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fassetqtycreate | 可建卡数量 | numeric | 19 | 6 | √ | 0 | 可建卡数量 |
| 38 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_purbilent_fnumber |  | fid |
| 2 | t_fa_purchasebillentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_fa_purchasebillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_purchasebillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnotaxamount | 金额（本位币）_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 金额（本位币）_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 8 | fnotaxamount_old | 金额（本位币）_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 金额（本位币）_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_purchasebillentry_lk_pkey |  | fpkid |
| 2 | idx_fa_purchasebillentry_lk_fk |  | fentryid |

---

## 采购转固单-关联追踪表 t_fa_purchasebill_tc

- **表名称：** 采购转固单-关联追踪表
- **表名：** t_fa_purchasebill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_purchasebill_tc_pkey |  | fid |
| 2 | idx_fa_purchasebill_tc_tbill |  | ftbillid |
| 3 | idx_fa_purchasebill_tc_tid |  | ftid |
