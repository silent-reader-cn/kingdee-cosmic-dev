# 历史消息-wf_msg_himessage

## 历史消息-主表 t_wf_himessage

- **表名称：** 历史消息-主表
- **表名：** t_wf_himessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftag | 自定义标签 | varchar | 230 |  | √ | ' ' | 自定义标签 |
| 3 | ftoall | 全员消息 | bpchar | 1 |  | √ | '0' | 全员消息 |
| 4 | fsendername | 发送人名称 | varchar | 230 |  | √ | ' ' | 发送人名称 |
| 5 | fbizdataid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 6 | fentitynumber | 实体对象 | varchar | 100 |  | √ | ' ' | 实体对象 |
| 7 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 8 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fconfig | 参数集合 | varchar | 2000 |  | √ | ' ' | 参数集合 |
| 11 | freadtime | 阅读日期 | timestamp | 0 |  |  | null | 阅读日期 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fnestappid | 内嵌业务来源应用 | varchar | 100 |  | √ | ' ' | 内嵌业务来源应用 |
| 14 | fsendtime | 发送日期 | timestamp | 0 |  |  | null | 发送日期 |
| 15 | ftplscene | 场景编码 | varchar | 200 |  | √ | ' ' | 场景编码 |
| 16 | fcontenturl | 详细信息url | varchar | 1000 |  | √ | ' ' | 详细信息url |
| 17 | fnestbillno | 内嵌业务编号 | varchar | 255 |  | √ | ' ' | 内嵌业务编号 |
| 18 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作 |
| 19 | fchannels | 发送渠道 | varchar | 200 |  | √ | ' ' | 发送渠道 |
| 20 | fsender | 发送人 | varchar | 100 |  | √ | ' ' | 发送人 |
| 21 | fdeletereason | 删除原因 | varchar | 50 |  | √ | ' ' | 删除原因 |
| 22 | freadstate | 阅读状态 | varchar | 30 |  | √ | ' ' | 阅读状态,枚举: read :已读 unread :未读 |
| 23 | fcontent_summary | 正文摘要 | varchar | 2000 |  | √ | ' ' | 正文摘要 |
| 24 | fdeletedate | 删除日期 | timestamp | 0 |  |  | null | 删除日期 |
| 25 | fmobcontenturl | 移动端信息url | varchar | 1000 |  | √ | ' ' | 移动端信息url |
| 26 | ftype | 消息类型 | int8 | 64 |  | √ | 0 | 消息类型 |
| 27 | fcontent_tag | 正文tag | text | 0 |  |  | null | 正文tag |
| 28 | fcontent | fcontent | text | 0 |  |  | null |  |
| 29 | fnestbillid | 内嵌业务单据ID | int8 | 64 |  | √ | 0 | 内嵌业务单据ID |
| 30 | fnestentitynumber | 内嵌业务编码 | varchar | 50 |  | √ | ' ' | 内嵌业务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_himessage_pkey |  | fid |
| 2 | idx_wf_himessage_createdate |  | fcreatedate |
| 3 | idx_wf_himessage_entnumber |  | fentitynumber |
| 4 | idx_wf_himessage_type |  | ftype |
| 5 | idx_wf_himessage_deldate |  | fdeletedate |
| 6 | idx_wf_himessage_tag |  | ftag |

---

## 历史消息-多语言表 t_wf_himessage_l

- **表名称：** 历史消息-多语言表
- **表名：** t_wf_himessage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | ftag | 自定义标签 | varchar | 230 |  | √ | ' ' | 自定义标签 |
| 4 | fcontent_tag | 正文tag | varchar | 2000 |  | √ | ' ' | 正文tag |
| 5 | fsendername | 发送人名称 | varchar | 230 |  | √ | ' ' | 发送人名称 |
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
| 1 | idx_wf_himessage_l_title |  | ftitle |
| 2 | t_wf_himessage_l_pkey |  | fpkid |
| 3 | idx_wf_himessage_l_tag |  | ftag |
| 4 | idx_wf_himessage_localeid |  | fid,flocaleid |
