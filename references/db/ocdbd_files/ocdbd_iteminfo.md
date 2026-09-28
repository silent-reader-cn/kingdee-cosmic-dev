# 商品信息-ocdbd_iteminfo

## 商品信息-多语言表 t_ocdbd_item_l

- **表名称：** 商品信息-多语言表
- **表名：** t_ocdbd_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fshorttitle | 商品简介 | varchar | 510 |  | √ | ' ' | 商品简介 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fmodelnum | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_l |  | fpkid |
| 2 | idx_ocdbd_iteml_fname |  | fname |
| 3 | idx_ocdbd_iteml_fidflid |  | fid,flocaleid |

---

## 商品信息-分表 t_ocdbd_item_c

- **表名称：** 商品信息-分表
- **表名：** t_ocdbd_item_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fitemorgstatus | 组织上架状态 | bpchar | 1 |  | √ | '0' | 组织上架状态,枚举: 0 :上架 1 :下架 |
| 4 | fitemchannelstatus | 渠道上架状态 | bpchar | 1 |  | √ | '0' | 渠道上架状态,枚举: 0 :上架 1 :下架 |
| 5 | fcreatechannelid | 创建渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 6 | fretailprice | 参考零售价 | numeric | 23 | 10 | √ | 0 | 参考零售价 |
| 7 | fbarcodenumber | 条形码 | varchar | 80 |  | √ | ' ' | 条形码 |
| 8 | fsupplerid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fiskneadprice | 要货订单到销售订单揉价处理 | bpchar | 1 |  | √ | '0' | 要货订单到销售订单揉价处理 |
| 11 | foperationmodel | 经营模式 | bpchar | 1 |  | √ | '1' | 经营模式,枚举: 0 :联营 1 :普通 |
| 12 | fonlineprice | 参考线上价 | numeric | 23 | 10 | √ | 0 | 参考线上价 |
| 13 | fenablelot | 启用批号 | bpchar | 1 |  | √ | '0' | 启用批号 |
| 14 | fminorderqty | 最小订货量 | numeric | 23 | 10 | √ | 0 | 最小订货量 |
| 15 | fisdelivery | 是否配送 | bpchar | 1 |  | √ | '0' | 是否配送 |
| 16 | fthumbnail | 缩略图 | varchar | 500 |  | √ | ' ' | 缩略图 |
| 17 | fdescription_tag | 商品信息_详情 | text | 0 |  |  | null | 商品信息_详情 |
| 18 | fkneadprice | 揉价价格 | numeric | 23 | 10 | √ | 0 | 揉价价格 |
| 19 | fsellingprice | 参考供货价 | numeric | 23 | 10 | √ | 0 | 参考供货价 |
| 20 | fsaletype | 售卖方式 | bpchar | 1 |  | √ | ' ' | 售卖方式,枚举: 1 :计重 2 :计个 |
| 21 | fisspecifykneadprice | 指定价格揉价 | bpchar | 1 |  | √ | '0' | 指定价格揉价 |
| 22 | fapprovedate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fstockunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fisinstall | 是否安装 | bpchar | 1 |  | √ | '0' | 是否安装 |
| 26 | fpicture5 | 图册 | varchar | 500 |  | √ | ' ' | 图册 |
| 27 | fonlyoutandinrequest | 序列号仅出入库控制 | bpchar | 1 |  | √ | '0' | 序列号仅出入库控制 |
| 28 | forderunitid | 分销订货单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fpicture4 | 图册 | varchar | 500 |  | √ | ' ' | 图册 |
| 30 | fpicture3 | 图册 | varchar | 500 |  | √ | ' ' | 图册 |
| 31 | fpicture2 | 图册 | varchar | 500 |  | √ | ' ' | 图册 |
| 32 | fpicture1 | 图册 | varchar | 500 |  | √ | ' ' | 图册 |
| 33 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fretailunitid | 零售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | fdescription | 商品信息 | varchar | 255 |  | √ | ' ' | 商品信息 |
| 37 | fenableserial | 启用序列号管理 | bpchar | 1 |  | √ | '0' | 启用序列号管理 |
| 38 | fitembrandid | 商品品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 39 | forderbatchqty | 订货批量 | numeric | 23 | 10 | √ | 0 | 订货批量 |
| 40 | fmemberprice | 参考会员价 | numeric | 23 | 10 | √ | 0 | 参考会员价 |
| 41 | fbarcodeid | 条形码ID | int8 | 64 |  | √ | 0 | 条形码ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_c |  | fid |
| 2 | idx_ocdbd_itemc_fbarcode |  | fbarcodeid,fbarcodenumber |

---

## 商品信息-使用范围表 t_ocdbd_item_u

- **表名称：** 商品信息-使用范围表
- **表名：** t_ocdbd_item_u

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
| 1 | idx_t_ocdbd_item_u_uo |  | fuseorgid |
| 2 | pk_t_ocdbd_item_u |  | fdataid,fuseorgid |

---

## 商品信息-主表 t_ocdbd_item

- **表名称：** 商品信息-主表
- **表名：** t_ocdbd_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | flengthunitid | 长度单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | flength | 长度 | numeric | 23 | 10 | √ | 0 | 长度 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fgrossweight | 毛重 | numeric | 23 | 10 | √ | 0 | 毛重 |
| 7 | fnetweight | 净重 | numeric | 23 | 10 | √ | 0 | 净重 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fconversionfor | 辅助单位换算 | varchar | 30 |  | √ | ' ' | 辅助单位换算,枚举: A :互相换算 B :仅计量单位换算辅助单位 C :仅辅助单位换算计量单位 D :互不换算 |
| 11 | feasnum | 第三方系统编码 | varchar | 80 |  | √ | ' ' | 第三方系统编码 |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fmaterial | 对应物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | ftaxclasscodeid | 税收分类编码 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 16 | fassistunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fweightunitid | 重量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fmaterialmasterid | 物料Fmasterid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 22 | fminpacknum | 最小包装数 | numeric | 23 | 10 | √ | 0 | 最小包装数 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 24 | fgoodsbelong | 商品归属 | bpchar | 1 |  | √ | '0' | 商品归属,枚举: 0 :内部 1 :外部 |
| 25 | fitemspuid | 商品SPU | int8 | 64 |  | √ | 0 | 商品SPU ocdbd_spu |
| 26 | fitemstatus | 商品状态 | bpchar | 1 |  | √ | '0' | 商品状态,枚举: 0 :上架 1 :下架 |
| 27 | fsaleunitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fsearchkey | 搜索关键字 | varchar | 255 |  | √ | ' ' | 搜索关键字 |
| 29 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 30 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 33 | fcreatetype | 商品来源 | bpchar | 1 |  | √ | 'A' | 商品来源,枚举: A :手工新增 B :物料下推 D :导入新增 E :WebAPI新增 |
| 34 | fshorttitle | 商品简介 | varchar | 510 |  | √ | ' ' | 商品简介 |
| 35 | fvolumnunitid | 体积单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | freferenceprice | 参考价格 | numeric | 23 | 10 | √ | 0 | 参考价格 |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 39 | fitemtypeid | 商品类型 | int8 | 64 |  | √ | 0 | 商品类型 bd_itemtype |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fproductmanagerid | 产品经理 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fvolume | 体积 | numeric | 23 | 10 | √ | 0 | 体积 |
| 44 | fitemattributeid | 商品属性 | int8 | 64 |  | √ | 0 | 商品属性 ocdbd_itemattribute |
| 45 | fwidth | 宽度 | numeric | 23 | 10 | √ | 0 | 宽度 |
| 46 | fcostprice | 成本单价 | numeric | 23 | 10 | √ | 0 | 成本单价 |
| 47 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 48 | fsortnumber | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 49 | fheight | 高度 | numeric | 23 | 10 | √ | 0 | 高度 |
| 50 | fmodelnum | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdbd_item_master |  | fmasterid |
| 2 | idx_ocdbd_item_fsk |  | fsearchkey |
| 3 | idx_t_ocdbd_item_createorg |  | fcreateorgid |
| 4 | pk_ocdbd_item |  | fid |
| 5 | idx_ocdbd_item_mcn |  | fmodifytime,fcreatetime,fnumber |
| 6 | idx_ocdbd_item_fno |  | fnumber |

---

## 商品分类单据体-子表 t_ocdbd_itemclassentry

- **表名称：** 商品分类单据体-子表
- **表名：** t_ocdbd_itemclassentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsclassid | 分类编码 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | fclassstandardid | 分类标准编码 | int8 | 64 |  | √ | 0 | 商品分类标准 bd_goodsclassstandard |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_itemclassentry |  | fentryid |
| 2 | idx_ocdbd_icentry_fid |  | fid |

---

## 关联子实体-子表 t_ocdbd_item_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocdbd_item_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_item_lk_fk |  | fid |
| 2 | pk_ocdbd_item_lk |  | fpkid |

---

## 商品SPU单据体-子表 t_ocdbd_itemspuentry

- **表名称：** 商品SPU单据体-子表
- **表名：** t_ocdbd_itemspuentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fspuspecid | SPU规格 | int8 | 64 |  | √ | 0 | SPU规格 ocdbd_spu_spec |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fspuspecvalueid | SPU规格值 | int8 | 64 |  | √ | 0 | SPU规格值 ocdbd_spu_specvalue |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemspuentry_fid |  | fid |
| 2 | pk_ocdbd_itemspuentry |  | fentryid |

---

## 规格参数单据体-子表 t_ocdbd_item_model

- **表名称：** 规格参数单据体-子表
- **表名：** t_ocdbd_item_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodelkey | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fitemmodel | 商品参数 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodelvalue | 属性 | varchar | 100 |  | √ | ' ' | 属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_model |  | fentryid |
| 2 | idx_ocdbd_im_fid |  | fid |
