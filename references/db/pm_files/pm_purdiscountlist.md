# 采购折扣表-pm_purdiscountlist

## 折扣明细-子表 t_pm_purdiscount_entry

- **表名称：** 折扣明细-子表
- **表名：** t_pm_purdiscount_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodel | fmodel | varchar | 100 |  | √ | ' ' |  |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | ftoamount | 至（金额） | numeric | 23 | 10 | √ | 0 | 至（金额） |
| 5 | fdiscountrate | 单位折扣（率） | numeric | 23 | 10 | √ | 0 | 单位折扣（率） |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fdiscountmode | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率（%） B :单位折扣额 |
| 11 | ffromqty | 从（数量） | numeric | 23 | 10 | √ | 0 | 从（数量） |
| 12 | ftoqty | 至（数量） | numeric | 23 | 10 | √ | 0 | 至（数量） |
| 13 | ffromamount | 从（金额） | numeric | 23 | 10 | √ | 0 | 从（金额） |
| 14 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fmaterialname | fmaterialname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purdiscount_entry |  | fentryid |
| 2 | idx_pm_discount_entry_fid |  | fid |

---

## 采购折扣表-多语言表 t_pm_purdiscount_l

- **表名称：** 采购折扣表-多语言表
- **表名：** t_pm_purdiscount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_discount_fid |  | fid |
| 2 | pk_t_pm_purdiscount_l |  | fpkid |

---

## 采购折扣表-主表 t_pm_purdiscount

- **表名称：** 采购折扣表-主表
- **表名：** t_pm_purdiscount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdiscountbasis | 折扣依据 | varchar | 5 |  | √ | ' ' | 折扣依据,枚举: A :数量 B :金额 |
| 5 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fdiscountobject | 折扣对象 | varchar | 5 |  | √ | ' ' | 折扣对象,枚举: 1 :物料 2 :物料分类 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purdiscount |  | fid |
| 2 | idx_pm_discount_fnumber |  | fnumber |
