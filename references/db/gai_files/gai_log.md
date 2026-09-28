# 监控日志-gai_log

## 子单据体-子表 t_gai_log_step_event

- **表名称：** 子单据体-子表
- **表名：** t_gai_log_step_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftotaltoken | token数 | int4 | 32 |  | √ | 0 | token数 |
| 2 | feventid | EventId | int8 | 64 |  | √ | 0 | EventId |
| 3 | feventinput | 输入 | varchar | 255 |  |  | null | 输入 |
| 4 | fmetadata | 元数据 | varchar | 255 |  |  | null | 元数据 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstepid | StepId | int8 | 64 |  | √ | 0 | StepId |
| 7 | feventinput_tag | 输入_详情 | text | 0 |  |  | null | 输入_详情 |
| 8 | fgptprocessid | GPT任务 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 9 | fgptprocessnodeid | GPT流程节点ID | int8 | 64 |  | √ | 0 | GPT流程节点ID |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | ftags | 标签 | varchar | 255 |  |  | null | 标签 |
| 12 | feventname | 事件名 | varchar | 100 |  | √ | ' ' | 事件名 |
| 13 | feventtime | 事件时间 | timestamp | 0 |  |  | null | 事件时间 |
| 14 | fsteptype | 步骤类型 | varchar | 50 |  | √ | ' ' | 步骤类型 |
| 15 | feventoutput | 输出 | varchar | 255 |  |  | null | 输出 |
| 16 | fmodelname | 模型名 | varchar | 100 |  | √ | ' ' | 模型名 |
| 17 | feventoutput_tag | 输出_详情 | text | 0 |  |  | null | 输出_详情 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_log_step_event_fk |  | fentryid |
| 2 | pk_t_gai_log_step_event |  | fdetailid |

---

## 单据体-子表 t_gai_log_step

- **表名称：** 单据体-子表
- **表名：** t_gai_log_step

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstepid | StepId | int8 | 64 |  | √ | 0 | StepId |
| 3 | fgptprocessnodeid | GPT流程节点ID | int8 | 64 |  | √ | 0 | GPT流程节点ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fstepfinishtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 6 | fsteptype | 步骤类型 | varchar | 50 |  | √ | ' ' | 步骤类型 |
| 7 | ffirsttokentime | 首Token时间 | timestamp | 0 |  |  | null | 首Token时间 |
| 8 | fparentstepid | 父步骤ID | int8 | 64 |  | √ | 0 | 父步骤ID |
| 9 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 10 | fstepinput | 输入 | varchar | 255 |  |  | null | 输入 |
| 11 | ferrorcode | 错误码 | varchar | 100 |  | √ | '0' | 错误码 |
| 12 | ftraceid | TraceId | int8 | 64 |  | √ | 0 | TraceId |
| 13 | ftotaltoken | token数 | int4 | 32 |  | √ | 0 | token数 |
| 14 | fmetadata | 元数据 | varchar | 255 |  |  | null | 元数据 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fconversation_tag | 上下文_详情 | text | 0 |  |  | null | 上下文_详情 |
| 17 | fstepoutput_tag | 输出_详情 | text | 0 |  |  | null | 输出_详情 |
| 18 | fthought | 思考 | varchar | 255 |  | √ | ' ' | 思考 |
| 19 | fgptprocessid | GPT任务 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 20 | flatency | 耗时 | numeric | 23 | 10 | √ | 0 | 耗时 |
| 21 | fstepinput_tag | 输入_详情 | text | 0 |  |  | null | 输入_详情 |
| 22 | ftags | 标签 | varchar | 255 |  |  | null | 标签 |
| 23 | fstepoutput | 输出 | varchar | 255 |  |  | null | 输出 |
| 24 | fthought_tag | 思考_详情 | text | 0 |  |  | null | 思考_详情 |
| 25 | fstepbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 26 | fmodelname | 模型名 | varchar | 100 |  | √ | ' ' | 模型名 |
| 27 | fconversation | 上下文 | varchar | 255 |  | √ | ' ' | 上下文 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_log_step_traceid |  | ftraceid |
| 2 | idx_gai_log_step_fk |  | fid |
| 3 | idx_gai_log_step_ctime |  | fcreatetime |
| 4 | pk_t_gai_log_step |  | fentryid |
| 5 | idx_gai_log_stepid |  | fstepid |

---

## 监控日志-主表 t_gai_log

- **表名称：** 监控日志-主表
- **表名：** t_gai_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 智能体 | int8 | 64 |  | √ | 0 | 智能体 |
| 3 | ftraceinput | trace输入 | varchar | 50 |  | √ | ' ' | trace输入 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpromptid | 提示词 | int8 | 64 |  | √ | 0 | 提示词 |
| 7 | fagent | 智能体 | int8 | 64 |  | √ | 0 | [智能体 gai_agent](../gai_files/gai_agent.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmonitortraceid | Monitor跟踪ID | varchar | 100 |  | √ | ' ' | Monitor跟踪ID |
| 10 | fprocess | 任务流 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | ftracetoken | trace_token数 | varchar | 50 |  | √ | ' ' | trace_token数 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | ftracelatency | trace耗时 | varchar | 50 |  | √ | ' ' | trace耗时 |
| 20 | fvectormodel | 向量模型 | varchar | 100 |  | √ | ' ' | 向量模型 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 24 | ftraceid | 追踪Id | int8 | 64 |  | √ | 0 | 追踪Id |
| 25 | fassistantid | 助手 | int8 | 64 |  | √ | 0 | 助手 |
| 26 | fgenerationmodel | 文本模型 | varchar | 100 |  | √ | ' ' | 文本模型 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fprocessid | 任务流 | int8 | 64 |  | √ | 0 | 任务流 |
| 29 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fchatsessionid | 对话Id | varchar | 150 |  | √ | ' ' | 对话Id |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fcloudid | 业务云 | varchar | 50 |  | √ | ' ' | 业务云 |
| 33 | fsessionid | 会话Id | int8 | 64 |  | √ | 0 | 会话Id |
| 34 | fenable | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :失败 1 :成功 |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | ftracenum | traces数 | int8 | 64 |  | √ | 0 | traces数 |
| 37 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_log_master |  | fmasterid |
| 2 | idx_gai_log_mtraceid |  | fcreatetime,fmonitortraceid,fsessionid |
| 3 | idx_t_gai_log_createorg |  | fcreateorgid |
| 4 | pk_t_gai_log |  | fid |
| 5 | idx_gai_log_chatsid |  | fchatsessionid |
| 6 | idx_gai_log |  | ftraceid |
| 7 | idx_gai_log_ctime |  | fcreatetime |

---

## 监控日志-使用范围表 t_gai_log_u

- **表名称：** 监控日志-使用范围表
- **表名：** t_gai_log_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_log_u_uo |  | fuseorgid |
| 2 | pk_t_gai_log_u |  | fdataid,fuseorgid |

---

## 监控日志-多语言表 t_gai_log_l

- **表名称：** 监控日志-多语言表
- **表名：** t_gai_log_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_log_l |  | fid |
| 2 | pk_t_gai_log_l |  | fpkid |
