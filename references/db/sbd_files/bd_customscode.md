# 海关编码对应表-bd_customscode

## 单据体-子表 t_bd_customscodeinfo

- **表名称：** 单据体-子表
- **表名：** t_bd_customscodeinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvatratevalue | 增值税率(%) | numeric | 23 | 10 | √ | 0 | 增值税率(%) |
| 3 | fconstaxratevalue | 消费税率(%) | numeric | 23 | 10 | √ | 0 | 消费税率(%) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fimpnormtaxratevalue | 进口普通税率(%) | numeric | 23 | 10 | √ | 0 | 进口普通税率(%) |
| 6 | fmfntaxrate | 最惠国税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 7 | fextaxratevalue | 出口税率(%) | numeric | 23 | 10 | √ | 0 | 出口税率(%) |
| 8 | fextaxrefundrate | 出口退税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 9 | fextaxrefundratevalue | 出口退税率(%) | numeric | 23 | 10 | √ | 0 | 出口退税率(%) |
| 10 | ftariffcode | 关税编码 | varchar | 50 |  | √ | ' ' | 关税编码 |
| 11 | fgoodsname | 商品名称 | varchar | 512 |  | √ | ' ' | 商品名称 |
| 12 | fvatrate | 增值税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 13 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fconstaxrate | 消费税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fentrycountry | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 16 | fcsconditions | 海关监管条件 | varchar | 50 |  | √ | ' ' | 海关监管条件 |
| 17 | fextaxrate | 出口税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fimpnormtaxrate | 进口普通税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 19 | fimpovtaxrate | 进口暂定税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 20 | fexpovtaxrate | 出口暂定税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 21 | fcustomsgoodscode | 海关商品编码 | varchar | 50 |  | √ | ' ' | 海关商品编码 |
| 22 | fexpovtaxratevalue | 出口暂定税率(%) | numeric | 23 | 10 | √ | 0 | 出口暂定税率(%) |
| 23 | fcustomscodegroup | 海关编码分组 | varchar | 512 |  | √ | ' ' | 海关编码分组 |
| 24 | fsecondarylegalunit | 法定第二单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fmfntaxratevalue | 最惠国税率(%) | numeric | 23 | 10 | √ | 0 | 最惠国税率(%) |
| 26 | fiqcategory | 检验检疫类别 | varchar | 50 |  | √ | ' ' | 检验检疫类别 |
| 27 | fprimarylegalunit | 法定第一单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fimpovtaxratevalue | 进口暂定税率(%) | numeric | 23 | 10 | √ | 0 | 进口暂定税率(%) |

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

## 海关编码对应表-主表 t_bd_customscode

- **表名称：** 海关编码对应表-主表
- **表名：** t_bd_customscode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |
| 24 | fcountry | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customscode |  | fid |
| 2 | idx_bd_customscode_m0 |  | fmasterid |
| 3 | idx_t_bd_customscode_createorg |  | fcreateorgid |
| 4 | idx_t_bd_customscode_master |  | fmasterid |

---

## 海关编码对应表-使用范围表 t_bd_customscode_u

- **表名称：** 海关编码对应表-使用范围表
- **表名：** t_bd_customscode_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_customscode_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_customscode_u_uo |  | fuseorgid |

---

## 海关编码对应表-多语言表 t_bd_customscode_l

- **表名称：** 海关编码对应表-多语言表
- **表名：** t_bd_customscode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_customscode_l |  | fpkid |
| 2 | idx_bd_customscode_l_0 |  | fid,flocaleid |

---

## 单据体-多语言表 t_bd_customscodeinfo_l

- **表名称：** 单据体-多语言表
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
