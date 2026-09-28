# 测试分表单据-isc_kdb_table

## 测试分表单据-主表 t_isc_kdb_table

- **表名称：** 测试分表单据-主表
- **表名：** t_isc_kdb_table

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcreatetieme | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_isc_kdb_table |  | fnumber |
| 2 | pk_t_isc_kdb_table |  | fid |
