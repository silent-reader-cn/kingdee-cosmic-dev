# 海关编码对应表明细-bd_customscodeinfo

## 海关编码对应表明细-主表 t_bd_customscodeinfo

- **表名称：** 海关编码对应表明细-主表
- **表名：** t_bd_customscodeinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 海关编码对应表内码 | int8 | 64 |  | √ | 0 | 海关编码对应表内码 |
| 2 | fvatratevalue | fvatratevalue | numeric | 23 | 10 | √ | 0 |  |
| 3 | fconstaxratevalue | fconstaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fimpnormtaxratevalue | fimpnormtaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 6 | fmfntaxrate | 最惠国税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 7 | fextaxratevalue | fextaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fextaxrefundrate | 出口退税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 9 | fextaxrefundratevalue | fextaxrefundratevalue | numeric | 23 | 10 | √ | 0 |  |
| 10 | ftariffcode | 关税编码 | varchar | 50 |  | √ | ' ' | 关税编码 |
| 11 | fgoodsname | 商品名称 | varchar | 512 |  | √ | ' ' | 商品名称 |
| 12 | fvatrate | fvatrate | int8 | 64 |  | √ | 0 |  |
| 13 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fconstaxrate | 消费税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fentrycountry | fentrycountry | int8 | 64 |  | √ | 0 |  |
| 16 | fcsconditions | 海关监管条件 | varchar | 50 |  | √ | ' ' | 海关监管条件 |
| 17 | fextaxrate | 出口税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fimpnormtaxrate | 进口普通税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 19 | fimpovtaxrate | fimpovtaxrate | int8 | 64 |  | √ | 0 |  |
| 20 | fexpovtaxrate | fexpovtaxrate | int8 | 64 |  | √ | 0 |  |
| 21 | fcustomsgoodscode | 海关商品编码 | varchar | 50 |  | √ | ' ' | 海关商品编码 |
| 22 | fexpovtaxratevalue | fexpovtaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 23 | fcustomscodegroup | 海关编码分组 | varchar | 512 |  | √ | ' ' | 海关编码分组 |
| 24 | fsecondarylegalunit | 法定第二单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fmfntaxratevalue | fmfntaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 26 | fiqcategory | 检验检疫类别 | varchar | 50 |  | √ | ' ' | 检验检疫类别 |
| 27 | fprimarylegalunit | 法定第一单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fimpovtaxratevalue | fimpovtaxratevalue | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customscodeinfo |  | fentryid |
| 2 | idx_bd_customscodeinfo_fk |  | fid |

---

## 海关编码对应表明细-多语言表 t_bd_customscodeinfo_l

- **表名称：** 海关编码对应表明细-多语言表
- **表名：** t_bd_customscodeinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcustomscodegroup | 海关编码分组 | varchar | 770 |  | √ | ' ' | 海关编码分组 |
| 2 | fgoodsname | 商品名称 | varchar | 770 |  | √ | ' ' | 商品名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customscodeinfo_l |  | fpkid |
| 2 | idx_bd_customscodeinfo_l_0 |  | fentryid,flocaleid |
