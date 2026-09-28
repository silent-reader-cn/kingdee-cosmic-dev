# 任务日志-pa_tasklog

## 任务日志-主表 t_pa_tasklog

- **表名称：** 任务日志-主表
- **表名：** t_pa_tasklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finstance | 运行同步操作的实例ID | varchar | 50 |  | √ | ' ' | 运行同步操作的实例ID |
| 3 | fmsg_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |
| 4 | fsyncdataschemeid | 数据同步方案Id | int8 | 64 |  | √ | 0 | 数据同步方案Id |
| 5 | fcreatetime | 日志创建时间 | timestamp | 0 |  |  | null | 日志创建时间 |
| 6 | ftasktype | 任务类型 | bpchar | 2 |  | √ | ' ' | 任务类型,枚举: 11 :从实体同步数据任务 |
| 7 | fmsg | 日志信息 | varchar | 255 |  | √ | ' ' | 日志信息 |
| 8 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | [数据源 pa_datasourceconfig](../pa_files/pa_datasourceconfig.md) |
| 9 | ftaskoperatetoken | 任务操作所使用的Token | int8 | 64 |  | √ | 0 | 任务操作所使用的Token |
| 10 | fstatus | 同步状态： | bpchar | 1 |  | √ | ' ' | 同步状态：,枚举: 0 :未开始 1 :进行中 2 :成功完成 9 :失败 5 :手动终止 |
| 11 | fdatasynctaskid | 所属的同步任务ID | int8 | 64 |  | √ | 0 | 所属的同步任务ID |
| 12 | fanalysismodelid | 分析模型Id | int8 | 64 |  | √ | 0 | 分析模型Id |
| 13 | fupdatetime | 日志更新时间 | timestamp | 0 |  |  | null | 日志更新时间 |
| 14 | fsyncschemename | 取数方案名称 | varchar | 255 |  | √ | ' ' | 取数方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_task_log |  | fdatasynctaskid |
| 2 | pk_t_pa_tasklog |  | fid |
