# 项目-plm_ipd_project

## 项目-主表 t_plm_ipd_project

- **表名称：** 项目-主表
- **表名：** t_plm_ipd_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 项目经理 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fintegerfield | fintegerfield | int8 | 64 |  | √ | 0 |  |
| 4 | fproductlib | 产品库 | int8 | 64 |  | √ | 0 | [产品库 plm_pdm_repo_product](../plmpdm_files/plm_pdm_repo_product.md) |
| 5 | ftextfield1 | ftextfield1 | varchar | 50 |  | √ | ' ' |  |
| 6 | fgroupid | 项目分组 | int8 | 64 |  | √ | 0 | [项目分组 plm_pm_projectgroup](../plmpm_files/plm_pm_projectgroup.md) |
| 7 | factworkinghours | 实际工时(h) | numeric | 23 | 10 | √ | 0 | 实际工时(h) |
| 8 | fdeviationrate | 偏差率（%） | numeric | 23 | 10 | √ | 0 | 偏差率（%） |
| 9 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 10 | fmulilangtextfield | fmulilangtextfield | varchar | 50 |  | √ | ' ' |  |
| 11 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 12 | fabstractordesc | fabstractordesc | int8 | 64 |  | √ | 0 |  |
| 13 | fleaf | fleaf | bpchar | 1 |  | √ | '1' |  |
| 14 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 15 | frelatmilestone | frelatmilestone | int8 | 64 |  | √ | 0 |  |
| 16 | ftestend | ftestend | timestamp | 0 |  |  | null |  |
| 17 | fprioritylevel | fprioritylevel | varchar | 50 |  | √ | ' ' |  |
| 18 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 19 | fstepperfield | fstepperfield | numeric | 23 | 10 | √ | 0 |  |
| 20 | freleasetype | freleasetype | varchar | 50 |  | √ | ' ' |  |
| 21 | fendtimeoffset | fendtimeoffset | numeric | 23 | 10 | √ | 0 |  |
| 22 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fprojectteamid | fprojectteamid | int8 | 64 |  | √ | 0 |  |
| 24 | fwbsnumber | fwbsnumber | varchar | 50 |  | √ | ' ' |  |
| 25 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 26 | factconstructionperiod | 实际工期(天) | numeric | 23 | 10 | √ | 0 | 实际工期(天) |
| 27 | fprojecttplid | 项目模板 | int8 | 64 |  | √ | 0 | [项目模板 plm_pm_projecttpl](../plmpm_files/plm_pm_projecttpl.md) |
| 28 | ftimerangeendtime | 时间范围.结束 | int4 | 32 |  | √ | '-1' | 时间范围.结束 |
| 29 | fprogression | 计划进度（%） | numeric | 23 | 10 | √ | 0 | 计划进度（%） |
| 30 | freasons | freasons | varchar | 50 |  | √ | ' ' |  |
| 31 | fdatefield | fdatefield | timestamp | 0 |  |  | null |  |
| 32 | fdecimalfield | fdecimalfield | numeric | 23 | 10 | √ | 0 |  |
| 33 | ftimerangestarttime | 时间范围.开始 | int4 | 32 |  | √ | '-1' | 时间范围.开始 |
| 34 | fparentitem | fparentitem | int8 | 64 |  | √ | 0 |  |
| 35 | fsourcebdprojectid | 源主数据项目id | int8 | 64 |  | √ | 0 | 源主数据项目id |
| 36 | ftemporary | ftemporary | bpchar | 1 |  | √ | '0' |  |
| 37 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fcalendarexampleid | 日历实例 | int8 | 64 |  | √ | 0 | [配置-项目日历 plm_ipd_projectcal](../plmpm_files/plm_ipd_projectcal.md) |
| 39 | fnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 40 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 41 | fconstructionperiod | 计划工期(天) | numeric | 23 | 10 | √ | 0 | 计划工期(天) |
| 42 | fexistprojectld | 已有项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 43 | fstartoffset | fstartoffset | numeric | 23 | 10 | √ | 0 |  |
| 44 | fproductgroupid | 产品分组 | int8 | 64 |  | √ | 0 | [产品分组 plm_pdm_productgroup](../plmpdm_files/plm_pdm_productgroup.md) |
| 45 | fprojectkind | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 plm_pm_projectkind](../plmpm_files/plm_pm_projectkind.md) |
| 46 | fisproffield | 启用专业领域计划 | bpchar | 1 |  | √ | '0' | 启用专业领域计划 |
| 47 | fcontrolmode | 管控模式 | varchar | 50 |  | √ | ' ' | 管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 48 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |
| 49 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: changing :变更中 |
| 50 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 51 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 52 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fbelongproject | fbelongproject | int8 | 64 |  | √ | 0 |  |
| 55 | fcreatetype | 项目创建方式 | varchar | 50 |  | √ | ' ' | 项目创建方式,枚举: 1 :手动新建 2 :引用项目模板新建 3 :复制已有项目新建 |
| 56 | fcompilationtype | 状态 | int8 | 64 |  | √ | 0 | [项目状态 plm_pm_projectstatus](../plmpm_files/plm_pm_projectstatus.md) |
| 57 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 58 | fprocharterid | 项目任务书 | int8 | 64 |  | √ | 0 | 项目任务书 |
| 59 | factprogression | 实际进度（%） | numeric | 23 | 10 | √ | 0 | 实际进度（%） |
| 60 | fworkinghours | 计划工时(h) | numeric | 23 | 10 | √ | 0 | 计划工时(h) |
| 61 | fprojectmanagerld | fprojectmanagerld | int8 | 64 |  | √ | 0 |  |
| 62 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fopen | fopen | bpchar | 1 |  | √ | '0' |  |
| 64 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 65 | fbdprojectid | 主数据项目id | int8 | 64 |  | √ | 0 | 主数据项目id |
| 66 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 67 | fnumberdel | fnumberdel | int8 | 64 |  | √ | 0 |  |
| 68 | fprojectkindld | fprojectkindld | int8 | 64 |  | √ | 0 |  |
| 69 | fdeadlinesubtime | fdeadlinesubtime | timestamp | 0 |  |  | null |  |
| 70 | fcreatetplid | fcreatetplid | int8 | 64 |  | √ | 0 |  |
| 71 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 72 | fcreatebasetype | fcreatebasetype | varchar | 50 |  | √ | ' ' |  |
| 73 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 74 | fteststart | fteststart | timestamp | 0 |  |  | null |  |
| 75 | fdecompositiontype | fdecompositiontype | varchar | 50 |  | √ | ' ' |  |
| 76 | factdeadlinesubtime | factdeadlinesubtime | timestamp | 0 |  |  | null |  |
| 77 | ftimefield | ftimefield | int4 | 32 |  | √ | '-1' |  |
| 78 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 79 | fcheckboxfield | fcheckboxfield | bpchar | 1 |  | √ | '0' |  |
| 80 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 81 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 82 | fprojectcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | [日历模板 plm_ipd_calendar](../plmpm_files/plm_ipd_calendar.md) |
| 83 | fcombofield | fcombofield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_project_fnumber |  | fnumber |
| 2 | idx_plm_ipd_project_fnumber |  | fnumber |
| 3 | idx_plm_ipd_project_m0 |  | fmasterid |
| 4 | pk_plm_ipd_project |  | fid |

---

## 关联子实体-子表 t_plm_ipd_project_lk

- **表名称：** 关联子实体-子表
- **表名：** t_plm_ipd_project_lk

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
| 1 | idx_plm_ipd_project_lk_fk |  | fid |
| 2 | pk_plm_ipd_project_lk |  | fpkid |

---

## 项目-多语言表 t_plm_ipd_project_l

- **表名称：** 项目-多语言表
- **表名：** t_plm_ipd_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 80 |  | √ | ' ' | 项目名称 |
| 3 | fmulilangtextfield | fmulilangtextfield | varchar | 50 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_project_l |  | fpkid |
| 2 | idx_plm_ipd_project_l_0 |  | fid,flocaleid |
