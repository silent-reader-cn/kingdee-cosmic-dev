# 表格引用关系-bos_nc_reftable

## 表格引用关系-主表 t_nc_reftable

- **表名称：** 表格引用关系-主表
- **表名：** t_nc_reftable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frefformid | 引用表单id | varchar | 50 |  | √ | ' ' | 引用表单id |
| 3 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reftable_frefformid |  | frefformid |
| 2 | idx_reftable_fformid |  | fformid |
| 3 | pk_t_nc_reftable |  | fid |
