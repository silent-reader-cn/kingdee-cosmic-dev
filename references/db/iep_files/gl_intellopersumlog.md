# 智能核算操作汇总日志-gl_intellopersumlog

## 智能核算操作汇总日志-主表 t_gl_intellopersumlog

- **表名称：** 智能核算操作汇总日志-主表
- **表名：** t_gl_intellopersumlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbussiness | 业务单据 | varchar | 36 |  | √ | ' ' | 业务单据 |
| 3 | fschemasumlogid | 执行方案日志 | int8 | 64 |  | √ | 0 | 执行方案日志 |
| 4 | foper | 操作 | varchar | 100 |  |  | ' ' | 操作 |
| 5 | fbillqty | 单据数量 | int8 | 64 |  | √ | 0 | 单据数量 |
| 6 | fexecstartdate | 操作开始时间 | timestamp | 0 |  |  | null | 操作开始时间 |
| 7 | fexecenddate | 操作结束时间 | timestamp | 0 |  |  | null | 操作结束时间 |
| 8 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 |
| 10 | fsuccessbillqty | 成功数量 | int4 | 32 |  | √ | 0 | 成功数量 |
| 11 | ffailbillqty | 失败数量 | int4 | 32 |  | √ | 0 | 失败数量 |
| 12 | fintelschemaid | 执行方案 | int8 | 64 |  | √ | 0 | [智能执行方案 gl_intellexecschema](../iep_files/gl_intellexecschema.md) |
| 13 | fdate | fdate | int8 | 64 |  | √ | 0 |  |
| 14 | fexecdetail | 执行描述 | text | 0 |  |  | null | 执行描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_opersumlog |  | fintelschemaid,fexecstatus |
| 2 | idx_gl_opersumlog_date |  | fdate |
| 3 | t_gl_intellopersumlog_pkey |  | fid |
