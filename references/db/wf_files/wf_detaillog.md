# 详细日志记录-wf_detaillog

## 详细日志记录-多语言表 t_wf_detaillog_l

- **表名称：** 详细日志记录-多语言表
- **表名：** t_wf_detaillog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 3 | fsubactivityname | 子节点名称 | varchar | 500 |  | √ | ' ' | 子节点名称 |
| 4 | fcurrentsubject | 当前任务主题 | varchar | 500 |  | √ | ' ' | 当前任务主题 |
| 5 | fstartname | 发起人姓名 | varchar | 255 |  | √ | ' ' | 发起人姓名 |
| 6 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 7 | fopinion | 审批意见 | varchar | 500 |  | √ | ' ' | 审批意见 |
| 8 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 9 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 11 | fassignee | 处理人名称 | varchar | 255 |  | √ | ' ' | 处理人名称 |
| 12 | fowner | 原处理人姓名 | varchar | 255 |  | √ | ' ' | 原处理人姓名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_detaillog_l |  | fid,flocaleid |
| 2 | pk_wf_detaillog_l |  | fpkid |

---

## 详细日志记录-主表 t_wf_detaillog

- **表名称：** 详细日志记录-主表
- **表名：** t_wf_detaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | varchar | 50 |  | √ | ' ' | 分组 |
| 3 | frejectactivityid | 驳回至节点ID | varchar | 255 |  | √ | ' ' | 驳回至节点ID |
| 4 | frejectactivityname | 驳回至节点名称 | varchar | 500 |  | √ | ' ' | 驳回至节点名称 |
| 5 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | fsubprocessinstanceid | 子流程实例ID | int8 | 64 |  | √ | 0 | 子流程实例ID |
| 9 | fassignee | 处理人名称 | varchar | 255 |  | √ | ' ' | 处理人名称 |
| 10 | fexecutiontype | 执行类型 | varchar | 50 |  | √ | ' ' | 执行类型 |
| 11 | fstartavatar | 发起人头像 | varchar | 300 |  | √ | ' ' | 发起人头像 |
| 12 | fentityname | 实体名称 | varchar | 115 |  | √ | ' ' | 实体名称 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fmessageid | 消息id | int8 | 64 |  | √ | 0 | 消息id |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 17 | ferrormessage | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 18 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 19 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 20 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 21 | fchannel | 渠道 | varchar | 100 |  | √ | ' ' | 渠道 |
| 22 | fsubactivityname | 子节点名称 | varchar | 500 |  | √ | ' ' | 子节点名称 |
| 23 | fcategory | 当前节点类型 | varchar | 50 |  | √ | ' ' | 当前节点类型 |
| 24 | fcurrentsubject | 当前任务主题 | varchar | 500 |  | √ | ' ' | 当前任务主题 |
| 25 | fstartname | 发起人姓名 | varchar | 255 |  | √ | ' ' | 发起人姓名 |
| 26 | fterminalway | 终端处理方式 | varchar | 255 |  | √ | ' ' | 终端处理方式 |
| 27 | fhandlestate | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: approve :已同意 reject :已驳回 terminate :已终止 handled :已处理 dismissed :被驳回 willApproval :待审批 freeze :已冻结 willHandled :待处理 manualSuspended :已挂起 converted :已转换 converting :转换中 unConverted :待转换 |
| 28 | factivityid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 29 | fowneravatar | 原处理人头像 | varchar | 300 |  | √ | ' ' | 原处理人头像 |
| 30 | fnodebusinesskey | 节点的业务主键 | varchar | 36 |  | √ | ' ' | 节点的业务主键 |
| 31 | fdecisiontype | 决策类型 | varchar | 50 |  | √ | ' ' | 决策类型 |
| 32 | fnodeentitynumber | 节点的实体编码 | varchar | 50 |  | √ | ' ' | 节点的实体编码 |
| 33 | fowner | 原处理人姓名 | varchar | 255 |  | √ | ' ' | 原处理人姓名 |
| 34 | fownerid | 原处理人ID | int8 | 64 |  | √ | 0 | 原处理人ID |
| 35 | fassigneeavatar | 处理人头像 | varchar | 300 |  | √ | ' ' | 处理人头像 |
| 36 | ftype | 类型 | varchar | 100 |  | √ | ' ' | 类型 |
| 37 | fstartid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 38 | fresultnumber | 结果编码 | varchar | 50 |  | √ | ' ' | 结果编码 |
| 39 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 40 | fopinion | 审批意见 | varchar | 500 |  | √ | ' ' | 审批意见 |
| 41 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_detaillog_procinstid |  | fprocinstid |
| 2 | pk_wf_detaillog |  | fid |
| 3 | idx_wf_detaillog_buskey |  | fbusinesskey |
