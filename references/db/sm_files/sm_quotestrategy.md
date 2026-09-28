# 取价策略-sm_quotestrategy

## 取价策略-使用范围表 t_plat_quotestrategy_u

- **表名称：** 取价策略-使用范围表
- **表名：** t_plat_quotestrategy_u

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
| 1 | pk_t_plat_quotestrategy_u |  | fdataid,fuseorgid |
| 2 | idx_t_plat_quotestrategy_u_uo |  | fuseorgid |

---

## 方案排序单据体-子表 t_plat_quotestentry

- **表名称：** 方案排序单据体-子表
- **表名：** t_plat_quotestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpreconditiondesc | fpreconditiondesc | varchar | 2000 |  |  | null |  |
| 3 | fiscontinuequote | 是否继续取价 | bpchar | 1 |  | √ | '0' | 是否继续取价 |
| 4 | fpreconditionjson | 条件(JSON) | varchar | 512 |  |  | null | 条件(JSON) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fquoteschemeid | 取价方案 | int8 | 64 |  | √ | 0 | 取价方案 plat_quotescheme |
| 7 | fprecondition | 条件(JSON)（废弃） | varchar | 2000 |  |  | null | 条件(JSON)（废弃） |
| 8 | fterminationsigndesc | 取到价格终止 | varchar | 200 |  |  | null | 取到价格终止 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fterminationsign | 取价终止字段标识 | varchar | 200 |  |  | null | 取价终止字段标识 |
| 11 | fpreconditionjson_tag | 条件(JSON)_详情 | text | 0 |  |  | null | 条件(JSON)_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_plat_quotestentry_pkey |  | fentryid |
| 2 | idx_plat_quotestentry_fid |  | fid |

---

## 取价策略-多语言表 t_plat_quotestrategy_l

- **表名称：** 取价策略-多语言表
- **表名：** t_plat_quotestrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_quotest_l_fid |  | fid,flocaleid |
| 2 | t_plat_quotestrategy_l_pkey |  | fpkid |

---

## 取价策略-使用范围位图表 t_plat_quotestrategy_m

- **表名称：** 取价策略-使用范围位图表
- **表名：** t_plat_quotestrategy_m

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
| 1 | pk_t_plat_quotestrategy_m |  | forgid |

---

## 取价策略-主表 t_plat_quotestrategy

- **表名称：** 取价策略-主表
- **表名：** t_plat_quotestrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpricecoverrule | 价格覆盖规则 | varchar | 5 |  | √ | 'A' | 价格覆盖规则,枚举: A :不覆盖已有价格 B :覆盖已有价格 |
| 12 | fheadquotebill | 取价单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 21 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | '7' | 控制策略,枚举: 5 :全局共享 7 :私有 |
| 22 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plat_quotestrategy_master |  | fmasterid |
| 2 | t_plat_quotestrategy_pkey |  | fid |
| 3 | idx_t_plat_quotestrategy_createorg |  | fcreateorgid |
| 4 | idx_plat_quotest_fnumber |  | fnumber |

---

## 前置条件-子表 t_plat_quoteconentry

- **表名称：** 前置条件-子表
- **表名：** t_plat_quoteconentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqsprecondition | 条件(JSON) | varchar | 512 |  |  | null | 条件(JSON) |
| 3 | fqspreconditiondesc | fqspreconditiondesc | varchar | 2000 |  |  | null |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fquotebill | 取价单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fqsprecondition_tag | 条件(JSON)_详情 | text | 0 |  |  | null | 条件(JSON)_详情 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_quoteconentry_fid |  | fid |
| 2 | pk_t_plat_quoteconentry |  | fentryid |
