# API授权-isc_apic_permission

## API授权-主表 t_iscb_apic_permission

- **表名称：** API授权-主表
- **表名：** t_iscb_apic_permission

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreated_time | 授权时间 | timestamp | 0 |  |  | null | 授权时间 |
| 3 | fcreator_id | 授权人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fapi_type | API类别 | varchar | 30 |  | √ | ' ' | API类别,枚举: isc_apic_for_external_api :外部系统API登记 isc_apic_script :自定义API isc_apic_by_sf :服务流程转API isc_apic_by_dc_schema :数据集成方案转API isc_apic_by_meta_schema :集成对象转API isc_apic_by_dc_trigger :启动方案转API isc_apic_by_vc :值转换规则转API isc_apic_mservice :苍穹微服务登记 |
| 5 | fapi_caller | 授权调用者 | int8 | 64 |  | √ | 0 | API调用者 isc_apic_caller |
| 6 | fapi_ref | 授权API | int8 | 64 |  | √ | 0 | 外部系统API登记 isc_apic_for_external_api |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_permission_t |  | fcreated_time |
| 2 | t_iscb_apic_permission_pkey |  | fid |
| 3 | idx_iscb_apic_permission_c |  | fapi_caller,fapi_type,fapi_ref |
