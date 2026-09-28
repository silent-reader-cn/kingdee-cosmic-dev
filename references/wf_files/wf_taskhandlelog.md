# 任务处理日志-wf_taskhandlelog

## 任务处理日志-主表 t_wf_taskhandlelog

- **表名称：** 任务处理日志-主表
- **表名：** t_wf_taskhandlelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassigneeformat | 现处理人名称格式化 | varchar | 500 |  | √ | ' ' | 现处理人名称格式化 |
| 3 | fisadminforward | 是否是管理员转交 | bpchar | 1 |  | √ | '0' | 是否是管理员转交 |
| 4 | fsendername | 发送人名称 | varchar | 500 |  | √ | ' ' | 发送人名称 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 7 | fbizidentifykey | 业务标识 | varchar | 255 |  | √ | ' ' | 业务标识 |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | fnote | 补充描述 | varchar | 500 |  | √ | ' ' | 补充描述 |
| 10 | fgroupnumber | 待办分组 | int8 | 64 |  | √ | 0 | 待办分组 wf_tohandlegroup |
| 11 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 12 | fassignee | 现处理人名称 | varchar | 255 |  | √ | ' ' | 现处理人名称 |
| 13 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 14 | fexecutiontype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型,枚举: byHand :手工执行 byAuto :自动执行 skip :忽略执行 jump :跳转执行 |
| 15 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态 |
| 16 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 17 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 19 | fbiztype | 业务类型 | varchar | 150 |  | √ | ' ' | 业务类型 |
| 20 | foriginalparticipant | 原始参与人 | varchar | 1000 |  | √ | ' ' | 原始参与人 |
| 21 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | factivityname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 23 | fendtype | 处理端类型 | varchar | 30 |  | √ | '1' | 处理端类型,枚举: all :PC和移动处理 pc :仅PC处理 mb :仅移动处理 |
| 24 | fsubscribe | 是否订阅结果 | bpchar | 1 |  | √ | '1' | 是否订阅结果 |
| 25 | fscenes | 场景 | varchar | 30 |  | √ | 'task' | 场景,枚举: task :任务 coordinateTask :协办任务 |
| 26 | fassigneeid | 现处理人 | int8 | 64 |  | √ | 0 | 现处理人 |
| 27 | fstartnameformat | 发起人显示设置 | varchar | 300 |  | √ | ' ' | 发起人显示设置 |
| 28 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 29 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 30 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 31 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 32 | ftaskstate | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态 |
| 33 | fterminalway | 终端处理方式 | varchar | 500 |  | √ | ' ' | 终端处理方式 |
| 34 | factivityid | 活动ID | varchar | 255 |  | √ | ' ' | 活动ID |
| 35 | fprocesstype | 流程类型 | varchar | 50 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 36 | fowner | 原处理人名称 | varchar | 50 |  | √ | ' ' | 原处理人名称 |
| 37 | fownerid | 原处理人 | int8 | 64 |  | √ | 0 | 原处理人 |
| 38 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 39 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 40 | fopinion | 处理意见 | varchar | 3000 |  | √ | ' ' | 处理意见 |
| 41 | fpresentassignee | 当前处理人 | varchar | 500 |  | √ | ' ' | 当前处理人 |
| 42 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 43 | fcompositetaskid | 聚合任务 | int8 | 64 |  | √ | 0 | 聚合任务 |
| 44 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 45 | fownerformat | 原处理人名称格式化 | varchar | 500 |  | √ | ' ' | 原处理人名称格式化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_taskhandlelog_ownerid |  | fownerid,ftype,fexecutiontype |
| 2 | idx_wf_taskhandlelog_task |  | ftaskid,ftype |
| 3 | idx_wf_taskhandlelog_credate |  | fcreatedate |
| 4 | t_wf_taskhandlelog_pkey |  | fid |
| 5 | idx_wf_taskhandlelog_type |  | ftype |
| 6 | idx_wf_taskhandlelog_procinst |  | fprocinstid |

---

## 任务处理日志-多语言表 t_wf_taskhandlelog_l

- **表名称：** 任务处理日志-多语言表
- **表名：** t_wf_taskhandlelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassigneeformat | 现处理人名称格式化 | varchar | 500 |  | √ | ' ' | 现处理人名称格式化 |
| 3 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 4 | fstartname | 发起人 | varchar | 200 |  | √ | ' ' | 发起人 |
| 5 | fsendername | 发送人名称 | varchar | 500 |  | √ | ' ' | 发送人名称 |
| 6 | fnote | 补充描述 | varchar | 500 |  | √ | ' ' | 补充描述 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 9 | fassignee | 现处理人名称 | varchar | 255 |  | √ | ' ' | 现处理人名称 |
| 10 | fowner | 原处理人名称 | varchar | 200 |  | √ | ' ' | 原处理人名称 |
| 11 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 12 | factivityname | 节点名称 | varchar | 255 |  | √ | ' ' | 节点名称 |
| 13 | fopinion | 处理意见 | varchar | 2000 |  | √ | ' ' | 处理意见 |
| 14 | fpresentassignee | 当前处理人 | varchar | 500 |  | √ | ' ' | 当前处理人 |
| 15 | fstartnameformat | 发起人显示设置 | varchar | 300 |  | √ | ' ' | 发起人显示设置 |
| 16 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 17 | fownerformat | 原处理人名称格式化 | varchar | 500 |  | √ | ' ' | 原处理人名称格式化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_taskhandlelog_l_pkey |  | fpkid |
| 2 | idx_wf_taskhandlelog_l |  | fid,flocaleid |
