# 班制-mpdm_classsystem

## 单据体-子表 t_mpdm_classsystementry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_classsystementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworktime | 工作时长(小时) | numeric | 23 | 10 | √ | 0.0000000000 | 工作时长(小时) |
| 3 | fworkstarttime | 工作开始时间 | int8 | 64 |  | √ | 0 | 工作开始时间 |
| 4 | fworkshiftid | 班次ID | int8 | 64 |  | √ | 0 | 班次ID |
| 5 | fiscrossday | 跨天 | bpchar | 1 |  | √ | '0' | 跨天 |
| 6 | fwsentryid | 班次分录ID | int8 | 64 |  | √ | 0 | 班次分录ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fworkendtime | 工作结束时间 | int8 | 64 |  | √ | 0 | 工作结束时间 |
| 9 | fworkshift | 班次编码 | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_classsystementry |  | fid,fseq |
| 2 | t_mpdm_classsystementry_pkey |  | fentryid |

---

## 班制-主表 t_mpdm_classsystem

- **表名称：** 班制-主表
- **表名：** t_mpdm_classsystem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisinterday | fisinterday | bpchar | 1 |  | √ | '0' |  |
| 8 | fworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fclasssystemtime | 班制总时长(小时) | numeric | 23 | 10 | √ | 0.0000000000 | 班制总时长(小时) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 班制编码 | varchar | 60 |  | √ | ' ' | 班制编码 |
| 19 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_classsystem_pkey |  | fid |
| 2 | idx_t_mpdm_classsystem_master |  | fmasterid |
| 3 | idx_mpdm_classsystem_fnumber |  | fnumber,fcreateorgid |
| 4 | idx_t_mpdm_classsystem_createorg |  | fcreateorgid |

---

## 班制-使用范围表 t_mpdm_classsystem_u

- **表名称：** 班制-使用范围表
- **表名：** t_mpdm_classsystem_u

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
| 1 | t_mpdm_classsystem_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_classsystem_u_uo |  | fuseorgid |

---

## 班制-使用范围位图表 t_mpdm_classsystem_m

- **表名称：** 班制-使用范围位图表
- **表名：** t_mpdm_classsystem_m

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
| 1 | pk_t_mpdm_classsystem_m |  | forgid |

---

## 班制-多语言表 t_mpdm_classsystem_l

- **表名称：** 班制-多语言表
- **表名：** t_mpdm_classsystem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 班制名称 | varchar | 100 |  | √ | ' ' | 班制名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_classsystem_l |  | fid,flocaleid |
| 2 | t_mpdm_classsystem_l_pkey |  | fpkid |
