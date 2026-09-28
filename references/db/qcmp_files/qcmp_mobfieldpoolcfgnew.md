# 移动质检字段池配置-qcmp_mobfieldpoolcfgnew

## 单据体-子表 t_qcmp_cfglistpoolentry

- **表名称：** 单据体-子表
- **表名：** t_qcmp_cfglistpoolentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeylistcol | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 3 | fnamelistcol | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fissysfield | 是否系统预设字段 | bpchar | 1 |  | √ | '0' | 是否系统预设字段 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcmp_cfgpool_fid |  | fid |
| 2 | idx_qcmp_cfgpool_fseq |  | fseq |
| 3 | pk_t_qcmp_cfglistpoolentry |  | fentryid |

---

## 移动质检字段池配置-多语言表 t_qcmp_mobfieldcfgpool_l

- **表名称：** 移动质检字段池配置-多语言表
- **表名：** t_qcmp_mobfieldcfgpool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcmp_mobfieldcfgpool_l |  | fpkid |
| 2 | idx_qcbd_cfgpool_fname |  | fname |
| 3 | idx_qcbd_cfgpool_fid |  | fid |

---

## 移动质检字段池配置-主表 t_qcmp_mobfieldcfgpool

- **表名称：** 移动质检字段池配置-主表
- **表名：** t_qcmp_mobfieldcfgpool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fbillobj | 单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 10 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | '5' |  |
| 13 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 17 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 19 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcmp_mobfieldcfgpool_createorg |  | fcreateorgid |
| 2 | pk_t_qcmp_mobfieldcfgpool |  | fid |
| 3 | idx_t_qcmp_mobfieldcfgpool_master |  | fmasterid |
| 4 | idx_qcmp_cfgpool_billobj |  | fbillobj |
