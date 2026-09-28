# 历史价格计算任务跟进表-aiqa_his_price_task_log

## 历史价格计算任务跟进表-主表 t_aiqa_his_price_task_log

- **表名称：** 历史价格计算任务跟进表-主表
- **表名：** t_aiqa_his_price_task_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fexecution_status | 任务执行状态 | varchar | 50 |  | √ | ' ' | 任务执行状态 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ferror_message | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 6 | fretry_count | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fis_history_data | 是否历史数据 | varchar | 50 |  | √ | ' ' | 是否历史数据 |
| 9 | fend_time | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 10 | fstart_time | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbizdate | 业务发生日期 | timestamp | 0 |  |  | null | 业务发生日期 |
| 16 | fexecution_date | 任务执行日期 | timestamp | 0 |  |  | null | 任务执行日期 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aiqa_his_price_task_log |  | fid |
| 2 | idx_aiqa_his_price_task_log_m0 |  | fid |
