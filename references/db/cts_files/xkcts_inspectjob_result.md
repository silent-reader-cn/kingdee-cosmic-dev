# 巡检任务执行结果-xkcts_inspectjob_result

## 单据体-子表 t_xkinsp_jobresentry

- **表名称：** 单据体-子表
- **表名：** t_xkinsp_jobresentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmsg | 检查消息 | varchar | 200 |  | √ | ' ' | 检查消息 |
| 5 | frepairstatus | 修复状态 | varchar | 50 |  | √ | ' ' | 修复状态,枚举: 2 :修复失败 1 :修复成功 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | frepairtime | 修复时间 | timestamp | 0 |  |  | null | 修复时间 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | [巡检检查项 xkcts_inspectitem](../cts_files/xkcts_inspectitem.md) |
| 10 | frepairuserid | 修复人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcheckstatus | 检查结果 | varchar | 50 |  | √ | ' ' | 检查结果,枚举: 100 :通过 200 :警告 300 :不通过 400 :异常 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_jobresentry |  | fentryid |
| 2 | idx_jobresentry_fid |  | fid,fseq |

---

## 巡检任务执行结果-主表 t_xkinsp_jobres

- **表名称：** 巡检任务执行结果-主表
- **表名：** t_xkinsp_jobres

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fjobstatus | 任务结果 | varchar | 50 |  | √ | ' ' | 任务结果,枚举: 100 :成功 200 :部分成功 300 :失败 400 :异常 |
| 4 | fparameter | 任务参数 | varchar | 255 |  | √ | ' ' | 任务参数 |
| 5 | fparametername | 巡检维度 | varchar | 300 |  | √ | ' ' | 巡检维度 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 8 | fjobid | 检查任务 | int8 | 64 |  | √ | 0 | [巡检任务 xkcts_inspectjob](../cts_files/xkcts_inspectjob.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fjobname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 11 | fjobmsg | 任务信息 | varchar | 300 |  | √ | ' ' | 任务信息 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 检查用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fscheduleid | 巡检计划 | int8 | 64 |  | √ | 0 | [巡检计划 xkcts_inspect_schedule](../cts_files/xkcts_inspect_schedule.md) |
| 15 | fbatchsnsn | 批次流水号 | int8 | 64 |  | √ | 0 | 批次流水号 |
| 16 | fjobexestatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未开始 B :执行中 C :已执行 D :已中止 |
| 17 | fparameter_tag | 任务参数_详情 | text | 0 |  |  | ' ' | 任务参数_详情 |
| 18 | fendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 19 | fusedtime | 执行耗时（秒） | numeric | 23 | 3 |  | 0 | 执行耗时（秒） |
| 20 | fbillno | 任务编号 | varchar | 30 |  | √ | ' ' | 任务编号 |
| 21 | fbegtime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_jobres |  | fid |
| 2 | idx_xkinsp_job_no |  | fbillno |
| 3 | idx_xkinsp_job_job |  | fjobid |
| 4 | idx_xkinsp_job_creat |  | fcreatetime |
| 5 | idx_xkinsp_job_sn |  | fbatchsnsn |
