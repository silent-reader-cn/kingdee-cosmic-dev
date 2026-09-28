# 电商上下架管理-pmm_ecprodaudit

## 电商上下架管理-分表 t_mal_prodenter_a

- **表名称：** 电商上下架管理-分表
- **表名：** t_mal_prodenter_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsuggestion | fsuggestion | varchar | 255 |  | √ | ' ' |  |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prodenter_a_pkey |  | fid |
| 2 | idx_mal_prodenter_a_ftime |  | fcreatetime |

---

## 电商上下架管理-多语言表 t_mal_prodenter_l

- **表名称：** 电商上下架管理-多语言表
- **表名：** t_mal_prodenter_l

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
| 1 | idx_mal_prodenter_l_fid |  | fid,flocaleid |
| 2 | t_mal_prodenter_l_pkey |  | fpkid |

---

## 电商上下架管理-主表 t_mal_prodenter

- **表名称：** 电商上下架管理-主表
- **表名：** t_mal_prodenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 5 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 8 | fsupplierid | 商家 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :待确认 B :已确认 C :已打回 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :上架 2 :下架 |
| 11 | fpersonid | 商家联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 13 | fprotocolid | 商城协议 | int8 | 64 |  | √ | 0 | [协议签订 pmm_protocol_bd](../pmm_files/pmm_protocol_bd.md) |
| 14 | fbillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 15 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodenter_fbilldate |  | fbilldate |
| 2 | idx_mal_prodenter_fbizid |  | fbizpartnerid |
| 3 | t_mal_prodenter_pkey |  | fid |
| 4 | idx_mal_prodenter_fbillno |  | fbillno |

---

## 商品明细-子表 t_mal_prodenterentry

- **表名称：** 商品明细-子表
- **表名：** t_mal_prodenterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricetype | fpricetype | bpchar | 1 |  | √ | 'A' |  |
| 3 | fprotocolentryid | fprotocolentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 5 | fmaterialid | ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 7 | fpriceinvaliddate | fpriceinvaliddate | timestamp | 0 |  |  | null |  |
| 8 | fecstatus | 电商上架状态 | bpchar | 1 |  | √ | ' ' | 电商上架状态,枚举: 1 :上架 0 :下架 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 11 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 12 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 13 | fentryaddressdata_tag | fentryaddressdata_tag | text | 0 |  |  | null |  |
| 14 | fprodpoolid | fprodpoolid | int8 | 64 |  | √ | 0 |  |
| 15 | fbarcode | 商品条形码 | varchar | 80 |  | √ | ' ' | 商品条形码 |
| 16 | fentryprotocolid | fentryprotocolid | int8 | 64 |  | √ | 0 |  |
| 17 | fentryresult | fentryresult | bpchar | 1 |  | √ | ' ' |  |
| 18 | fentryaddressdata | fentryaddressdata | varchar | 255 |  | √ | ' ' |  |
| 19 | fminorderqty | fminorderqty | numeric | 19 | 6 | √ | 0 |  |
| 20 | fleadtime | fleadtime | int8 | 64 |  | √ | 0 |  |
| 21 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0.0000000000 | 商城价 |
| 22 | fentrysupplierid | fentrysupplierid | int8 | 64 |  | √ | 0 |  |
| 23 | fsrcbillid | 来源单据ID | varchar | 80 |  | √ | ' ' | 来源单据ID |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 26 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 27 | fpriceeffectdate | fpriceeffectdate | timestamp | 0 |  |  | null |  |
| 28 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodenter_fid_fseq |  | fid,fseq |
| 2 | idx_mal_prodenter_fgoodsid |  | fgoodsid |
| 3 | t_mal_prodenterentry_pkey |  | fentryid |
