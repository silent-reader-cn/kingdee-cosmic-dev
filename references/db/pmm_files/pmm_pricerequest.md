# 调价申请-pmm_pricerequest

## 商品明细-子表 t_mal_priceadjustentry

- **表名称：** 商品明细-子表
- **表名：** t_mal_priceadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 商城价 |
| 3 | fpricetype | fpricetype | bpchar | 1 |  | √ | 'A' |  |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | ftaxprice | 新结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 新结算价 |
| 10 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 11 | fprice | 新不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 新不含税单价 |
| 12 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 13 | fshopprice_old | 原商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 原商城价 |
| 14 | ftaxprice_old | 原结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 原结算价 |
| 15 | fprice_old | 原不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 原不含税单价 |
| 16 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 17 | fprotocolid | fprotocolid | int8 | 64 |  | √ | 0 |  |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodadjenter_fgoodsid |  | fgoodsid |
| 2 | idx_mal_prodadjenter_fid_fseq |  | fid,fseq |
| 3 | t_mal_priceadjustentry_pkey |  | fentryid |

---

## 调价申请-主表 t_mal_priceadjust

- **表名称：** 调价申请-主表
- **表名：** t_mal_priceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 8 | fsupplierid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :待审批 B :同意 D :不同意 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :调价 |
| 11 | fpersonid | 商家联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 13 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_priceadjust_fbizid |  | fbizpartnerid |
| 2 | idx_mal_priceadjust_fbilldate |  | fbilldate |
| 3 | t_mal_priceadjust_pkey |  | fid |
| 4 | idx_mal_priceadjust_fbillno |  | fbillno |

---

## 调价申请-多语言表 t_mal_priceadjust_l

- **表名称：** 调价申请-多语言表
- **表名：** t_mal_priceadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_priceadjust_l_fid |  | fid,flocaleid |
| 2 | t_mal_priceadjust_l_pkey |  | fpkid |

---

## 调价申请-分表 t_mal_priceadjust_a

- **表名称：** 调价申请-分表
- **表名：** t_mal_priceadjust_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsuggestion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 审批时间 | timestamp | 0 |  |  | null | 审批时间 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcfmid | 审批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_priceadjust_a_ftime |  | fcreatetime |
| 2 | t_mal_priceadjust_a_pkey |  | fid |
