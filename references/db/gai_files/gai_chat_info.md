# 历史记录-gai_chat_info

## 历史记录-主表 t_gai_chat_info

- **表名称：** 历史记录-主表
- **表名：** t_gai_chat_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassistantid | 助手ID | int8 | 64 |  | √ | 0 | 助手ID |
| 3 | fsessionid | sessionid | varchar | 150 |  |  | ' ' | sessionid |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 5 | fchatsessionid | chatsessionid | varchar | 150 |  |  | ' ' | chatsessionid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_chat_info |  | fid |
| 2 | idx_t_gai_chat_info |  | fuserid,fassistantid |
