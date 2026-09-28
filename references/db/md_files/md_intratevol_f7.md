# 利率上限波动率曲面-md_intratevol_f7

## 利率上限波动率曲面-多语言表 t_md_intratevol_l

- **表名称：** 利率上限波动率曲面-多语言表
- **表名：** t_md_intratevol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_intratevol_l |  | fpkid |
| 2 | idx_md_intratevol_l_id |  | fid,flocaleid |

---

## 利率上限波动率曲面-主表 t_md_intratevol

- **表名称：** 利率上限波动率曲面-主表
- **表名：** t_md_intratevol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarketid | fmarketid | int8 | 64 |  | √ | 0 |  |
| 3 | fnameprice | fnameprice | int8 | 64 |  | √ | 0 |  |
| 4 | fpoint | fpoint | int4 | 32 |  | √ | 0 |  |
| 5 | fisfixedvol | fisfixedvol | bpchar | 1 |  | √ | ' ' |  |
| 6 | fpriceruleid | fpriceruleid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftermend | ftermend | timestamp | 0 |  |  | null |  |
| 12 | fdateadjustmethod | fdateadjustmethod | varchar | 30 |  | √ | ' ' |  |
| 13 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 16 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fstrikedif | fstrikedif | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | friskfactors | friskfactors | varchar | 30 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fisfixedprice | fisfixedprice | bpchar | 1 |  | √ | ' ' |  |
| 22 | finsertmethod | finsertmethod | varchar | 30 |  | √ | ' ' |  |
| 23 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 24 | fatmpricecol | fatmpricecol | int8 | 64 |  | √ | 0 |  |
| 25 | fbasis | fbasis | varchar | 30 |  | √ | ' ' |  |
| 26 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 27 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 28 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 29 | ftimeinterval | ftimeinterval | varchar | 30 |  | √ | ' ' |  |
| 30 | ftermstart | ftermstart | timestamp | 0 |  |  | null |  |
| 31 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 32 | fisatmprice | fisatmprice | bpchar | 1 |  | √ | ' ' |  |
| 33 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |
| 34 | frefdate | frefdate | timestamp | 0 |  |  | null |  |
| 35 | frefindexid | frefindexid | int8 | 64 |  | √ | 0 |  |
| 36 | fparvoldif | fparvoldif | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_intratevol |  | fid |
| 2 | idx_intratevol_bb |  | fbillno |
