# 集成云设置-er_isc_setting

## 单据体-子表 t_er_isc_settingentry

- **表名称：** 单据体-子表
- **表名：** t_er_isc_settingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | value | varchar | 255 |  | √ | ' ' | value |
| 3 | fkey | key | varchar | 255 |  | √ | ' ' | key |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdesc | 描述 | varchar | 800 |  | √ | ' ' | 描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_isc_settingentry_pkey |  | fentryid |

---

## 集成云设置-使用范围位图表 t_er_isc_setting_m

- **表名称：** 集成云设置-使用范围位图表
- **表名：** t_er_isc_setting_m

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
| 1 | pk_t_er_isc_setting_m |  | forgid |

---

## 集成云设置-多语言表 t_er_isc_setting_l

- **表名称：** 集成云设置-多语言表
- **表名：** t_er_isc_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_isc_setting_l |  | fpkid |
| 2 | idx_iscsetting_l_fid_flocaleid |  | fid,flocaleid |

---

## 集成云设置-使用范围表 t_er_isc_setting_u

- **表名称：** 集成云设置-使用范围表
- **表名：** t_er_isc_setting_u

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
| 1 | t_er_isc_setting_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_er_isc_setting_u_uo |  | fuseorgid |

---

## 集成云设置-主表 t_er_isc_setting

- **表名称：** 集成云设置-主表
- **表名：** t_er_isc_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrcsys | 源系统 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 4 | fdbtype | eas数据库 | varchar | 30 |  | √ | ' ' | eas数据库,枚举: 0 :MS SQLSERVER 2 :ORACLE 1 :DB2 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ftarsys | 目标系统 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_isc_setting_master |  | fmasterid |
| 2 | idx_er_isc_setting_number |  | fnumber |
| 3 | idx_t_er_isc_setting_createorg |  | fcreateorgid |
| 4 | t_er_isc_setting_pkey |  | fid |
