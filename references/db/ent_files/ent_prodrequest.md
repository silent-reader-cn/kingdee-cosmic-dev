# 上下架申请-ent_prodrequest

## 上下架申请-分表 t_mal_prodenter_a

- **表名称：** 上下架申请-分表
- **表名：** t_mal_prodenter_a

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
| 1 | t_mal_prodenter_a_pkey |  | fid |
| 2 | idx_mal_prodenter_a_ftime |  | fcreatetime |

---

## 上下架申请-多语言表 t_mal_prodenter_l

- **表名称：** 上下架申请-多语言表
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

## 上下架申请-主表 t_mal_prodenter

- **表名称：** 上下架申请-主表
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
| 9 | fcfmstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: E :草稿 A :待审批 B :通过 C :部分通过 D :不通过 |
| 10 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :上架 2 :下架 |
| 11 | fpersonid | 商家联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 13 | fprotocolid | 商城协议 | int8 | 64 |  | √ | 0 | [协议查询 ent_priceprotocol_bd](../ent_files/ent_priceprotocol_bd.md) |
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

## 阶梯价-子表 t_mal_ladderprice

- **表名称：** 阶梯价-子表
- **表名：** t_mal_ladderprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fladprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 2 | fqtyto | 数量至（<） | numeric | 19 | 6 | √ | 0 | 数量至（<） |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fqtyfrom | 数量从 | numeric | 19 | 6 | √ | 0 | 数量从 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_ladprice_fentryid_fseq |  | fentryid,fseq |
| 2 | pk_t_mal_ladderprice |  | fdetailid |

---

## 商品分录-子表 t_mal_prodenterentry

- **表名称：** 商品分录-子表
- **表名：** t_mal_prodenterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpricetype | 价格类型 | bpchar | 1 |  | √ | 'A' | 价格类型,枚举: A :固定价 B :阶梯价 |
| 3 | fprotocolentryid | 协议清单 | int8 | 64 |  | √ | 0 | [协议清单基础资料 ent_protocolentry_bd](../ent_files/ent_protocolentry_bd.md) |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fpriceinvaliddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 8 | fecstatus | fecstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 11 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 12 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 13 | fentryaddressdata_tag | 可供货区域_详情 | text | 0 |  |  | null | 可供货区域_详情 |
| 14 | fprodpoolid | 商品池 | int8 | 64 |  | √ | 0 | [商品池 ent_prodpool](../ent_files/ent_prodpool.md) |
| 15 | fbarcode | 商品条形码 | varchar | 80 |  | √ | ' ' | 商品条形码 |
| 16 | fentryprotocolid | 商城协议 | int8 | 64 |  | √ | 0 | [协议签订 pmm_protocol_bd](../pmm_files/pmm_protocol_bd.md) |
| 17 | fentryresult | 审批结果 | bpchar | 1 |  | √ | ' ' | 审批结果,枚举: 1 :同意 0 :不同意 |
| 18 | fentryaddressdata | 可供货区域 | varchar | 255 |  | √ | ' ' | 可供货区域 |
| 19 | fminorderqty | 起订量 | numeric | 19 | 6 | √ | 0 | 起订量 |
| 20 | fleadtime | 供货周期（天） | int8 | 64 |  | √ | 0 | 供货周期（天） |
| 21 | fshopprice | 市场价 | numeric | 23 | 10 | √ | 0.0000000000 | 市场价 |
| 22 | fentrysupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | fsrcbillid | 来源单据ID | varchar | 80 |  | √ | ' ' | 来源单据ID |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 26 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 27 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
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
