# 预警方案执行情况-warn_earlywarn_log

## 单据体-子表 t_warn_monitor_msglog

- **表名称：** 单据体-子表
- **表名：** t_warn_monitor_msglog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessageid | 消息ID | int8 | 64 |  | √ | 0 | 消息ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_warn_monitor_msglog |  | fentryid |
| 2 | idx_warn_msglog_fid |  | fid |

---

## 预警方案执行情况-主表 t_warn_monitorlog

- **表名称：** 预警方案执行情况-主表
- **表名：** t_warn_monitorlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :进行中 1 :执行成功 2 :执行失败 |
| 3 | fearlywarnid | 预警对象名称 | varchar | 36 |  | √ | ' ' | [业务预警对象 warn_earlywarn](../mdl_files/warn_earlywarn.md) |
| 4 | foperationtype | 执行方式 | varchar | 30 |  | √ | ' ' | 执行方式,枚举: task :调度触发 manual :手动执行 |
| 5 | foperatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcomment | 备注 | varchar | 200 |  |  | null | 备注 |
| 7 | fwarnscheduleid | 方案名称 | varchar | 36 |  | √ | ' ' | [监控方案基础资料 warn_schedule](../cts_files/warn_schedule.md) |
| 8 | fendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 9 | fexecutionmillis | 执行时长(millis) | int8 | 64 |  | √ | 0 | 执行时长(millis) |
| 10 | fexecutiontime | 执行时长 | varchar | 50 |  | √ | ' ' | 执行时长 |
| 11 | fstarttime | 执行开始时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 执行开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_log_fwarnscheduleid |  | fwarnscheduleid |
| 2 | t_warn_monitorlog_pkey |  | fid |

---

## 单据体-子表 t_warn_monitor_detaillog

- **表名称：** 单据体-子表
- **表名：** t_warn_monitor_detaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 3 | flogformat | 日志格式 | bpchar | 1 |  | √ | '1' | 日志格式,枚举: 1 :旧格式（纯文本，不支持多语言） 2 :新格式（Json，支持多语言） |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | faction | 操作 | varchar | 128 |  | √ | ' ' | 操作 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 1 | 分录行号 |
| 7 | fresult | 结果 | text | 0 |  |  | null | 结果 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_log_fentryid |  | fid |
| 2 | t_warn_monitor_detaillog_pkey |  | fentryid |
