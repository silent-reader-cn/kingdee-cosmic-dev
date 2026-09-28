# 项目任务变更单-fmm_prochanges

## 项目任务变更单-主表 t_fmm_prochanges

- **表名称：** 项目任务变更单-主表
- **表名：** t_fmm_prochanges

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproplantypeid | 项目计划类型 | int8 | 64 |  | √ | 0 | [项目计划类型 fmm_plantype](../fmm_files/fmm_plantype.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fratifierid | 批准人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 8 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fpronumberid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | applicationdate | applicationdate | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fapproveddate | 批准日期 | timestamp | 0 |  |  | null | 批准日期 |
| 15 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_prochanges |  | fid |
| 2 | idx_fmm_prochanges_fnum |  | fbillno |
| 3 | idx_fmm_prochanges_fct |  | fcreatetime |

---

## 单据体-子表 t_fmm_pc_changedetail

- **表名称：** 单据体-子表
- **表名：** t_fmm_pc_changedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangereason | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 3 | fplaningtime | 计划工期 | numeric | 23 | 2 | √ | 0 | 计划工期 |
| 4 | ftimeunitid | 工期单位 | int8 | 64 |  | √ | 0 | [工期单位 pmpd_timeunit](../fmm_files/pmpd_timeunit.md) |
| 5 | ffinnishtime | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fstarttime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 11 | fplaningareaid | 计划区域 | int8 | 64 |  | √ | 0 | [计划区域 fmm_planningarea](../fmm_files/fmm_planningarea.md) |
| 12 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fchangestype | 变更类型 | varchar | 5 |  | √ | ' ' | 变更类型,枚举: 0 :变更前 1 :变更后 |
| 14 | ftasknumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 15 | fchangesource | 变更来源 | varchar | 50 |  | √ | ' ' | 变更来源 |
| 16 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fscheduletype | 排程类型 | varchar | 5 |  | √ | ' ' | 排程类型,枚举: 1 :标准任务 2 :WBS汇总 3 :里程碑 4 :完成里程碑 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_pc_changedetail_fid |  | fid |
| 2 | pk_fmm_pc_changedetail |  | fentryid |
