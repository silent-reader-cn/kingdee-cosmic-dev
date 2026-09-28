# 执行计划日志详情-mbase_msgtasklogdetail

## 执行计划日志详情-主表 t_mbase_msgtasklogdetail

- **表名称：** 执行计划日志详情-主表
- **表名：** t_mbase_msgtasklogdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flogmsg | 日志信息 | varchar | 1000 |  | √ | ' ' | 日志信息 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 1 :失败 0 :成功 |
| 4 | fexecnumber | 执行编号 | varchar | 50 |  | √ | ' ' | 执行编号 |
| 5 | ftasknumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 6 | fendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 7 | fruntime | 耗时(s) | varchar | 50 |  | √ | ' ' | 耗时(s) |
| 8 | ftarget | 发送目标 | bpchar | 1 |  | √ | '0' | 发送目标,枚举: 0 :群组 1 :个人 |
| 9 | fstarttime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_msgtasklogdetail_fen |  | fexecnumber |
| 2 | pk_mbase_msgtasklogdetail |  | fid |
