# 值转换结果缓存-isc_value_convert_cache

## 值转换结果缓存-主表 t_iscb_value_conv_cache

- **表名称：** 值转换结果缓存-主表
- **表名：** t_iscb_value_conv_cache

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconvert_rule | 值转换规则 | int8 | 64 |  | √ | 0 | 值转换规则 isc_value_conver_rule |
| 3 | fsrc | 源单值 | varchar | 200 |  | √ | ' ' | 源单值 |
| 4 | ftar | 目标值 | varchar | 200 |  | √ | ' ' | 目标值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_value_conv_cache |  | fconvert_rule,fsrc |
| 2 | t_iscb_value_conv_cache_pkey |  | fid |
