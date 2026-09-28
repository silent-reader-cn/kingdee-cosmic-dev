# 流程任务参与者-wf_participant

## 流程任务参与者-主表 t_wf_participant

- **表名称：** 流程任务参与者-主表
- **表名：** t_wf_participant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fsendername | 发送人名称 | varchar | 500 |  | √ | ' ' | 发送人名称 |
| 4 | fextendnumber | 数字(金额)1 | numeric | 23 | 10 | √ | 0 | 数字(金额)1 |
| 5 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 6 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 7 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 8 | fendtype | 处理端类型 | varchar | 30 |  | √ | '1' | 处理端类型,枚举: all :PC和移动处理 pc :仅PC处理 mb :仅移动处理 |
| 9 | ftaskdefid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 10 | fbillno | 单据编码 | varchar | 200 |  | √ | ' ' | 单据编码 |
| 11 | fname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 12 | fextendformat | 业务字段格式 | text | 0 |  |  | null | 业务字段格式 |
| 13 | fcategory | 类别 | varchar | 100 |  | √ | ' ' | 类别 |
| 14 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 15 | ftaskstate | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态 |
| 16 | fstarterid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 17 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 18 | ftrustname | 受托人名称 | varchar | 255 |  | √ | ' ' | 受托人名称 |
| 19 | fparenttaskid | 父任务Id | int8 | 64 |  | √ | 0 | 父任务Id |
| 20 | fprocessingpage | 处理页面 | varchar | 50 |  | √ | ' ' | 处理页面 |
| 21 | fispublic | 是否公开 | bpchar | 1 |  | √ | '0' | 是否公开 |
| 22 | fownerid | 所有者id | int8 | 64 |  | √ | 0 | 所有者id |
| 23 | fdelegateid | 委托设置Id | int8 | 64 |  | √ | 0 | 委托设置Id |
| 24 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 25 | fcompositetaskid | 聚合任务 | int8 | 64 |  | √ | 0 | 聚合任务 |
| 26 | fmobileformkey | 移动表单KEY | varchar | 50 |  | √ | ' ' | 移动表单KEY |
| 27 | fextenddate | 时间1 | timestamp | 0 |  |  | null | 时间1 |
| 28 | ftrustnameformat | 受托人名称格式化 | varchar | 500 |  | √ | ' ' | 受托人名称格式化 |
| 29 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 30 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 31 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 32 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 33 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 34 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码,枚举: |
| 35 | fgroupnumber | 待办分组 | int8 | 64 |  | √ | 0 | 待办分组 wf_tohandlegroup |
| 36 | ftaskdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 37 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 38 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 39 | fsenderid | 发送人ID | text | 0 |  |  | null | 发送人ID |
| 40 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 41 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fbiztype | 业务类型 | varchar | 150 |  | √ | ' ' | 业务类型 |
| 43 | freadtime | 开封时间 | timestamp | 0 |  |  | null | 开封时间 |
| 44 | fparticipantname | 当前参与人 | varchar | 300 |  | √ | ' ' | 当前参与人 |
| 45 | fextendstr1 | 字符1 | varchar | 255 |  | √ | ' ' | 字符1 |
| 46 | fextendstr2 | 字符2 | varchar | 255 |  | √ | ' ' | 字符2 |
| 47 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 48 | fstartnameformat | 发起人显示设置 | varchar | 300 |  | √ | ' ' | 发起人显示设置 |
| 49 | fprocessingmobilepage | 移动处理页面 | varchar | 50 |  | √ | ' ' | 移动处理页面 |
| 50 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 51 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 52 | ftransferopinion | 转交意见 | varchar | 2000 |  | √ | ' ' | 转交意见 |
| 53 | fprocesstype | 流程类型 | varchar | 50 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 54 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 55 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 56 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_participant_pkey |  | fid |
| 2 | idx_wf_ident_lnk_user |  | fuserid |
| 3 | idx_wf_idlnk_task_user_prio |  | ftaskid,fuserid,fpriority |
| 4 | idx_wf_ident_lnk_ownerid |  | fownerid |
| 5 | idx_wf_athrz_procedef |  | fprocdefid |
| 6 | idx_wf_ident_lnk_procinst |  | fprocinstid |
| 7 | idx_wf_ident_lnk_entitynumber |  | fentitynumber |
| 8 | idx_wf_participant_createdate |  | fcreatedate |
| 9 | idx_wf_ident_lnk_ptaskid |  | fparenttaskid |

---

## 流程任务参与者-多语言表 t_wf_participant_l

- **表名称：** 流程任务参与者-多语言表
- **表名：** t_wf_participant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 4 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 5 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 6 | ftrustnameformat | 受托人名称格式化 | varchar | 500 |  | √ | ' ' | 受托人名称格式化 |
| 7 | fsendername | 发送人名称 | varchar | 500 |  | √ | ' ' | 发送人名称 |
| 8 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 9 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 10 | ftransferopinion | 转交意见 | varchar | 2000 |  | √ | ' ' | 转交意见 |
| 11 | ftrustname | 受托人名称 | varchar | 255 |  | √ | ' ' | 受托人名称 |
| 12 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 13 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 14 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 15 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 16 | fparticipantname | 当前参与人 | varchar | 300 |  | √ | ' ' | 当前参与人 |
| 17 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 18 | fstartnameformat | 发起人显示设置 | varchar | 300 |  | √ | ' ' | 发起人显示设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_participant_l |  | fid,flocaleid |
| 2 | t_wf_participant_l_pkey |  | fpkid |

---

## 流程任务参与者-分表 t_wf_participant_a

- **表名称：** 流程任务参与者-分表
- **表名：** t_wf_participant_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextendnumber2 | 数字(金额)2 | numeric | 23 | 10 | √ | 0 | 数字(金额)2 |
| 3 | fextenddate2 | 时间2 | timestamp | 0 |  |  | null | 时间2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_participant_a |  | fid |
| 2 | idx_wf_participant_a_extdate |  | fextenddate2 |
