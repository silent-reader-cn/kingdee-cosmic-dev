# 下发编制-plm_distributestaff_pops

## 下发编制-主表 t_plm_pm_distrstaffpops

- **表名称：** 下发编制-主表
- **表名：** t_plm_pm_distrstaffpops

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_distrstaff_number |  | fbillno |
| 2 | pk_plm_pm_distrstaffpops |  | fid |

---

## 单据体-子表 t_plm_pm_distrstaffpopsen

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_distrstaffpopsen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchargeperson | 负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | ftaskgroupid1 | 任务组id | varchar | 50 |  | √ | ' ' | 任务组id |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fsubmitdeadline | 提交截止时间 | timestamp | 0 |  |  | null | 提交截止时间 |
| 5 | fprojectid | 项目ID | varchar | 60 |  | √ | ' ' | 项目ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | factsubmittime | 实际提交时间 | timestamp | 0 |  |  | null | 实际提交时间 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ftextfield | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 10 | fdistributetime | 下发时间 | timestamp | 0 |  |  | null | 下发时间 |
| 11 | fcreaterfield | 下发人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcompilationtype | 编制状态 | int8 | 64 |  | √ | 0 | 任务状态 plm_pm_taskstatus |
| 14 | ftaskgroupld | 任务组 | int8 | 64 |  | √ | 0 | 任务 plm_ipd_task |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_distrstaffpopsen_fk |  | fid |
| 2 | pk_plm_pm_distrstaffpopsen |  | fentryid |
