# 库存水位信息-msplan_invlevel

## 库存水位信息-主表 t_msplan_invlevel

- **表名称：** 库存水位信息-主表
- **表名：** t_msplan_invlevel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: A :MRP B :SCM |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 21 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 msplan_plan_dimension |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_invlevel_num |  | fnumber |
| 2 | idx_t_msplan_invlevel_createorg |  | fcreateorgid |
| 3 | pk_msplan_invlevel |  | fid |
| 4 | idx_t_msplan_invlevel_master |  | fmasterid |

---

## 库存水位信息-多语言表 t_msplan_invlevel_l

- **表名称：** 库存水位信息-多语言表
- **表名：** t_msplan_invlevel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msplan_invlevel_l |  | fpkid |
| 2 | idx_msplan_invlevel_l_fid |  | fid,flocaleid |

---

## 库存水位信息-使用范围位图表 t_msplan_invlevel_m

- **表名称：** 库存水位信息-使用范围位图表
- **表名：** t_msplan_invlevel_m

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
| 1 | pk_t_msplan_invlevel_m |  | forgid |

---

## 单据体-子表 t_msplan_invlevelentry

- **表名称：** 单据体-子表
- **表名：** t_msplan_invlevelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/(1-损耗率) B :标准用量*(1+损耗率) |
| 4 | finspectionleadtime | 检验提前期（天） | int8 | 64 |  | √ | 0 | 检验提前期（天） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdatestart | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fentrymateriel | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fdailyconsume | 日均消耗量 | numeric | 23 | 10 | √ | 0 | 日均消耗量 |
| 9 | fmax | 最大值 | numeric | 23 | 10 | √ | 0 | 最大值 |
| 10 | fecobatch | 经济批量 | numeric | 23 | 10 | √ | 0 | 经济批量 |
| 11 | fyield | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 12 | fleadtime | 提前期（天） | int8 | 64 |  | √ | 0 | 提前期（天） |
| 13 | fwastagerate | 损耗率% | numeric | 23 | 10 | √ | 0 | 损耗率% |
| 14 | fmin | 最小值 | numeric | 23 | 10 | √ | 0 | 最小值 |
| 15 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制件 10040 :外购件 10050 :外协件 |
| 16 | fentrystock | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 17 | fentryorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | foperator | 计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsafeinv | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 20 | fpostprocessingtime | 后处理时间（天） | int8 | 64 |  | √ | 0 | 后处理时间（天） |
| 21 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 22 | fplantag | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 23 | fpreprocessingtime | 前处理时间（天） | int8 | 64 |  | √ | 0 | 前处理时间（天） |
| 24 | fvalue | 维度值 | varchar | 2000 |  | √ | ' ' | 维度值 |
| 25 | freservedtype | 预留类型 | varchar | 30 |  | √ | ' ' | 预留类型,枚举: A :强预留 B :弱预留 C :不预留 |
| 26 | fdateend | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 27 | fplantype | 计划方式 | varchar | 30 |  | √ | ' ' | 计划方式,枚举: A :再订货点 B :最大最小库存 |
| 28 | freorder | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_invlevelentry |  | fentryid |
| 2 | idx_msplan_invlevelentry_m |  | fentrymateriel |
| 3 | idx_msplan_inve_fid |  | fid |
| 4 | idx_msplan_invlevelentry_o |  | fentryorg |

---

## 库存水位信息-使用范围表 t_msplan_invlevel_u

- **表名称：** 库存水位信息-使用范围表
- **表名：** t_msplan_invlevel_u

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
| 1 | pk_t_msplan_invlevel_u |  | fdataid,fuseorgid |
| 2 | idx_t_msplan_invlevel_u_uo |  | fuseorgid |
