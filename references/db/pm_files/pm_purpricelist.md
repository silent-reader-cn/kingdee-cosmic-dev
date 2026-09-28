# 采购价目表-pm_purpricelist

## 阶梯价格-子表 t_pm_purstairpriceentry

- **表名称：** 阶梯价格-子表
- **表名：** t_pm_purstairpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstairprice | 阶梯价格（废弃） | numeric | 23 | 10 | √ | 0 | 阶梯价格（废弃） |
| 2 | fstairqtyend | 阶梯数量(至)（废弃） | numeric | 23 | 10 | √ | 0 | 阶梯数量(至)（废弃） |
| 3 | funitid | 采购单位（废弃） | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fstairqtystart | 阶梯数量(从)（废弃） | numeric | 23 | 10 | √ | 0 | 阶梯数量(从)（废弃） |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purstairpriceentry |  | fdetailid |
| 2 | idx_pm_purstairpriceentry |  | fentryid |

---

## 关联子实体-子表 t_pm_purpricelist_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purpricelist_lk

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
| 1 | idx_pm_purpricelist_lk_fk |  | fid |
| 2 | pk_pm_purpricelist_lk |  | fpkid |

---

## 关联子实体-子表 t_pm_pplentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_pplentry_lk

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
| 1 | idx_pm_pplentry_lk_fk |  | fentryid |
| 2 | pk_pm_pplentry_lk |  | fpkid |

---

## 采购价目表-主表 t_pm_purpricelist

- **表名称：** 采购价目表-主表
- **表名：** t_pm_purpricelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricetype | 价格类型 | varchar | 30 |  | √ | ' ' | 价格类型,枚举: A :标准采购 B :VMI采购 C :产品委外采购 D :工序委外采购 E :工序协作 |
| 3 | fdefpricelist | 默认价目表 | bpchar | 1 |  | √ | '0' | 默认价目表 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisstair | 启用阶梯（废弃） | bpchar | 1 |  | √ | '0' | 启用阶梯（废弃） |
| 13 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | ' ' |  |
| 21 | fpricelisttypeid | 价目类型 | int8 | 64 |  | √ | 0 | [价目类型 bd_pricelisttype](../sbd_files/bd_pricelisttype.md) |
| 22 | fpricelistgroupid | 价目表分组 | int8 | 64 |  | √ | 0 | [采购价目表分组 pm_purpricelistgroup](../pm_files/pm_purpricelistgroup.md) |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purpl_fnumber |  | fnumber |
| 2 | t_pm_purpricelist_pkey |  | fid |

---

## 价格明细单据体-子表 t_pm_pplentry

- **表名称：** 价格明细单据体-子表
- **表名：** t_pm_pplentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricefloor | 最低限价 | numeric | 23 | 10 | √ | 0.0000000000 | 最低限价 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 5 | fadjustbillno | 调整单编号 | varchar | 80 |  | √ | ' ' | 调整单编号 |
| 6 | fisstairprice | 阶梯价格（废弃） | bpchar | 1 |  | √ | '0' | 阶梯价格（废弃） |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fworkprocesses | 工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 11 | fmaterialwastepricetax | 料废含税价 | numeric | 23 | 10 | √ | 0 | 料废含税价 |
| 12 | funitpriceqty | 每单价数量 | numeric | 23 | 10 | √ | 0.0000000000 | 每单价数量 |
| 13 | fworkwastepricetax | 工废含税价 | numeric | 23 | 10 | √ | 0 | 工废含税价 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fqtyfrom | 从 | numeric | 23 | 10 | √ | 0.0000000000 | 从 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 18 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 19 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 20 | fbaseqtyfrom | 采购数量(从)(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 采购数量(从)(基本单位) |
| 21 | fmaterialwasteprice | 料废价 | numeric | 23 | 10 | √ | 0 | 料废价 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fbaseqtyto | 采购数量(至)(基本单位) | numeric | 23 | 10 | √ | 0.0000000000 | 采购数量(至)(基本单位) |
| 24 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fworkwasteprice | 工废价 | numeric | 23 | 10 | √ | 0 | 工废价 |
| 26 | fpriceexpirydate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 27 | fadjustbillid | 调整单ID | int8 | 64 |  | √ | 0 | 调整单ID |
| 28 | fpriceceiling | 最高限价 | numeric | 23 | 10 | √ | 0.0000000000 | 最高限价 |
| 29 | fqtyto | 至 | numeric | 23 | 10 | √ | 0.0000000000 | 至 |
| 30 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fsrcbilltypeid | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_pplentry_fid |  | fid |
| 2 | idx_pm_pplentry_material_uint |  | fmaterialid,funitid |
| 3 | t_pm_pplentry_pkey |  | fentryid |

---

## 采购价目表-多语言表 t_pm_purpricelist_l

- **表名称：** 采购价目表-多语言表
- **表名：** t_pm_purpricelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purpricelist_l_fid |  | fid,flocaleid |
| 2 | t_pm_purpricelist_l_pkey |  | fpkid |
