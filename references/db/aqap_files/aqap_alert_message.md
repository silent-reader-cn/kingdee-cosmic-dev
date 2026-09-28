# 预警消息平台-aqap_alert_message

## 预警消息平台-主表 t_aqap_alert_message

- **表名称：** 预警消息平台-主表
- **表名：** t_aqap_alert_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmessage_time | 消息发送时间 | timestamp | 0 |  |  | null | 消息发送时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fmessage_source | 预警消息来源 | varchar | 50 |  | √ | ' ' | 预警消息来源,枚举: 1 :证书预警监控 2 :前置机连接监控 3 :回单下载连接监控 4 :回单缺失监控 5 :交易明细完整度监控 |
| 9 | falert_type | 预警方式 | varchar | 50 |  | √ | ' ' | 预警方式,枚举: 手机短信 :手机短信 邮箱 :邮箱 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmessage_content | 消息内容 | varchar | 500 |  | √ | ' ' | 消息内容 |
| 12 | fmessage_status | 消息发送状态 | varchar | 50 |  | √ | ' ' | 消息发送状态,枚举: true :成功 false :失败 |
| 13 | fmessage_obj | 预警对象 | varchar | 255 |  | √ | ' ' | 预警对象 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_alert_message_pkey |  | fid |
