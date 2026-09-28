# 任务基线-plm_pm_taskbaseline

## 单据体-子表 t_plm_ipd_tasklineentity

- **表名称：** 单据体-子表
- **表名：** t_plm_ipd_tasklineentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasetypeitem | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型,枚举: plm_pm_projectbaseline :项目基线 plm_pm_taskbaseline :任务基线 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :完成-开始(FS) 2 :完成-完成(FF) 3 :开始-完成(SF) 1 :开始-开始(SS) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparentstage | 任务名称 | int8 | 64 |  | √ | 0 | 项目基线 plm_pm_projectbaseline |
| 6 | fpostponedate | 延隔日期（day） | numeric | 23 | 10 | √ | 0 | 延隔日期（day） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_tasklineentity_fk |  | fid |
| 2 | pk_plm_ipd_tasklineentity |  | fentryid |

---

## 任务基线-主表 t_plm_ipd_taskbaseline

- **表名称：** 任务基线-主表
- **表名：** t_plm_ipd_taskbaseline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | factworkinghours | 实际工时(h) | numeric | 23 | 1 | √ | 0 | 实际工时(h) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [工作项类型配置 plm_ipditemgroup](../plmipdsm_files/plm_ipditemgroup.md) |
| 5 | fdeviationrate | 偏差率（%） | numeric | 23 | 1 | √ | 0 | 偏差率（%） |
| 6 | ftaskfield | 所属领域 | int8 | 64 |  | √ | 0 | [专业领域 plm_pm_proffield](../plmpm_files/plm_pm_proffield.md) |
| 7 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 8 | fabstractordesc | 描述 | int8 | 64 |  | √ | 0 | [描述大文本 plm_ipd_description](../plmipdsm_files/plm_ipd_description.md) |
| 9 | fleaf | 是否叶子节点 | bpchar | 1 |  | √ | '1' | 是否叶子节点 |
| 10 | fstateapprovalchain | 启用状态转换流程审批 | bpchar | 1 |  | √ | '0' | 启用状态转换流程审批 |
| 11 | frelatmilestone | 关联里程碑 | int8 | 64 |  | √ | 0 | [里程碑 plm_ipd_milestone](../plmpm_files/plm_ipd_milestone.md) |
| 12 | freportdate | 汇报时间 | timestamp | 0 |  |  | null | 汇报时间 |
| 13 | fapprovalworkhous | 启用工时审批 | bpchar | 1 |  | √ | '0' | 启用工时审批 |
| 14 | fprioritylevel | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: A :高 B :较高 C :中 D :较低 E :低 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fgeneralrole | 通用角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 17 | fseqnumber | 顺序 | varchar | 100 |  | √ | ' ' | 顺序 |
| 18 | fendtimeoffset | 结束偏差值（天） | numeric | 23 | 1 | √ | 0 | 结束偏差值（天） |
| 19 | fwbsnumber | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 20 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 21 | factconstructionperiod | 实际工期(天) | numeric | 23 | 1 | √ | 0 | 实际工期(天) |
| 22 | fprogression | 计划进度（%） | numeric | 23 | 1 | √ | 0 | 计划进度（%） |
| 23 | freasons | 延期原因 | varchar | 50 |  | √ | ' ' | 延期原因 |
| 24 | fparentitem | 父项 | int8 | 64 |  | √ | 0 | [任务基线 plm_pm_taskbaseline](../plmpm_files/plm_pm_taskbaseline.md) |
| 25 | felectdstatus | 启用流程审批状态选择 | varchar | 50 |  | √ | ' ' | 启用流程审批状态选择,枚举: start :启动 finish :完成 pause :暂停 recovery :恢复 terminate :终止 |
| 26 | ftemporary | 是否临时 | bpchar | 1 |  | √ | '0' | 是否临时 |
| 27 | fapprovalres_tag | 审批意见_详情 | text | 0 |  |  | null | 审批意见_详情 |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | freportperson | 汇报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | fconstructionperiod | 计划工期(天) | numeric | 23 | 1 | √ | 0 | 计划工期(天) |
| 32 | fstartoffset | 开始偏差值（天） | numeric | 23 | 1 | √ | 0 | 开始偏差值（天） |
| 33 | fprophase | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 34 | fprojectkind | 分类 | int8 | 64 |  | √ | 0 | [任务分类 plm_pm_taskkind](../plmpm_files/plm_pm_taskkind.md) |
| 35 | fselfasslevel | 自评等级 | varchar | 50 |  | √ | ' ' | 自评等级,枚举: 0 :卓越 1 :优秀 2 :良好 |
| 36 | fsource | 任务来源 | varchar | 50 |  | √ | ' ' | 任务来源,枚举: S :手工新增 X :需求创建 |
| 37 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fbelongproject | 所属项目 | int8 | 64 |  | √ | 0 | [项目基线 plm_pm_projectbaseline](../plmpm_files/plm_pm_projectbaseline.md) |
| 42 | fcompilationtype | 状态 | int8 | 64 |  | √ | 0 | [任务状态 plm_pm_taskstatus](../plmpm_files/plm_pm_taskstatus.md) |
| 43 | fapprovalres | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 44 | factprogression | 实际进度（%） | numeric | 23 | 1 | √ | 0 | 实际进度（%） |
| 45 | fworkinghours | 计划工时(h) | numeric | 23 | 1 | √ | 0 | 计划工时(h) |
| 46 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fopen | 任务组是否展开 | bpchar | 1 |  | √ | '0' | 任务组是否展开 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fconfirmevel | 确认等级 | varchar | 50 |  | √ | ' ' | 确认等级,枚举: 0 :卓越 1 :优秀 2 :良好 |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fnumberdel | 是否有交付物/交付物数量 | int8 | 64 |  | √ | 0 | 是否有交付物/交付物数量 |
| 52 | fsourcetask | 原任务 | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 53 | fdeadlinesubtime | 阶段编制截止提交时间 | timestamp | 0 |  |  | null | 阶段编制截止提交时间 |
| 54 | fdistfield | 领域下发 | bpchar | 1 |  | √ | '0' | 领域下发 |
| 55 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 56 | fdecompositiontype | 分解类型 | varchar | 50 |  | √ | ' ' | 分解类型,枚举: subproject :子项目 task :任务 taskgroup :任务组 milestone :里程碑 temptask :临时任务 |
| 57 | factdeadlinesubtime | 阶段编制实际提交时间 | timestamp | 0 |  |  | null | 阶段编制实际提交时间 |
| 58 | fisessential | 是否关键任务 | bpchar | 1 |  | √ | '0' | 是否关键任务 |
| 59 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 60 | fprjrole | 项目角色 | int8 | 64 |  | √ | 0 | [项目权限模板 plm_pm_prjrole](../plmpm_files/plm_pm_prjrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_taskbaseline_m0 |  | fmasterid |
| 2 | pk_plm_ipd_taskbaseline |  | fid |

---

## 任务基线-多语言表 t_plm_ipd_taskbaseline_l

- **表名称：** 任务基线-多语言表
- **表名：** t_plm_ipd_taskbaseline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_taskbaseline_l |  | fpkid |
| 2 | idx_plm_ipd_taskbaseline_l_0 |  | fid,flocaleid |

---

## 协作单据体-子表 t_plm_ipd_lineaboraentity

- **表名称：** 协作单据体-子表
- **表名：** t_plm_ipd_lineaboraentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcollaborarole | 协作角色 | varchar | 50 |  | √ | ' ' | 协作角色,枚举: 1 :任务负责人 2 :协作人 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fbaseuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fproportion | 权重（%） | int8 | 64 |  | √ | 0 | 权重（%） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_lineaboraentity_fk |  | fid |
| 2 | pk_plm_ipd_lineaboraentity |  | fentryid |
