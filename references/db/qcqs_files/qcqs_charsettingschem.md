# 图表设置方案-qcqs_charsettingschem

## 业务类型-多选基础资料表 t_qcqs_biztype

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_qcqs_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 qcbd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcqs_biztype |  | fpkid |
| 2 | idx_qcqs_biztpe_fid |  | fid,fbasedataid |

---

## 单据体-子表 t_qcqs_chartentry

- **表名称：** 单据体-子表
- **表名：** t_qcqs_chartentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcharttype | 图表类型 | varchar | 5 |  | √ | ' ' | 图表类型,枚举: A :柱状图 B :折线图 C :饼状图 |
| 3 | fsecondyaxis | 次坐标轴 | bpchar | 1 |  | √ | '0' | 次坐标轴 |
| 4 | fchecked | 选择标记 | bpchar | 1 |  | √ | '0' | 选择标记 |
| 5 | fseriesnamesid | 序列名 | int8 | 64 |  | √ | 0 | 统计分析报表关键字 qcqs_analyrptkey |
| 6 | fcolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fseriesnamer | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 9 | fdatalabel | 数据标签 | bpchar | 1 |  | √ | '0' | 数据标签 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcqs_charry_fid |  | fid |
| 2 | pk_qcqs_chartentry |  | fentryid |
| 3 | idx_qcqs_charry_fseq |  | fseq |

---

## 图表设置方案-多语言表 t_qcqs_chartschem_l

- **表名称：** 图表设置方案-多语言表
- **表名：** t_qcqs_chartschem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcqs_chartschem_l |  | fpkid |
| 2 | idx_qcqs_chareml_fid |  | fid,flocaleid |
| 3 | idx_qcqs_chareml_fname |  | fname |

---

## 图表设置方案-使用范围表 t_qcqs_chartschem_u

- **表名称：** 图表设置方案-使用范围表
- **表名：** t_qcqs_chartschem_u

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
| 1 | pk_t_qcqs_chartschem_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcqs_chartschem_u_uo |  | fuseorgid |

---

## 图表设置方案-主表 t_qcqs_chartschem

- **表名称：** 图表设置方案-主表
- **表名：** t_qcqs_chartschem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxaxisselect | 单选横坐标(方案详情单选列表) | varchar | 255 |  | √ | ' ' | 单选横坐标(方案详情单选列表) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 10 | frptflagid | 报表实体 | varchar | 255 |  | √ | '0' | 主实体对象 bos_entityobject |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fmulxaxisselect | 多选横坐标(方案详情多选列表) | varchar | 500 |  | √ | ' ' | 多选横坐标(方案详情多选列表) |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 19 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fcheckbox | 是否选择 | bpchar | 1 |  | √ | '0' | 是否选择 |
| 21 | fseqindex | 方案优先级 | int4 | 32 |  | √ | 0 | 方案优先级 |
| 22 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fschemtype | 方案维度 | varchar | 5 |  | √ | ' ' | 方案维度,枚举: A :业务类型 |
| 24 | fnumber | 方案编码 | varchar | 100 |  | √ | ' ' | 方案编码 |
| 25 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcqs_chartschem_master |  | fmasterid |
| 2 | pk_qcqs_chartschem |  | fid |
| 3 | idx_qcqs_charem_fnumber |  | fnumber |
| 4 | idx_qcqs_charem_fcreatetime |  | fcreatetime |
| 5 | idx_t_qcqs_chartschem_createorg |  | fcreateorgid |

---

## 图表设置方案-使用范围位图表 t_qcqs_chartschem_m

- **表名称：** 图表设置方案-使用范围位图表
- **表名：** t_qcqs_chartschem_m

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
| 1 | pk_t_qcqs_chartschem_m |  | forgid |
