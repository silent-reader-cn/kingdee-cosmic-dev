# 定时工作-wf_timerjob

## 定时工作-主表 t_wf_timerjob

- **表名称：** 定时工作-主表
- **表名：** t_wf_timerjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 4 | frepeat | 重复 | varchar | 255 |  | √ | ' ' | 重复 |
| 5 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 6 | fhandlertype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型 |
| 7 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 11 | flockownerid | 锁定人ID | varchar | 100 |  | √ | ' ' | 锁定人ID |
| 12 | fretries | 重试次数 | int8 | 64 |  | √ | 3 | 重试次数 |
| 13 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 14 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 15 | flockexptime | 锁定失效日期 | timestamp | 0 |  |  | null | 锁定失效日期 |
| 16 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 17 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 19 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 20 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 21 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 22 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 23 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_timer_job_execution_id |  | fexecutionid |
| 2 | idx_wf_timer_job_process_id |  | fprocessinstanceid |
| 3 | idx_wf_timer_job_proc_def_id |  | fprocdefid |
| 4 | t_wf_timerjob_pkey |  | fid |
| 5 | idx_wf_timer_job_duedate |  | fduedate,fhandlertype,flockownerid |
| 6 | idx_wf_timer_job_buskey |  | fbusinesskey |
