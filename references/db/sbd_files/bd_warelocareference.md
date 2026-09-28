# 仓库仓位关系-bd_warelocareference

## 仓库仓位关系-多语言表 t_bd_warehouseentry_l

- **表名称：** 仓库仓位关系-多语言表
- **表名：** t_bd_warehouseentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_warehouseentry_l |  | fpkid |
| 2 | idx_bd_warehouseentry_l |  | fentryid,flocaleid |

---

## 仓库仓位关系-使用范围位图表 t_bd_warehouseentry_m

- **表名称：** 仓库仓位关系-使用范围位图表
- **表名：** t_bd_warehouseentry_m

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
| 1 | pk_t_bd_warehouseentry_m |  | forgid |

---

## 仓库仓位关系-使用范围表 t_bd_warehouseentry_u

- **表名称：** 仓库仓位关系-使用范围表
- **表名：** t_bd_warehouseentry_u

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
| 1 | pk_t_bd_warehouseentry_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_warehouseentry_u_uo |  | fuseorgid |

---

## 仓库仓位关系-主表 t_bd_warehouseentry

- **表名称：** 仓库仓位关系-主表
- **表名：** t_bd_warehouseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 仓库编码 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | flocationid | 仓位编码 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 4 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 5 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 6 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 7 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 11 | fisdefaultloc | 默认仓位 | bpchar | 1 |  | √ | '0' | 默认仓位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_warehouseentry_createorg |  | fcreateorgid |
| 2 | t_bd_warehouseentry_pkey |  | fentryid |
| 3 | idx_bd_warehouseentry_fid |  | fid |
| 4 | idx_t_bd_warehouseentry_master |  | fmasterid |
