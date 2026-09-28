# 历史消息接受者-wf_msg_hireceiver

## 历史消息接受者-主表 t_wf_himsgreceiver

- **表名称：** 历史消息接受者-主表
- **表名：** t_wf_himsgreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftoall | 全员消息 | bpchar | 1 |  | √ | '0' | 全员消息 |
| 3 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 4 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 5 | fbizdataid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 6 | fentitynumber | 实体对象 | varchar | 100 |  | √ | ' ' | 实体对象 |
| 7 | fsource | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 8 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 9 | fmessageid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fconfig | 参数集合 | varchar | 2000 |  | √ | ' ' | 参数集合 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | freadtime | 阅读日期 | timestamp | 0 |  |  | null | 阅读日期 |
| 14 | fnestappid | 内嵌业务来源应用 | varchar | 100 |  | √ | ' ' | 内嵌业务来源应用 |
| 15 | ftplscene | 场景编码 | varchar | 200 |  | √ | ' ' | 场景编码 |
| 16 | fcontenturl | 详细信息url | varchar | 1000 |  | √ | ' ' | 详细信息url |
| 17 | fnestbillno | 内嵌业务编号 | varchar | 255 |  | √ | ' ' | 内嵌业务编号 |
| 18 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作,枚举: |
| 19 | fsender | 发送人 | varchar | 100 |  | √ | ' ' | 发送人 |
| 20 | fterminalway | 终端处理方式 | varchar | 500 |  | √ | ' ' | 终端处理方式 |
| 21 | fdeletereason | 删除原因 | varchar | 50 |  | √ | ' ' | 删除原因 |
| 22 | freceiverid | 接收人ID | int8 | 64 |  | √ | 0 | 接收人ID |
| 23 | freadstate | 阅读状态 | varchar | 30 |  | √ | ' ' | 阅读状态,枚举: read :已读 unread :未读 |
| 24 | fpopup | 是否弹出 | bpchar | 1 |  | √ | '0' | 是否弹出 |
| 25 | fcontent_summary | 正文摘要 | varchar | 255 |  | √ | ' ' | 正文摘要 |
| 26 | fdeletedate | 删除日期 | timestamp | 0 |  |  | null | 删除日期 |
| 27 | ftype | 消息类型 | int8 | 64 |  | √ | 0 | 消息类型 |
| 28 | fnestbillid | 内嵌业务单据ID | int8 | 64 |  | √ | 0 | 内嵌业务单据ID |
| 29 | fnestentitynumber | 内嵌业务编码 | varchar | 50 |  | √ | ' ' | 内嵌业务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_himsgreceiver_pkey |  | fid |
| 2 | idx_wf_himsgreceiver_deldate |  | fdeletedate |
| 3 | idx_wf_himsgreceiver_msg |  | fmessageid |

---

## 历史消息接受者-多语言表 t_wf_himsgreceiver_l

- **表名称：** 历史消息接受者-多语言表
- **表名：** t_wf_himsgreceiver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 4 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 5 | fcontent_summary | 正文摘要 | varchar | 255 |  | √ | ' ' | 正文摘要 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_himsgreceiver_l |  | fpkid |
| 2 | idx_wf_himsgreceiver_l |  | fid,flocaleid |
