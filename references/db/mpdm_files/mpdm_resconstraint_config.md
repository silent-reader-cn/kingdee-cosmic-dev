# 资源约束配置-mpdm_resconstraint_config

## 资源约束配置-子表 t_mpdm_constraintentry

- **表名称：** 资源约束配置-子表
- **表名：** t_mpdm_constraintentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetobjectid | 约束对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fcategory | 约束类别 | varchar | 50 |  | √ | ' ' | 约束类别,枚举: A :检修设备型号 B :产品 C :客户 D :其他 |
| 4 | ffilterconfig | 约束维度后台存储数据 | varchar | 255 |  | √ | ' ' | 约束维度后台存储数据 |
| 5 | ffilterconfig_tag | 约束维度后台存储数据_详情 | text | 0 |  |  | null | 约束维度后台存储数据_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: and :并且 or :或者 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdimension | 约束维度 | varchar | 255 |  | √ | ' ' | 约束维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_constraintentry |  | fentryid |
| 2 | idx_mpdm_constraintentry_fs |  | fid,fseq |

---

## 资源约束配置-主表 t_mpdm_resconstraint

- **表名称：** 资源约束配置-主表
- **表名：** t_mpdm_resconstraint

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 资源约束名称 | varchar | 50 |  | √ | ' ' | 资源约束名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 资源约束编码 | varchar | 30 |  | √ | ' ' | 资源约束编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_resconstraint |  | fid |
| 2 | idx_t_mpdm_resconstraint_master |  | fmasterid |
| 3 | idx_t_mpdm_resconstraint_createorg |  | fcreateorgid |
| 4 | idx_t_mpdm_resconstraint_fnum |  | fnumber |

---

## 资源约束配置-使用范围表 t_mpdm_resconstraint_u

- **表名称：** 资源约束配置-使用范围表
- **表名：** t_mpdm_resconstraint_u

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
| 1 | pk_t_mpdm_resconstraint_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_resconstraint_u_uo |  | fuseorgid |

---

## 资源约束配置-多语言表 t_mpdm_resconstraint_l

- **表名称：** 资源约束配置-多语言表
- **表名：** t_mpdm_resconstraint_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源约束名称 | varchar | 50 |  | √ | ' ' | 资源约束名称 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_resconstraint_l |  | fpkid |
| 2 | idx_mpdm_resconstraint_l |  | fid,flocaleid |

---

## 资源约束配置-使用范围位图表 t_mpdm_resconstraint_m

- **表名称：** 资源约束配置-使用范围位图表
- **表名：** t_mpdm_resconstraint_m

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
| 1 | pk_t_mpdm_resconstraint_m |  | forgid |
