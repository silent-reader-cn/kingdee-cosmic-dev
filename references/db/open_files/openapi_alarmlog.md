# 预警日志-openapi_alarmlog

## 预警日志-主表 t_openapi_alarmlog

- **表名称：** 预警日志-主表
- **表名：** t_openapi_alarmlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 消息推送失败原因 | varchar | 500 |  | √ | ' ' | 消息推送失败原因 |
| 3 | fstatus | 消息推送状态 | bpchar | 1 |  | √ | '1' | 消息推送状态,枚举: 0 :推送失败 1 :推送成功 |
| 4 | fmsgtitle | 消息标题 | varchar | 50 |  | √ | ' ' | 消息标题 |
| 5 | fcreatetime | 消息发送日期 | timestamp | 0 |  |  | null | 消息发送日期 |
| 6 | fmsg | 消息内容 | varchar | 1000 |  | √ | ' ' | 消息内容 |
| 7 | falarmconfig | 预警规则模板 | int8 | 64 |  | √ | 0 | 预警规则模板 |
| 8 | fmsgtype | 消息渠道 | int8 | 64 |  | √ | 0 | [消息渠道 msg_channel](../wftask_files/msg_channel.md) |
| 9 | fchannelmsgid | 渠道消息日志关联ID | int8 | 64 |  | √ | 0 | 渠道消息日志关联ID |
| 10 | falarmtype | 预警类型 | bpchar | 1 |  | √ | '0' | 预警类型,枚举: 0 :慢接口 1 :API配额 2 :API熔断 3 :API安全 |
| 11 | frecevers | 接收人 | varchar | 100 |  | √ | ' ' | 接收人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_alarmlog_createtime |  | fcreatetime |
| 2 | pk_t_openapi_alarmlog |  | fid |
