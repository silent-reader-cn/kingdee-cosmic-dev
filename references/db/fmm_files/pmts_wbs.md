# WBS-pmts_wbs

## WBS-使用范围表 t_pmts_wbs_u

- **表名称：** WBS-使用范围表
- **表名：** t_pmts_wbs_u

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
| 1 | idx_t_pmts_wbs_u_uo |  | fuseorgid |
| 2 | pk_t_pmts_wbs_u |  | fdataid,fuseorgid |

---

## WBS-使用范围位图表 t_pmts_wbs_m

- **表名称：** WBS-使用范围位图表
- **表名：** t_pmts_wbs_m

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
| 1 | pk_t_pmts_wbs_m |  | forgid |

---

## WBS-多语言表 t_pmts_wbs_l

- **表名称：** WBS-多语言表
- **表名：** t_pmts_wbs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | WBS名称 | varchar | 50 |  | √ | ' ' | WBS名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_wbs_l |  | fpkid |
| 2 | idx_pmts_wbsl_fid |  | fid,flocaleid |
| 3 | idx_pmts_wbsl_fname |  | fname |

---

## 单据体-子表 t_pmts_wbs_order

- **表名称：** 单据体-子表
- **表名：** t_pmts_wbs_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderpro | 专业 | varchar | 50 |  | √ | ' ' | 专业 |
| 3 | forderid | 工单ID | varchar | 50 |  | √ | ' ' | 工单ID |
| 4 | fordertype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | forderlocal | 功能位置 | varchar | 30 |  | √ | ' ' | 功能位置 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | forderno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fprocess | 工序组 | varchar | 50 |  | √ | ' ' | 工序组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_wbs_order |  | fentryid |
| 2 | idx_pmts_wbs_order_fs |  | fid,fseq |

---

## WBS-主表 t_pmts_wbs

- **表名称：** WBS-主表
- **表名：** t_pmts_wbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | festimateddays | 预计工期 | int4 | 32 |  | √ | 0 | 预计工期 |
| 4 | fwbsdescriptions | WBS说明 | varchar | 255 |  | √ | ' ' | WBS说明 |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | 来源主键 | int8 | 64 |  | √ | 0 | 来源主键 |
| 8 | fac | 实际成本（AC） | numeric | 23 | 10 | √ | 0 | 实际成本（AC） |
| 9 | fshareorgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fplanstartdate | 计划开始日期 | timestamp | 0 |  |  | null | 计划开始日期 |
| 13 | frange | 工作范围 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fhrorgid | HR组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fqualityorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | factualdays | 实际工期 | int4 | 32 |  | √ | 0 | 实际工期 |
| 18 | fdurationunitid | 工期单位 | int8 | 64 |  | √ | 0 | [工期单位 pmpd_timeunit](../fmm_files/pmpd_timeunit.md) |
| 19 | fdevice | 检修设备 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 20 | fprofession | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 21 | fwbstype | WBS类型 | int8 | 64 |  | √ | 0 | [项目WBS类型 pmbd_projectwbstype](../fmm_files/pmbd_projectwbstype.md) |
| 22 | fname | WBS名称 | varchar | 50 |  | √ | ' ' | WBS名称 |
| 23 | fplanenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 24 | fcheckproduct | 启用项目生产清单 | bpchar | 1 |  | √ | '0' | 启用项目生产清单 |
| 25 | ffunlocation | 功能区域 | int8 | 64 |  | √ | 0 | [功能位置 mpdm_functionlocation](../mpdm_files/mpdm_functionlocation.md) |
| 26 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 27 | fprojectstageid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 pmbd_projectstage](../fmm_files/pmbd_projectstage.md) |
| 28 | fbsenddate | 基线计划完成时间 | timestamp | 0 |  |  | null | 基线计划完成时间 |
| 29 | fbaselinetype | 基线类别 | varchar | 50 |  | √ | ' ' | 基线类别 |
| 30 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 31 | fversionid | 版本 | int8 | 64 |  | √ | 0 | [版本 mpdm_gantt_version](../mpdm_files/mpdm_gantt_version.md) |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fbusinessstate | 计划状态 | varchar | 5 |  | √ | ' ' | 计划状态,枚举: A :计划 B :已确认 C :已发布 D :已下达 E :已完成 |
| 34 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | ftimeunit | 工期单位 | varchar | 5 |  | √ | ' ' | 工期单位,枚举: 1 :天 2 :周 |
| 36 | fplanarea | 计划区域 | int8 | 64 |  | √ | 0 | [计划区域 fmm_planningarea](../fmm_files/fmm_planningarea.md) |
| 37 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fcheckpurchase | 启用项目采购清单 | bpchar | 1 |  | √ | '0' | 启用项目采购清单 |
| 39 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fnumber | WBS编码 | varchar | 200 |  | √ | ' ' | WBS编码 |
| 41 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 42 | fpackage | 工作包 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | ftplid | 计划模板 | int8 | 64 |  | √ | 0 | [计划模板 pmpd_milestonetpl](../fmm_files/pmpd_milestonetpl.md) |
| 45 | fcheckregister | 启用任务计划文档 | bpchar | 1 |  | √ | '0' | 启用任务计划文档 |
| 46 | faccountingorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 48 | festimatedstartdate | 预计开始日期 | timestamp | 0 |  |  | null | 预计开始日期 |
| 49 | fplandays | 计划工期 | int4 | 32 |  | √ | 0 | 计划工期 |
| 50 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 51 | fcostobj | 成本对象 | bpchar | 1 |  | √ | '0' | 成本对象 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 54 | fcheckoutsour | 启用项目委外清单 | bpchar | 1 |  | √ | '0' | 启用项目委外清单 |
| 55 | fassetsorgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 57 | fresponsorgid | 责任单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | fbsstartdate | 基线计划开始时间 | timestamp | 0 |  |  | null | 基线计划开始时间 |
| 59 | fproductorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 60 | fcheckoutsource | 启用项目需求清单 | bpchar | 1 |  | √ | '0' | 启用项目需求清单 |
| 61 | fcapitalorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fparentid | 上级WBS | int8 | 64 |  | √ | 0 | [WBS pmts_wbs](../fmm_files/pmts_wbs.md) |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fresponspersonid | 责任人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 67 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 68 | fbsplandate | 基线计划工期 | numeric | 23 | 10 | √ | 0 | 基线计划工期 |
| 69 | fpv | 计划成本（PV） | numeric | 23 | 10 | √ | 0 | 计划成本（PV） |
| 70 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 71 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 72 | fbac | 完工预算（BAC） | numeric | 23 | 10 | √ | 0 | 完工预算（BAC） |
| 73 | fsourceplantypeid | 来源计划类型 | int8 | 64 |  | √ | 0 | [项目计划类型 fmm_plantype](../fmm_files/fmm_plantype.md) |
| 74 | fbaselinename | 基线计划名称 | varchar | 50 |  | √ | ' ' | 基线计划名称 |
| 75 | festimatedenddate | 预计完成日期 | timestamp | 0 |  |  | null | 预计完成日期 |
| 76 | fstandardtask | fstandardtask | int8 | 64 |  | √ | 0 |  |
| 77 | fplantype | 项目计划类型 | int8 | 64 |  | √ | 0 | [项目计划类型 fmm_plantype](../fmm_files/fmm_plantype.md) |
| 78 | ftplentryid | 计划模板分录ID | int8 | 64 |  | √ | 0 | 计划模板分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_wbs_fnumber |  | fnumber |
| 2 | pk_pmts_wbs |  | fid |
| 3 | idx_pmts_wbs_fcreatetime |  | fcreatetime |
| 4 | idx_t_pmts_wbs_master |  | fmasterid |
| 5 | idx_t_pmts_wbs_createorg |  | fcreateorgid |

---

## PMO信息-子表 t_pmts_orgprosentry

- **表名称：** PMO信息-子表
- **表名：** t_pmts_orgprosentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjobnumberid | 工号 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_orgprosentry |  | fentryid |
| 2 | idx_pmts_orgpry_fseq |  | fseq |
| 3 | idx_pmts_orgpry_fid |  | fid |

---

## 关联子实体-子表 t_pmts_wbs_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pmts_wbs_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_wbs_lk |  | fpkid |
| 2 | idx_pmts_wbs_lk_fk |  | fid |
