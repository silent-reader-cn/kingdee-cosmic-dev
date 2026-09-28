# 价格管理-pmm_price

## 价格管理-使用范围表 t_mal_prod_u

- **表名称：** 价格管理-使用范围表
- **表名：** t_mal_prod_u

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
| 1 | t_mal_prod_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mal_prod_u_uo |  | fuseorgid |

---

## 价格管理-多语言表 t_mal_prod_l

- **表名称：** 价格管理-多语言表
- **表名：** t_mal_prod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 4 | fmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fkeyword | fkeyword | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prod_l_pkey |  | fpkid |
| 2 | idx_mal_prod_l_fid |  | fid,flocaleid |

---

## 价格管理-使用范围位图表 t_mal_prod_m

- **表名称：** 价格管理-使用范围位图表
- **表名：** t_mal_prod_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prod_m |  | forgid |

---

## 价格管理-分表 t_mal_prod_a

- **表名称：** 价格管理-分表
- **表名：** t_mal_prod_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcentralpurtype | fcentralpurtype | bpchar | 1 |  | √ | ' ' |  |
| 3 | fsurchargeamount | fsurchargeamount | varchar | 255 |  | √ | ' ' |  |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fdownloaddate | fdownloaddate | timestamp | 0 |  |  | null |  |
| 7 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fadjustdate | fadjustdate | timestamp | 0 |  |  | null |  |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fthumbnail | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 13 | fsurchargeid | fsurchargeid | varchar | 255 |  | √ | ' ' |  |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpicture5 | fpicture5 | varchar | 255 |  | √ | ' ' |  |
| 17 | fpicture4 | fpicture4 | varchar | 255 |  | √ | ' ' |  |
| 18 | fpicture3 | fpicture3 | varchar | 255 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fpicture2 | fpicture2 | varchar | 255 |  | √ | ' ' |  |
| 21 | fpicture1 | fpicture1 | varchar | 255 |  | √ | ' ' |  |
| 22 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fuploaddate | fuploaddate | timestamp | 0 |  |  | null |  |
| 27 | fsurchargename | fsurchargename | varchar | 255 |  | √ | ' ' |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prod_fcreatetime |  | fcreatetime |
| 2 | t_mal_prod_a_pkey |  | fid |

---

## 价格管理-主表 t_mal_prod

- **表名称：** 价格管理-主表
- **表名：** t_mal_prod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxprefpolicy | ftaxprefpolicy | varchar | 255 |  | √ | ' ' |  |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fminorderqty | fminorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | fspecification | fspecification | text | 0 |  |  | null |  |
| 7 | fmulmodel | fmulmodel | bpchar | 1 |  | √ | '0' |  |
| 8 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 9 | fprodmatmappingstatus | fprodmatmappingstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fisprotocolprod | fisprotocolprod | bpchar | 1 |  | √ | '0' |  |
| 11 | fistaxpref | fistaxpref | bpchar | 1 |  | √ | ' ' |  |
| 12 | fgoodsdetail | fgoodsdetail | text | 0 |  |  | null |  |
| 13 | fgoodsdetail_tag | fgoodsdetail_tag | text | 0 |  |  | null |  |
| 14 | fgoodbarcode | fgoodbarcode | varchar | 80 |  | √ | ' ' |  |
| 15 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 商城价 |
| 16 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 17 | fcategory | fcategory | int8 | 64 |  | √ | 0 |  |
| 18 | ffullname | ffullname | varchar | 512 |  |  | ' ' |  |
| 19 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ftaxcode | ftaxcode | varchar | 50 |  | √ | ' ' |  |
| 21 | fcatlongnumber | fcatlongnumber | varchar | 255 |  | √ | ' ' |  |
| 22 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 23 | fmallstatus | 上架状态 | bpchar | 1 |  | √ | ' ' | 上架状态,枚举: A :待审批 B :已上架 C :已下架 D :退回修改 F :暂存 |
| 24 | fsupplierid | 所属商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 25 | fprodmatmappingid | fprodmatmappingid | int8 | 64 |  | √ | 0 |  |
| 26 | fpurleadday | fpurleadday | int8 | 64 |  | √ | 0 |  |
| 27 | fprodmatmappingtype | fprodmatmappingtype | varchar | 50 |  | √ | ' ' |  |
| 28 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fftstatus | fftstatus | bpchar | 1 |  | √ | ' ' |  |
| 30 | fnumber | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fmodel | fmodel | varchar | 100 |  | √ | ' ' |  |
| 33 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fprodtypeid | fprodtypeid | int8 | 64 |  | √ | '1576866653114004480' |  |
| 35 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 36 | fmaterielid | 对应ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 37 | fminpackqty | fminpackqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 38 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 39 | fsource | 商品来源 | bpchar | 1 |  | √ | ' ' | 商品来源,枚举: 1 :自建商城 |
| 40 | fspunumber | fspunumber | varchar | 30 |  | √ | ' ' |  |
| 41 | fbrandid | fbrandid | int8 | 64 |  | √ | 0 |  |
| 42 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 43 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 44 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 45 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 46 | fspumainprod | fspumainprod | bpchar | 1 |  | √ | '1' |  |
| 47 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 0 :价内税（含税） 1 :价外税（含税） |
| 48 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 49 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 50 | fspecification_tag | fspecification_tag | text | 0 |  |  | null |  |
| 51 | fpackinglist | fpackinglist | text | 0 |  |  | null |  |
| 52 | fvideolocation | fvideolocation | bpchar | 1 |  |  | '0' |  |
| 53 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 54 | fguarantee | fguarantee | text | 0 |  |  | null |  |
| 55 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 56 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 57 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 58 | fkeyword | fkeyword | varchar | 100 |  | √ | ' ' |  |
| 59 | fstandardid | 商品分类标准 | int8 | 64 |  | √ | 0 | [商品分类标准 bd_goodsclassstandard](../gmc_files/bd_goodsclassstandard.md) |
| 60 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prod_pkey |  | fid |
| 2 | idx_mal_prod_fnumber |  | fnumber |
| 3 | idx_mal_prod_fmasterid |  | fmasterid |
| 4 | idx_t_mal_prod_createorg |  | fcreateorgid |
| 5 | idx_mal_prod_fsupplierid |  | fsupplierid |
| 6 | idx_t_mal_prod_master |  | fmasterid |
