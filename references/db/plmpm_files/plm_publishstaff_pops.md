# 发布任务-plm_publishstaff_pops

## 发布任务-主表 t_plm_publishstaffpops

- **表名称：** 发布任务-主表
- **表名：** t_plm_publishstaffpops

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_publishstaffpops_m0 |  | fbillno |
| 2 | pk_plm_publishstaffpops |  | fid |

---

## 单据体-子表 t_plm_pm_publishstaffpop

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_publishstaffpop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | ftaskgroupid1 | 任务组id | varchar | 50 |  | √ | ' ' | 任务组id |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | ftasktype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型 |
| 5 | fdecompositiontypep | 分解类型 | varchar | 50 |  | √ | ' ' | 分解类型,枚举: subproject :子项目 task :任务 taskgroup :任务组 milestone :里程碑 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 9 | ftextfield | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 10 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcompilationtype | 编制状态 | int8 | 64 |  | √ | 0 | [任务状态 plm_pm_taskstatus](../plmpm_files/plm_pm_taskstatus.md) |
| 12 | ftask | 任务 | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 13 | fdesc | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 14 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | ftaskid | 任务ID | varchar | 50 |  | √ | ' ' | 任务ID |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fflag | 标识 | varchar | 50 |  | √ | ' ' | 标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_publishstaffpop_fk |  | fid |
| 2 | pk_plm_pm_publishstaffpop |  | fentryid |
