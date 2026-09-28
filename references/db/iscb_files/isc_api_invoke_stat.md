# API调用统计-isc_api_invoke_stat

## API调用统计-主表 t_isc_api_invoke_stat

- **表名称：** API调用统计-主表
- **表名：** t_isc_api_invoke_stat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapi_number | API编码 | varchar | 100 |  | √ | ' ' | API编码 |
| 3 | fsuccess_count | 调用成功次数 | int8 | 64 |  | √ | 0 | 调用成功次数 |
| 4 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 5 | flast_invoke_time | API最后调用时间 | timestamp | 0 |  |  | null | API最后调用时间 |
| 6 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffailed_count | 调用失败次数 | int8 | 64 |  | √ | 0 | 调用失败次数 |
| 8 | fapi_type | API类型 | varchar | 100 |  | √ | ' ' | API类型,枚举: isc_apic_by_dc_trigger :启动方案转API isc_apic_by_dc_schema :数据集成方案转API isc_apic_by_vc :值转换规则转API isc_apic_by_meta_schema :集成对象转API isc_apic_for_external_api :外部系统API登记 isc_apic_mservice :苍穹微服务登记 isc_apic_script :自定义API isc_apic_by_sf :服务流程转API |
| 9 | fapi_state | API状态 | varchar | 30 |  | √ | ' ' | API状态,枚举: 0 :已删除 1 :启用 2 :禁用 |
| 10 | fapi_name | API名称 | varchar | 100 |  | √ | ' ' | API名称 |
| 11 | finvoke_count | 调用总次数 | int8 | 64 |  | √ | 0 | 调用总次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_api_invoke_stat |  | fid |
| 2 | idx_invoke_stat |  | fapi_number |
