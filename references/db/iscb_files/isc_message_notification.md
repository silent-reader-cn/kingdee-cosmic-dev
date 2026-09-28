# 数据集成通知-isc_message_notification

## 数据集成通知-主表 t_isc_msg_notification

- **表名称：** 数据集成通知-主表
- **表名：** t_isc_msg_notification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 消息推送名称 | varchar | 400 |  | √ | ' ' | 消息推送名称 |
| 3 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fperson | 苍穹用户 | varchar | 2000 |  | √ | ' ' | 苍穹用户 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | foutsideperson | 非苍穹用户 | varchar | 2000 |  | √ | ' ' | 非苍穹用户 |
| 8 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fnumber | 消息推送编码 | varchar | 400 |  | √ | ' ' | 消息推送编码 |
| 10 | fmsgcontent | 消息编辑 | text | 0 |  |  | ' ' | 消息编辑 |
| 11 | fchannel | 发送渠道 | varchar | 30 |  | √ | ' ' | 发送渠道,枚举: 1 :系统消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_msg_notification_pkey |  | fid |
| 2 | idx_isc_msg_num |  | fnumber |

---

## 单据体-子表 t_isc_msg_object

- **表名称：** 单据体-子表
- **表名：** t_isc_msg_object

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcute | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: S :完成 F :失败 P :部分成功 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftrigger | 启动方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_msg_object_pkey |  | fentryid |
| 2 | idx_isc_msg_object_trigger |  | ftrigger |
| 3 | idx_isc_msg_object_fk |  | fid |
