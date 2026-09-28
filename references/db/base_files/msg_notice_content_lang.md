# 消息公告内容(多语言)-msg_notice_content_lang

## 消息公告内容(多语言)-主表 t_msg_notice_content_l

- **表名称：** 消息公告内容(多语言)-主表
- **表名：** t_msg_notice_content_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 消息公告主键 | int8 | 64 |  | √ | 0 | 消息公告主键 |
| 2 | fcontent_tag | 消息公告内容_详情 | text | 0 |  |  | null | 消息公告内容_详情 |
| 3 | flocaleid | 语言 | varchar | 10 |  | √ | ' ' | 语言 |
| 4 | fcontent | 消息公告内容 | text | 0 |  |  | null | 消息公告内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_notice_content_l_fid |  | fid,flocaleid |
| 2 | pk_t_msg_notice_content_l |  | fpkid |
