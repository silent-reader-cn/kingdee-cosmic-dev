# 集成云异常日志-isc_sys_ex_log

## 集成云异常日志-主表 t_isc_sys_ex_log

- **表名称：** 集成云异常日志-主表
- **表名：** t_isc_sys_ex_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 日志类型 | varchar | 50 |  | √ | ' ' | 日志类型,枚举: CLEAR_LOG_EX :清理日志异常 |
| 3 | fmessage | 日志信息 | varchar | 255 |  | √ | ' ' | 日志信息 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fmessage_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |
| 7 | ferror_count | 失败次数 | int8 | 64 |  | √ | 0 | 失败次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_sys_ex_log |  | fid |
| 2 | idx_isc_ex_log_t |  | ftype |
