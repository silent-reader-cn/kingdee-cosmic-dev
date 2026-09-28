# 报表查询日志-scmc_rpt_query_log

## 报表查询日志-主表 t_scmc_rpt_query_log

- **表名称：** 报表查询日志-主表
- **表名：** t_scmc_rpt_query_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frpt | 报表实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | ftraceid | TraceId | varchar | 30 |  | √ | ' ' | TraceId |
| 4 | fstart | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fcreater | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fresult | 服务执行结果 | bpchar | 1 |  | √ | ' ' | 服务执行结果,枚举: 1 :成功 0 :失败 |
| 7 | frptconf | 查询配置 | int8 | 64 |  | √ | 0 | [报表数据源配置 scmc_report_conf](../mscommon_files/scmc_report_conf.md) |
| 8 | fusetime | 服务耗时/ms | int4 | 32 |  | √ | 0 | 服务耗时/ms |
| 9 | frowcount | AlgoX数据行 | int4 | 32 |  | √ | 0 | AlgoX数据行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_scmc_rpt_qlog_tc |  | ftraceid |
| 2 | idx_t_scmc_rpt_qlog_rpt |  | frpt |
| 3 | pk_t_scmc_rpt_query_log |  | fid |
| 4 | idx_t_scmc_rpt_qlog_st |  | fstart |
