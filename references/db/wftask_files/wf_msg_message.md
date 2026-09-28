# 消息模型-wf_msg_message

## 消息模型-多语言表 t_wf_message_l

- **表名称：** 消息模型-多语言表
- **表名：** t_wf_message_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 4 | fcontent_tag | 正文tag | varchar | 2000 |  | √ | ' ' | 正文tag |
| 5 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 6 | fcontent_summary | 正文摘要 | varchar | 2000 |  | √ | ' ' | 正文摘要 |
| 7 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 8 | fcontent | 正文 | text | 0 |  |  | null | 正文 |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_message_localeid |  | fid,flocaleid |
| 2 | idx_wf_message_l_title |  | ftitle |
| 3 | idx_wf_message_l_tag |  | ftag |
| 4 | t_wf_message_l_pkey |  | fpkid |

---

## 消息模型-主表 t_wf_message

- **表名称：** 消息模型-主表
- **表名：** t_wf_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 3 | ftoall | 全员消息 | bpchar | 1 |  | √ | '0' | 全员消息 |
| 4 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 5 | fbizdataid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 6 | fentitynumber | 实体对象 | varchar | 100 |  | √ | ' ' | 实体对象 |
| 7 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 8 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fconfig | 参数集合 | varchar | 2000 |  | √ | ' ' | 参数集合 |
| 11 | freadtime | 阅读日期 | timestamp | 0 |  |  | null | 阅读日期 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fnestappid | 内嵌业务来源应用 | varchar | 100 |  | √ | ' ' | 内嵌业务来源应用 |
| 14 | fsendtime | 发送日期 | timestamp | 0 |  |  | null | 发送日期 |
| 15 | ftplscene | 场景编码 | varchar | 200 |  | √ | ' ' | 场景编码 |
| 16 | fcontenturl | 详细信息url | varchar | 1000 |  | √ | ' ' | 详细信息url |
| 17 | fnestbillno | 内嵌业务编号 | varchar | 255 |  | √ | ' ' | 内嵌业务编号 |
| 18 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作,枚举: |
| 19 | fchannels | 发送渠道 | varchar | 300 |  | √ | ' ' | 发送渠道 |
| 20 | fsender | 发送人 | varchar | 100 |  | √ | ' ' | 发送人 |
| 21 | freadstate | 阅读状态 | varchar | 30 |  | √ | ' ' | 阅读状态,枚举: read :已读 unread :未读 |
| 22 | fcontent_summary | 正文摘要 | varchar | 2000 |  | √ | ' ' | 正文摘要 |
| 23 | fmobcontenturl | 移动端信息url | varchar | 1000 |  | √ | ' ' | 移动端信息url |
| 24 | ftype | 消息类型 | int8 | 64 |  | √ | 0 | 消息类型 |
| 25 | fcontent_tag | 正文tag | text | 0 |  |  | null | 正文tag |
| 26 | fcontent | fcontent | text | 0 |  |  | null |  |
| 27 | fnestbillid | 内嵌业务单据ID | int8 | 64 |  | √ | 0 | 内嵌业务单据ID |
| 28 | fnestentitynumber | 内嵌业务编码 | varchar | 50 |  | √ | ' ' | 内嵌业务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_message_pkey |  | fid |
| 2 | idx_wf_message_tplscene |  | ftplscene |
| 3 | idx_wf_message_type |  | ftype |
| 4 | idx_wf_message_createdate |  | fcreatedate |
| 5 | idx_wf_message_tag |  | ftag |
| 6 | idx_wf_message_entnumber |  | fentitynumber |
