# 计划方案-mrp_planscheme

## 计划方案-使用范围表 t_mrp_planscheme_u

- **表名称：** 计划方案-使用范围表
- **表名：** t_mrp_planscheme_u

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
| 1 | idx_t_mrp_planscheme_u_uo |  | fuseorgid |
| 2 | pk_t_mrp_planscheme_u |  | fdataid,fuseorgid |

---

## 计划方案-多语言表 t_mrp_planscheme_l

- **表名称：** 计划方案-多语言表
- **表名：** t_mrp_planscheme_l

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
| 1 | pk_mrp_planscheme_l |  | fpkid |
| 2 | idx_mrp_planscheme_fid |  | fid |

---

## 需求优先级映射-子表 t_mrp_plspriorityentry

- **表名称：** 需求优先级映射-子表
- **表名：** t_mrp_plspriorityentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffruncondition_tag | 生效条件_详情 | text | 0 |  |  | null | 生效条件_详情 |
| 3 | felementtype | 要素类型 | varchar | 30 |  | √ | ' ' | 要素类型,枚举: 0 :数值 1 :日期 2 :实体 |
| 4 | fdemandentity | 业务实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fdemandlogo | 字段标识 | varchar | 100 |  | √ | ' ' | 字段标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 8 | ftypename | 名称 | int8 | 64 |  | √ | 0 | [优先级类型定义 mrp_priority_type](../msplan_files/mrp_priority_type.md) |
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
| 1 | pk_mrp_plspriorityentry |  | fentryid |
| 2 | idx_mrp_plspriorityentry_id |  | fid |

---

## 供应参数单据体-子表 t_mrp_plssupentry

- **表名称：** 供应参数单据体-子表
- **表名：** t_mrp_plssupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresourceregisters | 数据源配置 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconfig](../msplan_files/mrp_resource_dataconfig.md) |
| 3 | fsupbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 4 | fsupplyres | 供应资源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fcsdnoapproves | 计划状态参与计算 | bpchar | 1 |  | √ | '0' | 计划状态参与计算 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsupplypriority | 供应优先级 | int4 | 32 |  | √ | 0 | 供应优先级 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fisscmrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | ' ' | 参与MRP运算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plssupentry_fid |  | fid |
| 2 | pk_mrp_plssupentry |  | fentryid |

---

## 调整参数单据体-子表 t_mrp_plsadjentry

- **表名称：** 调整参数单据体-子表
- **表名：** t_mrp_plsadjentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjuststrategy | 调整策略 | varchar | 30 |  | √ | ' B' | 调整策略,枚举: C :不调整 A :整单调整 B :部分调整 |
| 3 | fresulttype | 输出类型 | varchar | 30 |  | √ | '0' | 输出类型,枚举: 0 :建议取消 1 :建议延后 2 :建议提前 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentitytype | 供应单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plsadjentry_fid |  | fid |
| 2 | pk_mrp_plsadjentry |  | fentryid |

---

## 计划标识-多选基础资料表 t_mrp_planprogram_tag

- **表名称：** 计划标识-多选基础资料表
- **表名：** t_mrp_planprogram_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [计划标识 mpdm_plantag](../mpdm_files/mpdm_plantag.md) |
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

## 释放需求计划预留-多选基础资料表 t_mrp_planscheme_vrd

- **表名称：** 释放需求计划预留-多选基础资料表
- **表名：** t_mrp_planscheme_vrd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planschemevrd_fid |  | fid |
| 2 | pk_mrp_planscheme_vrd |  | fpkid |

---

## 计划方案-主表 t_mrp_planscheme

- **表名称：** 计划方案-主表
- **表名：** t_mrp_planscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcsdrootbillno | 供需匹配优先考虑根需求单号 | bpchar | 1 |  | √ | '0' | 供需匹配优先考虑根需求单号 |
| 3 | fislossrate | 考虑损耗率 | bpchar | 1 |  | √ | ' ' | 考虑损耗率 |
| 4 | fcrossprjsupply | 考虑跨项目供应 | bpchar | 1 |  | √ | '0' | 考虑跨项目供应 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsafestockpriority | 安全库存优先级 | varchar | 30 |  | √ | '0' | 安全库存优先级,枚举: 0 :最低 1 :最高 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplorderrecalstatus | 计划订单状态 | varchar | 100 |  | √ | 'A,B,C' | 计划订单状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fautoauditinvadjust | 自动审核MTO库存调整 | bpchar | 1 |  | √ | '0' | 自动审核MTO库存调整 |
| 10 | freleasemode | 预留释放方式 | varchar | 30 |  | √ | '0' | 预留释放方式,枚举: 0 :不释放预留 1 :释放全部预留（除手工） 2 :仅释放弱预留 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcomputemode | 优先级计算模式 | varchar | 30 |  | √ | ' ' | 优先级计算模式,枚举: A :继承父项 B :重新计算 |
| 13 | fmtomatchcommoninway | MTO考虑通用跟踪号在途 | bpchar | 1 |  | √ | '0' | MTO考虑通用跟踪号在途 |
| 14 | finvlevel | 库存水位 | int8 | 64 |  | √ | 0 | [库存水位信息 msplan_invlevel](../msplan_files/msplan_invlevel.md) |
| 15 | fhiloinv | 最大最小库存 | bpchar | 1 |  | √ | '0' | 最大最小库存 |
| 16 | fautoauditro | 自动审核组织间需求单 | bpchar | 1 |  | √ | '0' | 自动审核组织间需求单 |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fdelaytoler | 延后容差（天） | int4 | 32 |  | √ | 0 | 延后容差（天） |
| 19 | fisreorderpoint | 再订货点 | bpchar | 1 |  | √ | ' ' | 再订货点 |
| 20 | fisreplace | 考虑替代 | bpchar | 1 |  | √ | ' ' | 考虑替代 |
| 21 | fallowdelaytime | 允许延后期间（天） | int4 | 32 |  | √ | 0 | 允许延后期间（天） |
| 22 | fispreciseselbill | 精确选单计算 | bpchar | 1 |  | √ | '0' | 精确选单计算 |
| 23 | fmtomatchfreeinway | MTO考虑无需求跟踪号在途 | bpchar | 1 |  | √ | '0' | MTO考虑无需求跟踪号在途 |
| 24 | fplorderrecalsub | 计划订单重算替代 | bpchar | 1 |  | √ | '0' | 计划订单重算替代 |
| 25 | fismps | MPS | bpchar | 1 |  | √ | ' ' | MPS |
| 26 | fgeneratemtoinwayadjust | 生成MTO在途调整建议 | bpchar | 1 |  | √ | '0' | 生成MTO在途调整建议 |
| 27 | fnotetotransprjtaskno | 非ETO物料携带项目编码和任务号 | bpchar | 1 |  | √ | '0' | 非ETO物料携带项目编码和任务号 |
| 28 | fvaliddays | 投放时间范围（天） | int4 | 32 |  | √ | 0 | 投放时间范围（天） |
| 29 | fauditrodays | 审核组织间需求单时间范围（天） | int4 | 32 |  | √ | 0 | 审核组织间需求单时间范围（天） |
| 30 | fisplansimulate | 计划模拟 | bpchar | 1 |  | √ | '0' | 计划模拟 |
| 31 | fscday | 供应拖期期间 | int4 | 32 |  | √ | 0 | 供应拖期期间 |
| 32 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fppbomrecalsub | 生产/委外用料清单替代重算 | bpchar | 1 |  | √ | '0' | 生产/委外用料清单替代重算 |
| 34 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 35 | focpweakreserve | 按优先级占用弱预留 | bpchar | 1 |  | √ | '0' | 按优先级占用弱预留 |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 37 | fchildsetid | 子项预测冲减定义 | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 38 | fisyield | 考虑成品率 | bpchar | 1 |  | √ | ' ' | 考虑成品率 |
| 39 | fmtomatchfreeinv | MTO考虑无需求跟踪号库存 | bpchar | 1 |  | √ | '0' | MTO考虑无需求跟踪号库存 |
| 40 | fcomputeid | 运算号 | int8 | 64 |  | √ | 0 | 运算号 |
| 41 | foutofdate | 需求：拖期期间 | varchar | 30 |  | √ | ' ' | 需求：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间（天） |
| 42 | fcsdoverduedate | 考虑近效期 | bpchar | 1 |  | √ | '0' | 考虑近效期 |
| 43 | fismrp | MRP | bpchar | 1 |  | √ | ' ' | MRP |
| 44 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 45 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 47 | fscoutofdate | 供应：拖期期间 | varchar | 30 |  | √ | ' ' | 供应：拖期期间,枚举: 1 :所有拖期期间 2 :指定拖期期间（天） |
| 48 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 49 | fmrptype | MRP类型 | bpchar | 1 |  | √ | 'A' | MRP类型,枚举: A :标准MRP B :预算MRP P :项目MRP |
| 50 | fconsiderbatchstr | 调整考虑批量策略 | bpchar | 1 |  | √ | ' ' | 调整考虑批量策略 |
| 51 | fday | 需求拖期期间 | int4 | 32 |  | √ | 0 | 需求拖期期间 |
| 52 | fautoauditpl | 自动审核计划订单 | bpchar | 1 |  | √ | '0' | 自动审核计划订单 |
| 53 | fisplanlrp | LRP | bpchar | 1 |  | √ | '0' | LRP |
| 54 | fissafestock | 考虑安全库存 | bpchar | 1 |  | √ | ' ' | 考虑安全库存 |
| 55 | fearlytoler | 提前容差（天） | int4 | 32 |  | √ | 0 | 提前容差（天） |
| 56 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 58 | fauditpldays | 审核计划订单时间范围（天） | int4 | 32 |  | √ | 0 | 审核计划订单时间范围（天） |
| 59 | fcsdshelflife | 考虑保质期 | bpchar | 1 |  | √ | '0' | 考虑保质期 |
| 60 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 61 | fallowleadtime | 允许提前期间（天） | int4 | 32 |  | √ | 0 | 允许提前期间（天） |
| 62 | ffreelinkbycalbill | 仅释放参与计算单据的预留关系 | bpchar | 1 |  | √ | '0' | 仅释放参与计算单据的预留关系 |
| 63 | fappmode | 优先级应用模式 | varchar | 30 |  | √ | ' ' | 优先级应用模式,枚举: A :需求日期 B :动态计算 |
| 64 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 65 | fplanoutlook | 计划展望期(天) | int4 | 32 |  | √ | 0 | 计划展望期(天) |
| 66 | fsubsfirstsupply | 替代物料资源优先供应 | varchar | 30 |  | √ | '0' | 替代物料资源优先供应,枚举: 0 :被替代物料需求 1 :自身物料需求 |
| 67 | fppbomrecalstatus | 生产/委外工单状态 | varchar | 100 |  | √ | 'B,C' | 生产/委外工单状态,枚举: A :计划 B :计划确认 C :下达 |
| 68 | fautorelease | 自动投放计划订单 | bpchar | 1 |  | √ | '0' | 自动投放计划订单 |
| 69 | fforceoverlay | 强制覆盖运算参数 | bpchar | 1 |  | √ | '0' | 强制覆盖运算参数 |
| 70 | fcsdrootbillnoonly | 供需匹配仅考虑根需求单号 | bpchar | 1 |  | √ | '0' | 供需匹配仅考虑根需求单号 |
| 71 | fmtomatchcommoninv | MTO考虑通用跟踪号库存 | bpchar | 1 |  | √ | '0' | MTO考虑通用跟踪号库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_planscheme |  | fid |
| 2 | idx_t_mrp_planscheme_master |  | fmasterid |
| 3 | idx_t_mrp_planscheme_createorg |  | fcreateorgid |
| 4 | idx_mrp_planscheme_number |  | fnumber |

---

## 组织参数单据体-子表 t_mrp_plsorgentry

- **表名称：** 组织参数单据体-子表
- **表名：** t_mrp_plsorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvstrategy | 库存供应策略 | int8 | 64 |  | √ | 0 | [库存供应策略 mrp_stocksupply_policy](../msplan_files/mrp_stocksupply_policy.md) |
| 3 | fsupplynet | 供应网络 | int8 | 64 |  | √ | 0 | [供应网络定义 mrp_definitionsupply](../msplan_files/mrp_definitionsupply.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plsorgentry_fid |  | fid |
| 2 | pk_mrp_plsorgentry |  | fentryid |

---

## 冲减定义编码-多选基础资料表 t_mrp_planscheme_setoff

- **表名称：** 冲减定义编码-多选基础资料表
- **表名：** t_mrp_planscheme_setoff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预测冲减定义 mds_setoffsetting](../mds_files/mds_setoffsetting.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_planscheme_setoff_fid |  | fid |
| 2 | pk_mrp_planscheme_setoff |  | fpkid |

---

## 需求参数单据体-子表 t_mrp_plsreqentry

- **表名称：** 需求参数单据体-子表
- **表名：** t_mrp_plsreqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmdsvrdsid | 版本定义 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 3 | fismrpoperat | 参与MRP运算 | bpchar | 1 |  | √ | ' ' | 参与MRP运算 |
| 4 | fresourceregister | 数据源配置 | int8 | 64 |  | √ | 0 | [数据源配置 msplan_resource_dataconf](../msplan_files/msplan_resource_dataconf.md) |
| 5 | fisselect | 选单 | bpchar | 1 |  | √ | '0' | 选单 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freqbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 8 | fcsdnoapproved | 计划状态参与计算 | bpchar | 1 |  | √ | '0' | 计划状态参与计算 |
| 9 | fdemandsrc | 需求来源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_plsreqentry |  | fentryid |
| 2 | idx_mrp_plsreqentry_fid |  | fid |
