# 异步处理错误日志-bal_error_log

## 异步处理错误日志-主表 t_bal_error_log

- **表名称：** 异步处理错误日志-主表
- **表名：** t_bal_error_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 3 | ferrormsg | 异常信息 | varchar | 200 |  | √ | ' ' | 异常信息 |
| 4 | fparams_tag | 参数信息_详情 | text | 0 |  |  | null | 参数信息_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 7 | fclassinfo | 类信息 | varchar | 200 |  | √ | ' ' | 类信息 |
| 8 | fparams | 参数信息 | varchar | 200 |  | √ | ' ' | 参数信息 |
| 9 | ftips | 提示信息 | varchar | 50 |  | √ | ' ' | 提示信息 |
| 10 | ferrormsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_err_log_fct |  | fcreatetime |
| 2 | pk_bal_error_log |  | fid |
