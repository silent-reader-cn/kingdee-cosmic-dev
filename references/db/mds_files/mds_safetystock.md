# 安全库存-mds_safetystock

## 安全库存-主表 t_mds_safetystock

- **表名称：** 安全库存-主表
- **表名：** t_mds_safetystock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmon6 | 当月+6 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+6 |
| 3 | fmon7 | 当月+7 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+7 |
| 4 | fmon8 | 当月+8 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+8 |
| 5 | fmon9 | 当月+9 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+9 |
| 6 | fsafetysource | 安全库存数据源 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 7 | fmon11 | 当月+11 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+11 |
| 8 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmon10 | 当月+10 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+10 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsafetyrats | 安全库存比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 安全库存比例（%） |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fsaftytype | 安全库存类型 | varchar | 30 |  | √ | ' ' | 安全库存类型,枚举: B :动态安全库存 C :动态安全库存（天） A :固定安全库存 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fmon0 | 当月 | numeric | 23 | 10 | √ | 0.0000000000 | 当月 |
| 21 | fmon1 | 当月+1 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+1 |
| 22 | fmon2 | 当月+2 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+2 |
| 23 | fmon3 | 当月+3 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+3 |
| 24 | fmon4 | 当月+4 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+4 |
| 25 | feffectttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 26 | fmon5 | 当月+5 | numeric | 23 | 10 | √ | 0.0000000000 | 当月+5 |
| 27 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 32 | floseeffecttime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 33 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_safetystock_master |  | fmasterid |
| 2 | idx_t_mds_safetystock_createorg |  | fcreateorgid |
| 3 | idx_mds_safetystock |  | fnumber,fcreateorgid |
| 4 | idx_mds_safetystock_m |  | fmaterialid |
| 5 | t_mds_safetystock_pkey |  | fid |

---

## 安全库存-多语言表 t_mds_safetystock_l

- **表名称：** 安全库存-多语言表
- **表名：** t_mds_safetystock_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mds_safetystock_l_pkey |  | fpkid |
| 2 | idx_mds_safetystock_l |  | fid,flocaleid |

---

## 安全库存-使用范围位图表 t_mds_safetystock_m

- **表名称：** 安全库存-使用范围位图表
- **表名：** t_mds_safetystock_m

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
| 1 | pk_t_mds_safetystock_m |  | forgid |

---

## 安全库存-使用范围表 t_mds_safetystock_u

- **表名称：** 安全库存-使用范围表
- **表名：** t_mds_safetystock_u

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
| 1 | pk_t_mds_safetystock_u |  | fdataid,fuseorgid |
| 2 | idx_t_mds_safetystock_u_uo |  | fuseorgid |
