# 监控日志-gai_log

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
| 7 | fparentstepid | 父步骤ID | int8 | 64 |  | √ | 0 | 父步骤ID |
| 8 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 9 | fstepinput | 输入 | varchar | 255 |  |  | null | 输入 |
| 10 | ftraceid | TraceId | int8 | 64 |  | √ | 0 | TraceId |
| 11 | ftotaltoken | token数 | int4 | 32 |  | √ | 0 | token数 |
| 12 | fmetadata | 元数据 | varchar | 255 |  |  | null | 元数据 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fconversation_tag | 上下文_详情 | text | 0 |  |  | null | 上下文_详情 |
| 15 | fstepoutput_tag | 输出_详情 | text | 0 |  |  | null | 输出_详情 |
| 16 | fthought | 思考 | varchar | 255 |  | √ | ' ' | 思考 |
| 17 | fgptprocessid | GPT任务 | int8 | 64 |  | √ | 0 | 任务流 gai_process |
| 18 | flatency | 耗时 | numeric | 23 | 10 | √ | 0 | 耗时 |
| 19 | fstepinput_tag | 输入_详情 | text | 0 |  |  | null | 输入_详情 |
| 20 | ftags | 标签 | varchar | 255 |  |  | null | 标签 |
| 21 | fstepoutput | 输出 | varchar | 255 |  |  | null | 输出 |
| 22 | fthought_tag | 思考_详情 | text | 0 |  |  | null | 思考_详情 |
| 23 | fstepbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 24 | fmodelname | 模型名 | varchar | 100 |  | √ | ' ' | 模型名 |
| 25 | fconversation | 上下文 | varchar | 255 |  | √ | ' ' | 上下文 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_log_step_fk |  | fid |
| 2 | pk_t_gai_log_step |  | fentryid |

---

## 监控日志-主表 t_gai_log

- **表名称：** 监控日志-主表
- **表名：** t_gai_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceinput | trace输入 | varchar | 50 |  | √ | ' ' | trace输入 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ftracetoken | trace_token数 | varchar | 50 |  | √ | ' ' | trace_token数 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | ftracelatency | trace耗时 | varchar | 50 |  | √ | ' ' | trace耗时 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftraceid | 追踪ID | int8 | 64 |  | √ | 0 | 追踪ID |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fchatsessionid | 对话ID | varchar | 150 |  | √ | ' ' | 对话ID |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fcloudid | 业务云 | varchar | 50 |  | √ | ' ' | 业务云 |
| 24 | fsessionid | 会话ID | int8 | 64 |  | √ | 0 | 会话ID |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 27 | ftracenum | traces数 | int8 | 64 |  | √ | 0 | traces数 |
| 28 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_log_master |  | fmasterid |
| 2 | pk_t_gai_log |  | fid |
| 3 | idx_t_gai_log_createorg |  | fcreateorgid |
| 4 | idx_gai_log |  | ftraceid |

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
| 8 | fgptprocessid | GPT任务 | int8 | 64 |  | √ | 0 | 任务流 gai_process |
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
