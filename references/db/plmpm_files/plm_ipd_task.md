# 任务-plm_ipd_task

## 协作单据体-子表 t_plm_ipd_collaboraentity

- **表名称：** 协作单据体-子表
- **表名：** t_plm_ipd_collaboraentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcollaborarole | 协作角色 | bpchar | 1 |  | √ | ' ' | 协作角色,枚举: 1 :任务负责人 2 :协作人 |
| 3 | fbaseuser | 用户 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fuseractworkinghours | fuseractworkinghours | numeric | 23 | 10 | √ | 0 |  |
| 5 | fpermissionrole | fpermissionrole | int8 | 64 |  |  | null |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcollaborativerole | fcollaborativerole | varchar | 50 |  | √ | ' ' |  |
| 8 | fproportion | 权重（%） | int8 | 64 |  |  | null | 权重（%） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_collaboraentity_fk |  | fid |
| 2 | pk_plm_ipd_collaboraentity |  | fentryid |

---

## 任务-多语言表 t_plm_ipd_task_l

- **表名称：** 任务-多语言表
- **表名：** t_plm_ipd_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_task_l_0 |  | fid,flocaleid |
| 2 | pk_plm_ipd_task_l |  | fpkid |

---

## 单据体-子表 t_plm_ipd_taskentity

- **表名称：** 单据体-子表
- **表名：** t_plm_ipd_taskentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasetypeitem | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型,枚举: plm_ipd_task :IPD任务 plm_ipd_project :IPD项目 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :完成-开始(FS) 2 :完成-完成(FF) 3 :开始-完成(SF) 1 :开始-开始(SS) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparentstage | 任务名称 | int8 | 64 |  |  | null | 任务 plm_ipd_task |
| 6 | fpostponedate | 延隔日期（day） | numeric | 23 | 10 | √ | 0 | 延隔日期（day） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_taskentity |  | fentryid |
| 2 | idx_plm_ipd_taskentity_fk |  | fid |

---

## 任务-主表 t_plm_ipd_task

- **表名称：** 任务-主表
- **表名：** t_plm_ipd_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 工作项类型配置 plm_ipditemgroup |
| 4 | factworkinghours | 实际工时(h) | numeric | 23 | 10 | √ | 0 | 实际工时(h) |
| 5 | fdeviationrate | 偏差率（%） | numeric | 23 | 10 | √ | 0 | 偏差率（%） |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 8 | fabstractordesc | 描述 | int8 | 64 |  | √ | 0 | 描述大文本 plm_ipd_description |
| 9 | fleaf | 是否叶子节点 | bpchar | 1 |  | √ | '1' | 是否叶子节点 |
| 10 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 11 | frelatmilestone | 关联里程碑 | int8 | 64 |  | √ | 0 | 里程碑 plm_ipd_milestone |
| 12 | freportdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 13 | fprioritylevel | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: A :高 B :较高 C :中 D :较低 E :低 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | freleasetype | freleasetype | varchar | 50 |  | √ | ' ' |  |
| 16 | fendtimeoffset | 结束偏差值（天） | numeric | 23 | 10 | √ | 0 | 结束偏差值（天） |
| 17 | fbitindex | fbitindex | int8 | 64 |  |  | null |  |
| 18 | fwbsnumber | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | factconstructionperiod | 实际工期(天) | numeric | 23 | 10 | √ | 0 | 实际工期(天) |
| 21 | fprogression | 计划进度（%） | numeric | 23 | 10 | √ | 0 | 计划进度（%） |
| 22 | freasons | 延期原因 | varchar | 50 |  | √ | ' ' | 延期原因 |
| 23 | fparentitem | 父项 | int8 | 64 |  | √ | 0 | 任务 plm_ipd_task |
| 24 | ftemporary | 是否临时 | bpchar | 1 |  | √ | '0' | 是否临时 |
| 25 | fapprovalres_tag | 审批意见_详情 | text | 0 |  |  | null | 审批意见_详情 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | freportperson | 汇报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fsourcebitindex | fsourcebitindex | int8 | 64 |  |  | null |  |
| 30 | fconstructionperiod | 计划工期(天) | numeric | 23 | 10 | √ | 0 | 计划工期(天) |
| 31 | fstartoffset | 开始偏差值（天） | numeric | 23 | 10 | √ | 0 | 开始偏差值（天） |
| 32 | fprojectkind | 分类 | int8 | 64 |  | √ | 0 | 任务分类 plm_pm_taskkind |
| 33 | fselfasslevel | 自评等级 | varchar | 50 |  | √ | ' ' | 自评等级,枚举: 0 :卓越 1 :优秀 2 :良好 |
| 34 | fsource | 任务来源 | varchar | 50 |  | √ | ' ' | 任务来源,枚举: S :手工新增 X :需求创建 |
| 35 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 37 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fbelongproject | 所属项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 40 | fcompilationtype | 状态 | int8 | 64 |  | √ | 0 | 任务状态 plm_pm_taskstatus |
| 41 | fsourcedataid | fsourcedataid | int8 | 64 |  |  | null |  |
| 42 | fapprovalres | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 43 | factprogression | 实际进度（%） | numeric | 23 | 10 | √ | 0 | 实际进度（%） |
| 44 | fworkinghours | 计划工时(h) | numeric | 23 | 10 | √ | 0 | 计划工时(h) |
| 45 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fopen | 任务组是否展开 | bpchar | 1 |  | √ | '0' | 任务组是否展开 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fconfirmevel | 确认等级 | varchar | 50 |  | √ | ' ' | 确认等级,枚举: 0 :卓越 1 :优秀 2 :良好 |
| 50 | fnumberdel | 是否有交付物/交付物数量 | int8 | 64 |  | √ | 0 | 是否有交付物/交付物数量 |
| 51 | fdeadlinesubtime | 阶段编制截止提交时间 | timestamp | 0 |  |  | null | 阶段编制截止提交时间 |
| 52 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 53 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 54 | fdecompositiontype | 分解类型 | varchar | 50 |  | √ | ' ' | 分解类型,枚举: subproject :子项目 task :任务 taskgroup :任务组 milestone :里程碑 temptask :临时任务 |
| 55 | factdeadlinesubtime | 阶段编制实际提交时间 | timestamp | 0 |  |  | null | 阶段编制实际提交时间 |
| 56 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 57 | fuseorgid | fuseorgid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_task |  | fid |
| 2 | idx_plm_ipd_task_m0 |  | fmasterid |
