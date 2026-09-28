# 流程实例-wf_execution

## 流程实例-多语言表 t_wf_execution_l

- **表名称：** 流程实例-多语言表
- **表名：** t_wf_execution_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fstarusernameformat | 发起人姓名格式化 | varchar | 500 |  | √ | ' ' | 发起人姓名格式化 |
| 4 | fsubject | 单据主题 | varchar | 3000 |  | √ | ' ' | 单据主题 |
| 5 | factivityname | 当前节点 | varchar | 500 |  | √ | ' ' | 当前节点 |
| 6 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fpresentassignee | 当前处理人 | varchar | 2000 |  | √ | ' ' | 当前处理人 |
| 9 | fentrabillname | 入口单据名称 | varchar | 255 |  | √ | ' ' | 入口单据名称 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_execution_l_pkey |  | fpkid |
| 2 | idx_wf_execution_localeid |  | fid,flocaleid |

---

## 流程实例-主表 t_wf_execution

- **表名称：** 流程实例-主表
- **表名：** t_wf_execution

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiseventscope | 事件范围 | bpchar | 1 |  | √ | '0' | 事件范围 |
| 3 | fismiroot | 是否多实例根 | bpchar | 1 |  | √ | '0' | 是否多实例根 |
| 4 | fisconcurrent | 是否单据实例 | bpchar | 1 |  | √ | '0' | 是否单据实例 |
| 5 | fsuperexec | 主流程实例ID | int8 | 64 |  | √ | 0 | 主流程实例ID |
| 6 | fstarusernameformat | 发起人姓名格式化 | varchar | 500 |  | √ | ' ' | 发起人姓名格式化 |
| 7 | fpriorityshow | 标记显示 | varchar | 50 |  | √ | ' ' | 标记显示,枚举: transfer :移交给我的 |
| 8 | factid | 当前活动节点ID | varchar | 2000 |  | √ | ' ' | 当前活动节点ID |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forgviewid | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型 |
| 11 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 12 | fstartuserid | 发起人ID | int8 | 64 |  | √ | 0 | 发起人ID |
| 13 | fevtsubscrcount | 事件子脚本数 | int8 | 64 |  | √ | 0 | 事件子脚本数 |
| 14 | frootprocinstid | 根流程实例ID | int8 | 64 |  | √ | 0 | 根流程实例ID |
| 15 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 16 | fisscope | 作用范围 | bpchar | 1 |  | √ | '0' | 作用范围 |
| 17 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 18 | fisactive | 是否存活 | bpchar | 1 |  | √ | '1' | 是否存活 |
| 19 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 20 | fsuspensionstate | 流程状态 | varchar | 50 |  | √ | ' ' | 流程状态,枚举: 1 :正在运行 2 :挂起 |
| 21 | fbatchnumber | 批次号 | varchar | 255 |  | √ | ' ' | 批次号 |
| 22 | fdeadletterjobcount | 死信工作数 | int8 | 64 |  | √ | 0 | 死信工作数 |
| 23 | factinstid | 当前节点实例ID | int8 | 64 |  | √ | 0 | 当前节点实例ID |
| 24 | ftaskcount | 任务数 | int8 | 64 |  | √ | 0 | 任务数 |
| 25 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 26 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 方案id |
| 27 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 28 | fentitynumber | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: |
| 29 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 30 | fiscountenabled | 是否计数 | bpchar | 1 |  | √ | '0' | 是否计数 |
| 31 | ftimerjobcount | 定时工作数 | int8 | 64 |  | √ | 0 | 定时工作数 |
| 32 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fbusinessid | 流程标识 | varchar | 255 |  | √ | ' ' | 流程标识 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fvarcount | 变量数 | int8 | 64 |  | √ | 0 | 变量数 |
| 36 | factivityname | 当前节点 | varchar | 500 |  | √ | ' ' | 当前节点 |
| 37 | fidlinkcount | 用户连接数 | int8 | 64 |  | √ | 0 | 用户连接数 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fparentid | 父流程实例ID | int8 | 64 |  | √ | 0 | 父流程实例ID |
| 40 | ftestingplanid | 测试计划id | int8 | 64 |  | √ | 0 | 测试计划id |
| 41 | fsubject | 单据主题 | varchar | 3000 |  | √ | ' ' | 单据主题 |
| 42 | fcachedentstate | 终止类型 | int8 | 64 |  | √ | 0 | 终止类型 |
| 43 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 44 | fmainorgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 45 | fjobcount | 工作数 | int8 | 64 |  | √ | 0 | 工作数 |
| 46 | fpresentassignee | 当前处理人 | varchar | 2000 |  | √ | ' ' | 当前处理人 |
| 47 | ftaskid | 当前任务ID | int8 | 64 |  | √ | 0 | 当前任务ID |
| 48 | fentrabillname | 入口单据名称 | varchar | 255 |  | √ | ' ' | 入口单据名称 |
| 49 | flocktime | 锁定时间 | timestamp | 0 |  |  | null | 锁定时间 |
| 50 | fbilltype | 业务单据类型 | varchar | 50 |  | √ | ' ' | 业务单据类型 |
| 51 | fsuspjobcount | 挂起工作数 | int8 | 64 |  | √ | 0 | 挂起工作数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_execution_parent |  | fparentid |
| 2 | idx_wf_execution_proc |  | fprocdefid |
| 3 | idx_wf_execution_super |  | fsuperexec |
| 4 | idx_wf_exec_proc_inst_id |  | fprocinstid |
| 5 | idx_wf_exec_root |  | frootprocinstid |
| 6 | t_wf_execution_pkey |  | fid |
| 7 | idx_wf_exec_buskey |  | fbusinesskey |
| 8 | idx_wf_exec_createdateorg |  | fcreatedate,fmainorgid |
| 9 | idx_wf_execution_tc_count |  | fcreatorid,fparentid,fentitynumber |
