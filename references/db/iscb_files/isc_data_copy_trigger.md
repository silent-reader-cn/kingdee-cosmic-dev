# 启动方案-isc_data_copy_trigger

## 后置任务-子表 t_iscb_next_tasks

- **表名称：** 后置任务-子表
- **表名：** t_iscb_next_tasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fnext_task | 方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_next_tasks_pkey |  | fentryid |
| 2 | idx_iscb_next_tasks_fk |  | fid |

---

## 过滤条件-子表 t_isc_data_copy_trigger_f

- **表名称：** 过滤条件-子表
- **表名：** t_isc_data_copy_trigger_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleft_bracket | 左括号 | varchar | 30 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 3 | ffilter_column | 条件字段 | varchar | 300 |  | √ | ' ' | 条件字段 |
| 4 | fcompare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 5 | flink | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 6 | ffilter_label | 字段描述 | varchar | 200 |  | √ | ' ' | 字段描述 |
| 7 | fvalue_var | 过滤条件参数 | varchar | 30 |  | √ | ' ' | 过滤条件参数,枚举: |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fvalue_fixed | 固定比较值 | varchar | 510 |  | √ | ' ' | 固定比较值 |
| 11 | fright_bracket | 右括号 | varchar | 30 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dc_trigger_f |  | fid,fseq |
| 2 | t_isc_data_copy_trigger_f_pkey |  | fentryid |

---

## 启动方案-主表 t_isc_data_copy_trigger

- **表名称：** 启动方案-主表
- **表名：** t_isc_data_copy_trigger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnew_target_system | 目标系统（重定向） | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 3 | ftasksize | 源单批量大小 | int8 | 64 |  | √ | 0 | 源单批量大小 |
| 4 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 5 | fmutex_name | 互斥锁标志 | varchar | 50 |  | √ | ' ' | 互斥锁标志 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fthread_ubound | 最大线程数 | int8 | 64 |  | √ | 0 | 最大线程数 |
| 8 | fvalue_rule_cache_size | 值转换缓存参数 | int8 | 64 |  | √ | 0 | 值转换缓存参数 |
| 9 | fexe_job_user | 执行作业的用户 | varchar | 100 |  | √ | ' ' | 执行作业的用户 |
| 10 | ftrigged_time | 最近触发时间 | timestamp | 0 |  |  | null | 最近触发时间 |
| 11 | fcallback_info | 回调信息 | varchar | 255 |  | √ | ' ' | 回调信息 |
| 12 | fnew_source_system | 来源系统（重定向） | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 13 | fretry_interval | 重试间隔(分钟) | varchar | 510 |  | √ | ' ' | 重试间隔(分钟) |
| 14 | ftimestamp_field | 时间戳属性 | varchar | 255 |  | √ | ' ' | 时间戳属性 |
| 15 | fismqs | 开启多选消息发布主题 | varchar | 10 |  | √ | ' ' | 开启多选消息发布主题 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | flog_record_count | 失败日志数阈值 | int8 | 64 |  | √ | 0 | 失败日志数阈值 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fretry_count_str | 最大重试次数 | varchar | 50 |  | √ | ' ' | 最大重试次数 |
| 20 | fevents | 触发事件 | varchar | 1000 |  | √ | ' ' | 触发事件,枚举: |
| 21 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 22 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 23 | fpriority | 优先级 | varchar | 10 |  | √ | '+0000' | 优先级,枚举: -9000 :最高 -7000 :很高 -5000 :高 -3000 :中高 +0000 :中 +3000 :中低 +5000 :低 +7000 :很低 +9000 :最低 |
| 24 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 25 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 28 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 29 | fclient_filter_log_level | 源端过滤日志级别 | varchar | 30 |  | √ | ' ' | 源端过滤日志级别,枚举: DEFAULT :默认 IGNORE :忽略 INFO :信息 WARN :警告 |
| 30 | fsource_protocal | 来源数据获取方式 | varchar | 30 |  | √ | ' ' | 来源数据获取方式,枚举: RPC :默认 MQ :消息队列 |
| 31 | fdata_copy | 数据集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 32 | fschema_category | 方案分类 | varchar | 100 |  | √ | ' ' | 方案分类 |
| 33 | fschedule | 触发间隔 | varchar | 100 |  | √ | ' ' | 触发间隔 |
| 34 | ftotal_count | 触发次数 | int8 | 64 |  | √ | 0 | 触发次数 |
| 35 | fjob_define | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 36 | fvalidated_time | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 37 | ftimestamp_type | 时间戳字段类型 | varchar | 50 |  | √ | ' ' | 时间戳字段类型 |
| 38 | ftrigger_type | 启动类型 | varchar | 30 |  | √ | ' ' | 启动类型,枚举: auto :定时启动 manual :人工启动 event :事件触发 message :消息启动 |
| 39 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 40 | fmax_timestamp | 最大时间戳 | varchar | 50 |  | √ | ' ' | 最大时间戳 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fsubscriber_queue | 消息订阅主题 | int8 | 64 |  | √ | 0 | [消息订阅主题 isc_mq_subscriber](../iscb_files/isc_mq_subscriber.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fretry_count | 重试次数(废弃) | int8 | 64 |  | √ | 0 | 重试次数(废弃) |
| 45 | fjob_mutex | 硬件资源分配 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 46 | fbatch_size | 目标单批量大小 | int8 | 64 |  | √ | 0 | 目标单批量大小 |
| 47 | fjob_schedule | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 48 | fdata_source | fdata_source | int8 | 64 |  | √ | 0 |  |
| 49 | fcontains_dynamic_filter | 过滤条件参数值包含变量 | bpchar | 1 |  | √ | '0' | 过滤条件参数值包含变量 |
| 50 | finterval | 执行频率 | varchar | 30 |  | √ | ' ' | 执行频率,枚举: 1 :执行频率 - 1次/小时 2 :执行频率 - 2次/小时 3 :执行频率 - 3次/小时 5 :执行频率 - 5次/小时 10 :执行频率 - 10次/小时 20 :执行频率 - 20次/小时 30 :执行频率 - 30次/小时 60 :执行频率 - 60次/小时 d :每天 w :每周 m :每月 d1 :每天凌晨一点（服务器时间） 0 :自定义 |
| 51 | fexpired_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 52 | ftrace_all | 保存全部日志 | bpchar | 1 |  | √ | '0' | 保存全部日志 |
| 53 | fdigest | 摘要模板 | varchar | 255 |  |  | ' ' | 摘要模板 |
| 54 | ftarget_protocal | 目标数据推送方式 | varchar | 30 |  | √ | ' ' | 目标数据推送方式,枚举: RPC :默认 MQ :消息队列 |
| 55 | fpublisher_queue | 消息发布主题 | int8 | 64 |  | √ | 0 | [消息发布主题 isc_mq_publisher](../iscb_files/isc_mq_publisher.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_data_copy_trigger_pkey |  | fid |
| 2 | idx_isc_data_copy_trigger_1 |  | fnumber |
| 3 | idx_isc_data_copy_trigger_0 |  | fdata_copy |

---

## 启动方案-多语言表 t_isc_data_copy_trigger_l

- **表名称：** 启动方案-多语言表
- **表名：** t_isc_data_copy_trigger_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 启动方案名称 | varchar | 100 |  | √ | ' ' | 启动方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_data_copy_trigger_l_pkey |  | fpkid |
| 2 | idx_isc_data_copy_trigger_l_0 |  | flocaleid,fid |

---

## 事件处理-子表 t_iscb_datacopy_events

- **表名称：** 事件处理-子表
- **表名：** t_iscb_datacopy_events

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevent | 数据集成事件 | varchar | 30 |  | √ | ' ' | 数据集成事件,枚举: OnRowSuccess :单据集成成功时 OnRowFailed :单据集成失败时 OnTaskSuccess :集成任务成功时 OnTaskFailed :集成任务失败时 |
| 3 | fevent_handler | 事件处理器 | varchar | 500 |  | √ | ' ' | 事件处理器 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftarget_consumer | 事件处理方 | varchar | 30 |  | √ | ' ' | 事件处理方,枚举: SourceSystem :源系统 TargetSystem :目标系统 ThisSystem :集成云本系统 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_datacopy_events_pkey |  | fentryid |
| 2 | idx_iscb_datacopy_events_fk |  | fid |

---

## 消息发布主题-多选基础资料表 t_isc_trigger_queue_mq

- **表名称：** 消息发布主题-多选基础资料表
- **表名：** t_isc_trigger_queue_mq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [消息发布主题 isc_mq_publisher](../iscb_files/isc_mq_publisher.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_trigger_queue_mq |  | fpkid |
| 2 | idx_isc_trigger_queue_mq |  | fid |

---

## 参数分录-子表 t_isc_dc_trigger_params

- **表名称：** 参数分录-子表
- **表名：** t_isc_dc_trigger_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fparams_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 4 | fdata_type | 参数类型 | varchar | 30 |  | √ | ' ' | 参数类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 5 | fiscustom | 是否启动方案添加的参数 | bpchar | 1 |  | √ | '1' | 是否启动方案添加的参数 |
| 6 | fparams_index | fparams_index | varchar | 100 |  | √ | ' ' |  |
| 7 | fparams_name | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fparams_label | 标题 | varchar | 100 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dc_trigger_p_0 |  | fid |
| 2 | t_isc_dc_trigger_params_pkey |  | fentryid |
