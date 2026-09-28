# 项目任务清单-pmts_task

## 班次-多选基础资料表 t_pmts_task_workshifts

- **表名称：** 班次-多选基础资料表
- **表名：** t_pmts_task_workshifts

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_task_workshifts |  | fid,fbasedataid |
| 2 | pk_pmts_task_workshifts |  | fpkid |

---

## 后置作业关系-子表 t_pmts_post_task

- **表名称：** 后置作业关系-子表
- **表名：** t_pmts_post_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpostdelayed | 延时 | numeric | 23 | 10 | √ | 0 | 延时 |
| 3 | ftaskrelationtwo | 任务关系 | varchar | 5 |  | √ | ' ' | 任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 4 | fpostpositiontaskid | 后置任务 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_postposition_task_fid |  | fid |
| 2 | pk_pmts_post_task |  | fentryid |
| 3 | idx_postposition_task_fseq |  | fseq |

---

## 停工复工分录-子表 t_pmts_task_stopentry

- **表名称：** 停工复工分录-子表
- **表名：** t_pmts_task_stopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | frestarttime | 复工时间 | timestamp | 0 |  |  | null | 复工时间 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fstopreason | 停工原因 | varchar | 50 |  | √ | ' ' | 停工原因 |
| 6 | fstoptime | 停工时间 | timestamp | 0 |  |  | null | 停工时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_task_fid |  | fid |
| 2 | pk_pmts_task_stopentry |  | fentryid |
| 3 | idx_pmts_task_fseq |  | fseq |

---

## 人力资源分配分录-子表 t_pmts_task_hs

- **表名称：** 人力资源分配分录-子表
- **表名：** t_pmts_task_hs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhsmain | 主要资源 | bpchar | 1 |  | √ | '0' | 主要资源 |
| 3 | fhsuser | 人员 | int8 | 64 |  | √ | 0 | 企业人力资源池 pmbd_enterprise_hm_res_po |
| 4 | fhsplanneedtime | 计划尚需工时（H） | numeric | 23 | 10 | √ | 0 | 计划尚需工时（H） |
| 5 | fhstype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: A :人员 B :角色 |
| 6 | fhsplanabilitytime | 计划能力工时（H） | numeric | 23 | 10 | √ | 0 | 计划能力工时（H） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fhsrole | 角色 | varchar | 50 |  | √ | ' ' | 通用角色 perm_role |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_task_hs |  | fentryid |
| 2 | idx_pmts_taskhs_fid |  | fid |
| 3 | idx_pmts_taskhs_fseq |  | fseq |

---

## 项目任务清单-使用范围表 t_pmts_task_u

- **表名称：** 项目任务清单-使用范围表
- **表名：** t_pmts_task_u

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
| 1 | pk_t_pmts_task_u |  | fdataid,fuseorgid |
| 2 | idx_t_pmts_task_u_uo |  | fuseorgid |

---

## 项目任务清单-使用范围位图表 t_pmts_task_m

- **表名称：** 项目任务清单-使用范围位图表
- **表名：** t_pmts_task_m

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
| 1 | pk_t_pmts_task_m |  | forgid |

---

## 项目任务清单-多语言表 t_pmts_task_l

- **表名称：** 项目任务清单-多语言表
- **表名：** t_pmts_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_taskl_fid |  | fid,flocaleid |
| 2 | pk_pmts_task_l |  | fpkid |
| 3 | idx_pmts_taskl_fname |  | fname |

---

## 项目任务清单-主表 t_pmts_task

- **表名称：** 项目任务清单-主表
- **表名：** t_pmts_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factualenddate | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 pmbd_jobtype |
| 5 | fprojectnumid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 6 | fviewschem | fviewschem | int8 | 64 |  | √ | 0 |  |
| 7 | fdevices | 检修设备 | int8 | 64 |  | √ | 0 | 检修设备 mpdm_over_device |
| 8 | fiscrux | 次关键任务 | bpchar | 1 |  | √ | '0' | 次关键任务 |
| 9 | fafacilityhours | 实际设备工时 | numeric | 23 | 10 | √ | 0 | 实际设备工时 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fabnormal | 异常 | bpchar | 1 |  | √ | '0' | 异常 |
| 12 | fganttentity | 甘特图视图方案 | int8 | 64 |  | √ | 0 | 视图方案 msplan_ganttentity |
| 13 | ffinishtime | 完成工期 | numeric | 23 | 10 | √ | 0 | 完成工期 |
| 14 | factualtime | 实际工期 | numeric | 23 | 10 | √ | 0 | 实际工期 |
| 15 | ftrade | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 16 | ftaskstatus | 计划状态 | varchar | 5 |  | √ | ' ' | 计划状态,枚举: 1 :计划 2 :计划确认 3 :下达 4 :关闭 |
| 17 | fnlaststartdate | 尚需最晚开始时间 | timestamp | 0 |  |  | null | 尚需最晚开始时间 |
| 18 | fprofession | fprofession | int8 | 64 |  | √ | 0 |  |
| 19 | fplanenddate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 20 | ffunlocation | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 21 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 22 | fneedtime | 尚需工期 | numeric | 23 | 10 | √ | 0 | 尚需工期 |
| 23 | fbsenddate | 基线计划完成时间 | timestamp | 0 |  |  | null | 基线计划完成时间 |
| 24 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 版本 mpdm_gantt_version |
| 25 | factualhours | 实际人工工时 | numeric | 23 | 10 | √ | 0 | 实际人工工时 |
| 26 | fnlastenddate | 尚需最晚完成时间 | timestamp | 0 |  |  | null | 尚需最晚完成时间 |
| 27 | fplanarea | 计划区域 | int8 | 64 |  | √ | 0 | 计划区域 fmm_planningarea |
| 28 | ffinishpercent | 实际完成百分比(%) | numeric | 23 | 10 | √ | 0 | 实际完成百分比(%) |
| 29 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 任务编码 | varchar | 200 |  | √ | ' ' | 任务编码 |
| 31 | fworkshift | fworkshift | int8 | 64 |  | √ | 0 |  |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | fisbaseline | 是否基线 | bpchar | 1 |  | √ | '0' | 是否基线 |
| 34 | fscheduletype | 排程类型 | varchar | 5 |  | √ | ' ' | 排程类型,枚举: 1 :标准任务 2 :WBS汇总 3 :里程碑 4 :完成里程碑 |
| 35 | ftplid | 计划模板 | int8 | 64 |  | √ | 0 | 计划模板 pmpd_milestonetpl |
| 36 | flimittwodate | 限制日期2 | timestamp | 0 |  |  | null | 限制日期2 |
| 37 | fnfacilityhours | 尚需设备工时 | numeric | 23 | 10 | √ | 0 | 尚需设备工时 |
| 38 | fbslaterdate | 基线最早完成时间 | timestamp | 0 |  |  | null | 基线最早完成时间 |
| 39 | factualstartdate | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 40 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 41 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: A :任务 B :里程碑 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 44 | fpercenttype | 完成百分比类型 | varchar | 5 |  | √ | ' ' | 完成百分比类型,枚举: 1 :实际百分比 2 :工期百分比 3 :数量百分比 |
| 45 | ftotalfloattime | 总浮动时间 | numeric | 23 | 10 | √ | 0 | 总浮动时间 |
| 46 | fffacilityhours | 完成设备工时 | numeric | 23 | 10 | √ | 0 | 完成设备工时 |
| 47 | fentityid | 视图方案 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 48 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | fworkrange | 工作范围 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 50 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fresponspersonid | 责任人 | int8 | 64 |  | √ | 0 | 企业人力资源池 pmbd_enterprise_hm_res_po |
| 53 | fisspecial | 特殊任务 | bpchar | 1 |  | √ | '0' | 特殊任务 |
| 54 | ftimetype | 工期类型 | varchar | 5 |  | √ | ' ' | 工期类型,枚举: 1 :固定工期与资源总量 2 :固定单位时间用量 3 :固定资源用量 4 :固定工期与单位时间用量 |
| 55 | fplantime | 计划工期 | numeric | 23 | 10 | √ | 0 | 计划工期 |
| 56 | factualdate | 实际时间 | timestamp | 0 |  |  | null | 实际时间 |
| 57 | fresourceplanid | 检修主资源计划ID | int8 | 64 |  | √ | 0 | 检修主资源计划ID |
| 58 | fbaselinename | 基线计划名称 | varchar | 50 |  | √ | ' ' | 基线计划名称 |
| 59 | fbsearlydate | 基线最早开始时间 | timestamp | 0 |  |  | null | 基线最早开始时间 |
| 60 | fstandardtask | 标准任务清单 | int8 | 64 |  | √ | 0 | 标准任务清单 fmm_standardtask |
| 61 | fneedhours | 尚需人工工时 | numeric | 23 | 10 | √ | 0 | 尚需人工工时 |
| 62 | fuseorgid | 项目组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 63 | flaststartdate | 最晚开始时间 | timestamp | 0 |  |  | null | 最晚开始时间 |
| 64 | ffirststartdate | 最早开始时间 | timestamp | 0 |  |  | null | 最早开始时间 |
| 65 | fbsplaneqhour | 基线计划设备工时 | numeric | 23 | 10 | √ | 0 | 基线计划设备工时 |
| 66 | fworkpackage | 工作包名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 67 | fsourceid | 来源主键 | int8 | 64 |  | √ | 0 | 来源主键 |
| 68 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 69 | ffreefloattime | 自由浮动时间 | numeric | 23 | 10 | √ | 0 | 自由浮动时间 |
| 70 | fplanstartdate | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 71 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 72 | fnfirststartdate | 尚需最早开始时间 | timestamp | 0 |  |  | null | 尚需最早开始时间 |
| 73 | fsysactualper | 系统实际完成进度 | numeric | 23 | 10 | √ | 0 | 系统实际完成进度 |
| 74 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 75 | fbindstatus | 绑定状态 | varchar | 50 |  | √ | ' ' | 绑定状态,枚举: A :未绑定 B :已绑定 |
| 76 | flastenddate | 最晚完成时间 | timestamp | 0 |  |  | null | 最晚完成时间 |
| 77 | fdurationunitid | 工期单位 | int8 | 64 |  | √ | 0 | 工期单位 pmpd_timeunit |
| 78 | fviewschemeid | 样式方案 | int8 | 64 |  | √ | 0 | 样式方案 msplan_viewscheme |
| 79 | flimitone | 限制条件1 | varchar | 5 |  | √ | ' ' | 限制条件1,枚举: 1 :开始不早于 2 :开始日期 3 :开始不晚于 4 :完成不晚于 5 :完成日期 6 :完成不早于 |
| 80 | fismaxpath | 关键任务 | bpchar | 1 |  | √ | '0' | 关键任务 |
| 81 | fprojectstage | fprojectstage | int8 | 64 |  | √ | 0 |  |
| 82 | fbaselinetype | 基线类别 | varchar | 50 |  | √ | ' ' | 基线类别 |
| 83 | ffinishhours | 完成人工工时 | numeric | 23 | 10 | √ | 0 | 完成人工工时 |
| 84 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 85 | freporttime | 最近一次汇报日期 | timestamp | 0 |  |  | null | 最近一次汇报日期 |
| 86 | fhopeenddate | 期望完成时间 | timestamp | 0 |  |  | null | 期望完成时间 |
| 87 | forderno | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 88 | fworkloadunit | 工时单位 | varchar | 5 |  | √ | ' ' | 工时单位,枚举: 1 :H |
| 89 | fislcb | 是否里程碑 | bpchar | 1 |  | √ | '0' | 是否里程碑 |
| 90 | fimportanttask | 重要任务 | bpchar | 1 |  | √ | '0' | 重要任务 |
| 91 | fwbsid | WBS | int8 | 64 |  | √ | 0 | WBS pmts_wbs |
| 92 | fworkspace | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 93 | ftimeunit | 工期单位 | varchar | 5 |  | √ | ' ' | 工期单位,枚举: 1 :天 2 :周 |
| 94 | flimittwo | 限制条件2 | varchar | 5 |  | √ | ' ' | 限制条件2,枚举: 1 :开始不早于 2 :开始日期 3 :开始不晚于 4 :完成不晚于 5 :完成日期 6 :完成不早于 |
| 95 | fispushdemand | 下推项目需求清单 | bpchar | 1 |  | √ | '0' | 下推项目需求清单 |
| 96 | fpfacilityhours | 计划设备工时 | numeric | 23 | 10 | √ | 0 | 计划设备工时 |
| 97 | ffirstenddate | 最早完成时间 | timestamp | 0 |  |  | null | 最早完成时间 |
| 98 | ftasklevel | 任务层级 | varchar | 5 |  | √ | ' ' | 任务层级,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 |
| 99 | fpriority | 资源平衡优先级 | int4 | 32 |  | √ | 0 | 资源平衡优先级 |
| 100 | flimitonedate | 限制日期1 | timestamp | 0 |  |  | null | 限制日期1 |
| 101 | fispushproduct | 下推项目生产清单 | bpchar | 1 |  | √ | '0' | 下推项目生产清单 |
| 102 | fnfirstenddate | 尚需最早完成时间 | timestamp | 0 |  |  | null | 尚需最早完成时间 |
| 103 | fisautonumber | 是否自动编码 | bpchar | 1 |  | √ | '0' | 是否自动编码 |
| 104 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 105 | fresponsorgid | 责任单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 106 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 107 | fbsstartdate | 基线计划开始时间 | timestamp | 0 |  |  | null | 基线计划开始时间 |
| 108 | ftaskcalendarld | 任务日历 | int8 | 64 |  | √ | 0 | 设置项目日历_标准日历 pmbd_calendar_standard |
| 109 | fexecutestatus | 执行状态 | varchar | 5 |  | √ | ' ' | 执行状态,枚举: 1 :未开始 2 :进行中 3 :暂停 4 :已完成 |
| 110 | fplanner | 计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 111 | fbsplandate | 基线计划工期 | numeric | 23 | 10 | √ | 0 | 基线计划工期 |
| 112 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 113 | fplanhours | 计划人工工时 | numeric | 23 | 10 | √ | 0 | 计划人工工时 |
| 114 | fbsplanerhour | 基线计划人工工时 | numeric | 23 | 10 | √ | 0 | 基线计划人工工时 |
| 115 | fsourceplantypeid | 来源计划类型 | int8 | 64 |  | √ | 0 | 项目计划类型 fmm_plantype |
| 116 | fplantype | 项目计划类型 | int8 | 64 |  | √ | 0 | 项目计划类型 fmm_plantype |
| 117 | ffloattime | 尚需浮时 | numeric | 23 | 10 | √ | 0 | 尚需浮时 |
| 118 | ftplentryid | 计划模板分录ID | int8 | 64 |  | √ | 0 | 计划模板分录ID |
| 119 | fresourcestatus | 资源状态 | varchar | 50 |  | √ | ' ' | 资源状态,枚举: A :未就绪 B :已就绪 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pmts_task_master |  | fmasterid |
| 2 | idx_pmts_task_fcreatetime |  | fcreatetime |
| 3 | pk_t_pmts_task |  | fid |
| 4 | idx_t_pmts_task_createorg |  | fcreateorgid |
| 5 | idx_pmts_task_fnumber |  | fnumber |

---

## 前置作业关系-子表 t_pmts_pre_task

- **表名称：** 前置作业关系-子表
- **表名：** t_pmts_pre_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskrelation | 任务关系 | varchar | 5 |  | √ | ' ' | 任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 3 | fprepositiontaskid | 前置任务 | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpredelayed | 延时 | numeric | 23 | 10 | √ | 0 | 延时 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_pre_task |  | fentryid |
| 2 | idx_preposition_task_fid |  | fid |

---

## 关联子实体-子表 t_pmts_task_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pmts_task_lk

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
| 1 | idx_pmts_task_lk_fk |  | fid |
| 2 | pk_pmts_task_lk |  | fpkid |

---

## 文档-子表 t_pmts_documententry

- **表名称：** 文档-子表
- **表名：** t_pmts_documententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuploadperson | 最新上传人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftaskreportid | 汇报ID | int8 | 64 |  | √ | 0 | 汇报ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdocname | 文档名称 | varchar | 50 |  | √ | ' ' | 文档名称 |
| 6 | forderno | forderno | int8 | 64 |  | √ | 0 |  |
| 7 | fdeliverablesid | 交付物单据内码 | int8 | 64 |  | √ | 0 | 交付物单据内码 |
| 8 | fweight | 权数 | numeric | 23 | 10 | √ | 0 | 权数 |
| 9 | fdoctype | 文档类型 | varchar | 5 |  | √ | ' ' | 文档类型,枚举: 1 :项目 2 :私有 |
| 10 | fbasedatafield | 关联模板 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fdocnumber | 文档编码 | varchar | 50 |  | √ | ' ' | 文档编码 |
| 12 | fdonestatus | 完成状态 | varchar | 5 |  | √ | ' ' | 完成状态,枚举: 1 :计划 2 :完成 |
| 13 | fisfrompd | 是否来源项目交付物 | bpchar | 1 |  | √ | '0' | 是否来源项目交付物 |
| 14 | fuploaddate | 最新上传日期 | timestamp | 0 |  |  | null | 最新上传日期 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fdocplandate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_docury_fid |  | fid |
| 2 | idx_pmts_docury_fseq |  | fseq |
| 3 | pk_pmts_documententry |  | fentryid |

---

## 附件-附件表 t_pmts_attachment

- **表名称：** 附件-附件表
- **表名：** t_pmts_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pmts_attachment |  | fpkid |

---

## 项目阶段-多选基础资料表 t_fmm_projectstage

- **表名称：** 项目阶段-多选基础资料表
- **表名：** t_fmm_projectstage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目阶段 pmbd_projectstage |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_projectstage |  | fpkid |
| 2 | idx_fmm_projectstage_fbas |  | fid,fbasedataid |

---

## 浮时路径-子表 t_pmts_floatpathentry

- **表名称：** 浮时路径-子表
- **表名：** t_pmts_floatpathentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ffloatpath | 浮时路径 | varchar | 50 |  | √ | ' ' | 浮时路径 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ffloatpathseq | 浮时路径序号 | varchar | 50 |  | √ | ' ' | 浮时路径序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_floary_fid |  | fid |
| 2 | idx_pmts_floary_fseq |  | fseq |
| 3 | pk_pmts_floatpathentry |  | fentryid |
