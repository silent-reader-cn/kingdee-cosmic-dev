# 预测冲减定义-mds_setoffsetting

## 预测冲减定义-使用范围位图表 t_mds_setoffsetting_m

- **表名称：** 预测冲减定义-使用范围位图表
- **表名：** t_mds_setoffsetting_m

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
| 1 | pk_t_mds_setoffsetting_m |  | forgid |

---

## 预测冲减定义-多语言表 t_mds_setoffsetting_l

- **表名称：** 预测冲减定义-多语言表
- **表名：** t_mds_setoffsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_setoffsettingl_fid |  | fid,flocaleid |
| 2 | pk_mds_setoffsetting_l |  | fpkid |

---

## 需方制造策略-多选基础资料表 t_mds_setoffsetmanu

- **表名称：** 需方制造策略-多选基础资料表
- **表名：** t_mds_setoffsetmanu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 制造策略 bd_manustrategy |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_setoffsetmanu |  | fpkid |
| 2 | idx_mds_setoffsetmanu_id |  | fentryid |

---

## 预测冲减定义-使用范围表 t_mds_setoffsetting_u

- **表名称：** 预测冲减定义-使用范围表
- **表名：** t_mds_setoffsetting_u

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
| 1 | pk_t_mds_setoffsetting_u |  | fdataid,fuseorgid |
| 2 | idx_t_mds_setoffsetting_u_uo |  | fuseorgid |

---

## 供方制造策略-多选基础资料表 t_mds_setoffsetmanusup

- **表名称：** 供方制造策略-多选基础资料表
- **表名：** t_mds_setoffsetmanusup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 制造策略 bd_manustrategy |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_setoffsetmanusup |  | fpkid |
| 2 | idx_mds_setoffsetmanusup_id |  | fentryid |

---

## 供方单据体-子表 t_mds_setoffsetentg

- **表名称：** 供方单据体-子表
- **表名：** t_mds_setoffsetentg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 3 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 7 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |
| 8 | fprovidersetid | 供方取数 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_rgt |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_setoffsetentg |  | fentryid |
| 2 | idx_mds_setoffsetentg_fid |  | fid |

---

## 单据体-子表 t_mds_setoffsetent

- **表名称：** 单据体-子表
- **表名：** t_mds_setoffsetent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgfdataid | 供方取数 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_rgt |
| 3 | fmanustrategy | 需方制造策略 | varchar | 500 |  | √ | ' ' | 需方制造策略 |
| 4 | fsxhcopy | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 5 | fxfdataid | 需方取数 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_rgt |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmanustrategysup | 供方制造策略 | varchar | 500 |  | √ | ' ' | 供方制造策略 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_setoffsetent_fid |  | fid |
| 2 | pk_mds_setoffsetent |  | fentryid |

---

## 需方单据体-子表 t_mds_setoffsetents

- **表名称：** 需方单据体-子表
- **表名：** t_mds_setoffsetents

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsalesetid | 需方取数 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_rgt |
| 3 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 4 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsxh | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 8 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 9 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_setoffsetents_fid |  | fid |
| 2 | pk_mds_setoffsetents |  | fentryid |

---

## 预测冲减定义-主表 t_mds_setoffsetting

- **表名称：** 预测冲减定义-主表
- **表名：** t_mds_setoffsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsetofforderid | 预测冲减顺序定义 | int8 | 64 |  | √ | 0 | 预测冲减顺序定义 mds_setofforder |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fplanid | 任务号 | varchar | 100 |  | √ | ' ' | 任务号 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpfilter_tag | 供方查询条件存储_详情 | text | 0 |  |  | null | 供方查询条件存储_详情 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fsfilter_tag | 需方查询条件存储_详情 | text | 0 |  |  | null | 需方查询条件存储_详情 |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fjobid | 作业号 | varchar | 100 |  | √ | ' ' | 作业号 |
| 18 | fsfilter | 需方查询条件存储 | varchar | 255 |  | √ | ' ' | 需方查询条件存储 |
| 19 | fmod | fmod | int8 | 64 |  | √ | 0 |  |
| 20 | fdataver | 数据版本 | int8 | 64 |  | √ | 0 | 数据版本 msplan_ds_version |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fpfilter | 供方查询条件存储 | varchar | 255 |  | √ | ' ' | 供方查询条件存储 |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_setoffsetting_createorg |  | fcreateorgid |
| 2 | idx_t_mds_setoffsetting_master |  | fmasterid |
| 3 | idx_mds_sofset_num |  | fnumber |
| 4 | pk_mds_setoffsetting |  | fid |
