# 事件日志-evt_job

## 事件日志-主表 t_evt_jobrecord

- **表名称：** 事件日志-主表
- **表名：** t_evt_jobrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 相关数据 | text | 0 |  |  | null | 相关数据 |
| 3 | frepeat | 重复 | varchar | 30 |  | √ | ' ' | 重复 |
| 4 | fhandlertype | 服务类型 | varchar | 30 |  | √ | ' ' | 服务类型,枚举: event-execute-operation :执行操作服务 async-event-dispatch :事件分发 event-execute-microservice :执行微服务 trigger-http-api :执行restful服务 customevent-execute-operation :自定义事件执行操作服务 event-send-message :发送消息服务 event-execute-plugin :执行插件服务 execute-ext-event :自定义服务 event-start-process :启动流程 tryCloseBizFlow :尝试关闭业务流 |
| 5 | fprocdefid | 服务ID | int8 | 64 |  | √ | 0 | 服务ID |
| 6 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 7 | fsource | 来源 | varchar | 60 |  | √ | ' ' | 来源 |
| 8 | flockownerid | 锁定人ID | varchar | 100 |  | √ | ' ' | 锁定人ID |
| 9 | fretries | 重试次数 | int4 | 32 |  | √ | 3 | 重试次数 |
| 10 | flockexptime | 锁定失效日期 | timestamp | 0 |  |  | null | 锁定失效日期 |
| 11 | fcreatedate | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 12 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 13 | frooteventinstid | 起始事件实例id | int8 | 64 |  | √ | 0 | 起始事件实例id |
| 14 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作,枚举: submit :提交 save :保存 audit :审核 |
| 15 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 16 | fbizkey | 业务标志 | varchar | 500 |  | √ | ' ' | 业务标志 |
| 17 | fexecutionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 18 | fsrctraceid | 源trace | varchar | 100 |  | √ | ' ' | 源trace |
| 19 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 20 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 21 | fsuccess | 结果 | bpchar | 1 |  | √ | '1' | 结果 |
| 22 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 23 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 24 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 25 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 26 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 |
| 27 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 28 | fexecutor | 执行机 | varchar | 100 |  | √ | ' ' | 执行机 |
| 29 | fprocessinstanceid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 30 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 31 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 32 | frootjobid | 根jobid | int8 | 64 |  | √ | 0 | 根jobid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_jobrecord_createdate |  | fcreatedate |
| 2 | idx_evt_jobrec_buskey_state |  | fbusinesskey,fstate |
| 3 | idx_evt_jobrecord_rootevtid |  | frooteventinstid |
| 4 | pk_evt_jobrecord |  | fid |
| 5 | idx_evt_jobrecord_lockstate |  | flockexptime,fstate |
| 6 | idx_evt_jobrecord_rootjobid |  | frootjobid |
| 7 | idx_evt_jobrecord_handtype |  | fhandlertype |
| 8 | idx_evt_jobrecord_roottrace |  | froottraceno |
