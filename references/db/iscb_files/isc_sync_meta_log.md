# 元数据列表同步日志-isc_sync_meta_log

## 元数据列表同步日志-主表 t_isc_sync_meta_log

- **表名称：** 元数据列表同步日志-主表
- **表名：** t_isc_sync_meta_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmessage | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 6 | fmodify_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstate | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: S :成功 F :失败 T :提前终止 P :部分成功 R :执行中 |
| 8 | fsuccess_count | 成功数 | int8 | 64 |  | √ | 0 | 成功数 |
| 9 | fcost_time | 耗时 | varchar | 100 |  | √ | ' ' | 耗时 |
| 10 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftotal_count | 总数 | int8 | 64 |  | √ | 0 | 总数 |
| 12 | ffailed_count | 失败数 | int8 | 64 |  | √ | 0 | 失败数 |
| 13 | fmessage_tag | 错误日志_详情 | text | 0 |  |  | null | 错误日志_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_sync_meta_log_pkey |  | fid |
| 2 | idx_isc_sync_meta_log_0 |  | fstate |
