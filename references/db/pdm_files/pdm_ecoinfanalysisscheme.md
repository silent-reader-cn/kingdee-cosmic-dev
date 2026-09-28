# 工程变更影响查询方案-pdm_ecoinfanalysisscheme

## 单据体-子表 t_pdm_eiaschemeentity

- **表名称：** 单据体-子表
- **表名：** t_pdm_eiaschemeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: |
| 3 | fsubeia | 子项物料影响分析 | varchar | 3 |  | √ | ' ' | 子项物料影响分析 |
| 4 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 8 | fmaineia | 主产品影响分析 | varchar | 3 |  | √ | ' ' | 主产品影响分析 |
| 9 | fbillno | 业务单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_eiaschemeentity |  | fentryid |
| 2 | idx_pdm_eco_eiaentity |  | fid,fseq |

---

## 工程变更影响查询方案-主表 t_pdm_eiascheme

- **表名称：** 工程变更影响查询方案-主表
- **表名：** t_pdm_eiascheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 21 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 23 | fonlychecked | 只展示参与分析的单据 | bpchar | 1 |  | √ | ' ' | 只展示参与分析的单据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pdm_eiascheme_createorg |  | fcreateorgid |
| 2 | pk_t_pdm_eiascheme |  | fid |
| 3 | idx_t_pdm_eiascheme_master |  | fmasterid |
| 4 | idx_pdm_eco_eia_fnumber |  | fnumber |

---

## 工程变更影响查询方案-多语言表 t_pdm_eiascheme_l

- **表名称：** 工程变更影响查询方案-多语言表
- **表名：** t_pdm_eiascheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_eiascheme_l |  | fpkid |
| 2 | idx_t_pdm_eiascheme_l |  | fid,flocaleid |

---

## 工程变更影响查询方案-使用范围表 t_pdm_eiascheme_u

- **表名称：** 工程变更影响查询方案-使用范围表
- **表名：** t_pdm_eiascheme_u

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
| 1 | pk_t_pdm_eiascheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_eiascheme_u_uo |  | fuseorgid |
