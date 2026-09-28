# 会话-dfa_chatsession

## 对话-子表 t_dfa_chatentry

- **表名称：** 对话-子表
- **表名：** t_dfa_chatentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgaiprocess | 任务流 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |
| 3 | fprocessid | 前端process | varchar | 50 |  | √ | ' ' | 前端process |
| 4 | fgaisessionid | 苍穹会话 | varchar | 50 |  | √ | ' ' | 苍穹会话 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutput | 输出 | varchar | 255 |  | √ | ' ' | 输出 |
| 7 | fmonitortraceid | MonitorTraceId | varchar | 50 |  | √ | ' ' | MonitorTraceId |
| 8 | finput | 输入 | varchar | 255 |  | √ | ' ' | 输入 |
| 9 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | foutput_tag | 输出_详情 | text | 0 |  |  | null | 输出_详情 |
| 11 | fchatstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :进行中 2 :完成 3 :失败 |
| 12 | ffinishtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 13 | finput_tag | 输入_详情 | text | 0 |  |  | null | 输入_详情 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_chatentry |  | fentryid |
| 2 | idx_dfa_chatentry_fk |  | fid |

---

## 会话-主表 t_dfa_chatsession

- **表名称：** 会话-主表
- **表名：** t_dfa_chatsession

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fusername | 用户名称 | varchar | 30 |  | √ | ' ' | 用户名称 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fuser | 用户ID | varchar | 50 |  | √ | ' ' | 用户ID |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_chatsession_m0 |  | fmasterid |
| 2 | pk_dfa_chatsession |  | fid |

---

## 消息-子表 t_dfa_chatmessage

- **表名称：** 消息-子表
- **表名：** t_dfa_chatmessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontent_tag | 消息内容_详情 | text | 0 |  |  | null | 消息内容_详情 |
| 3 | fprocess_id | 前端气泡ID | varchar | 50 |  | √ | ' ' | 前端气泡ID |
| 4 | fuser_type | 用户类型 | varchar | 50 |  | √ | ' ' | 用户类型,枚举: user :用户 agent :Agent |
| 5 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fcontent | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmsg_status | 消息状态 | varchar | 50 |  | √ | ' ' | 消息状态,枚举: 1 :处理中 2 :成功 3 :失败 4 :停止 |
| 11 | fparent_msg_id | 父级ID | int8 | 64 |  | √ | 0 | 父级ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_chatmessage_fk |  | fid |
| 2 | pk_dfa_chatmessage |  | fentryid |

---

## 会话-多语言表 t_dfa_chatsession_l

- **表名称：** 会话-多语言表
- **表名：** t_dfa_chatsession_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_chatsession_l_0 |  | fid,flocaleid |
| 2 | pk_dfa_chatsession_l |  | fpkid |
