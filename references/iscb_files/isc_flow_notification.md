# 服务流程通知-isc_flow_notification

## 服务流程通知-主表 t_iscb_flow_notification

- **表名称：** 服务流程通知-主表
- **表名：** t_iscb_flow_notification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecipientvar_erp | 苍穹用户（变量） | varchar | 500 |  | √ | ' ' | 苍穹用户（变量） |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frecipientvar_not_erp | 非苍穹用户（变量） | varchar | 500 |  | √ | ' ' | 非苍穹用户（变量） |
| 5 | ftitle | 消息标题 | varchar | 1000 |  | √ | ' ' | 消息标题 |
| 6 | fstatus | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | ftarget_system | 消息接收系统 | varchar | 30 |  | √ | ' ' | 消息接收系统,枚举: |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fnotice_method | 发送渠道 | varchar | 30 |  | √ | ' ' | 发送渠道,枚举: |
| 12 | frecipient | 苍穹用户 | varchar | 500 |  | √ | ' ' | 苍穹用户 |
| 13 | fflow | 服务流程 | int8 | 64 |  | √ | 0 | 服务流程 isc_service_flow |
| 14 | fcontent | 消息内容 | varchar | 1000 |  | √ | ' ' | 消息内容 |
| 15 | frecipient_not_erp | 非苍穹用户 | varchar | 500 |  | √ | ' ' | 非苍穹用户 |
| 16 | fexecute | 实例状态 | varchar | 50 |  | √ | ' ' | 实例状态,枚举: Complete :已结束 Failed :已失败 Terminated :已撤销 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_flow_notice |  | fflow |
| 2 | pk_t_iscb_flow_notification |  | fid |
