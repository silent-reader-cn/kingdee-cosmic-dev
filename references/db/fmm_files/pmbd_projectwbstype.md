# 项目WBS类型-pmbd_projectwbstype

## 项目WBS类型-主表 t_pmbd_projectwbstype

- **表名称：** 项目WBS类型-主表
- **表名：** t_pmbd_projectwbstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fschshowmode | 进度显示方式 | varchar | 5 |  | √ | ' ' | 进度显示方式,枚举: 1 :百分比 2 :数量 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fschctrlmode | 进度控制方式 | varchar | 5 |  | √ | ' ' | 进度控制方式,枚举: 1 :业务完成 2 :任务汇报 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fbustype | 业务类型 | varchar | 5 |  | √ | ' ' | 业务类型,枚举: 1 :设计 2 :采购 3 :委外 4 :生产 5 :文档 6 :其他 |
| 18 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | WBS类型编码 | varchar | 30 |  | √ | ' ' | WBS类型编码 |
| 20 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmbd_projpe_fcreatetime |  | fcreatetime |
| 2 | idx_pmbd_projpe_fnumber |  | fnumber |
| 3 | idx_t_pmbd_projectwbstype_master |  | fmasterid |
| 4 | pk_pmbd_projectwbstype |  | fid |
| 5 | idx_t_pmbd_projectwbstype_createorg |  | fcreateorgid |

---

## 项目WBS类型-多语言表 t_pmbd_projectwbstype_l

- **表名称：** 项目WBS类型-多语言表
- **表名：** t_pmbd_projectwbstype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | WBS类型名称 | varchar | 50 |  | √ | ' ' | WBS类型名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmbd_projectwbstype_l |  | fpkid |
| 2 | idx_pmbd_projpel_fid |  | fid,flocaleid |
| 3 | idx_pmbd_projpel_fname |  | fname |

---

## 项目WBS类型-使用范围位图表 t_pmbd_projectwbstype_m

- **表名称：** 项目WBS类型-使用范围位图表
- **表名：** t_pmbd_projectwbstype_m

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
| 1 | pk_t_pmbd_projectwbstype_m |  | forgid |

---

## 项目WBS类型-使用范围表 t_pmbd_projectwbstype_u

- **表名称：** 项目WBS类型-使用范围表
- **表名：** t_pmbd_projectwbstype_u

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
| 1 | pk_t_pmbd_projectwbstype_u |  | fdataid,fuseorgid |
| 2 | idx_t_pmbd_projectwbstype_u_uo |  | fuseorgid |
