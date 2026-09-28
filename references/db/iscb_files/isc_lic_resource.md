# 集成云方案许可-isc_lic_resource

## 集成云方案许可-主表 t_isc_lic_resource

- **表名称：** 集成云方案许可-主表
- **表名：** t_isc_lic_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_source_id | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 3 | fname | 资源名称 | varchar | 150 |  | √ | ' ' | 资源名称 |
| 4 | fstate | 许可状态 | varchar | 50 |  | √ | ' ' | 许可状态,枚举: Y :正常 N :无 |
| 5 | fcreator_id | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | ftype | 类别 | varchar | 50 |  | √ | ' ' | 类别,枚举: isc_service_flow :服务流程 iscx_resource.data_flow :数据流 isc_data_copy :数据集成方案 isc_metadata_schema :集成对象 isc_apic_script :自定义API isc_apic_webapi :WebAPI登记 isc_apic_for_external_api :外部系统API |
| 7 | fnumber | 资源编码 | varchar | 150 |  | √ | ' ' | 资源编码 |
| 8 | fresource_id | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 9 | fcreatedtime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_lic_resource |  | fid |
| 2 | pk_isc_lic_resource |  | fresource_id |
