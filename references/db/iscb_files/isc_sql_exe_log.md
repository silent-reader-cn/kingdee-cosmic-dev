# SQL&#x2f;脚本测试记录-isc_sql_exe_log

## SQL&#x2f;脚本测试记录-主表 t_isc_sql_exe_log

- **表名称：** SQL&#x2f;脚本测试记录-主表
- **表名：** t_isc_sql_exe_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fresources | 引用资源 | varchar | 2000 |  | √ | ' ' | 引用资源 |
| 4 | fcreatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fsql | SQL/脚本 | varchar | 2000 |  | √ | ' ' | SQL/脚本 |
| 6 | fdata_source | 数据源 | varchar | 100 |  | √ | ' ' | 数据源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_sql_exe_log_pkey |  | fid |
| 2 | idx_isc_sql_exe_log_1 |  | fcreator |
