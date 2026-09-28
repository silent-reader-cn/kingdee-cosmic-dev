# 质检业务组-qcbd_qualityorg

## 质检业务组-使用范围表 t_qcbd_qualityorgtpl_u

- **表名称：** 质检业务组-使用范围表
- **表名：** t_qcbd_qualityorgtpl_u

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
| 1 | idx_t_qcbd_qualityorgtpl_u_uo |  | fuseorgid |
| 2 | pk_t_qcbd_qualityorgtpl_u |  | fdataid,fuseorgid |

---

## 单据体-子表 t_qcbd_qualityorgentry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_qualityorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperatorname | 业务员名称 | varchar | 50 |  | √ | ' ' | 业务员名称 |
| 3 | foperatorid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | finvalid | 失效 | varchar | 5 |  | √ | '0' | 失效 |
| 5 | fopergrptype | 业务组类型 | varchar | 30 |  | √ | ' ' | 业务组类型,枚举: CGZ :采购组 KCZ :库存组 XSZ :销售组 JHZ :计划组 ZJZ :质检组 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foperatornumber | 业务员编码 | varchar | 50 |  | √ | ' ' | 业务员编码 |
| 8 | fopergrpnumber | 业务组编码 | varchar | 50 |  | √ | ' ' | 业务组编码 |
| 9 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qualityorgentry_fid |  | fid |
| 2 | pk_qcbd_qualityorgentry |  | fentryid |

---

## 单据体-多语言表 t_qcbd_qualityorgentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_qcbd_qualityorgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperatorname | 业务员名称 | varchar | 50 |  | √ | ' ' | 业务员名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qualityorgentry_l |  | fentryid,flocaleid |
| 2 | pk_qcbd_qualityorgentry_l |  | fpkid |

---

## 质检业务组-多语言表 t_qcbd_qualityorgtpl_l

- **表名称：** 质检业务组-多语言表
- **表名：** t_qcbd_qualityorgtpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_qualityorgtpl_l |  | fpkid |
| 2 | idx_qualityorgtpl_l |  | fid,flocaleid |

---

## 质检业务组-使用范围位图表 t_qcbd_qualityorgtpl_m

- **表名称：** 质检业务组-使用范围位图表
- **表名：** t_qcbd_qualityorgtpl_m

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
| 1 | pk_t_qcbd_qualityorgtpl_m |  | forgid |

---

## 质检业务组-主表 t_qcbd_qualityorgtpl

- **表名称：** 质检业务组-主表
- **表名：** t_qcbd_qualityorgtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | foperatorgrouptype | 业务组类型 | varchar | 5 |  | √ | ' ' | 业务组类型,枚举: CGZ :采购组 KCZ :库管组 XSZ :销售组 JHZ :计划组 ZJZ :质检组 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcbd_qualityorgtpl_createorg |  | fcreateorgid |
| 2 | uidx_qcbd_qualityorgtpl_billno |  | fnumber |
| 3 | pk_qcbd_qualityorgtpl |  | fid |
| 4 | idx_t_qcbd_qualityorgtpl_master |  | fmasterid |

---

## 质检主管-多选基础资料表 t_qcbd_qualorg_manager

- **表名称：** 质检主管-多选基础资料表
- **表名：** t_qcbd_qualorg_manager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_qualorg_manager |  | fpkid |
