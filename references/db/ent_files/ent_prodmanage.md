# 商品管理-ent_prodmanage

## 辅助属性单据体-子表 t_mal_prodattributeentry

- **表名称：** 辅助属性单据体-子表
- **表名：** t_mal_prodattributeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fprodattributeid | 属性编码 | int8 | 64 |  | √ | 0 | [属性映射商品分类 ent_prodattribute](../ent_files/ent_prodattribute.md) |
| 4 | fprodattributevalueid | 属性内容 | int8 | 64 |  | √ | 0 | [属性内容设置 ent_prodattributevalue](../ent_files/ent_prodattributevalue.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_proattrentry_fid_fseq |  | fseq,fid |
| 2 | pk_mal_prodattributeentry |  | fentryid |

---

## 价格及可采买范围-子表 t_mal_prodentry

- **表名称：** 价格及可采买范围-子表
- **表名：** t_mal_prodentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fprotocolid | 协议编码 | int8 | 64 |  | √ | 0 | [协议签订 pmm_protocol_bd](../pmm_files/pmm_protocol_bd.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fprodpoolid | 商品池 | int8 | 64 |  | √ | 0 | [商品池 pmm_prodpool](../pmm_files/pmm_prodpool.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prodentry |  | fentryid |
| 2 | idx_mal_prodentry_fid_fseq |  | fid,fseq |
| 3 | idx_mal_prodentry_fpropoolid |  | fprodpoolid |

---

## 商品管理-主表 t_mal_prod

- **表名称：** 商品管理-主表
- **表名：** t_mal_prod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxprefpolicy | 优惠政策 | varchar | 255 |  | √ | ' ' | 优惠政策 |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fminorderqty | 最小订货量 | numeric | 19 | 6 | √ | 0.000000 | 最小订货量 |
| 6 | fspecification | 商品参数 | text | 0 |  |  | null | 商品参数 |
| 7 | fmulmodel | fmulmodel | bpchar | 1 |  | √ | '0' |  |
| 8 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 9 | fprodmatmappingstatus | fprodmatmappingstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fisprotocolprod | 协议商品 | bpchar | 1 |  | √ | '0' | 协议商品 |
| 11 | fistaxpref | 税收优惠 | bpchar | 1 |  | √ | ' ' | 税收优惠,枚举: 0 :无 1 :优惠 |
| 12 | fgoodsdetail | 商品详情 | text | 0 |  |  | null | 商品详情 |
| 13 | fgoodsdetail_tag | 商品详情_详情 | text | 0 |  |  | null | 商品详情_详情 |
| 14 | fgoodbarcode | 商品条形码 | varchar | 80 |  | √ | ' ' | 商品条形码 |
| 15 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 商城价 |
| 16 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 17 | fcategory | fcategory | int8 | 64 |  | √ | 0 |  |
| 18 | ffullname | ffullname | varchar | 512 |  |  | ' ' |  |
| 19 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ftaxcode | 税收编码 | varchar | 50 |  | √ | ' ' | 税收编码 |
| 21 | fcatlongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 22 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 23 | fmallstatus | 上架状态 | bpchar | 1 |  | √ | ' ' | 上架状态,枚举: A :待审批 B :已上架 C :已下架 D :退回修改 F :暂存 |
| 24 | fsupplierid | 所属商家 | int8 | 64 |  | √ | 0 | [商城供应商 bd_malsupplier](../basedata_files/bd_malsupplier.md) |
| 25 | fprodmatmappingid | fprodmatmappingid | int8 | 64 |  | √ | 0 |  |
| 26 | fpurleadday | fpurleadday | int8 | 64 |  | √ | 0 |  |
| 27 | fprodmatmappingtype | fprodmatmappingtype | varchar | 50 |  | √ | ' ' |  |
| 28 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fftstatus | 已同步到全文检索库 | bpchar | 1 |  | √ | ' ' | 已同步到全文检索库,枚举: A :未同步 B :已同步 |
| 30 | fnumber | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fmodel | fmodel | varchar | 100 |  | √ | ' ' |  |
| 33 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fprodtypeid | 商品类型 | int8 | 64 |  | √ | '1576866653114004480' | [商品类型 pmm_producttype](../pmm_files/pmm_producttype.md) |
| 35 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 36 | fmaterielid | 对应ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 37 | fminpackqty | 最小包装量 | numeric | 19 | 6 | √ | 0.000000 | 最小包装量 |
| 38 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 39 | fsource | 商品来源 | bpchar | 1 |  | √ | ' ' | 商品来源,枚举: 1 :自建商城 2 :京东商城 4 :得力商城 |
| 40 | fspunumber | 关联SPU | varchar | 30 |  | √ | ' ' | 关联SPU |
| 41 | fbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 42 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 C :已审核 |
| 43 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 44 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 45 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 46 | fspumainprod | SPU主商品 | bpchar | 1 |  | √ | '1' | SPU主商品 |
| 47 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 0 :价内税（含税） 1 :价外税（含税） |
| 48 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 49 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 50 | fspecification_tag | 商品参数_详情 | text | 0 |  |  | null | 商品参数_详情 |
| 51 | fpackinglist | 包装清单 | text | 0 |  |  | null | 包装清单 |
| 52 | fvideolocation | 视频放主图后 | bpchar | 1 |  |  | '0' | 视频放主图后 |
| 53 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 54 | fguarantee | 售后保障 | text | 0 |  |  | null | 售后保障 |
| 55 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 57 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
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

---

## 商品管理-使用范围表 t_mal_prod_u

- **表名称：** 商品管理-使用范围表
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

## 商品管理-多语言表 t_mal_prod_l

- **表名称：** 商品管理-多语言表
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
| 8 | fkeyword | 搜索关键字 | varchar | 100 |  | √ | ' ' | 搜索关键字 |

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

## 商品管理-使用范围位图表 t_mal_prod_m

- **表名称：** 商品管理-使用范围位图表
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

## 商品管理-分表 t_mal_prod_a

- **表名称：** 商品管理-分表
- **表名：** t_mal_prod_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcentralpurtype | 签约商品 | bpchar | 1 |  | √ | ' ' | 签约商品,枚举: 1 :签约 |
| 3 | fsurchargeamount | 附加费金额 | varchar | 255 |  | √ | ' ' | 附加费金额 |
| 4 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fdownloaddate | 最近下架时间 | timestamp | 0 |  |  | null | 最近下架时间 |
| 7 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fadjustdate | 最近调价时间 | timestamp | 0 |  |  | null | 最近调价时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fthumbnail | 商品主图 | varchar | 255 |  | √ | ' ' | 商品主图 |
| 13 | fsurchargeid | 附加费方案ID | varchar | 255 |  | √ | ' ' | 附加费方案ID |
| 14 | fcreateorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpicture5 | 商品图片5 | varchar | 255 |  | √ | ' ' | 商品图片5 |
| 17 | fpicture4 | 商品图片5 | varchar | 255 |  | √ | ' ' | 商品图片5 |
| 18 | fpicture3 | 商品图片4 | varchar | 255 |  | √ | ' ' | 商品图片4 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fpicture2 | 商品图片3 | varchar | 255 |  | √ | ' ' | 商品图片3 |
| 21 | fpicture1 | 商品图片2 | varchar | 255 |  | √ | ' ' | 商品图片2 |
| 22 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fuploaddate | 最近上架时间 | timestamp | 0 |  |  | null | 最近上架时间 |
| 27 | fsurchargename | 附加费方案名称 | varchar | 255 |  | √ | ' ' | 附加费方案名称 |
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
