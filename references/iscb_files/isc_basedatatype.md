# 基础资料映射（废弃）-isc_basedatatype

## 基础资料映射（废弃）-主表 t_isc_basedatatype

- **表名称：** 基础资料映射（废弃）-主表
- **表名：** t_isc_basedatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgroupid | 元数据对照 | int8 | 64 |  | √ | 0 | 集成业务对象（废弃） isc_entity |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织单元 | varchar | 20 |  | √ | ' ' | 业务单元 bos_org |
| 6 | fsourcesystem | 来源系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 7 | fcommon | 是否通用 | varchar | 30 |  | √ | ' ' | 是否通用,枚举: 1 :是 0 :否 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | fpreset | int8 | 64 |  | √ | 0 |  |
| 13 | fbasedatafilter | 基础资料过滤条件 | varchar | 510 |  | √ | ' ' | 基础资料过滤条件 |
| 14 | fmappingtype | 数据匹配规则 | varchar | 30 |  | √ | ' ' | 数据匹配规则,枚举: 0 :编码 1 :名称 |
| 15 | ftargetsystem | 目标系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 16 | fenable | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fbaseentity | 金蝶云苍穹实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_basedatatype_pkey |  | fid |
| 2 | idx_isc_basedt_fnum |  | fnumber |

---

## 自动集成-子表 t_isc_basedatatypeentry_b

- **表名称：** 自动集成-子表
- **表名：** t_isc_basedatatypeentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 基础资料 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsrcname | 源数据名称 | varchar | 100 |  | √ | ' ' | 源数据名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsrcnumber | 源数据编码 | varchar | 100 |  | √ | ' ' | 源数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_basedatatypeentry_b_pkey |  | fentryid |
| 2 | idx_isc_bdte_b_fid |  | fid |

---

## 规则自动匹配-子表 t_isc_basedatatypeentry_a

- **表名称：** 规则自动匹配-子表
- **表名：** t_isc_basedatatypeentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 基础资料 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsrcname | 源数据名称 | varchar | 100 |  | √ | ' ' | 源数据名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsrcnumber | 源数据编码 | varchar | 100 |  | √ | ' ' | 源数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_basedatatypeentry_a_pkey |  | fentryid |
| 2 | idx_isc_bdte_a_fid |  | fid |

---

## 手工指定-多语言表 t_isc_basedatatypeentry_l

- **表名称：** 手工指定-多语言表
- **表名：** t_isc_basedatatypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdescname | 目标数据名称 | varchar | 100 |  | √ | ' ' | 目标数据名称 |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_bdye_l_fentyid |  | fentryid,flocaleid |
| 2 | t_isc_basedatatypeentry_l_pkey |  | fpkid |

---

## 基础资料映射（废弃）-多语言表 t_isc_basedatatype_l

- **表名称：** 基础资料映射（废弃）-多语言表
- **表名：** t_isc_basedatatype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_basedatatype_l_pkey |  | fpkid |
| 2 | idx_isc_basedt_l_fid |  | fid,flocaleid |

---

## 手工指定-子表 t_isc_basedatatypeentry

- **表名称：** 手工指定-子表
- **表名：** t_isc_basedatatypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestnumber | 目标数据编码 | varchar | 100 |  | √ | ' ' | 目标数据编码 |
| 3 | fbasedataid | 基础资料 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsrcname | 源数据名称 | varchar | 100 |  | √ | ' ' | 源数据名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsrcnumber | 源数据编码 | varchar | 100 |  | √ | ' ' | 源数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_basedte_fid |  | fid |
| 2 | t_isc_basedatatypeentry_pkey |  | fentryid |
