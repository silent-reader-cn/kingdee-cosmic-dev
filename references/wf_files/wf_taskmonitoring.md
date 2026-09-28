# 任务监控-wf_taskmonitoring

## 任务监控-主表 t_wf_task

- **表名称：** 任务监控-主表
- **表名：** t_wf_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaptionpc | 页面标题_PC | varchar | 300 |  | √ | ' ' | 页面标题_PC |
| 3 | fbatchop | 批量标识 | varchar | 30 |  | √ | ' ' | 批量标识 |
| 4 | fvalidateoperation | 校验操作 | varchar | 500 |  | √ | ' ' | 校验操作 |
| 5 | fsendername | 发送人名称 | varchar | 1000 |  | √ | ' ' | 发送人名称 |
| 6 | fextendnumber | 数字(金额)1 | numeric | 23 | 10 | √ | 0 | 数字(金额)1 |
| 7 | fcaptionmob | 页面标题_mob | varchar | 300 |  | √ | ' ' | 页面标题_mob |
| 8 | fassignee | 处理人 | varchar | 255 |  | √ | ' ' | 处理人 |
| 9 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 10 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 13 | fendtype | 处理端类型 | varchar | 30 |  | √ | '1' | 处理端类型,枚举: all :PC和移动处理 pc :仅PC处理 mb :仅移动处理 |
| 14 | fyzjgroupid | 云之家组ID | varchar | 36 |  | √ | ' ' | 云之家组ID |
| 15 | ftaskdefid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 16 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 17 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 18 | fextendformat | 业务字段格式 | text | 0 |  |  | null | 业务字段格式 |
| 19 | fcategory | 类别 | varchar | 100 |  | √ | ' ' | 类别 |
| 20 | fformkey | 表单KEY | varchar | 50 |  | √ | ' ' | 表单KEY |
| 21 | fstartname | 发起人 | varchar | 255 |  | √ | ' ' | 发起人 |
| 22 | ftaskstate | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态 |
| 23 | fstarterid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 24 | fhandlestate | 处理状态 | varchar | 30 |  | √ | ' ' | 处理状态,枚举: dismissed :被驳回 willApproval :待审批 freeze :已冻结 willHandled :待处理 unConverted :待转换 0 :待分配 converted :已转换 1 :处理中 converting :转换中 2 :已完成 manualSuspended :已挂起 3 :待影像上传 |
| 25 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 26 | fparenttaskid | 父任务ID | int8 | 64 |  | √ | 0 | 父任务ID |
| 27 | fdescription | 节点描述 | varchar | 255 |  | √ | ' ' | 节点描述 |
| 28 | fisactive | 是否活动 | bpchar | 1 |  | √ | '1' | 是否活动 |
| 29 | fprocessingpage | 处理页面 | varchar | 50 |  | √ | ' ' | 处理页面 |
| 30 | fownerid | 拥有人ID | int8 | 64 |  | √ | 0 | 拥有人ID |
| 31 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 32 | fsuspensionstate | 挂起状态 | varchar | 50 |  | √ | ' ' | 挂起状态 |
| 33 | fclaimtime | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 34 | fmobileformkey | 移动表单KEY | varchar | 50 |  | √ | ' ' | 移动表单KEY |
| 35 | fextenddate | 时间1 | timestamp | 0 |  |  | null | 时间1 |
| 36 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 37 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 38 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 39 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 40 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 41 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码,枚举: |
| 42 | fgroupnumber | 待办分组 | int8 | 64 |  | √ | 0 | 待办分组 wf_tohandlegroup |
| 43 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 44 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 45 | fexecutiontype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型,枚举: byHand :手工执行 byAuto :自动执行 skip :忽略执行 jump :跳转执行 |
| 46 | fsenderid | 发送人ID | text | 0 |  |  | null | 发送人ID |
| 47 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fparticipantname | 当前参与人 | varchar | 500 |  | √ | ' ' | 当前参与人 |
| 49 | fextendstr1 | 字符1 | varchar | 255 |  | √ | ' ' | 字符1 |
| 50 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 51 | fextendstr2 | 字符2 | varchar | 255 |  | √ | ' ' | 字符2 |
| 52 | fcontrol | 控件标识 | varchar | 300 |  | √ | ' ' | 控件标识 |
| 53 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 54 | fstartnameformat | 发起人显示设置 | varchar | 500 |  | √ | ' ' | 发起人显示设置 |
| 55 | forgunitid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 56 | fprocessingmobilepage | 移动处理页面 | varchar | 50 |  | √ | ' ' | 移动处理页面 |
| 57 | fsubactivityname | 节点子标题 | varchar | 100 |  | √ | ' ' | 节点子标题 |
| 58 | fsubject | 主题 | varchar | 3000 |  | √ | ' ' | 主题 |
| 59 | fprocesstype | 流程类型 | varchar | 100 |  | √ | ' ' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 60 | fowner | 拥有人 | varchar | 50 |  | √ | ' ' | 拥有人 |
| 61 | fduedate | 到期时间 | timestamp | 0 |  |  | null | 到期时间 |
| 62 | fdelegation | 委托类型 | varchar | 30 |  | √ | ' ' | 委托类型 |
| 63 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_task_create |  | fcreatedate |
| 2 | idx_wf_task_procdef |  | fprocdefid |
| 3 | idx_wf_task_procinst |  | fprocinstid |
| 4 | idx_wf_task_entitynumber |  | fentitynumber |
| 5 | idx_wf_task_ptaskid |  | fparenttaskid |
| 6 | idx_wf_task_exec |  | fexecutionid |
| 7 | idx_wf_task_businesskey |  | fbusinesskey |
| 8 | t_wf_task_pkey |  | fid |

---

## 任务监控-多语言表 t_wf_task_l

- **表名称：** 任务监控-多语言表
- **表名：** t_wf_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcaptionpc | 页面标题_PC | varchar | 300 |  | √ | ' ' | 页面标题_PC |
| 3 | fname | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 4 | fsubactivityname | 节点子标题 | varchar | 100 |  | √ | ' ' | 节点子标题 |
| 5 | fstartname | 发起人 | varchar | 255 |  | √ | ' ' | 发起人 |
| 6 | fsubject | 主题 | varchar | 3000 |  | √ | ' ' | 主题 |
| 7 | fsendername | 发送人名称 | varchar | 1000 |  | √ | ' ' | 发送人名称 |
| 8 | fextendmulstr2 | 多语言字符串2 | varchar | 255 |  | √ | ' ' | 多语言字符串2 |
| 9 | fextendmulstr1 | 多语言字符串1 | varchar | 255 |  | √ | ' ' | 多语言字符串1 |
| 10 | fcaptionmob | 页面标题_mob | varchar | 300 |  | √ | ' ' | 页面标题_mob |
| 11 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 12 | fdescription | 节点描述 | varchar | 255 |  | √ | ' ' | 节点描述 |
| 13 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 14 | fassignee | 处理人 | varchar | 255 |  | √ | ' ' | 处理人 |
| 15 | fentityname | 单据类型 | varchar | 115 |  | √ | ' ' | 单据类型 |
| 16 | fparticipantname | 当前参与人 | varchar | 3000 |  | √ | ' ' | 当前参与人 |
| 17 | fsendernameformat | 上一步处理人显示设置 | varchar | 500 |  | √ | ' ' | 上一步处理人显示设置 |
| 18 | fstartnameformat | 发起人显示设置 | varchar | 500 |  | √ | ' ' | 发起人显示设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_task_localeid |  | fid,flocaleid |
| 2 | t_wf_task_l_pkey |  | fpkid |

---

## 任务监控-分表 t_wf_task_a

- **表名称：** 任务监控-分表
- **表名：** t_wf_task_a

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
| 1 | pk_wf_task_a |  | fid |
| 2 | idx_wf_task_a_extdate |  | fextenddate2 |
