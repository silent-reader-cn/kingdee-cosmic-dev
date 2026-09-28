# 集成云定时任务计划-isc_job_schedule

## 集成云定时任务计划-分表 t_isc_job_schedule_t

- **表名称：** 集成云定时任务计划-分表
- **表名：** t_isc_job_schedule_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhost | 触发服务器 | varchar | 98 |  | √ | ' ' | 触发服务器 |
| 3 | fnext_trigger_time | 下次触发时间 | timestamp | 0 |  |  | null | 下次触发时间 |
| 4 | flast_triggered_time | 最近触发时间 | timestamp | 0 |  |  | null | 最近触发时间 |
| 5 | ftriggered_count | 触发次数 | int8 | 64 |  | √ | 0 | 触发次数 |
| 6 | fis_valid | 是否有效 | bpchar | 1 |  | √ | '0' | 是否有效 |
| 7 | flast_modified_time | 最近修改时间 | timestamp | 0 |  |  | null | 最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_job_schedule_t |  | fis_valid |
| 2 | pk_t_isc_job_schedule_t |  | fid |

---

## 集成云定时任务计划-主表 t_isc_job_schedule

- **表名称：** 集成云定时任务计划-主表
- **表名：** t_isc_job_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 4 | fjob_def_id | 任务定义ID | int8 | 64 |  | √ | 0 | 任务定义ID |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fvalidate_time | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 7 | fexpired_time | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 8 | ftitle | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 9 | fcreated_time | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 10 | fcron_expr | 调度计划 | varchar | 150 |  | √ | ' ' | 调度计划 |
| 11 | ftype | 任务类型编码 | varchar | 50 |  | √ | ' ' | 任务类型编码 |
| 12 | ftype2 | 任务类型 | varchar | 36 |  | √ | ' ' | [集成云后台任务类型 isc_job_type](../iscb_files/isc_job_type.md) |
| 13 | flang | 语言编码 | varchar | 50 |  | √ | ' ' | 语言编码 |
| 14 | fparam_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_job_schedule_def |  | fjob_def_id |
| 2 | pk_t_isc_job_schedule |  | fid |
