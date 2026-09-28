# 返利子任务详情-msrcs_subtask

## 返利子任务详情-主表 t_msrcs_subtask

- **表名称：** 返利子任务详情-主表
- **表名：** t_msrcs_subtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsuccess | 满足阶梯条件记录数 | int8 | 64 |  | √ | 0 | 满足阶梯条件记录数 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :准备 B :运行中 C :出错 D :终止 Z :完成 |
| 4 | fdetail | 日志详情 | varchar | 2000 |  | √ | ' ' | 日志详情 |
| 5 | frecords | 满足政策条件记录数 | int8 | 64 |  | √ | 0 | 满足政策条件记录数 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | ftaskno | 子任务号 | varchar | 50 |  | √ | ' ' | 子任务号 |
| 8 | fsourceid | 来源数据ID | int8 | 64 |  | √ | 0 | 来源数据ID |
| 9 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fsourcebillno | 来源数据编码 | varchar | 100 |  | √ | ' ' | 来源数据编码 |
| 11 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fmaintaskno | 主任务号 | varchar | 50 |  | √ | ' ' | 主任务号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_subtask |  | fid |
| 2 | idx_msrcs_subtask_taskid |  | fmaintaskno |
| 3 | idx_msrcs_subtask_taskno |  | ftaskno |
| 4 | idx_msrcs_subtask_sid |  | fsourceid |
