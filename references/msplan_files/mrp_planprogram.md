# 计划方案定义(作废)-mrp_planprogram

## 需求优先级映射关系子单据体-子表 t_mrp_planprodmentry

- **表名称：** 需求优先级映射关系子单据体-子表
- **表名：** t_mrp_planprodmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffruncondition_tag | 生效条件_详情 | text | 0 |  |  | null | 生效条件_详情 |
| 2 | felementtype | 要素类型 | varchar | 30 |  | √ | ' ' | 要素类型,枚举: 0 :数值 1 :日期 2 :实体 |
| 3 | fdemandentity | 业务实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fdemandlogo | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdemandname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | ftypename | 名称 | int8 | 64 |  | √ | 0 | 优先级类型定义 mrp_priority_type |
| 9 | ffruncondition | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 10 | ffrunconditiondesc | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | felementname | 要素名称 | varchar | 100 |  | √ | ' ' | 要素名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planprodmentry |  | fseq,fentryid |
| 2 | pk_t_mrp_planprodmentry |  | fdetailid |

---

## 计划方案定义(作废)-主表 t_mrp_planprogram

- **表名称：** 计划方案定义(作废)-主表
- **表名：** t_mrp_planprogram

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foutofrange | 超范围数据处理方式 | bpchar | 1 |  | √ | 'A' | 超范围数据处理方式,枚举: A :移除 B :标记例外 |
| 3 | fislossrate | 考虑损耗率 | bpchar | 1 |  | √ | '0' | 考虑损耗率 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | freleasemode | 预留释放方式 | varchar | 30 |  | √ | ' ' | 预留释放方式,枚举: 0 :不释放预留 1 :释放全部预留（除手工） 2 :仅释放弱预留 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcomputemode | 优先级计算模式 | varchar | 30 |  | √ | ' ' | 优先级计算模式,枚举: A :继承父项 B :重新计算 |
| 9 | fiscustomize | 定制 | bpchar | 1 |  | √ | '0' | 定制 |
| 10 | fadjusteffectset | 调整生效设置 | varchar | 30 |  | √ | ' ' | 调整生效设置,枚举: A :物料设置优先生效 B :方案设置优先生效 |
| 11 | finvlevel | 库存水位 | int8 | 64 |  | √ | 0 | 库存水位信息 msplan_invlevel |
| 12 | fmrpsetup | MRP参数设置ID | int8 | 64 |  | √ | 0 | MRP参数设置ID |
| 13 | fhiloinv | 最大最小库存 | bpchar | 1 |  | √ | '0' | 最大最小库存 |
| 14 | fsafestockeffectset | 安全库存生效设置 | varchar | 30 |  | √ | ' ' | 安全库存生效设置,枚举: A :按制造策略生效 B :按计划方案生效 C :空 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fdelaytoler | 延后容差（天） | int4 | 32 |  |  | 0 | 延后容差（天） |
| 17 | fisnew | 是否是新界面 | bpchar | 1 |  | √ | '0' | 是否是新界面 |
| 18 | fisreorderpoint | 再订货点 | bpchar | 1 |  | √ | '0' | 再订货点 |
| 19 | fisreplace | 考虑替代 | bpchar | 1 |  | √ | '0' | 考虑替代 |
| 20 | fisnotsetup | 未设置 | bpchar | 1 |  | √ | '0' | 未设置 |
| 21 | fallowdelaytime | 允许延后期间（天） | int4 | 32 |  |  | 0 | 允许延后期间（天） |
| 22 | finvsupplystrategy | 库存供应策略 | int8 | 64 |  | √ | 0 | 库存供应策略 mrp_stocksupply_policy |
| 23 | fiscenterwarehouse | 考虑央仓 | bpchar | 1 |  | √ | '0' | 考虑央仓 |
| 24 | fismps | MPS | bpchar | 1 |  | √ | '0' | MPS |
| 25 | fsupplymodel | 供应模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 26 | fselorgrangid | 选择的组织过滤范围id | varchar | 255 |  | √ | ' ' | 选择的组织过滤范围id |
| 27 | fiscommon | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 28 | fscday | 供应拖期期间 | int4 | 32 |  |  | 0 | 供应拖期期间 |
| 29 | fisselection | 选配 | bpchar | 1 |  | √ | '0' | 选配 |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fradiogroup | fradiogroup | varchar | 30 |  | √ | ' ' |  |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 34 | focpweakreserve | 按优先级占用弱预留 | varchar | 30 |  | √ | ' ' | 按优先级占用弱预留,枚举: 1 :是 0 :否 |
| 35 | fstockreserve | 考虑库存预留 | bpchar | 1 |  | √ | '0' | 考虑库存预留 |
| 36 | fisyield | 考虑成品率 | bpchar | 1 |  | √ | '0' | 考虑成品率 |
| 37 | fsupplynet | 供应网络 | int8 | 64 |  | √ | 0 | 供应网络定义 mrp_definitionsupply |
| 38 | fdemandmodel | 需求模型 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 39 | foutofdate | 需求：拖期期间 | varchar | 30 |  | √ | ' ' | 需求：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间（天） |
| 40 | fstepnum | 步骤数 | varchar | 255 |  | √ | ' ' | 步骤数 |
| 41 | fismrp | MRP | bpchar | 1 |  | √ | '0' | MRP |
| 42 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 45 | fscoutofdate | 供应：拖期期间 | varchar | 30 |  | √ | ' ' | 供应：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间（天） |
| 46 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 47 | fconsiderbatchstr | 调整考虑批量策略 | bpchar | 1 |  | √ | '0' | 调整考虑批量策略 |
| 48 | fday | 需求拖期期间 | int4 | 32 |  |  | 0 | 需求拖期期间 |
| 49 | fissimulation | 计划模拟 | bpchar | 1 |  | √ | '0' | 计划模拟 |
| 50 | fisadjust | 考虑调整 | bpchar | 1 |  | √ | '0' | 考虑调整 |
| 51 | fissafestock | 考虑安全库存 | bpchar | 1 |  | √ | '0' | 考虑安全库存 |
| 52 | fearlytoler | 提前容差（天） | int4 | 32 |  |  | 0 | 提前容差（天） |
| 53 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fallowleadtime | 允许提前期间（天） | int4 | 32 |  |  | 0 | 允许提前期间（天） |
| 57 | forgrangid | 需求组织运算范围存储id | varchar | 255 |  | √ | ' ' | 需求组织运算范围存储id |
| 58 | fselorgrangid_tag | 选择的组织过滤范围id_详情 | text | 0 |  |  | null | 选择的组织过滤范围id_详情 |
| 59 | fcussave | 自定义控件xy位置存储 | varchar | 255 |  | √ | ' ' | 自定义控件xy位置存储 |
| 60 | fplantag | 计划标识： | varchar | 30 |  | √ | ' ' | 计划标识： |
| 61 | fappmode | 优先级应用模式 | varchar | 30 |  | √ | ' ' | 优先级应用模式,枚举: A :需求日期 B :动态计算 |
| 62 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 63 | fplanoutlook | 计划展望期 | int8 | 64 |  | √ | 0 | 计划展望期 |
| 64 | fcussave_tag | 自定义控件xy位置存储_详情 | text | 0 |  |  | null | 自定义控件xy位置存储_详情 |
| 65 | forgrangid_tag | 需求组织运算范围存储id_详情 | text | 0 |  |  | null | 需求组织运算范围存储id_详情 |
| 66 | fisreserve | 考虑预留 | bpchar | 1 |  | √ | '0' | 考虑预留 |
| 67 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: A :MRP B :SCM |
| 68 | frelativetransfer | 供需匹配维度 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 69 | fmulid | 多组织供需关系 | int8 | 64 |  | √ | 0 | 多组织供需关系 mrp_multiorgsupdem |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planprogram |  | fid |
| 2 | idx_t_mrp_planprogram_createorg |  | fcreateorgid |
| 3 | idx_mrp_planprogram |  | fnumber,fcreateorgid |
| 4 | idx_t_mrp_planprogram_master |  | fmasterid |

---

## 供应参数单据体-子表 t_mrp_planproscentry

- **表名称：** 供应参数单据体-子表
- **表名：** t_mrp_planproscentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresourceregisters | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |
| 3 | fsupplyres | 供应资源 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsupplypriority | 供应优先级 | int4 | 32 |  | √ | 0 | 供应优先级 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fisscmrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | '0' | 参与MRP运算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planproscentry |  | fentryid |
| 2 | idx_mrp_planproscentry |  | fid,fseq |

---

## 需求优先级映射-子表 t_mrp_planpentry

- **表名称：** 需求优先级映射-子表
- **表名：** t_mrp_planpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffruncondition_tag | 生效条件_详情 | text | 0 |  |  | null | 生效条件_详情 |
| 3 | felementtype | 要素类型 | varchar | 30 |  | √ | ' ' | 要素类型,枚举: 0 :数值 1 :日期 2 :实体 |
| 4 | fdemandentity | 业务实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fdemandlogo | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | ftypename | 名称 | int8 | 64 |  | √ | 0 | 优先级类型定义 mrp_priority_type |
| 9 | fpentryfrunconditiondesc | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 10 | ffruncondition | 生效条件 | varchar | 255 |  | √ | ' ' | 生效条件 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | felementname | 要素名称 | varchar | 100 |  | √ | ' ' | 要素名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planpentry |  | fentryid |
| 2 | idx_mrp_planpentry |  | fid,fseq |

---

## 计划方案定义(作废)-多语言表 t_mrp_planprogram_l

- **表名称：** 计划方案定义(作废)-多语言表
- **表名：** t_mrp_planprogram_l

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
| 1 | pk_t_mrp_planprogram_l |  | fpkid |
| 2 | idx_mrp_planprogram_l |  | fid,flocaleid |

---

## 计划方案定义(作废)-使用范围位图表 t_mrp_planprogram_m

- **表名称：** 计划方案定义(作废)-使用范围位图表
- **表名：** t_mrp_planprogram_m

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
| 1 | pk_t_mrp_planprogram_m |  | forgid |

---

## 组织参数单据体-子表 t_mrp_planproorgentry

- **表名称：** 组织参数单据体-子表
- **表名：** t_mrp_planproorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvstrategy | 库存供应策略 | int8 | 64 |  | √ | 0 | 库存供应策略 mrp_stocksupply_policy |
| 3 | fsupplynet | 供应网络 | int8 | 64 |  | √ | 0 | 供应网络定义 mrp_definitionsupply |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planproorgentry |  | fentryid |
| 2 | idx_mrp_planproorgentry |  | fid,fseq |

---

## 计划方案定义(作废)-使用范围表 t_mrp_planprogram_u

- **表名称：** 计划方案定义(作废)-使用范围表
- **表名：** t_mrp_planprogram_u

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
| 1 | idx_t_mrp_planprogram_u_uo |  | fuseorgid |
| 2 | t_mrp_planprogram_u_pkey |  | fdataid,fuseorgid |

---

## 计划标识-多选基础资料表 t_mrp_planprogram_tag

- **表名称：** 计划标识-多选基础资料表
- **表名：** t_mrp_planprogram_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planprogram_tag |  | fpkid |
| 2 | idx_mrp_plantag_fid |  | fid |

---

## 需求参数单据体-子表 t_mrp_planproentry

- **表名称：** 需求参数单据体-子表
- **表名：** t_mrp_planproentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | '0' | 参与MRP运算 |
| 3 | fresourceregister | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 msplan_resource_dataconf |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdemandsrc | 需求来源 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_planproentry |  | fentryid |
| 2 | idx_mrp_planproentry |  | fid,fseq |

---

## 重排参数单据体-子表 t_mrp_planproreentry

- **表名称：** 重排参数单据体-子表
- **表名：** t_mrp_planproreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjuststrategy | 调整策略 | varchar | 30 |  | √ | ' ' | 调整策略,枚举: C :不调整 A :整单调整 B :部分调整 |
| 3 | fresulttype | 输出类型 | varchar | 50 |  | √ | ' ' | 输出类型,枚举: 0 :建议取消 1 :建议延后 2 :建议提前 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentitytype | 供应单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planproreentry |  | fid,fseq |
| 2 | pk_t_mrp_planproreentry |  | fentryid |
