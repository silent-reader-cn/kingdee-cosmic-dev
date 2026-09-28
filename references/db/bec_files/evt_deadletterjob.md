# 异常信息-evt_deadletterjob

## 异常信息-主表 t_evt_deadletterjob

- **表名称：** 异常信息-主表
- **表名：** t_evt_deadletterjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fexceptionstackmsg | 异常堆栈信息 | text | 0 |  |  | null | 异常堆栈信息 |
| 4 | frepeat | 重复 | varchar | 30 |  | √ | ' ' | 重复 |
| 5 | fhandlertype | 服务类型 | varchar | 30 |  | √ | ' ' | 服务类型,枚举: trigger-http-api :执行restful服务 event-execute-operation :执行操作服务 customevent-execute-operation :自定义事件执行操作服务 event-send-message :发送消息服务 event-execute-plugin :执行插件服务 async-event-dispatch :事件分发 execute-ext-event :自定义服务 event-execute-microservice :执行微服务 |
| 6 | fprocdefid | 服务ID | int8 | 64 |  | √ | 0 | 服务ID |
| 7 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 8 | fretries | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 9 | fcreatedate | 异常发生时间 | timestamp | 0 |  |  | null | 异常发生时间 |
| 10 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 11 | frooteventinstid | 起始事件实例id | int8 | 64 |  | √ | 0 | 起始事件实例id |
| 12 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 13 | felementname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 14 | ferrorcode | 异常代码 | varchar | 100 |  | √ | ' ' | 异常代码 |
| 15 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 16 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 17 | fsubject | 单据主题 | varchar | 2000 |  | √ | ' ' | 单据主题 |
| 18 | fbizkey | 业务标志 | varchar | 500 |  | √ | ' ' | 业务标志 |
| 19 | fexecutionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 20 | fsrctraceid | 源trace | varchar | 100 |  | √ | ' ' | 源trace |
| 21 | ferrortype | 异常类型 | varchar | 30 |  | √ | ' ' | 异常类型,枚举: engine :引擎异常 nullParticipant :参与人为空异常 business :业务调用异常 conditionParse :条件解析异常 messageService :消息异常 configuration :配置异常 outSet :出口线异常 |
| 22 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 23 | fsolution | 建议措施 | varchar | 2000 |  | √ | ' ' | 建议措施 |
| 24 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 25 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 26 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 27 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 28 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 29 | fprocessinstanceid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 30 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 31 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_deadletjob_buskey |  | fbusinesskey |
| 2 | idx_evt_deadletterjob_date |  | fcreatedate,fmodifydate |
| 3 | idx_evt_deadjob_errortype |  | ferrortype |
| 4 | idx_evt_deadletjob_exec |  | fexecutionid |
| 5 | idx_evt_deadletjob_proc |  | fprocessinstanceid |
| 6 | t_evt_deadletterjob_pkey |  | fid |
| 7 | idx_evt_deadletjob_procdef |  | fprocdefid |
| 8 | idx_evt_deadjob_type_retries |  | fretries,fhandlertype |
| 9 | idx_evt_deadjob_modifydate |  | fmodifydate |

---

## 异常信息-多语言表 t_evt_deadletterjob_l

- **表名称：** 异常信息-多语言表
- **表名：** t_evt_deadletterjob_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 流程编码版本 | varchar | 255 |  | √ | ' ' | 流程编码版本 |
| 3 | fsubject | 单据主题 | varchar | 2000 |  | √ | ' ' | 单据主题 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | felementname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_deadletterjob_l_pkey |  | fpkid |
| 2 | idx_evt_deadletterjob_l_loc |  | fid,flocaleid |
