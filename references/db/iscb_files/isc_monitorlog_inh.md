# 同步监控（废弃）-isc_monitorlog_inh

## 单据体-子表 t_isc_log_form

- **表名称：** 单据体-子表
- **表名：** t_isc_log_form

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetuniquevalue | 目标唯一标识值 | varchar | 600 |  | √ | ' ' | 目标唯一标识值 |
| 3 | fsublogid | 初始化子日志 | varchar | 100 |  | √ | ' ' | 初始化子日志 |
| 4 | fsingledata | 单条数据 | text | 0 |  |  | null | 单条数据 |
| 5 | ftargetuniquekey | 目标唯一标识字段 | varchar | 400 |  | √ | ' ' | 目标唯一标识字段 |
| 6 | fexcuteinfo | 执行信息 | text | 0 |  |  | null | 执行信息 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foriguniquekey | 源唯一标识字段 | varchar | 400 |  | √ | ' ' | 源唯一标识字段 |
| 9 | fviewsublog | 查看子日志 | varchar | 100 |  | √ | ' ' | 查看子日志 |
| 10 | forigorganization | 源主业务组织 | varchar | 100 |  | √ | ' ' | 源主业务组织 |
| 11 | ftargetdataid | 目标数据ID | int8 | 64 |  | √ | 0 | 目标数据ID |
| 12 | ftargetorganization | 目标主业务组织 | varchar | 100 |  | √ | ' ' | 目标主业务组织 |
| 13 | fexcuteinfo_tag | 执行信息_详情 | text | 0 |  |  | null | 执行信息_详情 |
| 14 | forigdataid | 源数据ID | int8 | 64 |  | √ | 0 | 源数据ID |
| 15 | fbatchnum | 批次 | int8 | 64 |  | √ | 1 | 批次 |
| 16 | fexcutestatus | 执行状态 | varchar | 100 |  | √ | ' ' | 执行状态,枚举: 0 :等待执行 1 :正在执行 2 :成功 3 :失败 4 :取消 5 :等待反馈 6 :部分成功 |
| 17 | fstack_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |
| 18 | fsingledata_tag | 单条数据_详情 | text | 0 |  |  | null | 单条数据_详情 |
| 19 | fstack | 异常堆栈 | text | 0 |  |  | null | 异常堆栈 |
| 20 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | foriguniquevalue | 源唯一标识值 | varchar | 600 |  | √ | ' ' | 源唯一标识值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_log_form_fid |  | fid |
| 2 | t_isc_log_form_pkey |  | fentryid |

---

## 执行记录-子表 t_isc_log_operation

- **表名称：** 执行记录-子表
- **表名：** t_isc_log_operation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffinishtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | foperationrow | 操作对象 | varchar | 100 |  | √ | ' ' | 操作对象 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fexetype | 执行类型 | int8 | 64 |  | √ | 1 | 执行类型,枚举: 1 :即时触发 2 :手工触发 3 :调度触发 4 :接口调用 5 :消息集成 6 :自动重试 7 :手工重试 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_log_opera_fid |  | fid |
| 2 | t_isc_log_operation_pkey |  | fentryid |

---

## 同步监控（废弃）-主表 t_isc_log_monitor

- **表名称：** 同步监控（废弃）-主表
- **表名：** t_isc_log_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigentity | 源实体 | varchar | 100 |  | √ | ' ' | 源实体 |
| 3 | ftotaltime | 执行总耗时 | varchar | 100 |  | √ | ' ' | 执行总耗时 |
| 4 | ftargetentity | 目标实体 | varchar | 100 |  | √ | ' ' | 目标实体 |
| 5 | fexportdata_tag | 传出数据_详情 | text | 0 |  |  | null | 传出数据_详情 |
| 6 | fexceptioninfo | 执行信息 | text | 0 |  |  | null | 执行信息 |
| 7 | fmetaentity | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 8 | fnoticetime | 任务下达时间 | timestamp | 0 |  |  | null | 任务下达时间 |
| 9 | fexceptionstack_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |
| 10 | fstatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 0 :等待执行 1 :正在执行 2 :成功 3 :失败 4 :取消 5 :等待反馈 6 :部分成功 |
| 11 | foperationtype | 操作类型 | varchar | 100 |  | √ | ' ' | 操作类型 |
| 12 | fintegration | 集成方案 | int8 | 64 |  | √ | 0 | [集成方案（废弃） isc_guide](../iscb_files/isc_guide.md) |
| 13 | fexportdata | 传出数据 | text | 0 |  |  | null | 传出数据 |
| 14 | fexcutetotal | 总执行条数 | varchar | 100 |  | √ | '0' | 总执行条数 |
| 15 | forigsystem | 源系统 | varchar | 100 |  | √ | ' ' | 源系统 |
| 16 | fparentid | 父日志ID | varchar | 100 |  | √ | ' ' | 父日志ID |
| 17 | fpage | 批次 | int8 | 64 |  | √ | 1 | 批次 |
| 18 | fexceptionstack | 异常堆栈 | text | 0 |  |  | null | 异常堆栈 |
| 19 | fexceptioninfo_tag | 执行信息_详情 | text | 0 |  |  | null | 执行信息_详情 |
| 20 | fexcutepercent | 执行百分比 | varchar | 100 |  | √ | '0' | 执行百分比 |
| 21 | fexecutor | 执行者 | varchar | 100 |  | √ | ' ' | 执行者 |
| 22 | fexcutednum | 已执行条数 | varchar | 100 |  | √ | '0' | 已执行条数 |
| 23 | ftargetsystem | 目标系统 | varchar | 100 |  | √ | ' ' | 目标系统 |
| 24 | fdirection | 数据集成方向 | varchar | 30 |  | √ | ' ' | 数据集成方向,枚举: 1 :金蝶云—>外部系统 2 :外部系统—>金蝶云 |
| 25 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 26 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: interception :操作拦截 Integration :数据集成 |
| 27 | fidentification | 认证标志 | varchar | 100 |  | √ | ' ' | 认证标志 |
| 28 | fexetype | 执行类型 | int8 | 64 |  | √ | 1 | 执行类型,枚举: 1 :即时触发 2 :手工触发 3 :调度触发 4 :接口调用 5 :消息集成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_log_mon_fstatus |  | fstatus |
| 2 | t_isc_log_monitor_pkey |  | fid |
| 3 | idx_isc_log_mon_fintegr |  | fintegration |
