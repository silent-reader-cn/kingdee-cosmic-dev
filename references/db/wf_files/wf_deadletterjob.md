# 异常流程信息-wf_deadletterjob

## 异常流程信息-多语言表 t_wf_deadletterjob_l

- **表名称：** 异常流程信息-多语言表
- **表名：** t_wf_deadletterjob_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 流程编码版本 | varchar | 255 |  | √ | ' ' | 流程编码版本 |
| 3 | fsubject | 单据主题 | varchar | 2000 |  | √ | ' ' | 单据主题 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | felementname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_deadletterjob_l_pkey |  | fpkid |
| 2 | idx_wf_deadletterjob_l_loc |  | fid,flocaleid |

---

## 异常流程信息-主表 t_wf_deadletterjob

- **表名称：** 异常流程信息-主表
- **表名：** t_wf_deadletterjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fexceptionstackmsg | 异常堆栈信息 | text | 0 |  |  | null | 异常堆栈信息 |
| 4 | frepeat | 重复 | varchar | 255 |  | √ | ' ' | 重复 |
| 5 | fhandlertype | 消息类型 | varchar | 30 |  | √ | ' ' | 消息类型,枚举: trigger-timer :trigger-timer |
| 6 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 7 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 8 | fentitynumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 9 | fretries | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 10 | fcreatedate | 异常发生时间 | timestamp | 0 |  |  | null | 异常发生时间 |
| 11 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 12 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 13 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 14 | felementname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 15 | forgunitid | 所属组织 | int8 | 64 |  | √ | 0 | 所属组织 |
| 16 | ferrorcode | 异常代码 | varchar | 100 |  | √ | ' ' | 异常代码 |
| 17 | fname | 流程编码版本 | varchar | 255 |  | √ | ' ' | 流程编码版本 |
| 18 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 19 | fsubject | 单据主题 | varchar | 2000 |  | √ | ' ' | 单据主题 |
| 20 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 21 | ferrortype | 异常类型 | varchar | 30 |  | √ | ' ' | 异常类型,枚举: engine :引擎异常 nullParticipant :参与人为空异常 business :业务调用异常 conditionParse :条件解析异常 messageService :消息异常 configuration :配置异常 outSet :出口线异常 subProcess :子流程运行异常 notFindSubprocess :启动子流程异常 billCalc :单据计算异常 mountBiz :单据挂载异常 cycleNumbersExceed :循环次数超出异常 rpa :RPA异常 targetBillFilter :目标单过滤异常 |
| 22 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 23 | fprocesstype | 流程类型 | varchar | 100 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 24 | fsolution | 建议措施 | varchar | 2000 |  | √ | ' ' | 建议措施 |
| 25 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 26 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 27 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 28 | froottraceno | TraceId | varchar | 100 |  | √ | ' ' | TraceId |
| 29 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 30 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 31 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 32 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_deadletjob_buskey |  | fbusinesskey |
| 2 | idx_wf_deadletjob_exec |  | fexecutionid |
| 3 | idx_wf_deadjob_type_retries |  | fretries,fhandlertype |
| 4 | idx_wf_deadletjob_proc |  | fprocessinstanceid |
| 5 | t_wf_deadletterjob_pkey |  | fid |
| 6 | idx_wf_deadjob_errortype |  | ferrortype |
| 7 | idx_wf_deadletjob_procdef |  | fprocdefid |
| 8 | idx_wf_deadletterjob_dateorg |  | fcreatedate,forgunitid |
| 9 | idx_wf_deadjob_modifydate |  | fmodifydate |
