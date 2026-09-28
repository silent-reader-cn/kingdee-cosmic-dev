# 排程方案定义-mrp_pls_scheme

## 班次能力分录-子表 t_mrp_plswasubentry

- **表名称：** 班次能力分录-子表
- **表名：** t_mrp_plswasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fworktime | 工作时长（小时） | numeric | 23 | 10 | √ | 0 | 工作时长（小时） |
| 2 | fworkstarttime | 工作开始时间 | int8 | 64 |  | √ | 0 | 工作开始时间 |
| 3 | fiscal | 参与排程计算 | varchar | 1 |  | √ | ' ' | 参与排程计算 |
| 4 | fiscrossday | 跨天 | varchar | 1 |  | √ | ' ' | 跨天 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fworkendtime | 工作结束时间 | int8 | 64 |  | √ | 0 | 工作结束时间 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fworkshift | 班次编码 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_plswasubentry |  | fdetailid |
| 2 | idx_mrp_plswasubentry |  | fentryid,fseq |

---

## 工作中心分录-子表 t_mrp_plswcentry

- **表名称：** 工作中心分录-子表
- **表名：** t_mrp_plswcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkcenterid | 工作中心编码 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_plswcentry |  | fentryid |
| 2 | idx_mrp_plswcentry |  | fid,fseq |

---

## 排程方案定义-主表 t_mrp_pls_scheme

- **表名称：** 排程方案定义-主表
- **表名：** t_mrp_pls_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupmapping | 物料主数据与物料控制组映射 | varchar | 255 |  | √ | ' ' | 物料主数据与物料控制组映射 |
| 3 | fsourceconfigids_tag | 数据源id_详情 | text | 0 |  |  | null | 数据源id_详情 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmapping | 工作中心与次数映射关系 | varchar | 255 |  | √ | ' ' | 工作中心与次数映射关系 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fgroupmapping_tag | 物料主数据与物料控制组映射_详情 | text | 0 |  |  | null | 物料主数据与物料控制组映射_详情 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fsourceconfigids | 数据源id | varchar | 255 |  | √ | ' ' | 数据源id |
| 15 | fallordernos_tag | 查询订单号_详情 | text | 0 |  |  | null | 查询订单号_详情 |
| 16 | fcreateorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fconsiderplandate1 | 考虑计划日期 | bpchar | 1 |  | √ | '0' | 考虑计划日期 |
| 19 | facrossdayshift1 | 跨天班次仅安排次日需求 | bpchar | 1 |  | √ | '0' | 跨天班次仅安排次日需求 |
| 20 | fisclasssystem | 是否启用班制 | bpchar | 1 |  | √ | '0' | 是否启用班制 |
| 21 | fallordernos | 查询订单号 | varchar | 255 |  | √ | ' ' | 查询订单号 |
| 22 | fworkshiftid | 班次 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fmapping_tag | 工作中心与次数映射关系_详情 | text | 0 |  |  | null | 工作中心与次数映射关系_详情 |
| 25 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fordermodelid | 订单模型 | int8 | 64 |  | √ | 0 | [资源注册模型 mrp_resourceregister_cf](../msplan_files/mrp_resourceregister_cf.md) |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fcycle | 周期（天） | int8 | 64 |  | √ | 0 | 周期（天） |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fclasssystemid | 班制 | int8 | 64 |  | √ | 0 | [班制 mpdm_classsystem](../mpdm_files/mpdm_classsystem.md) |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_pls_scheme |  | fid |
| 2 | idx_t_mrp_pls_scheme_master |  | fmasterid |
| 3 | idx_t_mrp_pls_scheme_createorg |  | fcreateorgid |
| 4 | idx_mrp_pls_scheme |  | fnumber |

---

## 物料类别分录-子表 t_mrp_plsmatentry

- **表名称：** 物料类别分录-子表
- **表名：** t_mrp_plsmatentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcategory | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: A :物料 C :物料控制组 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plsmatentry |  | fid,fseq |
| 2 | pk_t_mrp_plsmatentry |  | fentryid |

---

## 工作中心子分录-子表 t_mrp_plswcsubentry

- **表名称：** 工作中心子分录-子表
- **表名：** t_mrp_plswcsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fworkcenterid | 工作中心编码 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 2 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plswcsubentry |  | fentryid,fseq |
| 2 | pk_t_mrp_plswcsubentry |  | fdetailid |

---

## 排程方案定义-多语言表 t_mrp_pls_scheme_l

- **表名称：** 排程方案定义-多语言表
- **表名：** t_mrp_pls_scheme_l

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
| 1 | pk_t_mrp_pls_scheme_l |  | fpkid |
| 2 | idx_mrp_pls_scheme_l |  | fid,flocaleid |

---

## 排程方案定义-使用范围位图表 t_mrp_pls_scheme_m

- **表名称：** 排程方案定义-使用范围位图表
- **表名：** t_mrp_pls_scheme_m

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
| 1 | pk_t_mrp_pls_scheme_m |  | forgid |

---

## 组织参数单据体-子表 t_mrp_pls_orgentry

- **表名称：** 组织参数单据体-子表
- **表名：** t_mrp_pls_orgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_pls_orgentry |  | fentryid |

---

## 排程方案定义-使用范围表 t_mrp_pls_scheme_u

- **表名称：** 排程方案定义-使用范围表
- **表名：** t_mrp_pls_scheme_u

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
| 1 | pk_t_mrp_pls_scheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_mrp_pls_scheme_u_uo |  | fuseorgid |

---

## 固定能力项子分录-子表 t_mrp_plsfcsubentry

- **表名称：** 固定能力项子分录-子表
- **表名：** t_mrp_plsfcsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fcategory | 产品维度 | varchar | 50 |  | √ | ' ' | 产品维度,枚举: A :物料 C :物料控制组 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fefficiency | 效率 | numeric | 23 | 10 | √ | 0.0000000000 | 效率 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fabilityvalue | 能力数值 | numeric | 23 | 10 | √ | 0.0000000000 | 能力数值 |
| 10 | faddefficiency | 额外效率 | numeric | 23 | 10 | √ | 0.0000000000 | 额外效率 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fabilitygroupid | 能力项组编码 | int8 | 64 |  | √ | 0 | [能力项组 mpdm_capacitygroup](../mpdm_files/mpdm_capacitygroup.md) |
| 14 | fabilityname | 能力项名称 | varchar | 50 |  | √ | ' ' | 能力项名称 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fabilitynumber | 能力项编码 | varchar | 50 |  | √ | ' ' | 能力项编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_plsfcsubentry |  | fdetailid |
| 2 | idx_mrp_plsfcsubentry |  | fentryid,fseq |

---

## 计算能力项分录-子表 t_mrp_plscrsubentry

- **表名称：** 计算能力项分录-子表
- **表名：** t_mrp_plscrsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fispartincalc | 参与排程计算 | bpchar | 1 |  | √ | ' ' | 参与排程计算 |
| 2 | fcategory | 产品维度 | varchar | 50 |  | √ | ' ' | 产品维度,枚举: A :物料 C :物料控制组 |
| 3 | fexpression | 计算表达式 | varchar | 255 |  | √ | ' ' | 计算表达式 |
| 4 | fprecision | 精度 | int8 | 64 |  | √ | 0 | 精度 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 6 | fcompleteresult | 计算结果 | varchar | 50 |  | √ | ' ' | 计算结果 |
| 7 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fworkstype | 工时种类 | varchar | 50 |  | √ | ' ' | 工时种类,枚举: A :机器工时 B :人工工时 |
| 11 | fcapacitycalen | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 12 | fworkunits | 工时单位 | varchar | 50 |  | √ | ' ' | 工时单位,枚举: A :秒 B :分 C :时 D :天 |
| 13 | fabilitygroupid | 能力项组编码 | int8 | 64 |  | √ | 0 | [能力项组 mpdm_capacitygroup](../mpdm_files/mpdm_capacitygroup.md) |
| 14 | fabilityname | 能力项名称 | varchar | 50 |  | √ | ' ' | 能力项名称 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plscrsubentry |  | fentryid,fseq |
| 2 | pk_t_mrp_plscrsubentry |  | fdetailid |

---

## 数据源分录-子表 t_mrp_plssrcentry

- **表名称：** 数据源分录-子表
- **表名：** t_mrp_plssrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispartincalc | 参与排程计算 | bpchar | 1 |  | √ | ' ' | 参与排程计算 |
| 3 | fdatasoureid | 编码 | int8 | 64 |  | √ | 0 | [数据源配置 mrp_resource_dataconfig](../msplan_files/mrp_resource_dataconfig.md) |
| 4 | fsrcentityid | 源实体 | varchar | 26 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plssrcentry |  | fid,fseq |
| 2 | pk_t_mrp_plssrcentry |  | fentryid |
