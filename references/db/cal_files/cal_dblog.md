# 核算后台日志-cal_dblog

## 核算后台日志-主表 t_cal_dblog

- **表名称：** 核算后台日志-主表
- **表名：** t_cal_dblog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 3 | fparam | 调用信息 | varchar | 255 |  | √ | ' ' | 调用信息 |
| 4 | ftraceid | traceid | varchar | 80 |  | √ | ' ' | traceid |
| 5 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 6 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 8 | flevel | 级别 | bpchar | 1 |  | √ | 'A' | 级别,枚举: A :成功 B :警告 C :错误 |
| 9 | ftype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: A :缓冲池分拣 B :缓冲池计算 |
| 10 | frunat | 执行服务器 | varchar | 80 |  | √ | ' ' | 执行服务器 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fparam_tag | 调用信息_详情 | text | 0 |  |  | null | 调用信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cal_dblog |  | fid |
| 2 | idx_cal_sttp |  | fstarttime,ftype |
| 3 | idx_cal_trc |  | ftraceid |
