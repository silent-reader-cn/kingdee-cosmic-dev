# 实体字段映射-mrp_billfieldtransfer

## 实体字段映射-主表 t_mrp_bftransfer

- **表名称：** 实体字段映射-主表
- **表名：** t_mrp_bftransfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstrategyclass | fstrategyclass | varchar | 30 |  | √ | ' ' |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrcbill | 源实体 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdestentity | fdestentity | varchar | 30 |  | √ | ' ' |  |
| 7 | fissysteminsert | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fdestbill | 目标实体 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fsrcbillentity | fsrcbillentity | varchar | 30 |  | √ | ' ' |  |
| 16 | fismatchdim | 匹配维度 | bpchar | 1 |  | √ | '0' | 匹配维度 |
| 17 | fversion | 版本 | varchar | 30 |  | √ | ' ' | 版本 |
| 18 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fusetype | fusetype | varchar | 5 |  | √ | ' ' |  |
| 23 | flargetextfield_tag | 目标实体条件存储_详情 | text | 0 |  |  | null | 目标实体条件存储_详情 |
| 24 | ffieldtype | 实体字段类型 | varchar | 50 |  | √ | ' ' | 实体字段类型,枚举: A :mds B :mrp C :sfc |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | flargetextfield | 目标实体条件存储 | varchar | 255 |  | √ | ' ' | 目标实体条件存储 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_bftransfer |  | fnumber,fcreateorgid |
| 2 | pk_t_mrp_bftransfer |  | fid |
| 3 | idx_t_mrp_bftransfer_master |  | fmasterid |
| 4 | idx_t_mrp_bftransfer_createorg |  | fcreateorgid |

---

## 实体字段映射-使用范围位图表 t_mrp_bftransfer_m

- **表名称：** 实体字段映射-使用范围位图表
- **表名：** t_mrp_bftransfer_m

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
| 1 | pk_t_mrp_bftransfer_m |  | forgid |

---

## 实体字段映射-多语言表 t_mrp_bftransfer_l

- **表名称：** 实体字段映射-多语言表
- **表名：** t_mrp_bftransfer_l

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
| 1 | pk_t_mrp_bftransfer_l |  | fpkid |
| 2 | idx_mrp_bftransfer_l |  | fid,flocaleid |

---

## 实体字段映射-使用范围表 t_mrp_bftransfer_u

- **表名称：** 实体字段映射-使用范围表
- **表名：** t_mrp_bftransfer_u

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
| 1 | idx_t_mrp_bftransfer_u_uo |  | fuseorgid |
| 2 | t_mrp_bftransfer_u_pkey |  | fdataid,fuseorgid |

---

## 字段映射-子表 t_mrp_billtranferentry

- **表名称：** 字段映射-子表
- **表名：** t_mrp_billtranferentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalculateexc_tag | 计算公式_详情 | text | 0 |  |  | null | 计算公式_详情 |
| 3 | fdestentityflag | 目标单实体标识 | varchar | 50 |  | √ | ' ' | 目标单实体标识 |
| 4 | fdestfieldflag | 目标单字段标识 | varchar | 50 |  | √ | ' ' | 目标单字段标识 |
| 5 | fdestfieldname | 目标单字段名称 | varchar | 255 |  | √ | ' ' | 目标单字段名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsourceentityflag | 源单实体标识 | varchar | 50 |  | √ | ' ' | 源单实体标识 |
| 8 | fsourcefieldname | 源单字段名称 | varchar | 255 |  | √ | ' ' | 源单字段名称 |
| 9 | fcalculateexc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 10 | fsourcefieldflag | 源单字段标识 | varchar | 50 |  | √ | ' ' | 源单字段标识 |
| 11 | fcalculatetext | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fconverttype | 映射类型 | varchar | 30 |  | √ | ' ' | 映射类型,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 3 :常量 4 :其他 5 :弹性匹配 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_billtranferentry |  | fentryid |
| 2 | idx_mrp_billtranferentry |  | fid,fseq |
