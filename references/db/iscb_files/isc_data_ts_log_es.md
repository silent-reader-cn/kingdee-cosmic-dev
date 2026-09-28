# 单据时间戳日志（历史）-isc_data_ts_log_es

## 单据时间戳日志（历史）-主表 t_iscb_es_bak

- **表名称：** 单据时间戳日志（历史）-主表
- **表名：** t_iscb_es_bak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcolumn3 | fcolumn3 | varchar | 30 |  | √ | ' ' |  |
| 3 | fcolumn2 | 集成时间 | varchar | 30 |  | √ | ' ' | 集成时间 |
| 4 | fcolumn1 | 单据ID | varchar | 30 |  | √ | ' ' | 单据ID |
| 5 | fcolumn5 | fcolumn5 | varchar | 30 |  | √ | ' ' |  |
| 6 | fcolumn4 | fcolumn4 | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_es_bak |  | fid |
| 2 | idx_isc_es_bak |  | fcolumn1 |
