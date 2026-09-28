# 历史修复任务-wf_repairtask

## 历史修复任务-主表 t_wf_repairtask

- **表名称：** 历史修复任务-主表
- **表名：** t_wf_repairtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 3 | ftimes | 轮次 | int4 | 32 |  | √ | 0 | 轮次 |
| 4 | fretry | 连续失败次数 | int4 | 32 |  | √ | 0 | 连续失败次数 |
| 5 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: 3 :高 2 :中 1 :低 |
| 6 | fparams | 自定义参数集 | varchar | 2000 |  | √ | ' ' | 自定义参数集 |
| 7 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: TOHANDLE :未开始 RUNNING :进行中 FINISHED :已完成 ERRORED :失败 |
| 9 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 10 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 11 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 12 | fbusinessobj | 业务执行类 | varchar | 200 |  | √ | ' ' | 业务执行类 |
| 13 | flimitsize | 步长 | int4 | 32 |  | √ | 0 | 步长 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_repairtask |  | fid |
| 2 | idx_wf_repairtask_state |  | fstate |
