# 风险计算日志-tctrc_risk_run_log

## 风险计算日志-主表 t_tctrc_risk_run_log

- **表名称：** 风险计算日志-主表
- **表名：** t_tctrc_risk_run_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frunenddate | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 3 | frunresult | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果,枚举: 1 :成功 2 :执行中 3 :失败 |
| 4 | frunstartdate | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 5 | friskruntype | 风险操作类型 | varchar | 50 |  | √ | ' ' | 风险操作类型,枚举: 1 :自动运行 2 :手动运行 |
| 6 | fprocess | 执行进度 | varchar | 256 |  | √ | ' ' | 执行进度 |
| 7 | frunperson | 风险操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_risk_run_log |  | fid |
| 2 | index_bill_no |  | fbillno |
