# 调度失败重试记录表-sch_retryjob

## 调度失败重试记录表-主表 t_sch_retryjob

- **表名称：** 调度失败重试记录表-主表
- **表名：** t_sch_retryjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstatus | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :运行中 1 :失败 2 :成功 |
| 2 | fgroupid | 分组id | int8 | 64 |  | √ | 0 | 分组id |
| 3 | fretrytime | 剩余重试次数 | int4 | 32 |  | √ | 0 | 剩余重试次数 |
| 4 | ftaskinfo | ftaskinfo | text | 0 |  |  | null |  |
| 5 | fscheduleid | 计划id | varchar | 36 |  | √ | ' ' | 计划id |
| 6 | flatestexecutiontime | 最近执行时间 | timestamp | 0 |  |  | null | 最近执行时间 |
| 7 | fjobid | 作业id | varchar | 36 |  | √ | ' ' | 作业id |
| 8 | ffirstfailuretime | ffirstfailuretime | timestamp | 0 |  |  | null |  |
| 9 | fbatchtime | fbatchtime | int4 | 32 |  | √ | 0 |  |
| 10 | frunmode | frunmode | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fgroupid | fgroupid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sch_retryjob |  | fgroupid |
| 2 | idx_sch_retryjob_fjobid |  | fjobid |
| 3 | idx_sch_retryjob_fscheduleid |  | fscheduleid |
