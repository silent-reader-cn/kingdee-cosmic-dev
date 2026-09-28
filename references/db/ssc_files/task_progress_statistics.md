# 任务进度统计临时表-task_progress_statistics

## 任务进度统计临时表-主表 t_tk_tkprostatistic

- **表名称：** 任务进度统计临时表-主表
- **表名：** t_tk_tkprostatistic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdatetype | 日期类型 | int8 | 64 |  | √ | 0 | 日期类型 |
| 4 | fpooltype | 任务池类型 | int8 | 64 |  | √ | 0 | 任务池类型 |
| 5 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpersonid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcount | 统计数 | int8 | 64 |  | √ | 0 | 统计数 |
| 9 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_tkprstac_daterange |  | fdatetype |
| 2 | idx_tk_tkprstac_ssc |  | fsscid |
| 3 | t_tk_tkprostatistic_pkey |  | fid |
| 4 | idx_tk_tkprstac_tasktype |  | ftasktypeid |
