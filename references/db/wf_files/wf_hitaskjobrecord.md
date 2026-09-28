# 历史任务job-wf_hitaskjobrecord

## 历史任务job-主表 t_wf_hitaskjobrecord

- **表名称：** 历史任务job-主表
- **表名：** t_wf_hitaskjobrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | frepeat | 重复 | varchar | 255 |  | √ | ' ' | 重复 |
| 4 | fhandlertype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型 |
| 5 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 8 | fsource | 来源 | varchar | 60 |  | √ | ' ' | 来源 |
| 9 | flockownerid | 锁定人ID | varchar | 100 |  | √ | ' ' | 锁定人ID |
| 10 | fretries | 重试次数 | int4 | 32 |  | √ | 3 | 重试次数 |
| 11 | flockexptime | 锁定失效日期 | timestamp | 0 |  |  | null | 锁定失效日期 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 14 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 15 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 16 | forgunitid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 17 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 18 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 19 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 20 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 21 | fsuccess | 结果 | bpchar | 1 |  | √ | '1' | 结果 |
| 22 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 23 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 24 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 25 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 26 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 27 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 28 | fexecutor | 执行机 | varchar | 100 |  | √ | ' ' | 执行机 |
| 29 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 30 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 31 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 32 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 33 | frootjobid | 根jobid | int8 | 64 |  | √ | 0 | 根jobid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hitaskjob_buskeystate |  | fbusinesskey,fstate |
| 2 | idx_wf_hitaskjob_taskid |  | ftaskid |
| 3 | pk_wf_hitaskjobrecord |  | fid |
