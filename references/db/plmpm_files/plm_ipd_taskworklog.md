# 任务工时-plm_ipd_taskworklog

## 任务工时-主表 t_plm_ipd_taskworklog

- **表名称：** 任务工时-主表
- **表名：** t_plm_ipd_taskworklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremainhours | 预计剩余工时(h) | numeric | 23 | 1 | √ | 0 | 预计剩余工时(h) |
| 3 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 4 | fplanprogress | 计划进度（%） | numeric | 23 | 1 | √ | 0 | 计划进度（%） |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :审核中 C :已审核 D :重新审核 |
| 6 | fcreaterld | 填报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | freportdate | 填报日期 | timestamp | 0 |  |  | null | 填报日期 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | factprogress | 实际进度（%） | numeric | 23 | 1 | √ | 0 | 实际进度（%） |
| 10 | fdeviation | 偏差（%） | numeric | 23 | 1 | √ | 0 | 偏差（%） |
| 11 | fworkdesc | 工作描述 | varchar | 255 |  | √ | ' ' | 工作描述 |
| 12 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 13 | fdailyhours | 当日投入工时(h) | numeric | 23 | 1 | √ | 0 | 当日投入工时(h) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipd_taskworklog_m0 |  | freportdate |
| 2 | pk_plm_ipd_taskworklog |  | fid |
