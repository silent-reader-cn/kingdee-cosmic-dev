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
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fsaleorgchannelid | 销售组织渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fouttype | 出库方式 | bpchar | 1 |  | √ | '1' | 出库方式,枚举: 1 :手工出库 2 :自动出库 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fsaleorgid | 渠道库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fsumqty | 出库数量 | numeric | 23 | 10 | √ | 0 | 出库数量 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | foutdate | 出库日期 | timestamp | 0 |  |  | null | 出库日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fenquirychannelid | 要货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | foutchannelid | 出库渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 21 | foutdirection | 出库方向 | bpchar | 1 |  | √ | '1' | 出库方向,枚举: 1 :正向 2 :反向 |

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
| 2 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 bd_taxrate |
| 3 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式 |
| 4 | fdiscountrate | 折扣率 | numeric | 23 | 10 | √ | 0 | 折扣率 |
| 5 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 7 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |

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
| 2 | fstockstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 渠道库存状态 ococic_stockstatus |
| 3 | fbasequantity | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | fstockaddrid | 仓位 | int8 | 64 |  | √ | 0 | 渠道仓位 ococic_location |
| 5 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fproductdate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 10 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | 渠道库存类型 ococic_stocktype |
| 11 | fauxquantity | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 12 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 13 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 14 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | fauxptyunitid | 辅助计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fsnunitid | 序列号单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fsnquantity | 序列号数量 | numeric | 23 | 10 | √ | 0 | 序列号数量 |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 24 | fstockid | 仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 25 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: ocdbd_channel :渠道 bos_org :组织 |
| 26 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 28 | flotid | 批号Id | int8 | 64 |  | √ | 0 | 商品批号 ococic_lot |
| 29 | fsendqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 3 | fserialid | 序列号ID | int8 | 64 |  | √ | 0 | 商品序列号 ococic_snmainfile |
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
