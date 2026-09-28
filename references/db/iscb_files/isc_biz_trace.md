# 集成云业务调用追溯-isc_biz_trace

## 集成云业务调用追溯-主表 t_iscb_biz_trace_tree

- **表名称：** 集成云业务调用追溯-主表
- **表名：** t_iscb_biz_trace_tree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 2 | ftrace_id | 追溯号 | int8 | 64 |  | √ | 0 | 追溯号 |
| 3 | fstate | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: S :成功 Q :撤销 F :失败 |
| 4 | ftask_type | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型 |
| 5 | ftask_def_id | 任务定义ID | int8 | 64 |  | √ | 0 | 任务定义ID |
| 6 | fprior_id | 上游任务ID | int8 | 64 |  | √ | 0 | 上游任务ID |
| 7 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fprior_tag | 上游任务标签 | varchar | 100 |  | √ | ' ' | 上游任务标签 |
| 9 | felapsed_time | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 10 | ftask_number | 任务编码 | varchar | 150 |  | √ | ' ' | 任务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_trace_def_id |  | ftask_def_id |
| 2 | pk_t_iscb_biz_trace_tree |  | fid |
| 3 | idx_isc_trace_id |  | ftrace_id |
| 4 | idx_isc_trace_pri_id |  | fprior_id |
