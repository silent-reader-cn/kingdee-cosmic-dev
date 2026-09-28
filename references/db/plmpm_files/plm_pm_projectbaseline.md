# 项目基线-plm_pm_projectbaseline

## 项目基线-主表 t_plm_pm_probaseline

- **表名称：** 项目基线-主表
- **表名：** t_plm_pm_probaseline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 项目经理 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fconstructionperiod | 计划工期(天) | numeric | 23 | 1 | √ | 0 | 计划工期(天) |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fproductlib | 产品库 | int8 | 64 |  | √ | 0 | [产品库 plm_pdm_repo_product](../plmpdm_files/plm_pdm_repo_product.md) |
| 5 | factworkinghours | 实际工时(h) | numeric | 23 | 1 | √ | 0 | 实际工时(h) |
| 6 | fgroupid | 项目分组 | int8 | 64 |  | √ | 0 | [工作项类型配置 plm_ipditemgroup](../plmipdsm_files/plm_ipditemgroup.md) |
| 7 | fexistprojectld | 原项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 8 | fdeviationrate | 偏差率（%） | numeric | 23 | 1 | √ | 0 | 偏差率（%） |
| 9 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 10 | fprojectkind | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 plm_pm_projectkind](../plmpm_files/plm_pm_projectkind.md) |
| 11 | fisproffield | 启用专业领域计划 | bpchar | 1 |  | √ | '0' | 启用专业领域计划 |
| 12 | fcontrolmode | 管控模式 | varchar | 50 |  | √ | ' ' | 管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetype | 创建方式 | varchar | 50 |  | √ | ' ' | 创建方式,枚举: 1 :手动创建 4 :变更创建 |
| 19 | fcompilationtype | 状态 | int8 | 64 |  | √ | 0 | [项目状态 plm_pm_projectstatus](../plmpm_files/plm_pm_projectstatus.md) |
| 20 | fprocharterid | 项目任务书 | int8 | 64 |  | √ | 0 | 项目任务书 |
| 21 | factprogression | 实际进度（%） | numeric | 23 | 1 | √ | 0 | 实际进度（%） |
| 22 | fworkinghours | 计划工时(h) | numeric | 23 | 1 | √ | 0 | 计划工时(h) |
| 23 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 26 | fbdprojectid | 主数据项目id | int8 | 64 |  | √ | 0 | 主数据项目id |
| 27 | factconstructionperiod | 实际工期(天) | numeric | 23 | 1 | √ | 0 | 实际工期(天) |
| 28 | fprojecttplid | 项目模版 | int8 | 64 |  | √ | 0 | [项目模板 plm_pm_projecttpl](../plmpm_files/plm_pm_projecttpl.md) |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fprogression | 计划进度（%） | numeric | 23 | 1 | √ | 0 | 计划进度（%） |
| 31 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fcalendarexampleid | 日历实例 | int8 | 64 |  | √ | 0 | [配置-项目日历 plm_ipd_projectcal](../plmpm_files/plm_ipd_projectcal.md) |
| 34 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 35 | fnumber | 项目编码 | varchar | 30 |  | √ | ' ' | 项目编码 |
| 36 | fprojectcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | [日历模板 plm_ipd_calendar](../plmpm_files/plm_ipd_calendar.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_probaseline |  | fid |
| 2 | idx_plm_pm_probaseline_m0 |  | fnumber |

---

## 项目基线-多语言表 t_plm_pm_probaseline_l

- **表名称：** 项目基线-多语言表
- **表名：** t_plm_pm_probaseline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 项目名称 | varchar | 80 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_probaseline_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pm_probaseline_l |  | fpkid |
