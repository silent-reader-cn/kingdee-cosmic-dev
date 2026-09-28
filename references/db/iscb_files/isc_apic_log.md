# 集成API日志-isc_apic_log

## 集成API日志-主表 t_iscb_apic_log

- **表名称：** 集成API日志-主表
- **表名：** t_iscb_apic_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcaller | 调用者 | varchar | 50 |  | √ | ' ' | 调用者 |
| 3 | fend_time | 状态更新/结束时间 | timestamp | 0 |  |  | null | 状态更新/结束时间 |
| 4 | fout_digest | fout_digest | varchar | 150 |  | √ | ' ' |  |
| 5 | fstart_time | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 6 | fparams | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 7 | fresult | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 8 | fapi_type | 类别 | varchar | 30 |  | √ | ' ' | 类别,枚举: isc_apic_for_external_api :外部系统API isc_apic_by_dc_schema :数据集成方案转API isc_apic_by_meta_schema :集成对象转API isc_apic_by_dc_trigger :启动方案转API isc_apic_script :自定义API isc_apic_by_vc :值转换规则转API isc_apic_by_sf :服务流程转API isc_apic_mservice :苍穹微服务 isc_apic_webapi :WebAPI登记 |
| 9 | fapi_ref | API | int8 | 64 |  | √ | 0 | 外部系统API登记 isc_apic_for_external_api |
| 10 | fresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 11 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: R :执行中 S :成功 F :失败 |
| 12 | fserver | 执行服务器 | varchar | 100 |  | √ | ' ' | 执行服务器 |
| 13 | fparams_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 14 | fin_digest | fin_digest | varchar | 150 |  | √ | ' ' |  |
| 15 | freal_data_source | 实际数据源 | varchar | 60 |  | √ | ' ' | 实际数据源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_apic_log_pkey |  | fid |
| 2 | idx_iscb_apic_log_c |  | fcaller |
| 3 | idx_iscb_apic_log_s |  | fserver |
| 4 | idx_apic_log_param |  | fparams |
| 5 | idx_iscb_apic_log_st |  | fstate |
| 6 | idx_apic_log_out_digest |  | fout_digest |
| 7 | idx_apic_log_result |  | fresult |
| 8 | idx_apic_log_start_time |  | fstart_time |
| 9 | idx_iscb_apic_log_ref |  | fapi_ref,fstart_time |
| 10 | idx_apic_log_in_digest |  | fin_digest |
| 11 | idx_iscb_apic_log_e |  | fend_time |
