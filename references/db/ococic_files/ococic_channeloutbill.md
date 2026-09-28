# 渠道出库-ococic_channeloutbill

## 关联子实体-子表 t_ococic_chnlout_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_chnlout_lk

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
| 1 | pk_ococic_chnlout_lk |  | fpkid |
| 2 | idx_ococic_chnlout_lk_fk |  | fid |

---

## 渠道出库-主表 t_ococic_chnlout

- **表名称：** 渠道出库-主表
- **表名：** t_ococic_chnlout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsaleorgchannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fonwayower | 在途归属 | bpchar | 1 |  | √ | ' ' | 在途归属,枚举: A :调出货主 B :调入货主 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | foutdate | 出库日期 | timestamp | 0 |  |  | null | 出库日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 9 | finstockorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | foutchannelid | 出库渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fouttype | 出库方式 | bpchar | 1 |  | √ | '1' | 出库方式,枚举: 1 :手工出库 2 :自动出库 |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fsaleorgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsumqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 20 | frtchannelid | 出库店铺 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 21 | fenquirychannelid | 要货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 22 | ftransfertype | 调拨类型 | bpchar | 1 |  | √ | 'A' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 23 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 26 | foutdirection | 出库方向 | bpchar | 1 |  | √ | '1' | 出库方向,枚举: 1 :正向 2 :反向 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_chnlout |  | fid |
| 2 | idx_ococic_chnlout_no |  | fbillno |
| 3 | idx_ococic_chnlout_out |  | foutchannelid |
| 4 | idx_ococic_chnlout_order |  | fenquirychannelid |
| 5 | idx_ococic_chnlout_org |  | fsaleorgid |

---

## 关联子实体-子表 t_ococic_chnlout_sn_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_chnlout_sn_lk

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
| 1 | idx_ococic_chnlout_sn_lk_fk |  | fdetailid |
| 2 | pk_ococic_chnlout_sn_lk |  | fpkid |

---

## 单据体-分表 t_ococic_chnlout_entry_r

- **表名称：** 单据体-分表
- **表名：** t_ococic_chnlout_entry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 3 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 4 | fjoinbaseqty | 已关联基本数量 | numeric | 23 | 10 | √ | 0 | 已关联基本数量 |
| 5 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 6 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 7 | fjoinassistqty | 已关联辅助数量 | numeric | 23 | 10 | √ | 0 | 已关联辅助数量 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 9 | fsrcbillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 10 | fsrcbillentryseq | 源单分录序号 | int8 | 64 |  | √ | 0 | 源单分录序号 |
| 11 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 12 | fmainbillentryid | 核心单据分录ID | int8 | 64 |  | √ | 0 | 核心单据分录ID |
| 13 | fjoinqty | 已关联数量 | numeric | 23 | 10 | √ | 0 | 已关联数量 |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ococic_chnloutentryr_fid |  | fid |
| 2 | pk_ococic_chnlout_entry_r |  | fentryid |

---

## 关联子实体-子表 t_ococic_chnlout_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ococic_chnlout_entry_lk

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
| 1 | idx_ococic_chnlout_entry_lk_fk |  | fentryid |
| 2 | pk_ococic_chnlout_entry_lk |  | fpkid |

---

## 单据体-分表 t_ococic_chnlout_entry_f

- **表名称：** 单据体-分表
- **表名：** t_ococic_chnlout_entry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :无 |
| 4 | fdiscountrate | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 5 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | famountloc | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 11 | famountandtaxloc | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 12 | ftaxamountloc | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 13 | ftaxvalue | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
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
| 1 | pk_ococic_chnlout_entry_f |  | fentryid |
| 2 | idx_ococic_chnloutentryf_fid |  | fid |

---

## 单据体-子表 t_ococic_chnlout_entry

- **表名称：** 单据体-子表
- **表名：** t_ococic_chnlout_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [渠道库存状态 ococic_stockstatus](../ococic_files/ococic_stockstatus.md) |
| 3 | fbasequantity | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | fstockaddrid | 仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 5 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 6 | frelatebaseqty | ERP关联基本数量 | numeric | 23 | 10 | √ | 0 | ERP关联基本数量 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freturnbaseqty | 已退回基本数量 | numeric | 23 | 10 | √ | 0 | 已退回基本数量 |
| 10 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 12 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 13 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [渠道库存类型 ococic_stocktype](../ococic_files/ococic_stocktype.md) |
| 14 | fauxquantity | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 15 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 16 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 17 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 20 | fauxptyunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | foutlocationid | 调出ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 22 | fsnunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fsnquantity | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 26 | foutstockid | 调出ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | finlocationid | 调入ERP仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 29 | freturnqty | 已退回数量 | numeric | 23 | 10 | √ | 0 | 已退回数量 |
| 30 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 31 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 32 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 33 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 35 | flotid | 批号Id | int8 | 64 |  | √ | 0 | [商品批号 ococic_lot](../ococic_files/ococic_lot.md) |
| 36 | fsendqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 37 | fchinlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [渠道仓位 ococic_location](../ococic_files/ococic_location.md) |
| 38 | finstockid | 调入ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_chnlout_entry |  | fentryid |
| 2 | idx_ococic_chnloutentry_fid |  | fid |

---

## 渠道出库-反写记录表 t_ococic_chnlout_wb

- **表名称：** 渠道出库-反写记录表
- **表名：** t_ococic_chnlout_wb

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
| 1 | idx_ococic_chnlout_wb_fk |  | fid |
| 2 | pk_ococic_chnlout_wb |  | fentryid |

---

## 子单据体-子表 t_ococic_chnlout_sn

- **表名称：** 子单据体-子表
- **表名：** t_ococic_chnlout_sn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fserialid | 序列号ID | int8 | 64 |  | √ | 0 | [商品序列号 ococic_snmainfile](../ococic_files/ococic_snmainfile.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 6 | fserialcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_chnlout_sn |  | fdetailid |
| 2 | idx_ococic_chnloutsn_eid |  | fentryid |

---

## 渠道出库-关联追踪表 t_ococic_chnlout_tc

- **表名称：** 渠道出库-关联追踪表
- **表名：** t_ococic_chnlout_tc

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
| 1 | pk_ococic_chnlout_tc |  | fid |
| 2 | idx_ococic_chnlout_tc_tbill |  | ftbillid |
| 3 | idx_ococic_chnlout_tc_tid |  | ftid |

---

## 渠道出库-分表 t_ococic_chnlout_f

- **表名称：** 渠道出库-分表
- **表名：** t_ococic_chnlout_f

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
| 1 | pk_ococic_chnlout_f |  | fid |
