# 预警执行日志-warn_earlywarn_log

## 预警执行日志-主表 t_warn_monitorlog

- **表名称：** 预警执行日志-主表
- **表名：** t_warn_monitorlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :进行中 1 :执行成功 2 :执行失败 |
| 3 | fearlywarnid | 预警对象 | varchar | 36 |  | √ | ' ' | 业务预警对象 warn_earlywarn |
| 4 | foperationtype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型,枚举: task :调度触发 manual :手动执行 |
| 5 | foperatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcomment | 备注 | varchar | 200 |  |  | null | 备注 |
| 7 | fwarnscheduleid | 监控方案 | varchar | 36 |  | √ | ' ' | 监控方案基础资料 warn_schedule |
| 8 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fexecutionmillis | 执行时长(millis) | int8 | 64 |  | √ | 0 | 执行时长(millis) |
| 10 | fexecutiontime | 执行时长 | varchar | 50 |  | √ | ' ' | 执行时长 |
| 11 | fstarttime | 开始时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 开始时间 |

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
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | faction | 操作 | varchar | 128 |  | √ | ' ' | 操作 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 1 | 分录行号 |
| 6 | fresult | 结果 | text | 0 |  |  | null | 结果 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_warn_log_fentryid |  | fid |
| 2 | t_warn_monitor_detaillog_pkey |  | fentryid |
