# 基础数据映射关系-ai_basedatamapping

## 基础数据映射关系-主表 t_ai_basedatamapping

- **表名称：** 基础数据映射关系-主表
- **表名：** t_ai_basedatamapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourcebasedata | 源数据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fbyname | 按名称匹配 | bpchar | 1 |  | √ | '0' | 按名称匹配 |
| 13 | ffactorname | 源数据 | varchar | 250 |  | √ | ' ' | 源数据 |
| 14 | ffactorvalue | 源数据值 | varchar | 250 |  | √ | ' ' | 源数据值 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | ffactorvalue_base | 源数据_基础资料 | varchar | 250 |  | √ | ' ' | 源数据_基础资料 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 19 | ffactorvalue_asst | 源数据_辅助资料 | varchar | 250 |  | √ | ' ' | 源数据_辅助资料 |
| 20 | fbynumber | 按编码匹配 | bpchar | 1 |  | √ | '0' | 按编码匹配 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fbycustom | 自定义匹配 | bpchar | 1 |  | √ | '0' | 自定义匹配 |
| 24 | ftype | 单选按钮组 | varchar | 30 |  | √ | ' ' | 单选按钮组,枚举: plugin :使用插件映射 rule :使用规则映射 |
| 25 | fmappingplugin | 映射插件（实现IBaseDataMappingPlugin） | varchar | 200 |  |  | ' ' | 映射插件（实现IBaseDataMappingPlugin） |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fdestbasedata | 目标数据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ai_basedatamapping_master |  | fmasterid |
| 2 | t_ai_basedatamapping_pkey |  | fid |
| 3 | idx_t_ai_basedatamapping_createorg |  | fcreateorgid |
| 4 | idx_ai_basedatamapping |  | fdestbasedata |

---

## 基础数据映射关系-使用范围表 t_ai_basedatamapping_u

- **表名称：** 基础数据映射关系-使用范围表
- **表名：** t_ai_basedatamapping_u

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
| 1 | t_ai_basedatamapping_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_ai_basedatamapping_u_uo |  | fuseorgid |

---

## 基础数据映射关系-多语言表 t_ai_basedatamapping_l

- **表名称：** 基础数据映射关系-多语言表
- **表名：** t_ai_basedatamapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_basedatamapping_l_pkey |  | fpkid |
| 2 | idx_ai_basedatamapping_l |  | fid,flocaleid |

---

## 基础数据映射关系-使用范围位图表 t_ai_basedatamapping_m

- **表名称：** 基础数据映射关系-使用范围位图表
- **表名：** t_ai_basedatamapping_m

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
| 1 | pk_t_ai_basedatamapping_m |  | forgid |

---

## 映射数据-子表 t_ai_basedatamappingentry

- **表名称：** 映射数据-子表
- **表名：** t_ai_basedatamappingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbdinfoimport | 资料取值(导出) | varchar | 1000 |  | √ | ' ' | 资料取值(导出) |
| 3 | fdestdatamapping | 目标数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsrcdatamapping9 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fsrcdatamapping | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fsrcdatamapping8 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fsrcdatamapping7 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fsrcdatamapping6 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fassistsouce6 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 11 | fassistsouce7 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 12 | fassistsouce4 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 13 | fassistsouce5 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 14 | fassistsouce8 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 15 | fassistsouce9 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 16 | fsrcdatamapping5 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fsrcdatamapping4 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fsrcdatamapping3 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fsrcdatamapping2 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fsrcdatamapping1 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fassistsouce2 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fsrcdatamapping0 | 源数据 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fassistsouce3 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 25 | fassistsouce0 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 26 | fassistsouce1 | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_basedatamappingentry_pkey |  | fentryid |
| 2 | idx_ai_basedatamappingentry |  | fid,fdestdatamapping |

---

## 字段映射-子表 t_ai_basefieldmapentry

- **表名称：** 字段映射-子表
- **表名：** t_ai_basefieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentityid | 实体类型 | varchar | 50 |  | √ | ' ' | 实体类型 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 7 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_basefield_fid |  | fid |
| 2 | pk_t_ai_basefieldmapentry |  | fentryid |
