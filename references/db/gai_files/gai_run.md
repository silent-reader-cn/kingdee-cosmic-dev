# 执行-gai_run

## 单据体-执行步骤-子表 t_gai_run_step_entry

- **表名称：** 单据体-执行步骤-子表
- **表名：** t_gai_run_step_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsteperrormsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 3 | fsteperrorcode | 错误码 | varchar | 50 |  | √ | ' ' | 错误码 |
| 4 | fstepprompttokens | 提示Token数 | int8 | 64 |  | √ | 0 | 提示Token数 |
| 5 | fstepcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fstepcancelledat | 成功取消时间 | timestamp | 0 |  |  | null | 成功取消时间 |
| 8 | fstepfailedat | 执行失败时间 | timestamp | 0 |  |  | null | 执行失败时间 |
| 9 | fstepmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsteperrormsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 11 | fstepstartedat | 开始执行时间 | timestamp | 0 |  |  | null | 开始执行时间 |
| 12 | fstepchatitemid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 13 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: retrieval :检索 action :工具调用 llm_generation :大语言模型生成 |
| 14 | fstepcompletiontokens | 完成Token数 | int8 | 64 |  | √ | 0 | 完成Token数 |
| 15 | fstepdetails | 步骤详情 | varchar | 255 |  | √ | ' ' | 步骤详情 |
| 16 | fstepexpiredat | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 17 | fstepstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: in_progress :执行中 cancelled :已取消 failed :执行失败 completed :执行成功 expired :已过期 |
| 18 | fstepcompletedat | 执行成功时间 | timestamp | 0 |  |  | null | 执行成功时间 |
| 19 | fstepdetails_tag | 步骤详情_详情 | text | 0 |  |  | null | 步骤详情_详情 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_run_step_entry |  | fentryid |
| 2 | idx_gai_run_step_entry_fid |  | fid |

---

## 执行-主表 t_gai_run

- **表名称：** 执行-主表
- **表名：** t_gai_run

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpromptids | 使用的GPT提示ID | varchar | 2000 |  | √ | ' ' | 使用的GPT提示ID |
| 3 | fprocessids | 使用的GPT任务ID | varchar | 2000 |  | √ | ' ' | 使用的GPT任务ID |
| 4 | fcompletiontokens | 完成Token数 | int8 | 64 |  | √ | 0 | 完成Token数 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | ffailedat | 执行失败时间 | timestamp | 0 |  |  | null | 执行失败时间 |
| 7 | fmessageid | 用户消息 | int8 | 64 |  | √ | 0 | 用户消息 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcancelledat | 成功取消时间 | timestamp | 0 |  |  | null | 成功取消时间 |
| 10 | ffileids | 使用的文件ID | varchar | 2000 |  | √ | ' ' | 使用的文件ID |
| 11 | fcompletedat | 执行成功时间 | timestamp | 0 |  |  | null | 执行成功时间 |
| 12 | fexpiredat | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 13 | ferrormsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 14 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 15 | ferrorcode | 错误码 | varchar | 50 |  | √ | ' ' | 错误码 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ferrormsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 18 | fmetadata | 元数据 | varchar | 255 |  | √ | ' ' | 元数据 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fstartedat | 开始执行时间 | timestamp | 0 |  |  | null | 开始执行时间 |
| 21 | fassistantmessageid | 助手结果消息 | int8 | 64 |  | √ | 0 | 助手结果消息 |
| 22 | fprompttokens | 提示Token数 | int8 | 64 |  | √ | 0 | 提示Token数 |
| 23 | frunstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: in_progress :执行中 cancelling :取消中 cancelled :已取消 failed :执行失败 completed :执行成功 expired :已过期 |
| 24 | fsessionid | 会话 | int8 | 64 |  | √ | 0 | 会话 |
| 25 | fllm | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型 |
| 26 | ftoolids | 使用的工具ID | varchar | 2000 |  | √ | ' ' | 使用的工具ID |
| 27 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_run |  | fid |
| 2 | idx_gai_run_fchatinfoid |  | fsessionid |
