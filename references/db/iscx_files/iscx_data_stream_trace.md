# 数据流成功日志-iscx_data_stream_trace

## 数据流成功日志-主表 t_iscx_data_stream_trace

- **表名称：** 数据流成功日志-主表
- **表名：** t_iscx_data_stream_trace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: Ready :就绪 Running :执行中 Blocked :阻塞 Waiting :等待 Failed :已失败 Terminated :已撤销 Success :完成 Stopped :忽略 |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BatchTask :批处理 FiberTask :数据线 StreamTask :数据查询 |
| 5 | fdata_stream | 数据流实例 | int8 | 64 |  | √ | 0 | [数据流实例 iscx_data_stream](../iscx_files/iscx_data_stream.md) |
| 6 | fdata_tag | 任务上下文_详情 | text | 0 |  |  | null | 任务上下文_详情 |
| 7 | fdata | 任务上下文 | varchar | 255 |  | √ | ' ' | 任务上下文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_data_stream_trace |  | fid |
| 2 | idx_t_iscx_data_stream_trace_i |  | fdata_stream |
