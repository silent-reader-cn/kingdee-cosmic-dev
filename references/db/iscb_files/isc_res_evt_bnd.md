# 集成资源事件绑定-isc_res_evt_bnd

## 集成资源事件绑定-主表 t_isc_res_evt_bnd

- **表名称：** 集成资源事件绑定-主表
- **表名：** t_isc_res_evt_bnd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequired_fields | 取值字段 | varchar | 2000 |  | √ | ' ' | 取值字段 |
| 3 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | frequired_fields_tag | 取值字段_详情 | text | 0 |  |  | null | 取值字段_详情 |
| 5 | ftrigger | 触发方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 6 | fall_evt_schema | 所有事件源 | bpchar | 1 |  | √ | '0' | 所有事件源 |
| 7 | ftrigger_type | 触发方案类型 | varchar | 100 |  | √ | ' ' | 触发方案类型,枚举: isc_data_copy_trigger :启动方案 isc_mq_bill_data_pub :单据消息发布 isc_service_flow :服务流程 isc_call_api_by_evt :API任务（事件触发） |
| 8 | fevents | 事件 | varchar | 1024 |  | √ | ' ' | 事件 |
| 9 | fevt_schema_type | 事件源类型 | varchar | 100 |  | √ | ' ' | 事件源类型,枚举: isc_data_source :数据源 isc_data_copy_trigger :启动方案 isc_service_flow :服务流程 isc_user_defined_event :集成云自定义事件 |
| 10 | fevt_schema | 事件源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_res_evt_bnd |  | fid |
| 2 | idx_res_bnd_tm |  | fcreate_time |
| 3 | idx_res_bnd_trg |  | ftrigger,ftrigger_type |
| 4 | idx_res_bnd_scem |  | fevt_schema,fevt_schema_type |
