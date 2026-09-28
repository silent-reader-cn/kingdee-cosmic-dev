# 表单信息别名-bos_nc_forminfo_alias

## 表单信息别名-主表 t_nocode_forminfo_alias

- **表名称：** 表单信息别名-主表
- **表名：** t_nocode_forminfo_alias

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型(字段0，表单1) | varchar | 50 |  | √ | ' ' | 类型(字段0，表单1) |
| 3 | ffieldalias | ffieldalias | varchar | 50 |  | √ | ' ' |  |
| 4 | fmodelid | fmodelid | varchar | 50 |  | √ | ' ' |  |
| 5 | fentitynumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 6 | fsource | 源值 | varchar | 50 |  | √ | ' ' | 源值 |
| 7 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 8 | ffieldkey | ffieldkey | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_fia_en |  | fentitynumber |
| 2 | pk_nc_forminfo_alias |  | fid |
