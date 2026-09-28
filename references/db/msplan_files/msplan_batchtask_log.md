# 分布式任务处理日志-msplan_batchtask_log

## 单据体-子表 t_msplan_batchtask_entry

- **表名称：** 单据体-子表
- **表名：** t_msplan_batchtask_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryresult | 运行结果 | varchar | 5 |  | √ | ' ' | 运行结果,枚举: A :成功 B :失败 C :未运行 |
| 3 | finstanceid | 实例编号 | varchar | 255 |  | √ | ' ' | 实例编号 |
| 4 | fentrydetailmsg | 详细信息 | varchar | 1000 |  | √ | ' ' | 详细信息 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fevntid | 事件编号 | varchar | 50 |  | √ | ' ' | 事件编号 |
| 8 | fentryoperatms | 时长(ms) | int8 | 64 |  | √ | 0 | 时长(ms) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_batchtask_entry |  | fentryid |
| 2 | idx_msplan_batchtask_entry_fid |  | fid |

---

## 分布式任务处理日志-主表 t_msplan_batchtask_log

- **表名称：** 分布式任务处理日志-主表
- **表名：** t_msplan_batchtask_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fjobid | 任务ID | varchar | 50 |  | √ | ' ' | 任务ID |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 9 | fjobname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 10 | fcontrolqueue | 主控队列 | varchar | 255 |  | √ | ' ' | 主控队列 |
| 11 | fstarttime | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 任务运行状态 | varchar | 5 |  | √ | ' ' | 任务运行状态,枚举: A :成功 B :失败 C :手工终止 D :运行中 E :定时任务清理 |
| 14 | fbizclass | 处理类名称 | varchar | 255 |  | √ | ' ' | 处理类名称 |
| 15 | fduration | 执行时长(ms) | int8 | 64 |  | √ | 0 | 执行时长(ms) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fqueuename | 消费队列名称 | varchar | 255 |  | √ | ' ' | 消费队列名称 |
| 18 | fendtime | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_batchtask_log_fid |  | fstatus |
| 2 | pk_msplan_batchtask_log |  | fid |
