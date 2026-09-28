# 第三方配置异常日志-bos_log_thirdapp_auth

## 第三方配置异常日志-主表 t_log_thirdapp_auth

- **表名称：** 第三方配置异常日志-主表
- **表名：** t_log_thirdapp_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |
| 3 | fstatus | 运行状态 | bpchar | 1 |  | √ | '0' | 运行状态,枚举: 0 :异常 1 :正常 |
| 4 | ferrorcode | 错误码 | varchar | 50 |  | √ | ' ' | 错误码 |
| 5 | foptime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 6 | fresourceid | 多语言资源id | varchar | 50 |  | √ | ' ' | 多语言资源id |
| 7 | fcorpid | 企业id | varchar | 50 |  | √ | ' ' | 企业id |
| 8 | fopdesc | 异常描述 | varchar | 600 |  | √ | ' ' | 异常描述 |
| 9 | fimtypeid | 第三方映射 | int8 | 64 |  | √ | 0 | [移动平台类型 bas_instantmsgtype](../base_files/bas_instantmsgtype.md) |
| 10 | furl | URL | varchar | 600 |  | √ | ' ' | URL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_log_thirdapp_corpid |  | fcorpid |
| 2 | idx_t_log_thirdapp_imtypeid |  | fimtypeid |
| 3 | idx_t_log_thirdapp_errorcode |  | ferrorcode |
| 4 | pk_t_log_thirdapp_auth |  | fid |
