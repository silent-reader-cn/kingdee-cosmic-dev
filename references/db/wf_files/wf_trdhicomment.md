# 第三方任务执行结果-wf_trdhicomment

## 第三方任务执行结果-主表 t_wf_trdhicomment

- **表名称：** 第三方任务执行结果-主表
- **表名：** t_wf_trdhicomment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fgroupid | 分组 | varchar | 50 |  | √ | ' ' | 分组 |
| 4 | fmessage | 消息 | varchar | 2000 |  | √ | ' ' | 消息 |
| 5 | fcoordinviteopinion | 协办邀请意见 | varchar | 255 |  | √ | ' ' | 协办邀请意见 |
| 6 | fsourceapp | 来源应用 | varchar | 255 |  | √ | ' ' | 来源应用 |
| 7 | fbizidentifykey | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |
| 8 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | fsourcesystem | 来源系统 | varchar | 255 |  | √ | ' ' | 来源系统 |
| 11 | fsubprocessinstanceid | 子流程实例ID | int8 | 64 |  | √ | 0 | 子流程实例ID |
| 12 | fassignee | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |
| 13 | fsignature | 手写签名 | varchar | 255 |  | √ | ' ' | 手写签名 |
| 14 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 15 | fbacktoback | 是否背靠背 | bpchar | 1 |  | √ | '0' | 是否背靠背 |
| 16 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 17 | ftime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 18 | fstep | 审批步长 | int4 | 32 |  | √ | 0 | 审批步长 |
| 19 | fsubactivityname | 子节点名称 | varchar | 230 |  | √ | ' ' | 子节点名称 |
| 20 | fterminalway | 终端处理方式 | varchar | 500 |  | √ | ' ' | 终端处理方式 |
| 21 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 22 | factivityid | 活动ID | varchar | 255 |  | √ | ' ' | 活动ID |
| 23 | ftrustname | 委托人名称 | varchar | 255 |  | √ | ' ' | 委托人名称 |
| 24 | fdecisiontype | 决策类型 | varchar | 50 |  | √ | ' ' | 决策类型 |
| 25 | fispublic | 是否公开 | bpchar | 1 |  | √ | '0' | 是否公开 |
| 26 | fownerid | 所有者id | int8 | 64 |  | √ | 0 | 所有者id |
| 27 | ftype | 类型 | varchar | 100 |  | √ | ' ' | 类型 |
| 28 | fresultnumber | 结果编码 | varchar | 50 |  | √ | ' ' | 结果编码 |
| 29 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 30 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 31 | frichtextmessage | 富文本消息 | text | 0 |  |  | null | 富文本消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_trdhicomment_buskey |  | fbusinesskey |
| 2 | idx_wf_trdhicomment_owner |  | fownerid |
| 3 | idx_wf_trdhicomment_task |  | ftaskid |
| 4 | idx_wf_trdhicomment_proc |  | fprocinstid,factivityid |
| 5 | pk_t_wf_trdhicomment |  | fid |
| 6 | idx_wf_trdhicomment_enum |  | fentitynumber |
| 7 | idx_wf_trdhicomment_userid |  | fuserid |

---

## 第三方任务执行结果-多语言表 t_wf_trdhicomment_l

- **表名称：** 第三方任务执行结果-多语言表
- **表名：** t_wf_trdhicomment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fsubactivityname | 子节点名称 | varchar | 230 |  | √ | ' ' | 子节点名称 |
| 4 | fmessage | 消息 | varchar | 2000 |  | √ | ' ' | 消息 |
| 5 | factivityname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 6 | fcoordinviteopinion | 协办邀请意见 | varchar | 255 |  | √ | ' ' | 协办邀请意见 |
| 7 | ftrustname | 委托人名称 | varchar | 255 |  | √ | ' ' | 委托人名称 |
| 8 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 9 | fresultname | 结果名称 | varchar | 115 |  | √ | ' ' | 结果名称 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 11 | fassignee | 处理人 | varchar | 500 |  | √ | ' ' | 处理人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_trdhicomment_l |  | fpkid |
| 2 | idx_wf_trdhicomment |  | fid,flocaleid |

---

## 附件-附件表 t_wf_attachmentfield

- **表名称：** 附件-附件表
- **表名：** t_wf_attachmentfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_attachmentfield |  | fid |
| 2 | pk_t_wf_attachmentfield |  | fpkid |
