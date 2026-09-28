# 数据导入执行结果-isc_import_file_job

## 数据导入执行结果-主表 t_iscb_import_file_job

- **表名称：** 数据导入执行结果-主表
- **表名：** t_iscb_import_file_job

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexport_trigger | 数据导入任务 | int8 | 64 |  | √ | 0 | [数据导入任务 isc_import_file_trigger](../iscb_files/isc_import_file_trigger.md) |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fdeal_bytes | 导入数据量（字节） | int8 | 64 |  | √ | 0 | 导入数据量（字节） |
| 6 | fmessage | 日志信息 | varchar | 255 |  | √ | ' ' | 日志信息 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式(*.json) xlsx :Excel 工作簿(*.xlsx) xls :Excel 97-2003 工作簿(*.xls) csv :CSV 逗号分隔值(*.csv) |
| 9 | fbatch_size | 目标单批量大小 | int4 | 32 |  | √ | 0 | 目标单批量大小 |
| 10 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 11 | fignored_count | 忽略行数 | int4 | 32 |  | √ | 0 | 忽略行数 |
| 12 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 13 | ffileschema | 数据导入方案 | int8 | 64 |  | √ | 0 | [数据导入方案 isc_import_file](../iscb_files/isc_import_file.md) |
| 14 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 15 | fstate | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: C :创建 R :执行中 S :完成 F :失败 X :已撤销 W :等待中 P :部分成功 B :分批中 |
| 16 | fsuccess_count | 成功行数 | int4 | 32 |  | √ | 0 | 成功行数 |
| 17 | ftotal_count | 总行数 | int4 | 32 |  | √ | 0 | 总行数 |
| 18 | ffailed_count | 失败行数 | int4 | 32 |  | √ | 0 | 失败行数 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fmessage_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_import_file_job |  | fexport_trigger |
| 2 | pk_t_iscb_import_file_job |  | fid |
