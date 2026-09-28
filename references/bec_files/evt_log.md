# 事件日志（内部）-evt_log

## 事件日志（内部）-主表 t_evt_log

- **表名称：** 事件日志（内部）-主表
- **表名：** t_evt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 时间 | timestamp | 0 |  |  | null | 时间 |
| 3 | feventid | 事件id | int8 | 64 |  | √ | 0 | 事件id |
| 4 | feventnumber | 事件编码 | varchar | 500 |  | √ | ' ' | 事件编码 |
| 5 | fjobid | jobId | int8 | 64 |  | √ | 0 | jobId |
| 6 | fbusinesskey | 业务主键 | varchar | 200 |  | √ | ' ' | 业务主键 |
| 7 | fscene | 记录时机 | varchar | 50 |  | √ | ' ' | 记录时机 |
| 8 | fentitynumber | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 9 | fserviceid | 服务id | int8 | 64 |  | √ | 0 | 服务id |
| 10 | fsubscribeid | 订阅id | int8 | 64 |  | √ | 0 | 订阅id |
| 11 | fcontent | 内容 | text | 0 |  |  | null | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_log_jobid |  | fjobid |
| 2 | pk_t_evt_log |  | fid |
| 3 | idx_evt_log_createdate |  | fcreatedate |
