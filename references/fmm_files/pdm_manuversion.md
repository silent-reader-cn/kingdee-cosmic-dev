# 生产版本-pdm_manuversion

## 生产版本-多语言表 t_pdm_manuversion_l

- **表名称：** 生产版本-多语言表
- **表名：** t_pdm_manuversion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 生产版本名称 | varchar | 50 |  | √ | ' ' | 生产版本名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_manuversion_l_pkey |  | fpkid |
| 2 | idx_pdm_mvl_fid |  | fid,flocaleid |

---

## 生产版本-使用范围位图表 t_pdm_manuversion_m

- **表名称：** 生产版本-使用范围位图表
- **表名：** t_pdm_manuversion_m

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
| 1 | pk_t_pdm_manuversion_m |  | forgid |

---

## 生产版本-主表 t_pdm_manuversion

- **表名称：** 生产版本-主表
- **表名：** t_pdm_manuversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fenddate | 有效期范围.结束 | timestamp | 0 |  |  | null | 有效期范围.结束 |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fproductline | 生产线 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fbeginqty | 数量范围从 | numeric | 23 | 10 | √ | 0.0000000000 | 数量范围从 |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 18 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fbegindate | 有效期范围.开始 | timestamp | 0 |  |  | null | 有效期范围.开始 |
| 22 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 23 | fworkcenter | 工作中心编码 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fendqty | 数量至 | numeric | 23 | 10 | √ | 0.0000000000 | 数量至 |
| 26 | fisrepeat | 允许重复制造 | bpchar | 1 |  | √ | '0' | 允许重复制造 |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 生产版本编码 | varchar | 30 |  | √ | ' ' | 生产版本编码 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pdm_manuversion_createorg |  | fcreateorgid |
| 2 | t_pdm_manuversion_pkey |  | fid |
| 3 | idx_pdm_manuv_fbillno |  | fnumber |
| 4 | idx_t_pdm_manuversion_master |  | fmasterid |

---

## 单据体-子表 t_pdm_manuversionentry

- **表名称：** 单据体-子表
- **表名：** t_pdm_manuversionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fproject | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_manuversionentry_pkey |  | fentryid |
| 2 | idx_pdm_mve_fid |  | fid |

---

## 生产版本-使用范围表 t_pdm_manuversion_u

- **表名称：** 生产版本-使用范围表
- **表名：** t_pdm_manuversion_u

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
| 1 | t_pdm_manuversion_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_manuversion_u_uo |  | fuseorgid |

---

## 跟踪号-多选基础资料表 t_pdm_manuversiontrack

- **表名称：** 跟踪号-多选基础资料表
- **表名：** t_pdm_manuversiontrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_manuversiontrack_pkey |  | fpkid |
| 2 | idx_pdm_mvet_ftrack |  | fentryid |
