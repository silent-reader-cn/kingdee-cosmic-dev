# 异常待办任务-wf_failedjob

## 异常待办任务-多语言表 t_wf_failedjob_l

- **表名称：** 异常待办任务-多语言表
- **表名：** t_wf_failedjob_l

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
| 1 | idx_wf_failedjob_l |  | fid,flocaleid |
| 2 | t_wf_failedjob_l_pkey |  | fpkid |

---

## 异常待办任务-主表 t_wf_failedjob

- **表名称：** 异常待办任务-主表
- **表名：** t_wf_failedjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fexceptionstackmsg | 异常堆栈信息 | text | 0 |  |  | null | 异常堆栈信息 |
| 4 | fhandlertype | 消息类型 | varchar | 30 |  | √ | ' ' | 消息类型,枚举: trigger-timer :trigger-timer |
| 5 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fentitynumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 8 | fretries | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 11 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |
| 12 | felementname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 13 | ferrorcode | 异常代码 | varchar | 100 |  | √ | ' ' | 异常代码 |
| 14 | fname | 流程编码版本 | varchar | 255 |  | √ | ' ' | 流程编码版本 |
| 15 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 16 | fsubject | 单据主题 | varchar | 2000 |  | √ | ' ' | 单据主题 |
| 17 | foccurrencetime | 异常发生时间 | timestamp | 0 |  |  | null | 异常发生时间 |
| 18 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 19 | ferrortype | 异常类型 | varchar | 30 |  | √ | ' ' | 异常类型,枚举: engine :引擎异常 nullParticipant :参与人为空异常 business :业务调用异常 conditionParse :条件解析异常 messageService :消息异常 configuration :配置异常 |
| 20 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 21 | fsolution | 建议措施 | varchar | 2000 |  | √ | ' ' | 建议措施 |
| 22 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 23 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 24 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 25 | fbusinesskey | 业务主键 | varchar | 30 |  | √ | ' ' | 业务主键 |
| 26 | fchanneltype | 渠道类型 | varchar | 50 |  | √ | 'yunzhijia' | 渠道类型,枚举: yunzhijia :云之家 welink :WeLink dingding :钉钉 weixinqy :企业微信 sms :短信 email :邮件 |
| 27 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_failedjob_pkey |  | fid |
| 2 | idx_wf_failedjob_exec |  | fexecutionid |
| 3 | idx_wf_failedjob_buskey |  | fbusinesskey |
| 4 | idx_wf_failedjob_procinst |  | fprocessinstanceid |
| 5 | idx_wf_failedjob_procdef |  | fprocdefid |
| 6 | idx_wf_failedjob_retries |  | fretries |
| 7 | idx_wf_failedjob_occurtime |  | foccurrencetime |
