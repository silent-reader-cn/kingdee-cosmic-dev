# 消息反馈-gai_chat_msg_feedback

## 消息反馈-主表 t_gai_chat_msg_feedback

- **表名称：** 消息反馈-主表
- **表名：** t_gai_chat_msg_feedback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 反馈类型 | int4 | 32 |  | √ | 0 | 反馈类型 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fchatmessageid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 6 | fcontent | 反馈内容 | varchar | 255 |  | √ | ' ' | 反馈内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_chat_msg_feedback |  | fid |
| 2 | idx_gai_chat_msg_feedback_id |  | fchatmessageid |
