# 流程信息别名-bos_nc_wfinfo_alias

## 流程信息别名-主表 t_nocode_wfinfo_alias

- **表名称：** 流程信息别名-主表
- **表名：** t_nocode_wfinfo_alias

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型(字段0，表单1) | varchar | 50 |  | √ | ' ' | 类型(字段0，表单1) |
| 3 | fmodelid | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 4 | fsource | 源值 | varchar | 50 |  | √ | ' ' | 源值 |
| 5 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_wi_mi |  | fmodelid |
| 2 | pk_nc_wfinfo_alias |  | fid |
