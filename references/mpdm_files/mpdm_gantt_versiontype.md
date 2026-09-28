# 版本类型配置-mpdm_gantt_versiontype

## 版本类型配置-使用范围表 t_mpdm_ganttvertype_u

- **表名称：** 版本类型配置-使用范围表
- **表名：** t_mpdm_ganttvertype_u

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
| 1 | pk_t_mpdm_ganttvertype_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_ganttvertype_u_uo |  | fuseorgid |

---

## 版本类型配置-使用范围位图表 t_mpdm_ganttvertype_m

- **表名称：** 版本类型配置-使用范围位图表
- **表名：** t_mpdm_ganttvertype_m

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
| 1 | pk_t_mpdm_ganttvertype_m |  | forgid |

---

## 版本类型配置-多语言表 t_mpdm_ganttvertype_l

- **表名称：** 版本类型配置-多语言表
- **表名：** t_mpdm_ganttvertype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类型名称 | varchar | 100 |  | √ | ' ' | 类型名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_ganttvertype_l |  | fid,flocaleid |
| 2 | pk_mpdm_ganttvertype_l |  | fpkid |

---

## 版本类型配置-主表 t_mpdm_ganttvertype

- **表名称：** 版本类型配置-主表
- **表名：** t_mpdm_ganttvertype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitycondid | 实体 | varchar | 50 |  | √ | '0' | 主实体对象 bos_entityobject |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | filtervalue | 过滤条件 | bpchar | 1 |  | √ | '1' | 过滤条件,枚举: 0 :当前 1 :全部 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdefault | 默认版本 | bpchar | 1 |  | √ | '0' | 默认版本 |
| 10 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | forgpageid | 适用页面 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fversionpageid | 版本对应页面 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 20 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fdraggable | 整体移动 | bpchar | 1 |  | √ | '0' | 整体移动 |
| 23 | fnumber | 类型编码 | varchar | 30 |  | √ | ' ' | 类型编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fadjustable | 单项移动 | bpchar | 1 |  | √ | '0' | 单项移动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_ganttvertype |  | fid |
| 2 | idx_t_mpdm_ganttvertype_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_ganttvertype_master |  | fmasterid |
| 4 | idx_mpdm_ganttvertype_fnum |  | fnumber |
