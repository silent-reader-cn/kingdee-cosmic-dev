# 字段属性-isc_data_properties

## 字段属性-主表 t_isc_dataproperty

- **表名称：** 字段属性-主表
- **表名：** t_isc_dataproperty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 所属表id | int8 | 64 |  | √ | 0 | 所属表id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flabel | flabel | varchar | 100 |  | √ | ' ' |  |
| 5 | findex | findex | varchar | 100 |  | √ | ' ' |  |
| 6 | fdata_schema | fdata_schema | varchar | 100 |  | √ | ' ' |  |
| 7 | fis_primary_key | 主键 | bpchar | 1 |  | √ | ' ' | 主键 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fis_encrypt | fis_encrypt | bpchar | 1 |  | √ | ' ' |  |
| 10 | fcustomize | fcustomize | bpchar | 1 |  | √ | ' ' |  |
| 11 | frequired | 必填 | bpchar | 1 |  | √ | ' ' | 必填 |
| 12 | fdata_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dataproperty_fk |  | fid |
| 2 | idx_isc_dataproperty_s |  | fdata_schema |
| 3 | t_isc_dataproperty_pkey |  | fentryid |
