# 项目-plm_ipd_project

## 项目-多语言表 t_plm_ipd_project_l

- **表名称：** 项目-多语言表
- **表名：** t_plm_ipd_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
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

---

## 项目-主表 t_plm_ipd_project

- **表名称：** 项目-主表
- **表名：** t_plm_ipd_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 项目经理 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fintegerfield | fintegerfield | int8 | 64 |  | √ | 0 |  |
| 4 | ftextfield1 | ftextfield1 | varchar | 50 |  | √ | ' ' |  |
| 5 | fgroupid | 项目分组 | int8 | 64 |  | √ | 0 | 项目分组 plm_pm_projectgroup |
| 6 | factworkinghours | 实际工时(h) | numeric | 23 | 10 | √ | 0 | 实际工时(h) |
| 7 | fdeviationrate | 偏差率（%） | numeric | 23 | 10 | √ | 0 | 偏差率（%） |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fmulilangtextfield | fmulilangtextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 11 | fabstractordesc | fabstractordesc | int8 | 64 |  | √ | 0 |  |
| 12 | fleaf | fleaf | bpchar | 1 |  | √ | '1' |  |
| 13 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 14 | frelatmilestone | frelatmilestone | int8 | 64 |  | √ | 0 |  |
| 15 | ftestend | ftestend | timestamp | 0 |  |  | null |  |
| 16 | fprioritylevel | fprioritylevel | varchar | 50 |  | √ | ' ' |  |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstepperfield | fstepperfield | numeric | 23 | 10 | √ | 0 |  |
| 19 | freleasetype | freleasetype | varchar | 50 |  | √ | ' ' |  |
| 20 | fendtimeoffset | fendtimeoffset | numeric | 23 | 10 | √ | 0 |  |
| 21 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 22 | fprojectteamid | fprojectteamid | int8 | 64 |  | √ | 0 |  |
| 23 | fwbsnumber | fwbsnumber | varchar | 50 |  | √ | ' ' |  |
| 24 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 25 | factconstructionperiod | 实际工期(天) | numeric | 23 | 10 | √ | 0 | 实际工期(天) |
| 26 | ftimerangeendtime | 时间范围.结束 | int4 | 32 |  | √ | '-1' | 时间范围.结束 |
| 27 | fprogression | 计划进度（%） | numeric | 23 | 10 | √ | 0 | 计划进度（%） |
| 28 | freasons | freasons | varchar | 50 |  | √ | ' ' |  |
| 29 | fdatefield | fdatefield | timestamp | 0 |  |  | null |  |
| 30 | fdecimalfield | fdecimalfield | numeric | 23 | 10 | √ | 0 |  |
| 31 | ftimerangestarttime | 时间范围.开始 | int4 | 32 |  | √ | '-1' | 时间范围.开始 |
| 32 | fparentitem | fparentitem | int8 | 64 |  | √ | 0 |  |
| 33 | ftemporary | ftemporary | bpchar | 1 |  | √ | '0' |  |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fcalendarexampleid | 日历实例 | int8 | 64 |  | √ | 0 | 配置-项目日历 plm_ipd_projectcal |
| 36 | fnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 37 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 38 | fconstructionperiod | 计划工期(天) | numeric | 23 | 10 | √ | 0 | 计划工期(天) |
| 39 | fexistprojectld | 已有项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 40 | fstartoffset | fstartoffset | numeric | 23 | 10 | √ | 0 |  |
| 41 | fprojectkind | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 plm_pm_projectkind |
| 42 | fcontrolmode | 管控模式 | varchar | 50 |  | √ | ' ' | 管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 43 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |
| 44 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 45 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 46 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fbelongproject | fbelongproject | int8 | 64 |  | √ | 0 |  |
| 49 | fcreatetype | 项目创建方式 | varchar | 50 |  | √ | ' ' | 项目创建方式,枚举: 1 :手动新建 2 :引用项目模板新建 3 :复制已有项目新建 |
| 50 | fcompilationtype | 状态 | int8 | 64 |  | √ | 0 | 项目状态 plm_pm_projectstatus |
| 51 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 52 | factprogression | 实际进度（%） | numeric | 23 | 10 | √ | 0 | 实际进度（%） |
| 53 | fworkinghours | 计划工时(h) | numeric | 23 | 10 | √ | 0 | 计划工时(h) |
| 54 | fprojectmanagerld | fprojectmanagerld | int8 | 64 |  | √ | 0 |  |
| 55 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fopen | fopen | bpchar | 1 |  | √ | '0' |  |
| 57 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fnumberdel | fnumberdel | int8 | 64 |  | √ | 0 |  |
| 60 | fprojectkindld | fprojectkindld | int8 | 64 |  | √ | 0 |  |
| 61 | fdeadlinesubtime | fdeadlinesubtime | timestamp | 0 |  |  | null |  |
| 62 | fcreatetplid | fcreatetplid | int8 | 64 |  | √ | 0 |  |
| 63 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 64 | fcreatebasetype | fcreatebasetype | varchar | 50 |  | √ | ' ' |  |
| 65 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 66 | fteststart | fteststart | timestamp | 0 |  |  | null |  |
| 67 | fdecompositiontype | fdecompositiontype | varchar | 50 |  | √ | ' ' |  |
| 68 | factdeadlinesubtime | factdeadlinesubtime | timestamp | 0 |  |  | null |  |
| 69 | ftimefield | ftimefield | int4 | 32 |  | √ | '-1' |  |
| 70 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 71 | fcheckboxfield | fcheckboxfield | bpchar | 1 |  | √ | '0' |  |
| 72 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 73 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 74 | fprojectcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | 日历模版 plm_ipd_calendar |
| 75 | fcombofield | fcombofield | varchar | 50 |  | √ | ' ' |  |

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
