# 巡检任务执行情况-xkcts_insp_jobresult

## 巡检任务执行情况-主表 t_xkinsp_exeresult

- **表名称：** 巡检任务执行情况-主表
- **表名：** t_xkinsp_exeresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschedresult | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果,枚举: 100 :成功 200 :部分成功 300 :失败 |
| 3 | fschedtype | 执行方式 | bpchar | 1 |  | √ | 'A' | 执行方式,枚举: A :自动执行 B :手工执行 |
| 4 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fschedstatus | 执行状态 | bpchar | 1 |  | √ | 'A' | 执行状态,枚举: A :未开始 B :执行中 C :已执行 D :已终止 |
| 6 | finspectjobid | 任务名称 | int8 | 64 |  | √ | 0 | [巡检任务 xkcts_inspectjob](../cts_files/xkcts_inspectjob.md) |
| 7 | finspitemtypeid | 巡检分类 | int8 | 64 |  | √ | 0 | [巡检业务分类 xkcts_inspectitemtype](../cts_files/xkcts_inspectitemtype.md) |
| 8 | fparamjson | 执行参数 | varchar | 255 |  | √ | ' ' | 执行参数 |
| 9 | fjobname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 10 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 11 | fschedid | 计划名称 | int8 | 64 |  | √ | 0 | [巡检计划 xkcts_inspect_schedule](../cts_files/xkcts_inspect_schedule.md) |
| 12 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fjobnumber | 任务编码 | varchar | 30 |  | √ | ' ' | 任务编码 |
| 14 | fschedendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 15 | fparamjson_tag | 执行参数_详情 | text | 0 |  |  | null | 执行参数_详情 |
| 16 | fusedtime | 执行耗时（秒） | numeric | 23 | 3 | √ | 0 | 执行耗时（秒） |
| 17 | fschedbegtime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_exeresult_schedule |  | fschedid |
| 2 | pk_xkinsp_exeresult |  | fid |
| 3 | idx_insp_exeresult_job |  | finspectjobid |
