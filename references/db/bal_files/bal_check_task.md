# 余额检查任务-bal_check_task

## 余额检查任务-主表 t_bal_check_task

- **表名称：** 余额检查任务-主表
- **表名：** t_bal_check_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fentity | 实体对象 | varchar | 36 |  | √ | ' ' | 实体对象 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :已创建 B :已通知 C :有差异 D :无差异 E :异常 |
| 4 | ftb | 物理表 | varchar | 36 |  | √ | ' ' | 物理表 |
| 5 | fmanagertraceid | 调度TraceID | varchar | 30 |  | √ | ' ' | 调度TraceID |
| 6 | ftasktraceid | 任务TraceId | varchar | 30 |  | √ | ' ' | 任务TraceId |
| 7 | ffromid | 起始ID | int8 | 64 |  | √ | '0' | 起始ID |
| 8 | fappid | 应用标识 | varchar | 10 |  | √ | ' ' | 应用标识 |
| 9 | ftoid | 结束ID | int8 | 64 |  | √ | '0' | 结束ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_check_task |  | fid |
