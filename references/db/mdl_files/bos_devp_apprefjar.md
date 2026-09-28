# 应用jar包注册表-bos_devp_apprefjar

## 应用jar包注册表-主表 t_meta_apprefjar

- **表名称：** 应用jar包注册表-主表
- **表名：** t_meta_apprefjar

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjar | jar包 | varchar | 200 |  | √ | ' ' | jar包 |
| 3 | fbizappid | 应用id | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_apprefjar_pkey |  | fid |
| 2 | idx_kdp_apprefjar_bizappid |  | fbizappid |
