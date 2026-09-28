# 别名映射表-bos_cbs_shard_name_map

## 别名映射表-主表 t_cbs_shard_name_map

- **表名称：** 别名映射表-主表
- **表名：** t_cbs_shard_name_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftable_name | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | falias_name | 映射别名 | varchar | 50 |  | √ | ' ' | 映射别名 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foriginal_name | 原始名 | varchar | 50 |  | √ | ' ' | 原始名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_shard_name_map |  | fid |
| 2 | idx_cbs_shard_name_map |  | ftable_name |
