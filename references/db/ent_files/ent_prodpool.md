# 商品池-ent_prodpool

## 适用组织范围-子表 t_mal_protprodpoolentry

- **表名称：** 适用组织范围-子表
- **表名：** t_mal_protprodpoolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryorgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_protprodpoolentry |  | fentryid |
| 2 | idx_mal_prodpoolentry_fid_fseq |  | fid,fseq |

---

## 商品池-主表 t_mal_protocolprodpool

- **表名称：** 商品池-主表
- **表名：** t_mal_protocolprodpool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcentralpurtype | 采购模式 | bpchar | 1 |  | √ | ' ' | 采购模式,枚举: 1 :集团集采 2 :区域集采 3 :公司自采 |
| 3 | fpricetype | 价格类型 | bpchar | 1 |  | √ | 'A' | 价格类型,枚举: A :固定价 B :阶梯价 |
| 4 | fprotocolentryid | 协议清单 | int8 | 64 |  | √ | 0 | [协议清单基础资料 ent_protocolentry_bd](../ent_files/ent_protocolentry_bd.md) |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 6 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0 | 税率(%) |
| 7 | fpriceinvaliddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 8 | feffectstatus | 生效状态 | bpchar | 1 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :生效中 C :已失效 |
| 9 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 10 | fpurplanid | 采买方案 | int8 | 64 |  | √ | 0 | [采买方案 pmm_purchaseplan](../pmm_files/pmm_purchaseplan.md) |
| 11 | fauditorgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fminorderqty | 起订量 | numeric | 19 | 6 | √ | 0 | 起订量 |
| 18 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 19 | fplatform | 商城类型 | bpchar | 1 |  | √ | ' ' | 商城类型,枚举: 1 :自建商品 |
| 20 | fleadtime | 供货周期（天） | int8 | 64 |  | √ | 0 | 供货周期（天） |
| 21 | fregionrestriction | 区域限制策略 | bpchar | 1 |  | √ | 'A' | 区域限制策略,枚举: A :全地区可售 B :设置可售地区 C :设置不可售地区 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fshopprice | 市场价 | numeric | 23 | 10 | √ | 0 | 市场价 |
| 25 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fmallprotocolid | 商城协议 | int8 | 64 |  | √ | 0 | [协议查询 ent_priceprotocol_bd](../ent_files/ent_priceprotocol_bd.md) |
| 28 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fmallstatus | 上架状态 | bpchar | 1 |  | √ | ' ' | 上架状态,枚举: A :待上架 B :已上架 C :已下架 D :退回修改 F :暂存 E :待审批 |
| 32 | fsalestatus | 可售状态 | bpchar | 1 |  | √ | ' ' | 可售状态,枚举: A :可售 B :不可售 C :部分区域可售 D :— |
| 33 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fpriceeffectdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 35 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 36 | fisgoodvisible | 商品全集团可见 | bpchar | 1 |  | √ | '1' | 商品全集团可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_protocolprodpool |  | fid |
| 2 | idx_mal_protprodpool_fprotocol |  | fmallprotocolid |
| 3 | idx_mal_protprodpool_fgoods |  | fgoodsid |

---

## 商品池-多语言表 t_mal_protocolprodpool_l

- **表名称：** 商品池-多语言表
- **表名：** t_mal_protocolprodpool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_protocolprodpool_l |  | fpkid |
| 2 | idx_mal_protprodpool_l_fid |  | fid,flocaleid |

---

## 阶梯价分录-子表 t_mal_poolladderentry

- **表名称：** 阶梯价分录-子表
- **表名：** t_mal_poolladderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fladprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 3 | fqtyto | 数量至（<） | numeric | 19 | 6 | √ | 0 | 数量至（<） |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fqtyfrom | 数量从 | numeric | 19 | 6 | √ | 0 | 数量从 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_poolladentry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_poolladderentry |  | fentryid |

---

## 可售区域分录-子表 t_mal_pooladdressentry

- **表名称：** 可售区域分录-子表
- **表名：** t_mal_pooladdressentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | faddressid | 可售区域 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_pooladdressen_fid_fseq |  | fid |
| 2 | pk_mal_pooladdressentry |  | fentryid |
