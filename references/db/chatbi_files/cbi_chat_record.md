# 历史对话-cbi_chat_record

## 历史对话-主表 t_cbi_chat_record

- **表名称：** 历史对话-主表
- **表名：** t_cbi_chat_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffeedbacktype | 反馈情况 | varchar | 2 |  |  | '0' | 反馈情况,枚举: 1 :点赞 2 :点踩 |
| 3 | fstop_answer | 是否停止回答 | varchar | 50 |  |  | ' ' | 是否停止回答,枚举: 1 :是 0 :否 |
| 4 | fanswer_end_time | 回答结束时间 | timestamp | 0 |  |  | null | 回答结束时间 |
| 5 | fgroupid | fgroupid | varchar | 64 |  |  | ' ' |  |
| 6 | faskcontent | 回答内容 | varchar | 100 |  | √ | ' ' | 回答内容 |
| 7 | fstart_answer_cost_time | 开始回答耗时(ms) | int8 | 64 |  | √ | 0 | 开始回答耗时(ms) |
| 8 | fdialogue_type | 对话方式 | varchar | 50 |  | √ | ' ' | 对话方式,枚举: text :文本 voice :语音 |
| 9 | fsource | fsource | varchar | 64 |  |  | ' ' |  |
| 10 | fiserror | 是否出错 | varchar | 2 |  | √ | '0' | 是否出错,枚举: 1 :是 0 :否 |
| 11 | fanswer_begin_time | 回答开始时间 | timestamp | 0 |  |  | null | 回答开始时间 |
| 12 | fcreate_time | fcreate_time | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 13 | fassistant_id | fassistant_id | varchar | 100 |  |  | ' ' |  |
| 14 | fuser_id | fuser_id | varchar | 64 |  | √ | '0' |  |
| 15 | ftraceid | TraceID | varchar | 64 |  |  | ' ' | TraceID |
| 16 | ftopic_name | 分析主题 | varchar | 1000 |  |  | ' ' | 分析主题 |
| 17 | frequest_id | 回答ID | varchar | 100 |  |  | ' ' | 回答ID |
| 18 | fuser_name | 用户名 | varchar | 50 |  |  | ' ' | 用户名 |
| 19 | ftopic_id | ftopic_id | varchar | 64 |  |  | ' ' |  |
| 20 | faisessionid | faisessionid | varchar | 100 |  |  | ' ' |  |
| 21 | faimessage_id | faimessage_id | varchar | 64 |  |  | ' ' |  |
| 22 | faitask_id | faitask_id | varchar | 64 |  |  | ' ' |  |
| 23 | fservicetype | 服务类型 | varchar | 50 |  | √ | ' ' | 服务类型,枚举: agent :苍穹Agent dify :Dify workflowengine :工作流 |
| 24 | ftype | ftype | varchar | 100 |  |  | '0' |  |
| 25 | fask_time | 提问时间 | timestamp | 0 |  |  | null | 提问时间 |
| 26 | frepeatrequest | 是否重新生成 | varchar | 2 |  |  | '0' | 是否重新生成,枚举: 1 :是 0 :否 |
| 27 | frequeryid | 是否重新生成 | varchar | 64 |  | √ | ' ' | 是否重新生成 |
| 28 | fsessionid | fsessionid | varchar | 100 |  |  | ' ' |  |
| 29 | fanswer_cost_time | 回答耗时(ms) | int8 | 64 |  | √ | 0 | 回答耗时(ms) |
| 30 | fcontent | 提问内容 | text | 0 |  |  | null | 提问内容 |
| 31 | fassistant_name | fassistant_name | varchar | 50 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cbi_chat_record_pkey |  | fid |
| 2 | t_cbi_chat_record_frequestid_idx |  | frequest_id |
