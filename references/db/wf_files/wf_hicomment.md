# 任务执行结果-wf_hicomment

## 任务执行结果-主表 t_wf_hicomment

- **表名称：** 任务执行结果-主表
- **表名：** t_wf_hicomment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fgroupid | 分组 | varchar | 50 |  | √ | ' ' | 分组 |
| 4 | fcoordinviteopinion | 协办邀请意见 | text | 0 |  |  | null | 协办邀请意见 |
| 5 | fsendername | 上一步处理人名称 | varchar | 400 |  | √ | ' ' | 上一步处理人名称 |
| 6 | fextendnumber | 数字(金额) | numeric | 23 | 10 | √ | 0 | 数字(金额) |
| 7 | fbizidentifykey | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |
| 8 | fassignee | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |
| 9 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 10 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 11 | fendtype | 处理端类型 | varchar | 30 |  | √ | '1' | 处理端类型,枚举: all :PC和移动处理 pc :仅PC处理 mb :仅移动处理 |
| 12 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 13 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 14 | fextendformat | 业务字段格式 | text | 0 |  |  | null | 业务字段格式 |
| 15 | fcategory | 类别 | varchar | 50 |  | √ | ' ' | 类别 |
| 16 | fstartname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 17 | fterminalway | 终端处理方式 | varchar | 500 |  | √ | ' ' | 终端处理方式 |
| 18 | fstarterid | 发起人id | int8 | 64 |  | √ | 0 | 发起人id |
| 19 | fhandlestate | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: approve :已同意 reject :已驳回 terminate :已终止 handled :已处理 dismissed :被驳回 willApproval :待审批 freeze :已冻结 willHandled :待处理 manualSuspended :已挂起 converted :已转换 converting :转换中 unConverted :待转换 |
| 20 | fsensitivefieldchange | 敏感字段变化 | text | 0 |  |  | null | 敏感字段变化 |
| 21 | ftrustname | 委托人名称 | varchar | 255 |  | √ | ' ' | 委托人名称 |
| 22 | fprocessingpage | 处理页面 | varchar | 50 |  | √ | ' ' | 处理页面 |
| 23 | fispublic | 是否公开 | bpchar | 1 |  | √ | '0' | 是否公开 |
| 24 | fownerid | 所有者id | int8 | 64 |  | √ | 0 | 所有者id |
| 25 | fdelegateid | 委托设置Id | int8 | 64 |  | √ | 0 | 委托设置Id |
| 26 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 27 | fextenddate | 时间 | timestamp | 0 |  |  | null | 时间 |
| 28 | fmessage | 消息 | varchar | 2000 |  | √ | ' ' | 消息 |
| 29 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 30 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 31 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 32 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 33 | fsubprocessinstanceid | 子流程实例ID | int8 | 64 |  | √ | 0 | 子流程实例ID |
| 34 | fsource | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 35 | fexecutiontype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型 |
| 36 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 37 | fsignature | 手写签名 | varchar | 255 |  | √ | ' ' | 手写签名 |
| 38 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 39 | fextendstr1 | 字符1 | varchar | 255 |  | √ | ' ' | 字符1 |
| 40 | fextendstr2 | 字符2 | varchar | 255 |  | √ | ' ' | 字符2 |
| 41 | fbacktoback | 是否背靠背 | bpchar | 1 |  | √ | '0' | 是否背靠背 |
| 42 | fsendernameformat | 上一步处理人显示设置 | varchar | 255 |  | √ | ' ' | 上一步处理人显示设置 |
| 43 | fstartnameformat | 发起人显示设置 | varchar | 255 |  | √ | ' ' | 发起人显示设置 |
| 44 | ftime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 45 | fstep | 审批步长 | int8 | 64 |  | √ | 0 | 审批步长 |
| 46 | fsubactivityname | 子节点名称 | varchar | 230 |  | √ | ' ' | 子节点名称 |
| 47 | fprocessingmobilepage | 移动处理页面 | varchar | 50 |  | √ | ' ' | 移动处理页面 |
| 48 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 49 | fsourcename | 来源系统名称 | varchar | 100 |  | √ | ' ' | 来源系统名称 |
| 50 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 51 | factivityid | 活动ID | varchar | 255 |  | √ | ' ' | 活动ID |
| 52 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 53 | fdecisiontype | 决策类型 | varchar | 50 |  | √ | ' ' | 决策类型 |
| 54 | ftype | 类型 | varchar | 100 |  | √ | ' ' | 类型 |
| 55 | fresultnumber | 结果编码 | varchar | 50 |  | √ | ' ' | 结果编码 |
| 56 | fpresentassignee | 当前处理人 | varchar | 1000 |  | √ | ' ' | 当前处理人 |
| 57 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 58 | frichtextmessage | 富文本消息 | text | 0 |  |  | null | 富文本消息 |
| 59 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hicomment_delegateid |  | fdelegateid,ftype,fexecutiontype |
| 2 | idx_wf_hicomment_owner |  | fownerid,ftype,fexecutiontype |
| 3 | idx_wf_hicomment_enum |  | fentitynumber |
| 4 | idx_wf_hicomment_userid |  | fuserid,ftime |
| 5 | idx_wf_hicomment_time |  | ftime |
| 6 | idx_wf_hicomment_businesskey |  | fbusinesskey |
| 7 | idx_wf_hicomment_proc |  | fprocinstid |
| 8 | idx_wf_hicomment_task |  | ftaskid,ftype |
| 9 | t_wf_hicomment_pkey |  | fid |

---

## 任务执行结果-多语言表 t_wf_hicomment_l

- **表名称：** 任务执行结果-多语言表
- **表名：** t_wf_hicomment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fsubactivityname | 子节点名称 | varchar | 230 |  | √ | ' ' | 子节点名称 |
| 4 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 5 | fstartname | 发起人名称 | varchar | 255 |  | √ | ' ' | 发起人名称 |
| 6 | fmessage | 消息 | varchar | 2000 |  | √ | ' ' | 消息 |
| 7 | fcoordinviteopinion | 协办邀请意见 | text | 0 |  |  | null | 协办邀请意见 |
| 8 | fsendername | 上一步处理人名称 | varchar | 400 |  | √ | ' ' | 上一步处理人名称 |
| 9 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 10 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 11 | fsourcename | 来源系统名称 | varchar | 100 |  | √ | ' ' | 来源系统名称 |
| 12 | fsensitivefieldchange | 敏感字段变化 | text | 0 |  |  | null | 敏感字段变化 |
| 13 | ftrustname | 委托人名称 | varchar | 255 |  | √ | ' ' | 委托人名称 |
| 14 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 15 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 16 | fassignee | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |
| 17 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 18 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 19 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 20 | fpresentassignee | 当前处理人 | varchar | 1000 |  | √ | ' ' | 当前处理人 |
| 21 | fsendernameformat | 上一步处理人显示设置 | varchar | 255 |  | √ | ' ' | 上一步处理人显示设置 |
| 22 | fstartnameformat | 发起人显示设置 | varchar | 255 |  | √ | ' ' | 发起人显示设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hicomment_l_pkey |  | fpkid |
| 2 | idx_wf_hicomment_localeid |  | fid,flocaleid |

---

## 任务执行结果-分表 t_wf_hicomment_a

- **表名称：** 任务执行结果-分表
- **表名：** t_wf_hicomment_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextendnumber2 | 数字2(金额) | numeric | 23 | 10 | √ | 0 | 数字2(金额) |
| 3 | fextenddate2 | 时间2 | timestamp | 0 |  |  | null | 时间2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hicomment_a_extdate |  | fextenddate2 |
| 2 | pk_wf_hicomment_a |  | fid |
