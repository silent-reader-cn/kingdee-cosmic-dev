# 系统公告-srm_notice_system

## 系统公告-主表 t_pur_component

- **表名称：** 系统公告-主表
- **表名：** t_pur_component

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组件类型 | int8 | 64 |  | √ | 0 | 门户组件类型 srm_compgroup |
| 3 | forgfield | forgfield | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fitemclass | fitemclass | varchar | 100 |  | √ | ' ' |  |
| 6 | fmulilangtextfield | fmulilangtextfield | varchar | 100 |  | √ | ' ' |  |
| 7 | fitembrands | fitembrands | varchar | 100 |  | √ | ' ' |  |
| 8 | fsaleunit | fsaleunit | int8 | 64 |  | √ | 0 |  |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fcurrencyprice | fcurrencyprice | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置,枚举: 1 :是 0 :否 |
| 18 | fmateril | fmateril | varchar | 100 |  | √ | ' ' |  |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 22 | fdelay | fdelay | int8 | 64 |  | √ | 0 |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdescription | fdescription | varchar | 200 |  | √ | ' ' |  |
| 25 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fspeed | fspeed | int8 | 64 |  | √ | 0 |  |
| 27 | fenable | 可用状态 | varchar | 80 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fisautoplay | fisautoplay | bpchar | 1 |  | √ | ' ' |  |
| 29 | fcurrencyfield | fcurrencyfield | int8 | 64 |  | √ | 0 |  |
| 30 | fnumber | 组件编码 | varchar | 80 |  | √ | ' ' | 组件编码 |
| 31 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_component_fnumber |  | fnumber |
| 2 | idx_pur_component_fctime |  | fcreatetime |
| 3 | idx_t_pur_component_createorg |  | fcreateorgid |
| 4 | t_pur_component_pkey |  | fid |
| 5 | idx_t_pur_component_master |  | fmasterid |

---

## 单据体-子表 t_pur_compentry

- **表名称：** 单据体-子表
- **表名：** t_pur_compentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 3 | faddress | faddress | varchar | 100 |  | √ | ' ' |  |
| 4 | ftheme | ftheme | bpchar | 1 |  | √ | ' ' |  |
| 5 | finfomation | finfomation | varchar | 100 |  | √ | ' ' |  |
| 6 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | protal | protal | varchar | 100 |  | √ | ' ' |  |
| 9 | fprotal | fprotal | varchar | 100 |  | √ | ' ' |  |
| 10 | ftitle | ftitle | varchar | 100 |  | √ | ' ' |  |
| 11 | fpicture | fpicture | varchar | 512 |  | √ | ' ' |  |
| 12 | finformation | finformation | varchar | 512 |  | √ | ' ' |  |
| 13 | furl | furl | varchar | 200 |  | √ | ' ' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_compentry_fid_fseq |  | fid,fseq |
| 2 | t_pur_compentry_pkey |  | fentryid |

---

## 系统公告-使用范围表 t_pur_component_u

- **表名称：** 系统公告-使用范围表
- **表名：** t_pur_component_u

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
| 1 | t_pur_component_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pur_component_u_uo |  | fuseorgid |

---

## 系统公告-使用范围位图表 t_pur_component_m

- **表名称：** 系统公告-使用范围位图表
- **表名：** t_pur_component_m

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
| 1 | pk_t_pur_component_m |  | forgid |

---

## 系统公告-多语言表 t_pur_component_l

- **表名称：** 系统公告-多语言表
- **表名：** t_pur_component_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组件名称 | varchar | 100 |  | √ | ' ' | 组件名称 |
| 3 | fmulilangtextfield | fmulilangtextfield | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_component_l_flid |  | fid,flocaleid |
| 2 | pk_pur_component_l_fid |  | fpkid |
