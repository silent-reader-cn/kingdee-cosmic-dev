# 消息反馈-gai_chat_msg_feedback

## 消息反馈-主表 t_gai_chat_msg_feedback

- **表名称：** 消息反馈-主表
- **表名：** t_gai_chat_msg_feedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffbcontenttype | 点踩反馈内容类型 | varchar | 50 |  | √ | ' ' | 点踩反馈内容类型 |
| 3 | fagentid | agent | int8 | 64 |  | √ | 0 | [智能体 gai_agent](../gai_files/gai_agent.md) |
| 4 | fassistantid | 助手ID | varchar | 50 |  | √ | ' ' | 助手ID |
| 5 | fcreatorname | fcreatorname | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | 消息创建时间 | timestamp | 0 |  |  | null | 消息创建时间 |
| 7 | fprocessid | 任务流 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 8 | fchatmessageid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 9 | fmonitortraceid | MonitorTraceId | varchar | 50 |  | √ | ' ' | MonitorTraceId |
| 10 | fdepartmentid | 部门ID | varchar | 50 |  | √ | ' ' | 部门ID |
| 11 | fchatsessionid | 会话ID | varchar | 50 |  | √ | ' ' | 会话ID |
| 12 | ftype | 用户反馈(1点赞/0点踩) | int4 | 32 |  | √ | 0 | 用户反馈(1点赞/0点踩) |
| 13 | fcreatorid | 用户id | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffeedbacksource | 反馈渠道 | varchar | 50 |  | √ | ' ' | 反馈渠道 |
| 15 | fchatmessage_tag | 消息内容_详情 | text | 0 |  |  | ' ' | 消息内容_详情 |
| 16 | fcontent_tag | 用户反馈内容_详情 | text | 0 |  |  | ' ' | 用户反馈内容_详情 |
| 17 | fdepartment | 部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 18 | fappmessageid | app消息ID | varchar | 50 |  | √ | ' ' | app消息ID |
| 19 | fchatmessage | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 20 | fassistantname | 助手 | varchar | 50 |  | √ | ' ' | 助手 |
| 21 | fcontent | 用户反馈内容 | varchar | 255 |  | √ | ' ' | 用户反馈内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_chat_msg_feedback |  | fid |
| 2 | idx_gai_chat_msg_feedback_id |  | fchatmessageid |
