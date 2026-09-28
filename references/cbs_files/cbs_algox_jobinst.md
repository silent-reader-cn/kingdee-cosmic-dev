# 计算任务监控-cbs_algox_jobinst

## 计算任务监控-主表 t_cbs_algox_jobinst

- **表名称：** 计算任务监控-主表
- **表名：** t_cbs_algox_jobinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtype | 任务类型 | varchar | 40 |  | √ | ' ' | 任务类型 |
| 3 | fbillstatus | 单据状态 | varchar | 40 |  |  | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | foperator | 操作人 | varchar | 40 |  | √ | ' ' | 操作人 |
| 5 | fjobid | 计算任务ID | varchar | 40 |  | √ | ' ' | 计算任务ID |
| 6 | fmasterweburl | fmasterweburl | varchar | 50 |  | √ | ' ' |  |
| 7 | fjobdetails | 任务详情 | text | 0 |  |  | ' ' | 任务详情 |
| 8 | fjobname | 任务名称 | varchar | 40 |  | √ | ' ' | 任务名称 |
| 9 | fstarttime | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 10 | fstatus | 任务运行状态 | int8 | 64 |  | √ | 0 | 任务运行状态,枚举: 0 :成功 1 :失败 2 :运行中 |
| 11 | fduration | 执行时间 | int8 | 64 |  | √ | 0 | 执行时间 |
| 12 | fstatisticalanalyze | 统计分析 | varchar | 256 |  |  | ' ' | 统计分析 |
| 13 | fendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 14 | fbillno | 单据编号 | varchar | 40 |  |  | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_algox_jobinst |  | fjobid |
| 2 | t_cbs_algox_jobinst_pkey |  | fid |
| 3 | idx_cbs_algox_starttime |  | fstarttime |
