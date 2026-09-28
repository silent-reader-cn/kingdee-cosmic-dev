# 用户行为反馈-gai_user_feedback

## 用户行为反馈-主表 t_gai_user_feedback

- **表名称：** 用户行为反馈-主表
- **表名：** t_gai_user_feedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffeedbacktype | 反馈状态 | varchar | 2 |  | √ | ' ' | 反馈状态,枚举: 0 :点踩 1 :点赞 2 :正常 3 :异常 4 :停止生成 |
| 3 | fagentname | 智能体 | varchar | 50 |  | √ | ' ' | 智能体 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fanswer | 智能体回复 | text | 0 |  |  | null | 智能体回复 |
| 6 | ftraceid | RequestID | int8 | 64 |  | √ | 0 | RequestID |
| 7 | fchattraceid | chatTraceId | varchar | 50 |  | √ | ' ' | chatTraceId |
| 8 | fassistant | 助手 | int8 | 64 |  | √ | 0 | 助手 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fsysuserorg | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fclienttype | 上报终端 | int8 | 64 |  | √ | 0 | [终端 gai_client_type](../gai_files/gai_client_type.md) |
| 12 | fcontenttype | 反馈类型 | varchar | 255 |  | √ | ' ' | 反馈类型 |
| 13 | fagent | 智能体 | int8 | 64 |  | √ | 0 | [智能体 gai_agent](../gai_files/gai_agent.md) |
| 14 | fquestion | 用户问题 | text | 0 |  |  | null | 用户问题 |
| 15 | fopusername | 上报用户名 | varchar | 100 |  | √ | ' ' | 上报用户名 |
| 16 | fchatsessionid | 会话ID | varchar | 150 |  | √ | ' ' | 会话ID |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | foptime | 上报时间 | timestamp | 0 |  |  | null | 上报时间 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fagenttype | 智能体类型 | varchar | 30 |  | √ | ' ' | 智能体类型,枚举: AGENT :AI自主规划 PROCESS :任务流 |
| 21 | fsysuser | 系统用户名 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcontent | 反馈内容 | text | 0 |  |  | null | 反馈内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_ufb_optime |  | foptime |
| 2 | pk_t_gai_user_feedback |  | fid |
| 3 | idx_gai_ufb_fbtype |  | ffeedbacktype |
| 4 | idx_gai_ufb_agenttype |  | fagenttype |
