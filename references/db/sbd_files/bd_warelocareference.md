# 仓库仓位关系-bd_warelocareference

## 仓库仓位关系-多语言表 t_bd_warehouseentry_l

- **表名称：** 仓库仓位关系-多语言表
- **表名：** t_bd_warehouseentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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

## 仓库仓位关系-主表 t_bd_warehouseentry

- **表名称：** 仓库仓位关系-主表
- **表名：** t_bd_warehouseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 仓库编码 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 8 | fisdefaultloc | 默认仓位 | bpchar | 1 |  | √ | '0' | 默认仓位 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | flocationid | 仓位编码 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | flocationstatus | 使用状态 | bpchar | 1 |  |  | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fenbale | fenbale | bpchar | 1 |  | √ | '1' |  |
| 17 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 18 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

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
