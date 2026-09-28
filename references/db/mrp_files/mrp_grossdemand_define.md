# 毛需求定义-mrp_grossdemand_define

## 毛需求定义-使用范围表 t_mrp_grossdemand_define_u

- **表名称：** 毛需求定义-使用范围表
- **表名：** t_mrp_grossdemand_define_u

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
| 1 | idx_t_mrp_grossdemand_define_u_uo |  | fuseorgid |
| 2 | pk_t_mrp_grossdemand_define_u |  | fdataid,fuseorgid |

---

## 毛需求定义-使用范围位图表 t_mrp_grossdemand_define_m

- **表名称：** 毛需求定义-使用范围位图表
- **表名：** t_mrp_grossdemand_define_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_grossdemand_define_m |  | forgid |

---

## 毛需求定义-多语言表 t_mrp_grossdemand_define_l

- **表名称：** 毛需求定义-多语言表
- **表名：** t_mrp_grossdemand_define_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmrpdemandtype | MRP需求类别 | varchar | 50 |  | √ | ' ' | MRP需求类别 |
| 4 | fmrpsupplytype | MRP供应类别 | varchar | 50 |  | √ | ' ' | MRP供应类别 |
| 5 | fsupplysluggishtype | 供应呆滞类别 | varchar | 50 |  | √ | ' ' | 供应呆滞类别 |
| 6 | fsafetystock | 安全库存标识 | varchar | 50 |  | √ | ' ' | 安全库存标识 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_grossdemand_define_l |  | fpkid |
| 2 | idx_mrp_grossdemand_define_l |  | fid,flocaleid |

---

## 毛需求定义分录-子表 t_mrp_gdm_define_entry

- **表名称：** 毛需求定义分录-子表
- **表名：** t_mrp_gdm_define_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsetoffsettingid | 预测冲减定义id | int8 | 64 |  | √ | 0 | 预测冲减定义id |
| 3 | fsetofftype | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: a :预测数量 b :未发货订单 c :已发货订单 d :预测剩余数量 |
| 4 | fsetoffname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_gdm_define_entry |  | fid,fseq |
| 2 | pk_t_mrp_gdm_define_entry |  | fentryid |

---

## 毛需求定义-主表 t_mrp_grossdemand_define

- **表名称：** 毛需求定义-主表
- **表名：** t_mrp_grossdemand_define

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fcodetype | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 18 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 19 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_grossdemand_define |  | fid |
| 2 | idx_t_mrp_grossdemand_define_master |  | fmasterid |
| 3 | idx_mrp_grossdemand_define |  | fnumber |
| 4 | idx_t_mrp_grossdemand_define_createorg |  | fcreateorgid |
