# 集成资源历史-isc_res_history

## 集成资源历史-主表 t_iscb_res_history

- **表名称：** 集成资源历史-主表
- **表名：** t_iscb_res_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreated_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fres_content_tag | 资源内容_详情 | text | 0 |  |  | null | 资源内容_详情 |
| 4 | fres_type | 资源类别 | varchar | 50 |  | √ | ' ' | 资源类别,枚举: isc_metadata_schema :集成对象 isc_dataset_schema :数据集 isc_custom_function :自定义函数 isc_data_copy :数据集成方案 isc_data_copy_trigger :启动方案 isc_value_conver_rule :值转换规则 isc_apic_by_meta_schema :集成对象转API isc_apic_by_dc_trigger :启动方案转API isc_apic_by_vc :值转换规则转API isc_apic_by_sf :服务流程转API isc_apic_script :自定义API isc_apic_for_external_api :外部系统API登记 isc_apic_mservice :苍穹微服务登记 isc_call_api_by_evt :API任务（事件触发） isc_call_api_by_mq :API任务（MQ） isc_call_api_by_timer :API任务（定时） isc_mq_bill_data_pub :单据消息发布 isc_mq_bill_data_sub :单据消息订阅 isc_mq_subscriber :消息订阅主题 isc_mq_publisher :消息发布主题 isc_service_flow_r :服务流程（已发布） isc_data_comp :数据对比方案 isc_export_file :数据导出方案 isc_export_file_trigger :数据导出任务 isc_import_file :数据导入方案 isc_import_file_trigger :数据导入任务 isc_apic_by_dc_schema :数据集成方案转API isc_solution_center :解决方案 isc_solution_center_m :解决方案管理 isc_apic_webapi :WebAPI登记 |
| 5 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fres_id | 资源ID | int8 | 64 |  | √ | 0 | 资源ID |
| 7 | fres_content | 资源内容 | varchar | 255 |  | √ | ' ' | 资源内容 |
| 8 | fres_name | 资源名称 | varchar | 100 |  | √ | ' ' | 资源名称 |
| 9 | fres_number | 资源编码 | varchar | 150 |  | √ | ' ' | 资源编码 |
| 10 | foperate_key | 操作类别 | varchar | 50 |  | √ | ' ' | 操作类别 |
| 11 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_res_com |  | fres_id,fversion |
| 2 | pk_t_iscb_res_history |  | fid |
