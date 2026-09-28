# 执行统计（废弃）-isc_statistics

## 执行统计（废弃）-主表 t_isc_statistics

- **表名称：** 执行统计（废弃）-主表
- **表名：** t_isc_statistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecute_count | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 3 | fsuccess_count | 成功行数 | int8 | 64 |  | √ | 0 | 成功行数 |
| 4 | fread_bytes | 读取数据流量（字节） | int8 | 64 |  | √ | 0 | 读取数据流量（字节） |
| 5 | ftotal_count | 总行数 | int8 | 64 |  | √ | 0 | 总行数 |
| 6 | fday | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fschema_name | 集成方案名称 | varchar | 100 |  | √ | ' ' | 集成方案名称 |
| 8 | fload_bytes | 加载数据流量（字节） | int8 | 64 |  | √ | 0 | 加载数据流量（字节） |
| 9 | ftotal_bytes | 总数据流量（字节） | int8 | 64 |  | √ | 0 | 总数据流量（字节） |
| 10 | fschema_number | 集成方案编码 | varchar | 100 |  | √ | ' ' | 集成方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_statistics_t |  | fschema_number |
| 2 | t_isc_statistics_pkey |  | fid |
