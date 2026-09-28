# 服务流程日志-isc_sf_proc_log

## 服务流程日志-主表 t_isc_sf_proc_log

- **表名称：** 服务流程日志-主表
- **表名：** t_isc_sf_proc_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproc_inst | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 3 | fcreated_time | 日志时间 | timestamp | 0 |  |  | null | 日志时间 |
| 4 | ftype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: ERROR :错误 CONTROL :控制 WARN :警告 INFO :信息 |
| 5 | fcontent_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |
| 6 | fhost_id | 服务器ID | varchar | 50 |  | √ | ' ' | 服务器ID |
| 7 | fcontent | 日志内容 | varchar | 255 |  | √ | ' ' | 日志内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_sf_proc_log_c |  | fcreated_time |
| 2 | idx_t_isc_sf_proc_log_t |  | ftype |
| 3 | t_isc_sf_proc_log_pkey |  | fid |
| 4 | idx_t_isc_sf_proc_log_p |  | fproc_inst |
