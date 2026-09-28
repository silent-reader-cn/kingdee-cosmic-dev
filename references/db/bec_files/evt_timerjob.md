# 定时工作-evt_timerjob

## 定时工作-主表 t_evt_timerjob

- **表名称：** 定时工作-主表
- **表名：** t_evt_timerjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | frepeat | 重复 | varchar | 30 |  | √ | ' ' | 重复 |
| 4 | fhandlertype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型 |
| 5 | fprocdefid | 服务ID | int8 | 64 |  | √ | 0 | 服务ID |
| 6 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 7 | flockownerid | 锁定人ID | varchar | 100 |  | √ | ' ' | 锁定人ID |
| 8 | fretries | 重试次数 | int8 | 64 |  | √ | 3 | 重试次数 |
| 9 | flockexptime | 锁定失效日期 | timestamp | 0 |  |  | null | 锁定失效日期 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 12 | frooteventinstid | 起始事件实例id | int8 | 64 |  | √ | 0 | 起始事件实例id |
| 13 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 14 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 15 | fbizkey | 业务标志 | varchar | 500 |  | √ | ' ' | 业务标志 |
| 16 | fexecutionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 17 | fsrctraceid | 源trace | varchar | 100 |  | √ | ' ' | 源trace |
| 18 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 19 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 20 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 21 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 22 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 23 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 24 | fprocessinstanceid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 25 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_timer_job_duedate |  | flockownerid,fduedate |
| 2 | t_evt_timerjob_pkey |  | fid |
| 3 | idx_evt_timer_job_executionid |  | fexecutionid |
| 4 | idx_evt_timer_job_process_id |  | fprocessinstanceid |
| 5 | idx_evt_timer_job_proc_def_id |  | fprocdefid |
| 6 | idx_evt_timer_job_buskey |  | fbusinesskey |
