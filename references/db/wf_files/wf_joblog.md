# Job处理日志-wf_joblog

## Job处理日志-主表 t_wf_joblog

- **表名称：** Job处理日志-主表
- **表名：** t_wf_joblog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fconfiguration | job配置 | varchar | 2000 |  | √ | ' ' | job配置 |
| 4 | fjobid | jobId | int8 | 64 |  | √ | 0 | jobId |
| 5 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fentitynumber | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 8 | felementid | 节点id | varchar | 200 |  | √ | ' ' | 节点id |
| 9 | fretries | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 10 | fsuccess | 结果 | bpchar | 1 |  | √ | '1' | 结果 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fduration | 耗时 | numeric | 23 | 10 | √ | 0.0000000000 | 耗时 |
| 13 | fstate | 状态 | varchar | 20 |  | √ | ' ' | 状态 |
| 14 | fexecutor | 执行机 | varchar | 100 |  | √ | ' ' | 执行机 |
| 15 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 16 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 17 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 18 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 19 | ftaskid | 任务id | varchar | 100 |  | √ | ' ' | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_joblog_proc |  | fprocessinstanceid |
| 2 | t_wf_joblog_pkey |  | fid |
| 3 | idx_wf_joblog_busikey |  | fbusinesskey |
