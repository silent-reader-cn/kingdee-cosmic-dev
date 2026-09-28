# 消息去重日志-msg_duplicatelog

## 消息去重日志-主表 t_wf_duplicatelog

- **表名称：** 消息去重日志-主表
- **表名：** t_wf_duplicatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | fsender | 发送人 | varchar | 100 |  | √ | ' ' | 发送人 |
| 4 | ftag | 业务标签 | varchar | 100 |  | √ | ' ' | 业务标签 |
| 5 | freceiver | 接收人 | text | 0 |  |  | null | 接收人 |
| 6 | fduplicateid | 判重ID | varchar | 200 |  | √ | ' ' | 判重ID |
| 7 | fduplicatedate | 去重时间 | timestamp | 0 |  |  | null | 去重时间 |
| 8 | fcontent | 内容摘要 | varchar | 2000 |  | √ | ' ' | 内容摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_duplicatelog_duplidate |  | fduplicatedate |
| 2 | pk_wf_duplicatelog |  | fid |
| 3 | idx_wf_duplicatelog_dupliteid |  | fduplicateid |

---

## 消息去重日志-多语言表 t_wf_duplicatelog_l

- **表名称：** 消息去重日志-多语言表
- **表名：** t_wf_duplicatelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | ftag | 业务标签 | varchar | 100 |  | √ | ' ' | 业务标签 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fcontent | 内容摘要 | varchar | 2000 |  | √ | ' ' | 内容摘要 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_duplicatelog_l |  | fpkid |
| 2 | idx_wf_duplicatelog_l |  | fid,flocaleid |
