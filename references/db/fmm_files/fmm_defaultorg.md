# 生产组织设置-fmm_defaultorg

## 生产组织设置-使用范围表 t_fmm_defaultorg_u

- **表名称：** 生产组织设置-使用范围表
- **表名：** t_fmm_defaultorg_u

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
| 1 | idx_t_fmm_defaultorg_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_defaultorg_u |  | fdataid,fuseorgid |

---

## 生产组织设置-使用范围位图表 t_fmm_defaultorg_m

- **表名称：** 生产组织设置-使用范围位图表
- **表名：** t_fmm_defaultorg_m

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
| 1 | pk_t_fmm_defaultorg_m |  | forgid |

---

## 生产组织设置-多语言表 t_fmm_defaultorg_l

- **表名称：** 生产组织设置-多语言表
- **表名：** t_fmm_defaultorg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fmm_defaultorg_l_pkey |  | fid |
| 2 | idx_fmm_defaultorg_l_0 |  | fname |

---

## 生产组织设置-主表 t_fmm_defaultorg

- **表名称：** 生产组织设置-主表
- **表名：** t_fmm_defaultorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcallinwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcalendar | 默认生产日历 | int8 | 64 |  | √ | 0 | 生产日历 mpdm_calendar |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 7 | fissueplan | 配送计划 | bpchar | 1 |  | √ | '0' | 配送计划 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fclasssysteam | 默认班制 | int8 | 64 |  | √ | 0 | 班制 mpdm_classsystem |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fallocplan | 调拨计划 | bpchar | 1 |  | √ | '0' | 调拨计划 |
| 16 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcallinlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fcallinorgid | 调入库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fisoutsrcmft | 外协厂商 | bpchar | 1 |  | √ | '0' | 外协厂商 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_defaultorg_master |  | fmasterid |
| 2 | idx_t_fmm_defaultorg_createorg |  | fcreateorgid |
| 3 | t_fmm_defaultorg_pkey |  | fid |
| 4 | idx_fmm_defaultorg |  | fnumber |
