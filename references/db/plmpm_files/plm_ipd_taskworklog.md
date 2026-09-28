# 任务工作日志-plm_ipd_taskworklog

## 任务工作日志-主表 t_plm_ipd_taskworklog

- **表名称：** 任务工作日志-主表
- **表名：** t_plm_ipd_taskworklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fremainhours | 预计剩余工时(h) | numeric | 23 | 1 | √ | 0 | 预计剩余工时(h) |
| 4 | fplanprogress | 计划进度（%） | numeric | 23 | 1 | √ | 0 | 计划进度（%） |
| 5 | factprogress | 实际进度（%） | numeric | 23 | 1 | √ | 0 | 实际进度（%） |
| 6 | fcreaterld | 填报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdeviation | 偏差（%） | numeric | 23 | 1 | √ | 0 | 偏差（%） |
| 8 | fworkdesc | 工作描述 | varchar | 255 |  | √ | ' ' | 工作描述 |
| 9 | freportdate | 填报日期 | timestamp | 0 |  |  | null | 填报日期 |
| 10 | ftaskid | 任务名称 | int8 | 64 |  | √ | 0 | 任务 plm_ipd_task |
| 11 | fdailyhours | 当日投入工时(h) | numeric | 23 | 1 | √ | 0 | 当日投入工时(h) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_taskworklog_m0 |  | freportdate |
| 2 | pk_plm_ipd_taskworklog |  | fid |
