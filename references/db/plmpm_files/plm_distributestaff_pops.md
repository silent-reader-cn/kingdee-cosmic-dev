# 下发编制-plm_distributestaff_pops

## 单据体-子表 t_plm_pm_distrstaffpopsen

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_distrstaffpopsen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | ftaskgroupid1 | 任务组id | varchar | 50 |  | √ | ' ' | 任务组id |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fpublishuser | fpublishuser | int8 | 64 |  | √ | 0 |  |
| 5 | fsubmitdeadline | 提交截止时间 | timestamp | 0 |  |  | null | 提交截止时间 |
| 6 | fprojectid | 项目ID | varchar | 60 |  | √ | ' ' | 项目ID |
| 7 | fflowflag | fflowflag | varchar | 50 |  | √ | ' ' |  |
| 8 | ffieldplan | ffieldplan | int8 | 64 |  | √ | 0 |  |
| 9 | fpublishtime | fpublishtime | timestamp | 0 |  |  | null |  |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | factsubmittime | 实际提交时间 | timestamp | 0 |  |  | null | 实际提交时间 |
| 12 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftextfield | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 14 | fdistributetime | 下发时间 | timestamp | 0 |  |  | null | 下发时间 |
| 15 | fcreaterfield | 下发人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fprofield | fprofield | int8 | 64 |  | √ | 0 |  |
| 18 | fcompilationtype | 编制状态 | int8 | 64 |  | √ | 0 | [任务状态 plm_pm_taskstatus](../plmpm_files/plm_pm_taskstatus.md) |
| 19 | fdistributeuser | fdistributeuser | int8 | 64 |  | √ | 0 |  |
| 20 | ftaskgroupld | 任务组 | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_distrstaffpopsen_fk |  | fid |
| 2 | pk_plm_pm_distrstaffpopsen |  | fentryid |

---

## 下发编制-主表 t_plm_pm_distrstaffpops

- **表名称：** 下发编制-主表
- **表名：** t_plm_pm_distrstaffpops

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbelongproject | 所属项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fitemclasstype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: plm_ipd_project :项目 plm_pm_projecttpl :项目模板 plm_pm_projectcopy :项目副本 plm_pm_projectbaseline :项目基线 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_distrstaff_number |  | fbillno |
| 2 | pk_plm_pm_distrstaffpops |  | fid |
