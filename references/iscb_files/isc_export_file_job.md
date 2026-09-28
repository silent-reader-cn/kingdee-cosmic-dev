# 数据导出执行结果-isc_export_file_job

## 数据导出执行结果-主表 t_iscb_export_file_job

- **表名称：** 数据导出执行结果-主表
- **表名：** t_iscb_export_file_job

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexport_trigger | 数据导出任务 | int8 | 64 |  | √ | 0 | 数据导出任务 isc_export_file_trigger |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fdeal_bytes | 导出数据量（字节） | int8 | 64 |  | √ | 0 | 导出数据量（字节） |
| 6 | fmessage | 日志信息 | varchar | 255 |  | √ | ' ' | 日志信息 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式(*.json) xlsx :Excel 工作簿(*.xlsx) xls :Excel 97-2003 工作簿(*.xls) csv :CSV文件(*.csv) |
| 9 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fignored_count | 忽略行数 | int4 | 32 |  | √ | 0 | 忽略行数 |
| 11 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | ffileschema | 数据导出方案 | int8 | 64 |  | √ | 0 | 数据导出方案 isc_export_file |
| 13 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 14 | fstate | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: C :创建 R :执行中 S :完成 F :失败 X :已撤销 W :等待中 P :部分成功 B :分批中 |
| 15 | fsuccess_count | 成功行数 | int4 | 32 |  | √ | 0 | 成功行数 |
| 16 | ftotal_count | 总行数 | int4 | 32 |  | √ | 0 | 总行数 |
| 17 | ffailed_count | 失败行数 | int4 | 32 |  | √ | 0 | 失败行数 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fmessage_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_export_file_job |  | fid |
| 2 | idx_iscb_export_file_job |  | fexport_trigger |

---

## 执行参数-子表 t_iscb_export_job_params

- **表名称：** 执行参数-子表
- **表名：** t_iscb_export_job_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparams_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 3 | fparams_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fparams_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparams_label | 标题 | varchar | 50 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_export_job_params_fk |  | fid |
| 2 | pk_t_iscb_export_job_params |  | fentryid |
