# 采购套餐-pmm_packageselection

## 采购套餐-主表 t_mal_prodobtain

- **表名称：** 采购套餐-主表
- **表名：** t_mal_prodobtain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcount_rows | fcount_rows | int4 | 32 |  | √ | 0 |  |
| 3 | fsalesesconfigid | 商品销量统计配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | frange | frange | varchar | 20 |  | √ | ' ' |  |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fplatform | fplatform | varchar | 2 |  | √ | ' ' |  |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | facquisition_mode | 商品推荐方式 | varchar | 10 |  | √ | ' ' | 商品推荐方式,枚举: 1 :分类 2 :供应商 3 :销量 4 :自定义过滤条件 6 :自由组合 |
| 16 | fplugin | fplugin | varchar | 255 |  | √ | ' ' |  |
| 17 | ffiltercondition | ffiltercondition | varchar | 2000 |  | √ | ' ' |  |
| 18 | fgoodsesconfigid | 商品全文检索配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 套餐名称 | varchar | 100 |  | √ | ' ' | 套餐名称 |
| 22 | flimit | flimit | int4 | 32 |  | √ | 0 |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 25 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 26 | fctrlstrategy | 管控策略 | varchar | 50 |  | √ | ' ' | 管控策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | ftype | 方案类型 | bpchar | 1 |  | √ | ' ' | 方案类型,枚举: 1 :楼层展示 2 :场景采购 3 :采购套餐 |
| 28 | fsort_in_category | fsort_in_category | bpchar | 1 |  | √ | '0' |  |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 套餐编码 | varchar | 80 |  | √ | ' ' | 套餐编码 |
| 31 | forderby | 排序 | varchar | 100 |  | √ | ' ' | 排序,枚举: sales :按销量从高到低 price_false :按价格从高到低 price_true :按价格从低到高 modifytime_false :按更新时间降序 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_prodobtain_fnum |  | fnumber |
| 2 | pk_t_mal_prodobtain |  | fid |
| 3 | idx_t_mal_prodobtain_createorg |  | fcreateorgid |
| 4 | idx_t_mal_prodobtain_master |  | fmasterid |

---

## 关联商品信息-分表 t_mal_prodobtainentry_p

- **表名称：** 关联商品信息-分表
- **表名：** t_mal_prodobtainentry_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fisprimary | 主商品 | bpchar | 1 |  | √ | '0' | 主商品 |
| 6 | fgoodssupplier | 商家 | varchar | 255 |  | √ | ' ' | 商家 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prodobtainentry_p |  | fentryid |
| 2 | idx_mal_prodobtainentry_p |  | fid |

---

## 采购套餐-使用范围表 t_mal_prodobtain_u

- **表名称：** 采购套餐-使用范围表
- **表名：** t_mal_prodobtain_u

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
| 1 | pk_t_mal_prodobtain_u |  | fdataid,fuseorgid |
| 2 | idx_t_mal_prodobtain_u_uo |  | fuseorgid |

---

## 采购套餐-分表 t_mal_prodobtain_p

- **表名称：** 采购套餐-分表
- **表名：** t_mal_prodobtain_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: A :采购方 B :供应商 |
| 3 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 4 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fheadsupplierid | fheadsupplierid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prodobtain_p |  | fid |
| 2 | idx_mal_prodobtain_p_s |  | forigin,fheadsupplierid |

---

## 采购套餐-多语言表 t_mal_prodobtain_l

- **表名称：** 采购套餐-多语言表
- **表名：** t_mal_prodobtain_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 套餐名称 | varchar | 100 |  | √ | ' ' | 套餐名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_prodobtain_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_prodobtain_l |  | fpkid |

---

## 关联商品信息-子表 t_mal_prodobtainentry

- **表名称：** 关联商品信息-子表
- **表名：** t_mal_prodobtainentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 自建商品池 pmm_prodmanage |
| 3 | fscenariotag | fscenariotag | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsource | 商品来源 | varchar | 50 |  | √ | ' ' | 商品来源,枚举: pmm_prodmanage :自建商品 pbd_mallgoods :电商商品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_prodoentry_fgoods |  | fgoodsid |
| 2 | idx_mal_prodentry_fid |  | fid |
| 3 | pk_t_mal_prodobtainentry |  | fentryid |
