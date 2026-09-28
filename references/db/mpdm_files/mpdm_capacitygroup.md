# 能力项组-mpdm_capacitygroup

## 能力项组-主表 t_mpdm_capacitygroup

- **表名称：** 能力项组-主表
- **表名：** t_mpdm_capacitygroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 能力项组类别 | int8 | 64 |  | √ | 0 | [能力项组类别 mpdm_capacitygrouptype](../mpdm_files/mpdm_capacitygrouptype.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 能力项组编码 | varchar | 30 |  | √ | ' ' | 能力项组编码 |
| 18 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_capacitygroup |  | fid |
| 2 | idx_t_mpdm_capacitygroup_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_capacitygroup_master |  | fmasterid |
| 4 | idx_mpdm_capacitygroup_fnum |  | fnumber |

---

## 能力项-子表 t_mpdm_capagroupet

- **表名称：** 能力项-子表
- **表名：** t_mpdm_capagroupet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fcapacitytype | 能力项类别 | varchar | 50 |  | √ | ' ' | 能力项类别,枚举: A :固定值 B :计算值 |
| 4 | fcapacityname | 能力项名称 | varchar | 50 |  | √ | ' ' | 能力项名称 |
| 5 | fcapacitynumber | 能力项编码 | varchar | 50 |  | √ | ' ' | 能力项编码 |
| 6 | fcapacitycalen | 能力公式（英文） | varchar | 255 |  | √ | ' ' | 能力公式（英文） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fworkunits | 工时单位 | varchar | 50 |  | √ | ' ' | 工时单位,枚举: A :秒 B :分 C :时 D :天 |
| 9 | fcapacitycal | 能力公式配置 | varchar | 255 |  | √ | ' ' | 能力公式配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_capagroupet_fid |  | fid |
| 2 | pk_t_mpdm_capagroupet |  | fentryid |

---

## 能力项组-多语言表 t_mpdm_capacitygroup_l

- **表名称：** 能力项组-多语言表
- **表名：** t_mpdm_capacitygroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 能力项组名称 | varchar | 50 |  | √ | ' ' | 能力项组名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_capacitygroup_l |  | fpkid |
| 2 | idx_mpdm_capagroupl_fid |  | fid |

---

## 能力项组-使用范围位图表 t_mpdm_capacitygroup_m

- **表名称：** 能力项组-使用范围位图表
- **表名：** t_mpdm_capacitygroup_m

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
| 1 | pk_t_mpdm_capacitygroup_m |  | forgid |

---

## 能力项组-使用范围表 t_mpdm_capacitygroup_u

- **表名称：** 能力项组-使用范围表
- **表名：** t_mpdm_capacitygroup_u

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
| 1 | pk_t_mpdm_capacitygroup_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_capacitygroup_u_uo |  | fuseorgid |
