# 商品SPU-ocdbd_spu

## 商品SPU-主表 t_ocdbd_spu

- **表名称：** 商品SPU-主表
- **表名：** t_ocdbd_spu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | fname | SPU名称 | varchar | 100 |  | √ | ' ' | SPU名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | feditorid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcreatechannelid | 创建渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fspubelong | SPU归属 | bpchar | 1 |  | √ | '0' | SPU归属,枚举: 0 :内部 1 :外部 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fedittime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fthumbnail | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | SPU编码 | varchar | 80 |  | √ | ' ' | SPU编码 |
| 21 | fdesc | SPU备注 | varchar | 255 |  | √ | ' ' | SPU备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_spu_number |  | fnumber |
| 2 | pk_ocdbd_spu |  | fid |

---

## 规格组合值单据体-子表 t_ocdbd_spuentry_map

- **表名称：** 规格组合值单据体-子表
- **表名：** t_ocdbd_spuentry_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspumapname | 规格组合值 | varchar | 1000 |  | √ | ' ' | 规格组合值 |
| 3 | fspumapids | 规则组合值idmap | varchar | 1000 |  | √ | ' ' | 规则组合值idmap |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fspumapnumber | 规格组合值编码 | varchar | 1000 |  | √ | ' ' | 规格组合值编码 |
| 7 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fitemid | 对应商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_spuentrymap_fid |  | fid |
| 2 | pk_ocdbd_spuentry_map |  | fentryid |
| 3 | idx_ocdbd_spuentrymap_itemid |  | fitemid |

---

## 商品SPU-多语言表 t_ocdbd_spu_l

- **表名称：** 商品SPU-多语言表
- **表名：** t_ocdbd_spu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | SPU名称 | varchar | 100 |  | √ | ' ' | SPU名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fdesc | SPU备注 | varchar | 255 |  | √ | ' ' | SPU备注 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_spul_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_spu_l |  | fpkid |

---

## 规格单据体-子表 t_ocdbd_spuentry_spec

- **表名称：** 规格单据体-子表
- **表名：** t_ocdbd_spuentry_spec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fspecid | spu规格编码 | int8 | 64 |  | √ | 0 | [SPU规格 ocdbd_spu_spec](../ocdbd_files/ocdbd_spu_spec.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_spuentryspec_specid |  | fspecid |
| 2 | idx_ocdbd_spuentry_spec |  | fid |
| 3 | pk_ocdbd_spuentry_spec |  | fentryid |

---

## 规格值子单据体-子表 t_ocdbd_spudetail_spec

- **表名称：** 规格值子单据体-子表
- **表名：** t_ocdbd_spudetail_spec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 3 | fspecvalueid | spu规格值编码 | int8 | 64 |  | √ | 0 | [SPU规格值 ocdbd_spu_specvalue](../ocdbd_files/ocdbd_spu_specvalue.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_spudetail_spec |  | fdetailid |
| 2 | idx_ocdbd_spudetailspec_eid |  | fentryid |

---

## 规格组合值子单据体-子表 t_ocdbd_spudetail_map

- **表名称：** 规格组合值子单据体-子表
- **表名：** t_ocdbd_spudetail_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmapspecvalueid | spu规格值 | int8 | 64 |  | √ | 0 | [SPU规格值 ocdbd_spu_specvalue](../ocdbd_files/ocdbd_spu_specvalue.md) |
| 2 | fmapspecid | spu规格 | int8 | 64 |  | √ | 0 | [SPU规格 ocdbd_spu_spec](../ocdbd_files/ocdbd_spu_spec.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_spudetailmap_specid |  | fmapspecvalueid,fmapspecid |
| 2 | pk_ocdbd_spudetail_map |  | fdetailid |

---

## 商品分类单据体-子表 t_ocdbd_spu_itemclass

- **表名称：** 商品分类单据体-子表
- **表名：** t_ocdbd_spu_itemclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 3 | fclassstandardid | 商品分类标准 | int8 | 64 |  | √ | 0 | [商品分类标准 bd_goodsclassstandard](../gmc_files/bd_goodsclassstandard.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_spu_itemclass |  | fentryid |
| 2 | idx_ocdbd_spu_itemclass_fid |  | fid |
