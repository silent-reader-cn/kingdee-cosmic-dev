# 渠道入库-ococic_channelinbill

## 渠道入库-反写记录表 t_ococic_channelinbill_wb

- **表名称：** 渠道入库-反写记录表
- **表名：** t_ococic_channelinbill_wb

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
| 1 | idx_ococic_channelinbill_wb_fk |  | fid |
| 2 | pk_ococic_channelinbill_wb |  | fentryid |

---

## 单据体-子表 t_ococic_inbillentry

- **表名称：** 单据体-子表
- **表名：** t_ococic_inbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | frelatebaseqty | ERP关联基本数量 | numeric | 23 | 10 | √ | 0 | ERP关联基本数量 |
| 5 | fmaterialid | 物料ID | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | freturnqty | 已退回数量 | numeric | 23 | 10 | √ | 0 | 已退回数量 |
| 9 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 10 | fserialqty | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | freturnbaseqty | 已退回基本数量 | numeric | 23 | 10 | √ | 0 | 已退回基本数量 |
| 13 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 14 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 16 | fassistqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 17 | frowremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fassistunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_inbillentry |  | fentryid |
| 2 | idx_ococic_inbillentry_fid |  | fid |

---

## 渠道入库-分表 t_ococic_inbill_f

- **表名称：** 渠道入库-分表
- **表名：** t_ococic_inbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalamountloc | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | ftotaldisamountloc | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |
| 6 | ftotalallamountloc | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 7 | ftotaltaxamountloc | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | ftotaldisamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 12 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 13 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_inbill_f |  | fid |

---

## 单据体-分表 t_ococic_inbillentry_f

- **表名称：** 单据体-分表
- **表名：** t_ococic_inbillentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fdiscounttype | 折扣方式 | bpchar | 1 |  | √ | 'C' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :无 |
| 4 | fdiscountrate | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 5 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 8 | fcuramountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 9 | famountloc | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 10 | famountandtaxloc | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 11 | ftaxamountloc | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 12 | ftaxvalue | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 13 | ftaxratedid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 16 | fdiscountamountloc | 折扣额(本位币) | numeric | 23 | 10 | √ | 0 | 折扣额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_inbillentryf_fid |  | fid |
| 2 | pk_ococic_inbillentry_f |  | fentryid |

---

## 关联子实体-子表 t_ococic_inbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_inbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_inbill_lk_fk |  | fid |
| 2 | pk_ococic_inbill_lk |  | fpkid |

---

## 关联子实体-子表 t_ococic_inbillseria_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_inbillseria_lk

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
| 1 | idx_ococic_inbillseria_lk_fk |  | fdetailid |
| 2 | pk_ococic_inbillseria_lk |  | fpkid |

---

## 关联子实体-子表 t_ococic_inbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_inbillentry_lk

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
| 1 | pk_ococic_inbillentry_lk |  | fpkid |
| 2 | idx_ococic_inbillentry_lk_fk |  | fentryid |

---

## 单据体-分表 t_ococic_inbillentry_s

- **表名称：** 单据体-分表
- **表名：** t_ococic_inbillentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 3 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 4 | fsourceentryserialseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 5 | fsourceid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fsourceentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 7 | fcorebillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 8 | fcorebillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 9 | fsourcecodeno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 10 | fcorebillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 11 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 12 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fcorebillrowid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_inbille_sid |  | fsourceid |
| 2 | pk_ococic_inbillentry_s |  | fentryid |
| 3 | idx_ococic_inbillentrys_fid |  | fid |

---

## 渠道入库-关联追踪表 t_ococic_channelinbill_tc

- **表名称：** 渠道入库-关联追踪表
- **表名：** t_ococic_channelinbill_tc

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
| 1 | idx_ococic_channelinbill_tc_tbill |  | ftbillid |
| 2 | idx_ococic_channelinbill_tc_tid |  | ftid |
| 3 | pk_ococic_channelinbill_tc |  | fid |

---

## 单据体-分表 t_ococic_inbillentry_w

- **表名称：** 单据体-分表
- **表名：** t_ococic_inbillentry_w

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstockstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | flotnumberid | 批号ID | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 4 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 5 | foutstockid | 调出ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 6 | finlocationid | 调入ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 7 | fchoutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 8 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 10 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 12 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 13 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 14 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :组织 ocdbd_channel :渠道 |
| 15 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | finstockid | 调入ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | foutlocationid | 调出ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_inbillentry_w |  | fentryid |
| 2 | idx_ococic_inbillentryw_fid |  | fid |

---

## 渠道入库-主表 t_ococic_inbill

- **表名称：** 渠道入库-主表
- **表名：** t_ococic_inbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplychannelid | 供货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 3 | foutstockorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fonwayower | 在途归属 | bpchar | 1 |  | √ | 'A' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 6 | finway | 入库方向 | bpchar | 1 |  | √ | '1' | 入库方向,枚举: 1 :正向 2 :反向 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsellorgchannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 11 | ferpsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fintype | 入库方式 | bpchar | 1 |  | √ | '1' | 入库方式,枚举: 1 :手工入库 2 :自动签收 3 :手工签收 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fsumqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 21 | fsupplierid | 供货方 | int8 | 64 |  | √ | 0 | [供货关系 ocdbd_channel_authorize](../ocdbd_files/ocdbd_channel_authorize.md) |
| 22 | frtchannelid | 入库店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 23 | ftransfertype | 调拨类型 | bpchar | 1 |  | √ | 'A' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 24 | finchannelid | 入库渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 25 | frtbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 26 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | finstocktime | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_inbill |  | fid |
| 2 | idx_ococic_inbill_billno |  | fbillno |

---

## 子单据体-子表 t_ococic_inbillseria

- **表名称：** 子单据体-子表
- **表名：** t_ococic_inbillseria

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fauxsnt | 辅序列号2 | varchar | 80 |  | √ | ' ' | 辅序列号2 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fserialid | 序列号ID | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |
| 5 | fauxsno | 辅序列号1 | varchar | 80 |  | √ | ' ' | 辅序列号1 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 8 | fpackageno | 箱码 | varchar | 80 |  | √ | ' ' | 箱码 |
| 9 | fserialcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | foutboxno | 外盒码 | varchar | 80 |  | √ | ' ' | 外盒码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_inbillserial_eid |  | fentryid |
| 2 | pk_ococic_inbillseria |  | fdetailid |
