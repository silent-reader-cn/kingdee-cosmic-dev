# 商品推荐方案-pmm_product_obtain

## 商品分类-多选基础资料表 t_mal_prodobtain_cat

- **表名称：** 商品分类-多选基础资料表
- **表名：** t_mal_prodobtain_cat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodobtain_cat_fid |  | fbasedataid |
| 2 | pk_t_mal_prodobtain_cat |  | fpkid |

---

## 商品推荐方案-主表 t_mal_prodobtain

- **表名称：** 商品推荐方案-主表
- **表名：** t_mal_prodobtain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcount_rows | 统计行数 | int4 | 32 |  | √ | 0 | 统计行数 |
| 3 | fsalesesconfigid | 商品销量统计配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 6 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | frange | 销量 | varchar | 20 |  | √ | ' ' | 销量,枚举: 10 :TOP10 20 :TOP20 50 :TOP50 100 :TOP100 |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fplatform | 电商平台 | varchar | 2 |  | √ | ' ' | 电商平台,枚举: 1 :自建商品 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 14 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 15 | facquisition_mode | 商品推荐方式 | varchar | 10 |  | √ | ' ' | 商品推荐方式,枚举: 1 :分类 2 :供应商 3 :销量 4 :自定义过滤条件 6 :自由组合 |
| 16 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 17 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 18 | fgoodsesconfigid | 商品全文检索配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 19 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 22 | flimit | 数量限制 | int4 | 32 |  | √ | 0 | 数量限制 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 25 | fsupplierid | 商家 | int8 | 64 |  | √ | 0 | [商城供应商 bd_malsupplier](../basedata_files/bd_malsupplier.md) |
| 26 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 27 | ftype | 方案类型 | bpchar | 1 |  | √ | ' ' | 方案类型,枚举: 1 :楼层展示 2 :场景采购 3 :采购套餐 4 :商品监控 |
| 28 | fsort_in_category | 分类内排序 | bpchar | 1 |  | √ | '0' | 分类内排序 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | forderby | 排序 | varchar | 100 |  | √ | ' ' | 排序,枚举: sales :按销量从高到低 price_false :按价格从高到低 price_true :按价格从低到高 modifytime_false :按更新时间降序 |
| 32 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

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

## 商品推荐方案-多语言表 t_mal_prodobtain_l

- **表名称：** 商品推荐方案-多语言表
- **表名：** t_mal_prodobtain_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
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

## 商品信息-子表 t_mal_prodobtainentry

- **表名称：** 商品信息-子表
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
