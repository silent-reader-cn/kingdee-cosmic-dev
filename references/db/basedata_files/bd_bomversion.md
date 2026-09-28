# BOM版本-bd_bomversion

## BOM版本-主表 t_bd_bomversion

- **表名称：** BOM版本-主表
- **表名：** t_bd_bomversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fecnbillno | 工程变更单编号 | varchar | 60 |  | √ | ' ' | 工程变更单编号 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fecodate | ECO执行时间 | timestamp | 0 |  |  | null | ECO执行时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fversionname | fversionname | int8 | 64 |  | √ | 0 |  |
| 18 | fbomversionrule | BOM版本规则 | int8 | 64 |  | √ | 0 | [BOM版本规则 bd_bomversionrule](../basedata_files/bd_bomversionrule.md) |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fremark | 备注 | varchar | 60 |  | √ | ' ' | 备注 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 23 | fenableorid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 128 |  |  | ' ' | 编码 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdisableorid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bomversion_createorg |  | fcreateorgid |
| 2 | idx_bd_bomversion |  | fnumber,fcreateorgid |
| 3 | idx_t_bd_bomversion_master |  | fmasterid |
| 4 | t_bd_bomversion_pkey |  | fid |
| 5 | idx_bd_bomversion_material |  | fmaterialid |

---

## BOM版本-使用范围表 t_bd_bomversion_u

- **表名称：** BOM版本-使用范围表
- **表名：** t_bd_bomversion_u

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
| 1 | idx_t_bd_bomversion_u_uo |  | fuseorgid |
| 2 | t_bd_bomversion_u_pkey |  | fdataid,fuseorgid |

---

## BOM版本-使用范围位图表 t_bd_bomversion_m

- **表名称：** BOM版本-使用范围位图表
- **表名：** t_bd_bomversion_m

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
| 1 | pk_t_bd_bomversion_m |  | forgid |

---

## BOM版本-多语言表 t_bd_bomversion_l

- **表名称：** BOM版本-多语言表
- **表名：** t_bd_bomversion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 版本 | varchar | 100 |  | √ | ' ' | 版本 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_bomversion_l_pkey |  | fpkid |
| 2 | idx_bd_bomversion_l |  | fid,flocaleid |
