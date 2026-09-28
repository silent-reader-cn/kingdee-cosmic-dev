# 固定资产操作日志-fa_imsc_log

## 固定资产操作日志-主表 t_fa_imsc_log

- **表名称：** 固定资产操作日志-主表
- **表名：** t_fa_imsc_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | floginfo | 执行日志 | text | 0 |  |  | null | 执行日志 |
| 3 | foperatname | 操作名称 | varchar | 100 |  |  | null | 操作名称 |
| 4 | fservicename | 微服务名称 | varchar | 100 |  |  | null | 微服务名称 |
| 5 | fdatetime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 6 | fformid | 单据标识 | varchar | 100 |  |  | null | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_imsc_log |  | fid |
| 2 | idx_fa_imsc_log_formid |  | fformid |
| 3 | idx_fa_imsc_log_servicename |  | fservicename |
