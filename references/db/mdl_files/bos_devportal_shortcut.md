# 常用业务-bos_devportal_shortcut

## 常用业务-主表 t_dev_shortcut

- **表名称：** 常用业务-主表
- **表名：** t_dev_shortcut

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizpageid | 业务页面 | varchar | 36 |  | √ | ' ' | 业务页面 |
| 3 | fuserid | 当前用户 | int8 | 64 |  | √ | 0 | 当前用户 |
| 4 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_shortcut_num |  | fuserid |
| 2 | t_dev_shortcut_pkey |  | fid |
