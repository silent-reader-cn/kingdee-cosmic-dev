# 历史记录详情-gai_chat_item

## 历史记录详情-主表 t_gai_chat_item

- **表名称：** 历史记录详情-主表
- **表名：** t_gai_chat_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时间戳 | int8 | 64 |  | √ | 0 | 时间戳 |
| 3 | ftype | 消息类型 | int8 | 64 |  | √ | 0 | 消息类型 |
| 4 | fthought_tag | 思考内容_详情 | text | 0 |  |  | null | 思考内容_详情 |
| 5 | fchatinfoid | chatInfoId | int8 | 64 |  | √ | 0 | chatInfoId |
| 6 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 7 | fthought | 思考内容 | varchar | 255 |  | √ | ' ' | 思考内容 |
| 8 | fcontent | 内容 | varchar | 255 |  |  | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_chat_item |  | fid |
| 2 | idx_t_gai_chat_item |  | fchatinfoid,ftime |
