# 日志详情-kem_nodelog_bill

## 日志详情-主表 t_kem_nodelog

- **表名称：** 日志详情-主表
- **表名：** t_kem_nodelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnodetype | 日志类型 | bpchar | 1 |  | √ | ' ' | 日志类型,枚举: 1 :触发事件 2 :订阅规则 4 :事件目标 |
| 2 | ferrorcode | 错误码 | varchar | 40 |  | √ | ' ' | 错误码 |
| 3 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 4 | fmessage | 失败消息 | varchar | 255 |  | √ | ' ' | 失败消息 |
| 5 | fcreatorname | 操作人 | varchar | 50 |  | √ | ' ' | 操作人 |
| 6 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fopdesc | 事件目标 | varchar | 200 |  | √ | ' ' | 事件目标 |
| 8 | foutput | 出参 | varchar | 255 |  | √ | ' ' | 出参 |
| 9 | fnodelogid | fnodelogid | int8 | 64 |  | √ | 0 | id |
| 10 | flogid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 11 | fretryseq | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 12 | finput | 入参 | varchar | 255 |  | √ | ' ' | 入参 |
| 13 | fhostip | IP | varchar | 40 |  | √ | ' ' | IP |
| 14 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 15 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :成功 0 :失败 |
| 16 | fretrytype | 执行方式 | bpchar | 1 |  | √ | ' ' | 执行方式,枚举: 1 :手动 0 :自动 |
| 17 | foutput_tag | 出参_详情 | text | 0 |  |  | null | 出参_详情 |
| 18 | fnodeid | 节点ID | int8 | 64 |  | √ | 0 | 节点ID |
| 19 | finput_tag | 入参_详情 | text | 0 |  |  | null | 入参_详情 |
| 20 | frequestid | 事件跟踪ID | varchar | 50 |  | √ | ' ' | 事件跟踪ID |
| 21 | factiontypeid | 事件目标服务类型 | int8 | 64 |  | √ | 0 | 事件目标服务类型 |
| 22 | fmessage_tag | 失败消息_详情 | text | 0 |  |  | null | 失败消息_详情 |
| 23 | fcost | 执行耗时(ms) | int8 | 64 |  | √ | 0 | 执行耗时(ms) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fnodelogid | fnodelogid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kem_nodelog |  | fnodelogid |
| 2 | idx_kem_nodelog_frequestid |  | frequestid |
| 3 | idx_kem_nodelog_logid |  | flogid |
| 4 | idx_kem_nodelog_createtime_b |  | fcreatetime |
| 5 | idx_kem_nodelog_frequestid_b |  | frequestid |
| 6 | idx_kem_nodelog_logid_b |  | flogid |
| 7 | idx_kem_nodelog_createtime |  | fcreatetime |
