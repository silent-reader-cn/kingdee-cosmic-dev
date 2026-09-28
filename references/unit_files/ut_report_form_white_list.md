# 测试统计表单白名单-ut_report_form_white_list

## 测试统计表单白名单-主表 t_ut_white_list

- **表名称：** 测试统计表单白名单-主表
- **表名：** t_ut_white_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 表单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ut_white_list_fnumber |  | fnumber |
| 2 | t_ut_white_list_pkey |  | fid |
