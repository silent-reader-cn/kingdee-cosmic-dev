# 监控日志单据-gai_log_bak

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

## 步骤单据体-子表 t_gai_log_step

- **表名称：** 步骤单据体-子表
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
| 7 | ffirsttokentime | ffirsttokentime | timestamp | 0 |  |  | null |  |
| 8 | fparentstepid | 父步骤ID | int8 | 64 |  | √ | 0 | 父步骤ID |
| 9 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 10 | fstepinput | 输入 | varchar | 255 |  |  | null | 输入 |
| 11 | ferrorcode | ferrorcode | varchar | 100 |  | √ | '0' |  |
| 12 | ftraceid | TraceId | int8 | 64 |  | √ | 0 | TraceId |
| 13 | ftotaltoken | token数 | int4 | 32 |  | √ | 0 | token数 |
| 14 | fmetadata | 元数据 | varchar | 255 |  |  | null | 元数据 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fconversation_tag | fconversation_tag | text | 0 |  |  | null |  |
| 17 | fstepoutput_tag | 输出_详情 | text | 0 |  |  | null | 输出_详情 |
| 18 | fthought | fthought | varchar | 255 |  | √ | ' ' |  |
| 19 | fgptprocessid | GPT任务 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 20 | flatency | 耗时 | numeric | 23 | 10 | √ | 0 | 耗时 |
| 21 | fstepinput_tag | 输入_详情 | text | 0 |  |  | null | 输入_详情 |
| 22 | ftags | 标签 | varchar | 255 |  |  | null | 标签 |
| 23 | fstepoutput | 输出 | varchar | 255 |  |  | null | 输出 |
| 24 | fthought_tag | fthought_tag | text | 0 |  |  | null |  |
| 25 | fstepbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 26 | fmodelname | 模型名 | varchar | 100 |  | √ | ' ' | 模型名 |
| 27 | fconversation | fconversation | varchar | 255 |  | √ | ' ' |  |
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

## 监控日志单据-主表 t_gai_log

- **表名称：** 监控日志单据-主表
- **表名：** t_gai_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | fagentid | int8 | 64 |  | √ | 0 |  |
| 3 | ftraceinput | ftraceinput | varchar | 50 |  | √ | ' ' |  |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fpromptid | fpromptid | int8 | 64 |  | √ | 0 |  |
| 7 | fagent | fagent | int8 | 64 |  | √ | 0 |  |
| 8 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fmonitortraceid | fmonitortraceid | varchar | 100 |  | √ | ' ' |  |
| 10 | fprocess | fprocess | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用 |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | ftracetoken | ftracetoken | varchar | 50 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 19 | ftracelatency | ftracelatency | varchar | 50 |  | √ | ' ' |  |
| 20 | fvectormodel | fvectormodel | varchar | 100 |  | √ | ' ' |  |
| 21 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 24 | ftraceid | 追踪ID | int8 | 64 |  | √ | 0 | 追踪ID |
| 25 | fassistantid | fassistantid | int8 | 64 |  | √ | 0 |  |
| 26 | fgenerationmodel | fgenerationmodel | varchar | 100 |  | √ | ' ' |  |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fprocessid | fprocessid | int8 | 64 |  | √ | 0 |  |
| 29 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fchatsessionid | 对话ID | varchar | 150 |  | √ | ' ' | 对话ID |
| 31 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 32 | fcloudid | 业务云 | varchar | 50 |  | √ | ' ' | 业务云 |
| 33 | fsessionid | 会话ID | int8 | 64 |  | √ | 0 | 会话ID |
| 34 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 35 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 36 | ftracenum | ftracenum | int8 | 64 |  | √ | 0 |  |
| 37 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

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
