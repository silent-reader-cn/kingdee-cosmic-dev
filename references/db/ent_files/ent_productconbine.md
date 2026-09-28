# 采购套餐（作废）-ent_productconbine

## 采购套餐（作废）-主表 t_mal_productcombine

- **表名称：** 采购套餐（作废）-主表
- **表名：** t_mal_productcombine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricetype | 价格类型 | bpchar | 1 |  | √ | ' ' | 价格类型,枚举: A :固定价 B :折扣价 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fdiscounttype | 优惠方式 | bpchar | 1 |  | √ | ' ' | 优惠方式,枚举: A :整单优惠 B :子商品优惠 C :无优惠 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcombinesid | 主商品 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fdiscount | 优惠折扣 | numeric | 10 | 4 | √ | 0 | 优惠折扣 |
| 11 | fsupplierid | 所属商家 | int8 | 64 |  | √ | 0 | [商城供应商 bd_malsupplier](../basedata_files/bd_malsupplier.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 15 | fbillno | 套餐编号 | varchar | 80 |  | √ | ' ' | 套餐编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_productcombine_fbillno |  | fbillno |
| 2 | idx_mal_productcombine_fcomb |  | fcombinesid |
| 3 | pk_t_mal_productcombine |  | fid |

---

## 采购套餐（作废）-多语言表 t_mal_productcombine_l

- **表名称：** 采购套餐（作废）-多语言表
- **表名：** t_mal_productcombine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 单据体-子表 t_mal_productcombineentry

- **表名称：** 单据体-子表
- **表名：** t_mal_productcombineentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 商品数量 | numeric | 23 | 10 | √ | 0 | 商品数量 |
| 3 | fproductid | 商品编码 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 4 | ffixprice | 固定价格 | numeric | 23 | 10 | √ | 0 | 固定价格 |
| 5 | fentrydiscount | 优惠折扣 | numeric | 10 | 4 | √ | 0 | 优惠折扣 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodcombentry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_productcombineentry |  | fentryid |
