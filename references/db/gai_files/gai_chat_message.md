# 消息-gai_chat_message

## 消息-主表 t_gai_chat_message

- **表名称：** 消息-主表
- **表名：** t_gai_chat_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | TraceId | int8 | 64 |  | √ | 0 | TraceId |
| 3 | fassistantid | 助手ID | int8 | 64 |  | √ | 0 | 助手ID |
| 4 | fchattraceid | chatTraceId | varchar | 50 |  | √ | ' ' | chatTraceId |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fskilltype | 技能类型 | varchar | 50 |  | √ | ' ' | 技能类型,枚举: process :GPT任务 agent :Agent智能体 |
| 7 | fthought | 思考内容 | varchar | 255 |  | √ | ' ' | 思考内容 |
| 8 | frunid | 执行ID | int8 | 64 |  | √ | 0 | 执行ID |
| 9 | fskillsrc | 技能来源 | varchar | 50 |  | √ | ' ' | 技能来源,枚举: user :用户选择 auto :中控命中 |
| 10 | frunstepid | 执行步骤ID | int8 | 64 |  | √ | 0 | 执行步骤ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmsgstatus | 消息状态 | varchar | 50 |  | √ | ' ' | 消息状态,枚举: in_progress :执行中（暂未启用） cancelled :已取消 completed :执行成功（暂未启用） |
| 13 | ftype | 类型 | int4 | 32 |  | √ | 0 | 类型 |
| 14 | fconfig | 消息配置 | varchar | 255 |  | √ | ' ' | 消息配置 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fskillid | 技能ID | int8 | 64 |  | √ | 0 | 技能ID |
| 17 | fthought_tag | 思考内容_详情 | text | 0 |  |  | null | 思考内容_详情 |
| 18 | fcontent_tag | 消息内容_详情 | text | 0 |  |  | null | 消息内容_详情 |
| 19 | fsessionid | 会话FID | int8 | 64 |  | √ | 0 | 会话FID |
| 20 | fconfig_tag | 消息配置_详情 | text | 0 |  |  | null | 消息配置_详情 |
| 21 | fenable | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 22 | fcontent | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_message_type |  | ftype |
| 2 | pk_t_gai_chat_message |  | fid |
| 3 | idx_gai_chat_message_sid |  | fsessionid |
| 4 | idx_gai_chat_message_tid |  | fchattraceid,ftype |
