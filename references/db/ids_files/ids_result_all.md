# 智能销售预测-预测数据-ids_result_all

## 智能销售预测-预测数据-主表 t_ids_result

- **表名称：** 智能销售预测-预测数据-主表
- **表名：** t_ids_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeptid | fdept_id | varchar | 100 |  | √ | ' ' | fdept_id |
| 3 | facqtime | acq_time | varchar | 50 |  | √ | ' ' | acq_time |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forg_id | varchar | 100 |  | √ | ' ' | forg_id |
| 6 | fsubserviceid | sub_service_id | varchar | 100 |  | √ | ' ' | sub_service_id |
| 7 | fmodelid | model_id | varchar | 100 |  | √ | ' ' | model_id |
| 8 | fdata_tag | data_详情 | text | 0 |  |  | null | data_详情 |
| 9 | fmodtime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | app_id | varchar | 50 |  | √ | ' ' | app_id |
| 11 | fisenable | is_enable | bpchar | 1 |  | √ | '0' | is_enable |
| 12 | fdata | data | varchar | 255 |  | √ | ' ' | data |
| 13 | fstoreid | fstore_id | varchar | 100 |  | √ | ' ' | fstore_id |
| 14 | fcustomerid | fcustomer_id | varchar | 100 |  | √ | ' ' | fcustomer_id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_result |  | fid |
| 2 | idx_ids_modelid |  | fmodelid |
