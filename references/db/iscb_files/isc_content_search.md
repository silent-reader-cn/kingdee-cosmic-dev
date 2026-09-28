# 集成内容检索-isc_content_search

## 集成内容检索-主表 t_isc_content_search

- **表名称：** 集成内容检索-主表
- **表名：** t_isc_content_search

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 处理状态 | bpchar | 1 |  | √ | 'D' | 处理状态,枚举: D :待处理 Y :已处理 |
| 4 | flocation_tag | 关键词位置_详情 | varchar | 2000 |  | √ | ' ' | 关键词位置_详情 |
| 5 | fresource_type | 资源类型 | varchar | 100 |  | √ | ' ' | 资源类型,枚举: isc_data_copy :数据集成方案 isc_service_flow :服务流程 isc_value_conver_rule :值转换规则 isc_data_copy_trigger :启动方案 isc_metadata_schema :集成对象 iscx_resource :数据流资源 isc_apic_script :自定义API isc_apic_for_external_api :外部系统API登记 isc_apic_webapi :WebAPI登记 isc_custom_function :自定义函数 isc_call_api_by_timer :API任务（定时） isc_call_api_by_evt :API任务（事件触发） isc_call_api_by_mq :API任务（MQ） isc_mq_publisher :消息发布主题 isc_mq_subscriber :消息订阅主题 isc_mq_bill_data_pub :单据消息发布 isc_mq_bill_data_sub :单据消息订阅 isc_data_comp :数据对比方案 isc_export_file :数据导出方案 isc_export_file_trigger :数据导出任务 isc_import_file :数据导入方案 |
| 6 | flocation | 关键词位置 | varchar | 255 |  | √ | ' ' | 关键词位置 |
| 7 | fresource | 资源 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 8 | fkeyword | 关键词 | varchar | 100 |  | √ | ' ' | 关键词 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_content_search |  | fid |
| 2 | idx_isc_content_search_2 |  | fcreator |
| 3 | idx_isc_content_search_1 |  | fkeyword |
| 4 | idx_isc_content_search_0 |  | fresource |
