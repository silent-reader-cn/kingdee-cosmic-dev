# 预留方案（旧）（废弃）-sbs_reserve_st

## 预留方案（旧）（废弃）-使用范围位图表 t_sbs_reserve_st_m

- **表名称：** 预留方案（旧）（废弃）-使用范围位图表
- **表名：** t_sbs_reserve_st_m

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
| 1 | pk_t_sbs_reserve_st_m |  | forgid |

---

## 预留方案（旧）（废弃）-多语言表 t_sbs_reserve_st_l

- **表名称：** 预留方案（旧）（废弃）-多语言表
- **表名：** t_sbs_reserve_st_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sbs_reserve_st_l_pkey |  | fpkid |
| 2 | idx_sbs_r_st_flid |  | fid,flocaleid |
| 3 | idx_sbs_r_st_fname |  | fname |

---

## 预留方案（旧）（废弃）-主表 t_sbs_reserve_st

- **表名称：** 预留方案（旧）（废弃）-主表
- **表名：** t_sbs_reserve_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequirestockorgname | 需求库存组织 | varchar | 50 |  | √ | ' ' | 需求库存组织 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frequirestockdateno | 需求日期编码 | varchar | 50 |  | √ | ' ' | 需求日期编码 |
| 5 | frequirestockdatename | 需求日期 | varchar | 50 |  | √ | ' ' | 需求日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdatastatus | 状态 | bpchar | 1 |  | √ | '2' | 状态,枚举: 0 :禁用 1 :启用 2 :暂存 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fstockmatch | 可用库存匹配条件 | varchar | 2000 |  | √ | ' ' | 可用库存匹配条件 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | frequirestockorgno | 需求库存组织编码 | varchar | 50 |  | √ | ' ' | 需求库存组织编码 |
| 18 | fstockseq | 可用库存预留顺序 | varchar | 2000 |  | √ | ' ' | 可用库存预留顺序 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 21 | fstockfilter | 可用库存过滤条件 | varchar | 2000 |  | √ | ' ' | 可用库存过滤条件 |
| 22 | freservefilter | 预留条件 | varchar | 2000 |  | √ | ' ' | 预留条件 |
| 23 | frequirebill | 需求单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fbillsetting | 单据设置方案 | int8 | 64 |  | √ | 0 | [字段映射（旧）（废弃） sbs_reserve_colmap](../sbs_files/sbs_reserve_colmap.md) |
| 26 | fisautoreserve | 自动预留方案 | bpchar | 1 |  | √ | '0' | 自动预留方案 |
| 27 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 28 | fautoreservemsg | 库存不足处理方式 | bpchar | 1 |  | √ | 'A' | 库存不足处理方式,枚举: A :提示不预留 B :尽量预留不提示 C :尽量预留且提示 D :提示且操作失败 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sbs_reserve_st_createorg |  | fcreateorgid |
| 2 | t_sbs_reserve_st_pkey |  | fid |
| 3 | idx_sbs_r_st_foid |  | forgid |
| 4 | idx_sbs_r_st_frb |  | frequirebill,fisautoreserve |
| 5 | idx_t_sbs_reserve_st_master |  | fmasterid |
| 6 | idx_sbs_r_st_fno |  | fnumber |

---

## 预留方案（旧）（废弃）-使用范围表 t_sbs_reserve_st_u

- **表名称：** 预留方案（旧）（废弃）-使用范围表
- **表名：** t_sbs_reserve_st_u

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
| 1 | t_sbs_reserve_st_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_sbs_reserve_st_u_uo |  | fuseorgid |
