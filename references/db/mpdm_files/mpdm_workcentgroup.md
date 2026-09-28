# 工作中心类别(废弃)-mpdm_workcentgroup

## 工作中心类别(废弃)-使用范围表 t_mpdm_workcentgroup_u

- **表名称：** 工作中心类别(废弃)-使用范围表
- **表名：** t_mpdm_workcentgroup_u

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
| 1 | idx_t_mpdm_workcentgroup_u_uo |  | fuseorgid |
| 2 | t_mpdm_workcentgroup_u_pkey |  | fdataid,fuseorgid |

---

## 工作中心类别(废弃)-多语言表 t_mpdm_workcentgroup_l

- **表名称：** 工作中心类别(废弃)-多语言表
- **表名：** t_mpdm_workcentgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工作中心类别名称 | varchar | 100 |  | √ | ' ' | 工作中心类别名称 |
| 3 | ffullname | 长名称 | varchar | 100 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workcentgroup_l_pkey |  | fpkid |
| 2 | idx_mpdm_workcentgroup_l |  | fid,flocaleid |

---

## 工作中心类别(废弃)-使用范围位图表 t_mpdm_workcentgroup_m

- **表名称：** 工作中心类别(废弃)-使用范围位图表
- **表名：** t_mpdm_workcentgroup_m

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
| 1 | pk_t_mpdm_workcentgroup_m |  | forgid |

---

## 工作中心类别(废弃)-主表 t_mpdm_workcentgroup

- **表名称：** 工作中心类别(废弃)-主表
- **表名：** t_mpdm_workcentgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fremake | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fabilitygroup | 能力类别 | int8 | 64 |  | √ | 0 | 基础资料模板 mpdm_abilitytype |
| 15 | fparentid | 上级类别 | int8 | 64 |  | √ | 0 | 工作中心类别(废弃) mpdm_workcentgroup |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | flongnumber | 长编码 | varchar | 100 |  | √ | ' ' | 长编码 |
| 18 | fproabilitymust | 生产能力/资源必录 | bpchar | 1 |  | √ | '0' | 生产能力/资源必录 |
| 19 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 21 | factivitystamust | 活动量标准值必录 | bpchar | 1 |  | √ | '0' | 活动量标准值必录 |
| 22 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 工作中心类别编码 | varchar | 60 |  | √ | ' ' | 工作中心类别编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_workcentgroup_createorg |  | fcreateorgid |
| 2 | idx_t_mpdm_workcentgroup_master |  | fmasterid |
| 3 | t_mpdm_workcentgroup_pkey |  | fid |
| 4 | idx_mpdm_workcentgroup |  | fnumber,fcreateorgid |
