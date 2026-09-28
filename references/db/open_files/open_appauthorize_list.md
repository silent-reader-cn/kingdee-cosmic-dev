# 应用授权-open_appauthorize_list

## 应用授权-主表 t_open_appauthorize

- **表名称：** 应用授权-主表
- **表名：** t_open_appauthorize

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizapp | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fisforbidden | 禁止访问 | bpchar | 1 |  | √ | '0' | 禁止访问 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_appauthorize_fbizapp |  | fbizapp |
| 2 | t_open_appauthorize_pkey |  | fid |
