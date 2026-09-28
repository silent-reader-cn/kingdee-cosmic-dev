# 脱敏操作日志-isc_schema_encrypt_log

## 脱敏操作日志-主表 t_isc_schema_enpt_log

- **表名称：** 脱敏操作日志-主表
- **表名：** t_isc_schema_enpt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 集成对象名称 | varchar | 150 |  | √ | ' ' | 集成对象名称 |
| 3 | flog_tag | 数据脱敏操作_详情 | text | 0 |  |  | null | 数据脱敏操作_详情 |
| 4 | ftype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 5 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fnumber | 集成对象编码 | varchar | 150 |  | √ | ' ' | 集成对象编码 |
| 8 | fschemaid | 集成对象id | varchar | 50 |  | √ | ' ' | 集成对象id |
| 9 | flog | 数据脱敏操作 | varchar | 255 |  | √ | ' ' | 数据脱敏操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_shcema_et |  | fnumber |
| 2 | pk_isc_schema_enpt_log |  | fid |
