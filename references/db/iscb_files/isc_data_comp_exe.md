# 数据对比结果-isc_data_comp_exe

## 数据对比结果-主表 t_isc_data_comp_exe

- **表名称：** 数据对比结果-主表
- **表名：** t_isc_data_comp_exe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecute_count | 已补偿行数 | int8 | 64 |  | √ | 0 | 已补偿行数 |
| 3 | ftar_no_same_count | 目标单不一致总行数 | varchar | 50 |  | √ | ' ' | 目标单不一致总行数 |
| 4 | fcomp_trigger | fcomp_trigger | int8 | 64 |  | √ | 0 |  |
| 5 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fstrategy | 对比策略 | varchar | 30 |  | √ | ' ' | 对比策略,枚举: CheckExist :目标单是否存在 CheckUpdate :目标单是否未更新 CheckConsistency :源和目标单是否一致 Custom :自定义 |
| 7 | freal_target_system | 实际目标系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 8 | fdata_comp | 数据对比方案 | int8 | 64 |  | √ | 0 | [数据对比方案 isc_data_comp](../iscb_files/isc_data_comp.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ffailed_count | 失败行数 | int8 | 64 |  | √ | 0 | 失败行数 |
| 12 | ftrigger_type | ftrigger_type | varchar | 50 |  | √ | ' ' |  |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | freal_source_system | 实际源系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcallback_info | 回调微服务结果 | varchar | 500 |  | √ | ' ' | 回调微服务结果 |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdatetime | fauditdatetime | timestamp | 0 |  |  | null |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fjob_mutex | 后台任务组 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 21 | fbatch_size | 比较批量大小 | int4 | 32 |  | √ | 0 | 比较批量大小 |
| 22 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 23 | fconclusion | 结论 | varchar | 50 |  | √ | ' ' | 结论 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | ftar_no_syn_count | 目标单未更新行数 | int8 | 64 |  | √ | 0 | 目标单未更新行数 |
| 26 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: C :创建 R :执行中 S :完全匹配 F :失败 X :已撤销 P :部分匹配 N :完全不匹配 |
| 27 | ftar_no_exist_count | 目标单缺失行数 | int8 | 64 |  | √ | 0 | 目标单缺失行数 |
| 28 | fsource_count | 源单行数 | int8 | 64 |  | √ | 0 | 源单行数 |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_data_comp_exe2 |  | fdata_comp |
| 2 | pk_t_isc_data_comp_exe |  | fid |
| 3 | idx_isc_data_comp_exe3 |  | fcomp_trigger |

---

## 数据范围-子表 t_isc_data_comp_filter_1

- **表名称：** 数据范围-子表
- **表名：** t_isc_data_comp_filter_1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilter_column | 条件字段 | varchar | 50 |  | √ | ' ' | 条件字段 |
| 3 | ffilter_compare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 4 | ffilter_right_bracket | 右括号 | bpchar | 1 |  | √ | ' ' | 右括号 |
| 5 | ffilter_label | 条件描述 | varchar | 50 |  | √ | ' ' | 条件描述 |
| 6 | ffilter_value_var | 比较值变量 | varchar | 30 |  | √ | ' ' | 比较值变量 |
| 7 | ffilter_link | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符 |
| 8 | ffilter_value_fixed | 固定比较值 | varchar | 500 |  | √ | ' ' | 固定比较值 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffilter_left_bracket | 左括号 | bpchar | 1 |  | √ | ' ' | 左括号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp_filter_1 |  | fentryid |
| 2 | idx_isc_data_comp_filter_1 |  | fid,fentryid |

---

## 执行参数-子表 t_isc_data_exe_params

- **表名称：** 执行参数-子表
- **表名：** t_isc_data_exe_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparam_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fparam_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparam_title | 标题 | varchar | 50 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_exe_params |  | fentryid |
| 2 | idx_isc_data_exe_params |  | fid,fentryid |
