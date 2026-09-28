# 销售报表查询任务-sm_reporttask

## 销售报表查询任务-主表 t_sm_reporttask

- **表名称：** 销售报表查询任务-主表
- **表名：** t_sm_reporttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskexp | 任务异常信息 | varchar | 512 |  |  | null | 任务异常信息 |
| 3 | ftaskexp_tag | 任务异常信息_详情 | text | 0 |  |  | null | 任务异常信息_详情 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fconditionjson_tag | 查询条件_详情 | text | 0 |  |  | null | 查询条件_详情 |
| 6 | fconditionjson | 查询条件 | varchar | 512 |  |  | null | 查询条件 |
| 7 | fconditiontext_tag | 查询条件文字_详情 | text | 0 |  |  | null | 查询条件文字_详情 |
| 8 | fprogress | 进度 | numeric | 23 | 10 | √ | 0 | 进度 |
| 9 | freportname | 报表页面名称 | varchar | 100 |  | √ | ' ' | 报表页面名称 |
| 10 | ftaskclass | 任务执行线程类 | varchar | 100 |  | √ | ' ' | 任务执行线程类 |
| 11 | fstarttime | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 12 | ftaskstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :待启动 B :执行中 C :已完成 D :异常终止 E :手工终止 |
| 13 | fendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 14 | freport | 报表页面编码 | varchar | 80 |  | √ | ' ' | 报表页面编码 |
| 15 | fbillno | 任务编号 | varchar | 80 |  | √ | ' ' | 任务编号 |
| 16 | fmiddlereport | 报表中间实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fconditiontext | 查询条件文字 | varchar | 512 |  |  | null | 查询条件文字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_rt_fbillno |  | fbillno |
| 2 | pk_t_sm_reporttask |  | fid |
