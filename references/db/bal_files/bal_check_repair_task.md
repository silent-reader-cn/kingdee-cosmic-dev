# 余额巡检重算任务-bal_check_repair_task

## 余额巡检重算任务-主表 t_bal_check_repair_task

- **表名称：** 余额巡检重算任务-主表
- **表名：** t_bal_check_repair_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fparam | 任务参数 | varchar | 100 |  | √ | ' ' | 任务参数 |
| 3 | ferrormsg | 错误信息 | varchar | 100 |  | √ | ' ' | 错误信息 |
| 4 | fponitkey | 增量标识 | varchar | 80 |  | √ | ' ' | 增量标识 |
| 5 | fbill | 单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fmanagertraceid | 调度Traceid | varchar | 30 |  | √ | ' ' | 调度Traceid |
| 7 | fparenttaskid | 父任务 | int8 | 64 |  | √ | '0' | 余额巡检重算 bal_check_repair |
| 8 | ftasktraceid | 执行Traceid | varchar | 30 |  | √ | ' ' | 执行Traceid |
| 9 | ffromid | 起始ID | int8 | 64 |  | √ | '0' | 起始ID |
| 10 | ftoid | 结束ID | int8 | 64 |  | √ | '0' | 结束ID |
| 11 | frule | 余额更新规则 | varchar | 36 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 12 | fstatus | 执行结果 | bpchar | 1 |  | √ | ' ' | 执行结果,枚举: A :已创建 B :已通知 C :有差异 D :无差异 E :异常失败 F :成功 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fresultdata_tag | 异常数据_详情 | text | 0 |  |  | null | 异常数据_详情 |
| 15 | fsparseseq | 稀疏序列 | int8 | 64 |  | √ | '0' | 稀疏序列 bal_sparse_seq |
| 16 | ftaskno | 任务编号 | varchar | 50 |  | √ | ' ' | 任务编号 |
| 17 | fcreater | 创建人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 18 | frunstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :已结束 3 :系统繁忙 |
| 19 | fparam_tag | 任务参数_详情 | text | 0 |  |  | null | 任务参数_详情 |
| 20 | fresultdata | 异常数据 | varchar | 100 |  | √ | ' ' | 异常数据 |
| 21 | fmsgappid | 消息路由标识 | varchar | 20 |  | √ | ' ' | 消息路由标识 |
| 22 | flastsuccessid | 最后一个执行成功的ID | int8 | 64 |  | √ | '0' | 最后一个执行成功的ID |
| 23 | ferrormsg_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_check_repair_task |  | fid |
| 2 | idx_bal_crt_ptid |  | fparenttaskid |
| 3 | idx_bal_crt_ct |  | fcreatedate |
| 4 | idx_bal_crt_no |  | ftaskno |
