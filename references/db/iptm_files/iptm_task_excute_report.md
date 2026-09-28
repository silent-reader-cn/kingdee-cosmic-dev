# 导入报告-iptm_task_excute_report

## 导入报告-主表 t_iptm_task_report

- **表名称：** 导入报告-主表
- **表名：** t_iptm_task_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalsuccesscnt | 总成功行数 | int4 | 32 |  | √ | 0 | 总成功行数 |
| 3 | ftotalfailcnt | 总失败行数 | int4 | 32 |  | √ | 0 | 总失败行数 |
| 4 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fimpstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: A :导入成功 B :导入失败 |
| 6 | fimpdatetime | 导入时间 | timestamp | 0 |  |  | null | 导入时间 |
| 7 | fnumber | 报告编码 | varchar | 255 |  | √ | ' ' | 报告编码 |
| 8 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | ftaskid | 任务编码 | int8 | 64 |  | √ | 0 | [导入任务 iptm_imptask](../iptm_files/iptm_imptask.md) |
| 10 | ftextfield | 导入时长 | varchar | 50 |  | √ | ' ' | 导入时长 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_task_report_fnumber |  | fnumber |
| 2 | pk_t_iptm_task_report |  | fid |

---

## 任务详情单据体-子表 t_iptm_task_reportentry

- **表名称：** 任务详情单据体-子表
- **表名：** t_iptm_task_reportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 业务对象名称 | varchar | 255 |  | √ | ' ' | 业务对象名称 |
| 3 | ffailcount | 失败行数 | int4 | 32 |  | √ | 0 | 失败行数 |
| 4 | fimplogid | 导入结果 | int8 | 64 |  | √ | 0 | 导入结果 bos_importlog |
| 5 | fbillentityno | 业务对象标识 | varchar | 255 |  | √ | ' ' | 业务对象标识 |
| 6 | fexecstatus | 子任务执行状态 | varchar | 50 |  | √ | ' ' | 子任务执行状态,枚举: A :导入成功 B :导入失败 |
| 7 | fstart | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fend | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffcount | 数据行数 | int4 | 32 |  | √ | 0 | 数据行数 |
| 12 | fsuccesscount | 成功行数 | int4 | 32 |  | √ | 0 | 成功行数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_task_reportentry |  | fentryid |
| 2 | idx_iptm_task_reportentry_fid |  | fid |
