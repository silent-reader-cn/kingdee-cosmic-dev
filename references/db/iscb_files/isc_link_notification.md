# 连接通知-isc_link_notification

## 连接通知-主表 t_isc_link_notification

- **表名称：** 连接通知-主表
- **表名：** t_isc_link_notification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperson | 消息接收人-苍穹用户 | varchar | 1000 |  | √ | ' ' | 消息接收人-苍穹用户 |
| 3 | fmethod | 通知方式 | varchar | 50 |  | √ | ' ' | 通知方式,枚举: system_message :系统消息 |
| 4 | foutsideperson | 非苍穹用户 | varchar | 1000 |  | √ | ' ' | 非苍穹用户 |
| 5 | fdblink | 连接配置 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmsg_title | 消息标题 | varchar | 50 |  | √ | ' ' | 消息标题 |
| 8 | fmsgcontent | 消息编辑 | varchar | 1000 |  | √ | ' ' | 消息编辑 |
| 9 | fstate | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftarget_system | 消息接收系统 | varchar | 50 |  | √ | ' ' | 消息接收系统,枚举: COSMIC :当前苍穹 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_link_notification |  | fid |
| 2 | idx_isc_log_form_fdblink |  | fdblink |
