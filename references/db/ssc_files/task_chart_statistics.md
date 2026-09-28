# 任务进度图统计临时表-task_chart_statistics

## 任务进度图统计临时表-主表 t_tk_tkprochartstatistic

- **表名称：** 任务进度图统计临时表-主表
- **表名：** t_tk_tkprochartstatistic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdatetype | 日期类型 | int8 | 64 |  | √ | 0 | 日期类型 |
| 4 | fpooltype | 任务池类型 | int8 | 64 |  | √ | 0 | 任务池类型 |
| 5 | fstatdaterange | 统计时间范围 | int8 | 64 |  | √ | 0 | 统计时间范围 |
| 6 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 7 | fcount | 统计量 | int8 | 64 |  | √ | 0 | 统计量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_tkrostastic__daterange |  | fdatetype |
| 2 | idx_tk_tkrostastic__tasktype |  | ftasktypeid |
| 3 | idx_tk_tkrochstastic_ssc |  | fsscid |
| 4 | t_tk_tkprochartstatistic_pkey |  | fid |
