# 时间段-fmm_industrytimerel

## 时间段-主表 t_fmm_industrytimerel

- **表名称：** 时间段-主表
- **表名：** t_fmm_industrytimerel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 时间段 | varchar | 255 |  | √ | ' ' | 时间段 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 18 | fperiod | 业务期间（封存） | int8 | 64 |  | √ | 0 | 业务期间（封存） |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 22 | fworkshifts | 班次（封存） | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_industrytimerel |  | fid |
| 2 | idx_t_fmm_industrytimerel_createorg |  | fcreateorgid |
| 3 | idx_t_fmm_industrytimerel_master |  | fmasterid |
| 4 | idx_t_fmm_industrytimerel_mst |  | fmasterid |
| 5 | idx_t_fmm_industrytimerel_org |  | fcreateorgid |

---

## 时间段信息-子表 t_fmm_itrelentry

- **表名称：** 时间段信息-子表
- **表名：** t_fmm_itrelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworktime | 工作时长(小时) | numeric | 23 | 10 | √ | 0 | 工作时长(小时) |
| 3 | fworkstarttime | 工作开始时间 | int8 | 64 |  | √ | 0 | 工作开始时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fworkendtime | 工作结束时间 | int8 | 64 |  | √ | 0 | 工作结束时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_itrelentry |  | fentryid |
| 2 | idx_fmm_itrelentry_fk |  | fid |

---

## 时间段-多语言表 t_fmm_industrytimerel_l

- **表名称：** 时间段-多语言表
- **表名：** t_fmm_industrytimerel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 时间段 | varchar | 255 |  | √ | ' ' | 时间段 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_industrytimerel_l |  | fpkid |
| 2 | idx_fmm_industrytimerel_l |  | fid,flocaleid |

---

## 时间段-使用范围表 t_fmm_industrytimerel_u

- **表名称：** 时间段-使用范围表
- **表名：** t_fmm_industrytimerel_u

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
| 1 | idx_t_fmm_industrytimerel_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_industrytimerel_u |  | fdataid,fuseorgid |
