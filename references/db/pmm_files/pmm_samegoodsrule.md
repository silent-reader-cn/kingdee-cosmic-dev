# 运营监控策略-pmm_samegoodsrule

## 监控维度-子表 t_mal_dimensionentry

- **表名称：** 监控维度-子表
- **表名：** t_mal_dimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimpricerange | 价格区间影响监控规则 | bpchar | 1 |  | √ | '0' | 价格区间影响监控规则 |
| 3 | fmuldimruleid | 运营监控规则 | int8 | 64 |  | √ | 0 | [运营监控规则 pmm_operaterule](../pmm_files/pmm_operaterule.md) |
| 4 | fmuldimautodown | 自动下架 | bpchar | 1 |  | √ | '0' | 自动下架 |
| 5 | fmuldimthreshold | 阈值 | varchar | 50 |  | √ | ' ' | 阈值 |
| 6 | fmuldimendprice | 价格上限（<） | numeric | 23 | 10 | √ | 0 | 价格上限（<） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmuldimstartprice | 价格下限（>=） | numeric | 23 | 10 | √ | 0 | 价格下限（>=） |
| 9 | fmuldimcontroltype | 控制方式 | bpchar | 1 |  | √ | '0' | 控制方式,枚举: 1 :提示 2 :禁止 3 :不控制 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdimension | 监控维度 | int8 | 64 |  | √ | 0 | [商品推荐方案 pmm_product_obtain](../pmm_files/pmm_product_obtain.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_dimensionentry_fid |  | fid |
| 2 | pk_t_mal_dimensionentry |  | fentryid |

---

## 同款规则-多选基础资料表 t_mal_samerule

- **表名称：** 同款规则-多选基础资料表
- **表名：** t_mal_samerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [全文检索映射属性 pbd_esmapping_property](../pbd_files/pbd_esmapping_property.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_samerule |  | fpkid |
| 2 | idx_mal_samerule_fid |  | fentryid,fbasedataid |

---

## 同款分录-子表 t_mal_sameentry

- **表名称：** 同款分录-子表
- **表名：** t_mal_sameentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartprice | 价格下限（>=） | numeric | 23 | 10 | √ | 0 | 价格下限（>=） |
| 3 | fissameautodown | 自动下架 | bpchar | 1 |  | √ | '0' | 自动下架 |
| 4 | fcontroltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: 1 :提示 2 :禁止 3 :不控制 |
| 5 | fendprice | 价格上限（<） | numeric | 23 | 10 | √ | 0 | 价格上限（<） |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsamethreshold | 阈值 | varchar | 50 |  | √ | ' ' | 阈值 |
| 8 | fpriceruleid | 运营监控规则 | int8 | 64 |  | √ | 0 | [运营监控规则 pmm_operaterule](../pmm_files/pmm_operaterule.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_sameentry |  | fentryid |
| 2 | idx_mal_sameentry_fentryid |  | fid |

---

## 运营监控策略-多语言表 t_mal_samegoodsrule_l

- **表名称：** 运营监控策略-多语言表
- **表名：** t_mal_samegoodsrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mal_samerule_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_samegoodsrule_l |  | fpkid |

---

## 单据体-子表 t_mal_sameruleentry

- **表名称：** 单据体-子表
- **表名：** t_mal_sameruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_sameruleentry |  | fentryid |
| 2 | idx_mal_sameruleentry_fid |  | fid |

---

## 运营监控策略-主表 t_mal_samegoodsrule

- **表名称：** 运营监控策略-主表
- **表名：** t_mal_samegoodsrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fispricesameprice | 价格区间影响监控规则 | bpchar | 1 |  |  | '0' | 价格区间影响监控规则 |
| 6 | fiscomparesameprice | 价格区间影响监控规则 | bpchar | 1 |  |  | '0' | 价格区间影响监控规则 |
| 7 | fproductobtainid | 不参与价格监控商品范围 | int8 | 64 |  | √ | 0 | [商品推荐方案 pmm_product_obtain](../pmm_files/pmm_product_obtain.md) |
| 8 | fissamekind | 开启自动识别同款 | bpchar | 1 |  | √ | '0' | 开启自动识别同款 |
| 9 | fisautocompare | 自动生成比价快照 | bpchar | 1 |  |  | '0' | 自动生成比价快照 |
| 10 | fdim | 启用多个监控维度 | bpchar | 1 |  | √ | '0' | 启用多个监控维度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fisgoodsmonitor | 开启商品监控 | bpchar | 1 |  |  | '0' | 开启商品监控 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fpriceproductobtainid | 不参与价格监控商品范围 | int8 | 64 |  | √ | 0 | [商品推荐方案 pmm_product_obtain](../pmm_files/pmm_product_obtain.md) |
| 19 | fissimilar | 开启同类商品推荐 | bpchar | 1 |  | √ | '0' | 开启同类商品推荐 |
| 20 | ffields | 同款规则字段范围 | varchar | 512 |  | √ | ' ' | 同款规则字段范围,枚举: brandname :品牌名称 brandnumber :品牌编码 centralpurtype :采购模式 classname :分类编码 classnumber :分类名称 model :规格型号 name :商品名称 number :商品编码 source :电商平台 suppliername :供应商名称 unitname :计量单位.名称 barcode :商品编码.商品条形码 materielnumber :商品编码.对应ERP物料.编码 materielname :商品编码.对应ERP物料.名称 |
| 21 | fgoodssort | 同款商品排序 | varchar | 20 |  | √ | ' ' | 同款商品排序,枚举: sales_false :按销量从高到低 sales_true :按销量从低到高 price_false :按价格从高到低 price_true :按价格从低到高 modifytime_true :按更新时间升序 modifytime_false :按更新时间降序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_samerule_fsort |  | fgoodssort |
| 2 | pk_t_mal_samegoodsrule |  | fid |

---

## 监控规则分录-子表 t_mal_pricemonitorentry

- **表名称：** 监控规则分录-子表
- **表名：** t_mal_pricemonitorentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmonitorstartprice | 价格下限（>=） | numeric | 23 | 10 | √ | 0 | 价格下限（>=） |
| 3 | fmonitorcontroltype | 控制方式 | bpchar | 1 |  | √ | '0' | 控制方式,枚举: 1 :提示 2 :禁止 3 :不控制 |
| 4 | fmonitorissameautodown | 自动下架 | bpchar | 1 |  | √ | '0' | 自动下架 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmonitorpriceruleid | 运营监控规则 | int8 | 64 |  | √ | 0 | [运营监控规则 pmm_operaterule](../pmm_files/pmm_operaterule.md) |
| 7 | fmonitorendprice | 价格上限（<） | numeric | 23 | 10 | √ | 0 | 价格上限（<） |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmonitorsamethreshold | 阈值 | varchar | 50 |  | √ | ' ' | 阈值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_pricemonitorentry |  | fentryid |
| 2 | idx_mal_pricemonentry_fid |  | fid |
