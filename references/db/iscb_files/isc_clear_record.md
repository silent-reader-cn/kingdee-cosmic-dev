# 日志清理记录-isc_clear_record

## 日志清理记录-主表 t_iscb_log_cleanup_log

- **表名称：** 日志清理记录-主表
- **表名：** t_iscb_log_cleanup_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fstate | 状态 | varchar | 20 |  | √ | ' ' | 状态,枚举: running :正在运行 failed :失败 complete :完成 aborted :中断 cancelled :撤销 |
| 4 | ftotal_count | 总条数 | int8 | 64 |  | √ | 0 | 总条数 |
| 5 | foperator_id | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 7 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fstart_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fserver_id | IP地址 | varchar | 150 |  | √ | ' ' | IP地址 |
| 10 | flog_time_range | 时间范围（服务器时间） | varchar | 50 |  | √ | ' ' | 时间范围（服务器时间） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_log_cleanup_log_pkey |  | fid |
| 2 | idx_iscb_log_cleanup_log |  | fstart_time |
