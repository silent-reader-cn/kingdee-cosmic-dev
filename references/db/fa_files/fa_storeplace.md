# 存放地点-fa_storeplace

## 存放地点-使用范围表 t_fa_storeplace_u

- **表名称：** 存放地点-使用范围表
- **表名：** t_fa_storeplace_u

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
| 1 | t_fa_storeplace_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_fa_storeplace_u_uo |  | fuseorgid |

---

## 存放地点-多语言表 t_fa_storeplace_l

- **表名称：** 存放地点-多语言表
- **表名：** t_fa_storeplace_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | ffulladdress | 地址全称 | varchar | 500 |  |  | ' ' | 地址全称 |
| 4 | ffullname | ffullname | varchar | 100 |  |  | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 7 | fdetailaddress | 详细地址 | varchar | 500 |  |  | ' ' | 详细地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_spl_fid_flocaleid |  | fid,flocaleid |
| 2 | t_fa_storeplace_l_pkey |  | fpkid |

---

## 存放地点-使用范围位图表 t_fa_storeplace_m

- **表名称：** 存放地点-使用范围位图表
- **表名：** t_fa_storeplace_m

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
| 1 | pk_t_fa_storeplace_m |  | forgid |

---

## 存放地点-主表 t_fa_storeplace

- **表名称：** 存放地点-主表
- **表名：** t_fa_storeplace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 存放地点分组 | int8 | 64 |  | √ | 0 | 存放地点分组 fa_storeplace_group |
| 5 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fstrativedivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | ffulladdress | 地址全称 | varchar | 500 |  |  | ' ' | 地址全称 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 20 | fdetailaddress | 详细地址 | varchar | 255 |  |  | ' ' | 详细地址 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_storeplace_pkey |  | fid |
| 2 | idx_sp_fnumber |  | fnumber |
| 3 | idx_t_fa_storeplace_master |  | fmasterid |
| 4 | idx_t_fa_storeplace_createorg |  | fcreateorgid |
