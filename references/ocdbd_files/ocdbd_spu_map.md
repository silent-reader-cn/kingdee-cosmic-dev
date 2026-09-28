# SPU规格组合值-ocdbd_spu_map

## SPU规格组合值-主表 t_ocdbd_spuentry_map

- **表名称：** SPU规格组合值-主表
- **表名：** t_ocdbd_spuentry_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | spu | int8 | 64 |  | √ | 0 | 商品SPU ocdbd_spu |
| 2 | fspumapname | 规格组合值 | varchar | 1000 |  | √ | ' ' | 规格组合值 |
| 3 | fspumapids | 规则组合值idmap | varchar | 1000 |  | √ | ' ' | 规则组合值idmap |
| 4 | fauxptyid | 对应商品辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fspumapnumber | 规格组合值编码 | varchar | 1000 |  | √ | ' ' | 规格组合值编码 |
| 7 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fitemid | 对应商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

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

## 单据体-子表 t_ocdbd_spudetail_map

- **表名称：** 单据体-子表
- **表名：** t_ocdbd_spudetail_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmapspecvalueid | spu规格值 | int8 | 64 |  | √ | 0 | SPU规格值 ocdbd_spu_specvalue |
| 2 | fmapspecid | spu规格 | int8 | 64 |  | √ | 0 | SPU规格 ocdbd_spu_spec |
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
