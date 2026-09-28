# 事件订阅-wf_eventsubscription

## 事件订阅-主表 t_wf_eventsubscr

- **表名称：** 事件订阅-主表
- **表名：** t_wf_eventsubscr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feventname | 事件名称 | varchar | 255 |  | √ | ' ' | 事件名称 |
| 3 | fconfiguration | 配置 | varchar | 255 |  | √ | ' ' | 配置 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbusinesskey | businesskey | varchar | 36 |  | √ | ' ' | businesskey |
| 7 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | factivityid | 活动实例ID | varchar | 255 |  | √ | ' ' | 活动实例ID |
| 10 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 11 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 12 | feventtype | 事件类型 | varchar | 30 |  | √ | ' ' | 事件类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_eventsubscr_procdefid |  | fprocdefid |
| 2 | t_wf_eventsubscr_pkey |  | fid |
| 3 | idx_wf_eventsubsc_proacttype |  | fprocinstid,factivityid,feventtype |
| 4 | idx_wf_eventsubscr_eventname |  | feventname |
| 5 | idx_wf_event_subscr_exec_id |  | fexecutionid |
