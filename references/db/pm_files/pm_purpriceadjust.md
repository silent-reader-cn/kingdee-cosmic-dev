# 采购基价调整单-pm_purpriceadjust

## 调整明细单据体-子表 t_pm_purpadjustentry

- **表名称：** 调整明细单据体-子表
- **表名：** t_pm_purpadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricefloor | 原最低限价 | numeric | 23 | 10 | √ | 0 | 原最低限价 |
| 3 | fadjpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 6 | fadjqtyto | 至 | numeric | 23 | 10 | √ | 0 | 至 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fprice | 原单价 | numeric | 23 | 10 | √ | 0 | 原单价 |
| 10 | fadjustflag | 调整标识 | varchar | 5 |  | √ | ' ' | 调整标识,枚举: A :保留 B :新增 C :取消 |
| 11 | ftaxrateid | 原税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 12 | fqtyfrom | 从（原） | numeric | 23 | 10 | √ | 0 | 从（原） |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fsrcpriceentryid | 原价目表行id | int8 | 64 |  | √ | 0 | 原价目表行id |
| 15 | fadjtaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fpriceandtax | 原含税单价 | numeric | 23 | 10 | √ | 0 | 原含税单价 |
| 17 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 18 | fsrcpricelistid | 原价目表 | int8 | 64 |  | √ | 0 | [采购价目表 pm_purpricelist](../pm_files/pm_purpricelist.md) |
| 19 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fadjpricefloor | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 21 | fadjqtyfrom | 从 | numeric | 23 | 10 | √ | 0 | 从 |
| 22 | fadjpriceceiling | 最高限价 | numeric | 23 | 10 | √ | 0 | 最高限价 |
| 23 | fadjprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 24 | fadjpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 25 | fpriceexpirydate | 原价格失效日期 | timestamp | 0 |  |  | null | 原价格失效日期 |
| 26 | fpriceceiling | 原最高限价 | numeric | 23 | 10 | √ | 0 | 原最高限价 |
| 27 | fqtyto | 至（原） | numeric | 23 | 10 | √ | 0 | 至（原） |
| 28 | fpriceeffectdate | 原价格生效日期 | timestamp | 0 |  |  | null | 原价格生效日期 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fadjpriceexpirydate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purpadjustentry_fid |  | fid |
| 2 | pk_t_pm_purpadjustentry |  | fentryid |

---

## 采购基价调整单-主表 t_pm_purpriceadjust

- **表名称：** 采购基价调整单-主表
- **表名：** t_pm_purpriceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fpurpricelistid | 原价目表 | int8 | 64 |  | √ | 0 | [采购价目表 pm_purpricelist](../pm_files/pm_purpricelist.md) |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fadjustmode | 调整方式 | varchar | 10 |  | √ | ' ' | 调整方式,枚举: single :单一调整 batch :批量调整 manual :手工新增 |
| 13 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 14 | fbatchadjustno | 批量调整单号 | varchar | 80 |  | √ | ' ' | 批量调整单号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpricelisttypeid | 价目类型 | int8 | 64 |  | √ | 0 | [价目类型 bd_pricelisttype](../sbd_files/bd_pricelisttype.md) |
| 17 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 18 | fpricelistgroupid | 价目表分组 | int8 | 64 |  | √ | 0 | [采购价目表分组 pm_purpricelistgroup](../pm_files/pm_purpricelistgroup.md) |
| 19 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 20 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 21 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purpriceadjust_fnumber |  | fbillno |
| 2 | pk_t_pm_purpriceadjust |  | fid |

---

## 采购基价调整单-多语言表 t_pm_purpriceadjust_l

- **表名称：** 采购基价调整单-多语言表
- **表名：** t_pm_purpriceadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purpriceadjust_l_fid |  | fid,flocaleid |
| 2 | pk_t_pm_purpriceadjust_l |  | fpkid |
