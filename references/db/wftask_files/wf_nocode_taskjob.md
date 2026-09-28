# 无代码渠道待办日志-wf_nocode_taskjob

## 无代码渠道待办日志-主表 t_wf_nocode_taskjob

- **表名称：** 无代码渠道待办日志-主表
- **表名：** t_wf_nocode_taskjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fchannelname | 渠道名称 | varchar | 150 |  | √ | ' ' | 渠道名称 |
| 4 | fchannelnumber | 渠道编码 | varchar | 100 |  | √ | ' ' | 渠道编码 |
| 5 | frepeat | 重复 | varchar | 255 |  | √ | ' ' | 重复 |
| 6 | fhandlertype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型 |
| 7 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | fsource | 来源 | varchar | 60 |  | √ | ' ' | 来源 |
| 11 | fretrycount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 12 | flockownerid | 锁定人ID | varchar | 100 |  | √ | ' ' | 锁定人ID |
| 13 | fretries | 重试次数 | int4 | 32 |  | √ | 3 | 重试次数 |
| 14 | fentityname | 单据名称 | varchar | 115 |  | √ | ' ' | 单据名称 |
| 15 | flockexptime | 锁定失效日期 | timestamp | 0 |  |  | null | 锁定失效日期 |
| 16 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 18 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 19 | factivityname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 20 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 21 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 22 | forgunitid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 23 | finterfacetype | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: NEW :创建待办 DEAL :处理待办 DELETE :删除待办 DELETEANDCREATE :删除已办并创建待办 |
| 24 | ftraceid | traceid | varchar | 100 |  | √ | ' ' | traceid |
| 25 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 26 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 27 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 28 | fprocesstype | 流程类型 | varchar | 30 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 NoCodeFlow :无代码 |
| 29 | ftodostate | 渠道待办状态 | varchar | 50 |  | √ | ' ' | 渠道待办状态,枚举: DEALSUCCESS :处理成功 DEALFAIL :处理失败 UNTREATED :未消费 |
| 30 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 31 | fsuccess | 结果 | bpchar | 1 |  | √ | '1' | 结果 |
| 32 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 33 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 34 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 35 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 36 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 37 | fassigneename | 任务处理人名称 | varchar | 255 |  | √ | ' ' | 任务处理人名称 |
| 38 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 39 | fexecutor | 执行机 | varchar | 100 |  | √ | ' ' | 执行机 |
| 40 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 41 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 42 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 43 | ftaskid | 流程待办taskId | int8 | 64 |  | √ | 0 | 流程待办taskId |
| 44 | frootjobid | 根jobid | int8 | 64 |  | √ | 0 | 根jobid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nc_taskjob_datestate |  | fcreatedate,ftodostate |
| 2 | idx_wf_nc_taskjob_proctype |  | fprocesstype |
| 3 | pk_wf_nocode_taskjob |  | fid |
| 4 | idx_wf_nc_taskjob_billno |  | fbillno |
| 5 | idx_wf_nc_taskjob_rootjob |  | frootjobid |

---

## 无代码渠道待办日志-多语言表 t_wf_nocode_taskjob_l

- **表名称：** 无代码渠道待办日志-多语言表
- **表名：** t_wf_nocode_taskjob_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 单据名称 | varchar | 115 |  | √ | ' ' | 单据名称 |
| 3 | fassigneename | 任务处理人名称 | varchar | 255 |  | √ | ' ' | 任务处理人名称 |
| 4 | fchannelname | 渠道名称 | varchar | 150 |  | √ | ' ' | 渠道名称 |
| 5 | factivityname | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_nocode_taskjob_l |  | fpkid |
| 2 | idx_wf_nocode_taskjob_l |  | fid,flocaleid |
