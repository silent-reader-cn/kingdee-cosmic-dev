# 数据导入日志-isc_import_file_data_log

## 数据导入日志-主表 t_iscb_import_file_log

- **表名称：** 数据导入日志-主表
- **表名：** t_iscb_import_file_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 日志内容 | varchar | 1000 |  | √ | ' ' | 日志内容 |
| 3 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 4 | fimport_trigger | 数据导入任务 | int8 | 64 |  | √ | 0 | 数据导入任务 isc_import_file_trigger |
| 5 | fimport_schema | 数据导入方案 | int8 | 64 |  | √ | 0 | 数据导入方案 isc_import_file |
| 6 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fstate | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: S :成功 F :失败 G :失效 N :忽略 |
| 8 | fmodified_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fjudgefields | 候选键值 | varchar | 100 |  | √ | ' ' | 候选键值 |
| 10 | fserver | 执行服务器 | varchar | 50 |  | √ | ' ' | 执行服务器 |
| 11 | fimport_file_job | 数据导入执行结果 | int8 | 64 |  | √ | 0 | 数据导入执行结果 isc_import_file_job |
| 12 | fdata | 数据 | varchar | 255 |  | √ | ' ' | 数据 |
| 13 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_import_file_log |  | fimport_file_job |
| 2 | pk_t_iscb_import_file_log |  | fid |
