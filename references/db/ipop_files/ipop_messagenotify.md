# 消息通知配置-ipop_messagenotify

## 消息通知配置-主表 t_ipop_messagenotify

- **表名称：** 消息通知配置-主表
- **表名：** t_ipop_messagenotify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessagecenter | 站内信 | varchar | 1 |  | √ | '1' | 站内信 |
| 3 | fmessagereceivers_tag | 消息接收人_详情 | text | 0 |  |  | ' ' | 消息接收人_详情 |
| 4 | fmessagereceivers | 消息接收人 | varchar | 2000 |  | √ | ' ' | 消息接收人 |
| 5 | femail | 邮件 | varchar | 1 |  | √ | '0' | 邮件 |
| 6 | fmessagetype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型,枚举: lowCondition :资源可用量低于剩余量时提醒 exhaust :资源已用尽提醒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_messagenotify_type |  | fmessagetype |
| 2 | pk_ipop_messagenotify |  | fid |
