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
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fprice | 原单价 | numeric | 23 | 10 | √ | 0 | 原单价 |
| 9 | fadjustflag | 调整标识 | varchar | 5 |  | √ | ' ' | 调整标识,枚举: A :保留 B :新增 C :取消 |
| 10 | ftaxrateid | 原税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 11 | fqtyfrom | 从 | numeric | 23 | 10 | √ | 0 | 从 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fsrcpriceentryid | 原价目表行id | int8 | 64 |  | √ | 0 | 原价目表行id |
| 14 | fadjtaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 15 | fpriceandtax | 原含税单价 | numeric | 23 | 10 | √ | 0 | 原含税单价 |
| 16 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 17 | fsrcpricelistid | 原价目表 | int8 | 64 |  | √ | 0 | 采购价目表 pm_purpricelist |
| 18 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fadjpricefloor | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 20 | fadjpriceceiling | 最高限价 | numeric | 23 | 10 | √ | 0 | 最高限价 |
| 21 | fadjprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 22 | fadjpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 23 | fpriceexpirydate | 原价格失效日期 | timestamp | 0 |  |  | null | 原价格失效日期 |
| 24 | fpriceceiling | 原最高限价 | numeric | 23 | 10 | √ | 0 | 原最高限价 |
| 25 | fqtyto | 至 | numeric | 23 | 10 | √ | 0 | 至 |
| 26 | fpriceeffectdate | 原价格生效日期 | timestamp | 0 |  |  | null | 原价格生效日期 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fadjpriceexpirydate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |

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
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fpurpricelistid | 原价目表 | int8 | 64 |  | √ | 0 | 采购价目表 pm_purpricelist |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fadjustmode | 调整方式 | varchar | 10 |  | √ | ' ' | 调整方式,枚举: single :单一调整 batch :批量调整 |
| 13 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 14 | fbatchadjustno | 批量调整单号 | varchar | 80 |  | √ | ' ' | 批量调整单号 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fpricelisttypeid | 价目类型 | int8 | 64 |  | √ | 0 | 价目类型 bd_pricelisttype |
| 17 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 18 | fpricelistgroupid | 价目表分组 | int8 | 64 |  | √ | 0 | 采购价目表分组 pm_purpricelistgroup |
| 19 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 20 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
