# 返利任务-msrcs_task

## 返利任务-主表 t_msrcs_task

- **表名称：** 返利任务-主表
- **表名：** t_msrcs_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :准备 B :运行中 C :出错 Z :完成 |
| 3 | ffailcount | 失败任务数 | int4 | 32 |  | √ | 0 | 失败任务数 |
| 4 | fdetail | 日志详情 | varchar | 2000 |  | √ | ' ' | 日志详情 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | ftaskcount | 总计算任务数 | int4 | 32 |  | √ | 0 | 总计算任务数 |
| 7 | ftaskno | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |
| 8 | foptype | 发起类型 | bpchar | 1 |  | √ | 'A' | 发起类型,枚举: A :自动 B :手动 |
| 9 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_task |  | fid |
| 2 | idx_msrcs_task_time |  | fstarttime |
| 3 | idx_msrcs_task_status |  | fstatus |
