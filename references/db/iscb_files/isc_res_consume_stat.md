# 脚本及值转换耗时统计-isc_res_consume_stat

## 脚本及值转换耗时统计-主表 t_isc_res_consume_stat

- **表名称：** 脚本及值转换耗时统计-主表
- **表名：** t_isc_res_consume_stat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注信息 | varchar | 400 |  | √ | ' ' | 备注信息 |
| 3 | fres_type | 资源类别 | varchar | 60 |  | √ | ' ' | 资源类别,枚举: isc_data_copy :数据集成方案 isc_service_flow :服务流程 isc_value_conver_rule :值转换规则 isc_apic_script :自定义API |
| 4 | ftotal_consume_time | 调用总耗时（毫秒） | int8 | 64 |  | √ | 0 | 调用总耗时（毫秒） |
| 5 | favg_consume_time | 执行平均耗时（毫秒） | int4 | 32 |  | √ | 0 | 执行平均耗时（毫秒） |
| 6 | ftotal_invoke_count | 调用总次数 | int4 | 32 |  | √ | 0 | 调用总次数 |
| 7 | frecord_time | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |
| 8 | fres_number | 资源编码 | varchar | 150 |  | √ | ' ' | 资源编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_res_consume_stat_r |  | frecord_time |
| 2 | pk_t_isc_res_consume_stat |  | fid |
