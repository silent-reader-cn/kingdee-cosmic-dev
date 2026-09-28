# 订阅日志-kem_log_bill

## 订阅日志-主表 t_kem_log

- **表名称：** 订阅日志-主表
- **表名：** t_kem_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdatasourcenumber | 数据源编码 | varchar | 60 |  | √ | ' ' | 数据源编码 |
| 2 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 3 | feventid | 事件 | int8 | 64 |  | √ | 0 | 事件 |
| 4 | feventsourcename | feventsourcename | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fsrcsubtype | 来源 | bpchar | 1 |  |  | '0' | 来源,枚举: 1 :开放事件 2 :组装流 0 :手工创建 |
| 7 | fopdesc | Tag | varchar | 200 |  | √ | ' ' | Tag |
| 8 | fsubnumber | 订阅编码 | varchar | 100 |  | √ | ' ' | 订阅编码 |
| 9 | fsubname | 订阅名称 | varchar | 40 |  | √ | ' ' | 订阅名称 |
| 10 | feventcode | 事件编码 | varchar | 100 |  | √ | ' ' | 事件编码 |
| 11 | factionname | 事件目标 | varchar | 200 |  | √ | ' ' | 事件目标 |
| 12 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | 数据源 |
| 13 | fsubid | 事件订阅ID | int8 | 64 |  | √ | 0 | 事件订阅ID |
| 14 | flogid | flogid | int8 | 64 |  | √ | 0 | id |
| 15 | fusername | 操作人 | varchar | 50 |  | √ | ' ' | 操作人 |
| 16 | fopname | fopname | varchar | 50 |  | √ | ' ' |  |
| 17 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :失败 1 :等待中 2 :成功 3 :部分成功 4 :忽略 |
| 18 | feventbusid | 事件通道 | int8 | 64 |  | √ | 0 | 事件通道 |
| 19 | feventname | 事件名称 | varchar | 40 |  | √ | ' ' | 事件名称 |
| 20 | fmsgid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 21 | fsubversion | 订阅版本号 | int4 | 32 |  | √ | 0 | 订阅版本号 |
| 22 | frequestid | 事件跟踪ID | varchar | 50 |  | √ | ' ' | 事件跟踪ID |
| 23 | feventsourceid | feventsourceid | int8 | 64 |  | √ | 0 |  |
| 24 | fcost | 执行耗时（ms） | int8 | 64 |  | √ | 0 | 执行耗时（ms） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | flogid | flogid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_log_frequestid_b |  | frequestid |
| 2 | idx_kem_log_frequestid |  | frequestid |
| 3 | idx_kem_log_subid_b |  | fsubid |
| 4 | idx_kem_log_evtid_b |  | feventid |
| 5 | idx_kem_log_subid |  | fsubid |
| 6 | pk_kem_log |  | flogid |
| 7 | idx_kem_log_evtid |  | feventid |
| 8 | idx_kem_log_ct |  | fcreatetime |
| 9 | idx_kem_log_ct_b |  | fcreatetime |
