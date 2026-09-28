# 智能合并任务信息-xkcr_smart_merge_task

## 智能合并任务信息-主表 t_xkcr_sm_task

- **表名称：** 智能合并任务信息-主表
- **表名：** t_xkcr_sm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 错误消息 | varchar | 500 |  | √ | ' ' | 错误消息 |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | ftaskname | ftaskname | varchar | 100 |  | √ | ' ' |  |
| 5 | fbosorg | fbosorg | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 7 | ftaskclass | ftaskclass | varchar | 200 |  | √ | ' ' |  |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | ferrordetail | 错误详情 | varchar | 2000 |  | √ | ' ' | 错误详情 |
| 10 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 11 | fdependencies | fdependencies | text | 0 |  |  | null |  |
| 12 | fpara | fpara | varchar | 2000 |  | √ | ' ' |  |
| 13 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | 'UNDO' | 任务状态,枚举: |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fscope | fscope | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_sm_task |  | fentryid |
| 2 | idx_xkcr_sm_task_fid |  | fid |
| 3 | idx_xkcr_sm_task_taskid |  | ftaskid |
