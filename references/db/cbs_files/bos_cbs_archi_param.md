# 参数-bos_cbs_archi_param

## 参数-主表 t_cbs_archi_param

- **表名称：** 参数-主表
- **表名：** t_cbs_archi_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fdata | 参数数据 | text | 0 |  |  | null | 参数数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_param |  | ftype |
| 2 | pk_cbs_archi_param |  | fid |
