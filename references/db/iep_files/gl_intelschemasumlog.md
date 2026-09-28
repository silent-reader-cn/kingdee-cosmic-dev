# 智能方案日志-gl_intelschemasumlog

## 智能方案日志-主表 t_gl_intellschemasumlog

- **表名称：** 智能方案日志-主表
- **表名：** t_gl_intellschemasumlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecutedetails | 执行详情 | varchar | 200 |  | √ | ' ' | 执行详情 |
| 3 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 4 :已中止 |
| 4 | ftype | 执行类型 | bpchar | 1 |  | √ | ' ' | 执行类型,枚举: 0 :自动执行 1 :手动执行 |
| 5 | fintelschemaid | 执行方案 | int8 | 64 |  | √ | 0 | [智能执行方案 gl_intellexecschema](../iep_files/gl_intellexecschema.md) |
| 6 | fdate | 日期 | int8 | 64 |  | √ | 0 | 日期 |
| 7 | fexecstartdate | 方案开始时间 | timestamp | 0 |  |  | null | 方案开始时间 |
| 8 | fexecenddate | 方案结束时间 | timestamp | 0 |  |  | null | 方案结束时间 |
| 9 | ftaskid | 后台执行任务id | varchar | 50 |  | √ | ' ' | 后台执行任务id |
| 10 | fquantity | 单据数量 | int8 | 64 |  | √ | 0 | 单据数量 |
| 11 | ffailsumquantity | 方案累计错误数据 | int4 | 32 |  | √ | 0 | 方案累计错误数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_intellschemasumlog_pkey |  | fid |
| 2 | idx_gl_sumlog_fexecstartdate |  | fexecstartdate |
| 3 | idx_gl_sumlog_fid_fexecstatus |  | fintelschemaid,ftype |
