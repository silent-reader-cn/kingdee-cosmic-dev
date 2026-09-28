# 工作流操作日志-wf_operationlog

## 工作流操作日志-主表 t_wf_operationlog

- **表名称：** 工作流操作日志-主表
- **表名：** t_wf_operationlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizidentifykey | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |
| 3 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 4 | fnote | 补充描述 | text | 0 |  |  | null | 补充描述 |
| 5 | fnopinion | n意见 | varchar | 2000 |  | √ | ' ' | n意见 |
| 6 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 7 | fassignee | 目标人 | varchar | 2000 |  | √ | ' ' | 目标人 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | factivityname | 活动实例名称 | varchar | 500 |  | √ | ' ' | 活动实例名称 |
| 11 | fassigneeid | 目标人ID | varchar | 2000 |  | √ | ' ' | 目标人ID |
| 12 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 13 | fbillno | 表单编号 | varchar | 255 |  | √ | ' ' | 表单编号 |
| 14 | fstep | 步骤 | int8 | 64 |  | √ | 0 | 步骤 |
| 15 | fterminalway | 终端类型 | varchar | 100 |  | √ | ' ' | 终端类型,枚举: web :PC端 mobile :流程助手 background :后台 api :API mobile_dd :钉钉 mobile_email :邮件 mobile_sms :短信 mobile_wxqyh :企业微信 mobile_kingdee_sky :公有云企业微信 mobile_wl :WeLink mobile_yunzhijia :云之家 mobile_yunzhijiaup :云之家统一流程 mobile_yunzhijiaeco :生态云之家 mobile_other :未知渠道 |
| 16 | factivityid | 活动实例ID | varchar | 255 |  | √ | ' ' | 活动实例ID |
| 17 | fdecisiontype | 决策类型 | varchar | 50 |  | √ | ' ' | 决策类型 |
| 18 | fbiznote | 业务关键信息 | varchar | 2000 |  | √ | ' ' | 业务关键信息 |
| 19 | fowner | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |
| 20 | fnote_summary | 补充描述摘要 | varchar | 300 |  | √ | ' ' | 补充描述摘要 |
| 21 | fispublic | 是否公开 | bpchar | 1 |  | √ | '0' | 是否公开 |
| 22 | fownerid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 23 | fcommentid | 审批意见ID | int8 | 64 |  | √ | 0 | 审批意见ID |
| 24 | ftype | 操作类型 | varchar | 100 |  | √ | ' ' | 操作类型,枚举: transfer :转交 coordinateRequest :协办请求 coordinateReply :协办回复 coordinateCancel :协办撤回 comment :任务处理 addComment :材料补录 withdraw :撤回 circulation :传阅 reminders :催办 jump :跳转 addsign :加签 suspend :挂起 suspendCancel :撤销挂起 terminal_f :强制终止 delegate :任务委托 textMessage :消息链接 converted :手动下推 addSignClear :删除加签 auto :自动 billWithdraw :整单撤回 |
| 25 | fresultnumber | 结果编码 | varchar | 50 |  | √ | ' ' | 结果编码 |
| 26 | fbusinesskey | 业务ID | varchar | 36 |  | √ | ' ' | 业务ID |
| 27 | fopinion | 意见 | varchar | 3000 |  | √ | ' ' | 意见 |
| 28 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_operlog_billno |  | fbillno |
| 2 | pk_t_wf_operationlog |  | fid |
| 3 | idx_wf_operlog_buskey |  | fbusinesskey |
| 4 | idx_wf_operationlog |  | fprocinstid |
| 5 | idx_wf_operlog_taskid |  | ftaskid |

---

## 工作流操作日志-多语言表 t_wf_operationlog_l

- **表名称：** 工作流操作日志-多语言表
- **表名：** t_wf_operationlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factivityname | 活动实例名称 | varchar | 500 |  | √ | ' ' | 活动实例名称 |
| 3 | fopinion | 意见 | varchar | 3000 |  | √ | ' ' | 意见 |
| 4 | fnote | 补充描述 | text | 0 |  |  | null | 补充描述 |
| 5 | fnopinion | n意见 | varchar | 2000 |  | √ | ' ' | n意见 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 9 | fassignee | 目标人 | varchar | 2000 |  | √ | ' ' | 目标人 |
| 10 | fbiznote | 业务关键信息 | varchar | 2000 |  | √ | ' ' | 业务关键信息 |
| 11 | fowner | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |
| 12 | fnote_summary | 补充描述摘要 | varchar | 300 |  | √ | ' ' | 补充描述摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_operationlog_l |  | fpkid |
| 2 | idx_wf_operationlog_l |  | fid,flocaleid |
