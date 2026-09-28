# 执行结果-isc_data_copy_execution

## 执行结果-多语言表 t_isc_data_copy_execution_l

- **表名称：** 执行结果-多语言表
- **表名：** t_isc_data_copy_execution_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_data_copy_exec_l_0 |  | fid,flocaleid |
| 2 | t_isc_data_copy_execution_l_pkey |  | fpkid |

---

## 执行参数-子表 t_isc_dc_execution_params

- **表名称：** 执行参数-子表
- **表名：** t_isc_dc_execution_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparams_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 3 | fparams_index | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 4 | fparams_name | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fparams_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fparams_label | 标题 | varchar | 100 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dc_execution_params_pkey |  | fentryid |
| 2 | idx_isc_dc_exe_params_0 |  | fid |

---

## 执行结果-主表 t_isc_data_copy_execution

- **表名称：** 执行结果-主表
- **表名：** t_isc_data_copy_execution

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 执行服务器 | varchar | 50 |  | √ | ' ' | 执行服务器 |
| 3 | fexecute_count | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 4 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | fignored_count | 忽略行数 | int8 | 64 |  | √ | 0 | 忽略行数 |
| 6 | freal_target_system | 实际目标系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 7 | fsource_data_tag | 源单数据_详情 | text | 0 |  |  | ' ' | 源单数据_详情 |
| 8 | fmodifytime | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fexec_time | 执行耗时(毫秒) | int4 | 32 |  | √ | 0 | 执行耗时(毫秒) |
| 13 | fconvert_time | 转换时间(毫秒) | int8 | 64 |  | √ | 0 | 转换时间(毫秒) |
| 14 | fread_time | 读取时间(毫秒) | int8 | 64 |  | √ | 0 | 读取时间(毫秒) |
| 15 | fthread_count | 执行线程数 | int8 | 64 |  | √ | 0 | 执行线程数 |
| 16 | ftaskstage | 分批 | int8 | 64 |  | √ | 0 | [分批结果 isc_data_copy_taskstage](../iscb_files/isc_data_copy_taskstage.md) |
| 17 | ftotal_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 18 | ffailed_count | 失败行数 | int8 | 64 |  | √ | 0 | 失败行数 |
| 19 | ftrigger | ftrigger | int8 | 64 |  | √ | 0 |  |
| 20 | fsource_data | 源单数据 | varchar | 255 |  | √ | ' ' | 源单数据 |
| 21 | freal_source_system | 实际源系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fparent_execution | 父任务 | int8 | 64 |  | √ | 0 | [执行结果 isc_data_copy_execution](../iscb_files/isc_data_copy_execution.md) |
| 24 | fcallback_info | 回调信息 | varchar | 255 |  | √ | ' ' | 回调信息 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fread_bytes | 读取数据流量（字节） | int8 | 64 |  | √ | 0 | 读取数据流量（字节） |
| 27 | fjob_mutex | 后台任务锁 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 28 | fbatch_size | 目标单批量大小 | int8 | 64 |  | √ | 0 | 目标单批量大小 |
| 29 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 30 | fdata_copy_schama | 集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 31 | fstate | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: C :创建 R :执行中 S :完成 F :失败 X :已撤销 W :等待中 P :部分成功 B :分批中 I :已忽略 |
| 32 | fdata_copy_trigger | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 33 | ftype | 任务类型 | varchar | 30 |  | √ | ' ' | 任务类型,枚举: 0 :独立任务 1 :子任务 2 :父任务 |
| 34 | fsuccess_count | 成功行数 | int8 | 64 |  | √ | 0 | 成功行数 |
| 35 | fload_time | 加载时间(毫秒) | int8 | 64 |  | √ | 0 | 加载时间(毫秒) |
| 36 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fprepare_time | 准备时间(毫秒) | int8 | 64 |  | √ | 0 | 准备时间(毫秒) |
| 38 | fload_bytes | 加载数据流量（字节） | int8 | 64 |  | √ | 0 | 加载数据流量（字节） |
| 39 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_data_copy_execution_m |  | fmodifytime |
| 2 | idx_isc_data_copy_execution_2 |  | fdata_copy_trigger,fstate |
| 3 | idx_isc_data_copy_execution_3 |  | fparent_execution |
| 4 | idx_isc_data_copy_execution_s |  | fstate |
| 5 | idx_isc_data_copy_execution_1 |  | fnumber |
| 6 | idx_isc_data_copy_execution_t |  | fstart_time |
| 7 | t_isc_data_copy_execution_pkey |  | fid |
