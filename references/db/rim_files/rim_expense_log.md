# 报销单日志-rim_expense_log

## 报销单日志-主表 t_rim_expense_log

- **表名称：** 报销单日志-主表
- **表名：** t_rim_expense_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flog_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | fcontent_tag | 请求内容_详情 | text | 0 |  |  | null | 请求内容_详情 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 8 | fcontent | 请求内容 | varchar | 255 |  | √ | ' ' | 请求内容 |
| 9 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_expense_log |  | fbillno |
| 2 | pk_rim_expense_log |  | fid |
| 3 | idx_rim_expense_log_id |  | fbillid |
| 4 | idx_rim_expense_log_time |  | fcreate_time,flog_type |
