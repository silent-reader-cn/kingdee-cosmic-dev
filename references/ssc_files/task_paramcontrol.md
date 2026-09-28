# 共享参数管理-task_paramcontrol

## 共享参数管理-主表 t_tk_paramcontrol

- **表名称：** 共享参数管理-主表
- **表名：** t_tk_paramcontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 1000 |  | √ | ' ' | 参数值 |
| 3 | fparamname | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | fnumber | 参数编码 | varchar | 1000 |  | √ | ' ' | 参数编码 |
| 5 | fdescription | 参数说明 | varchar | 300 |  | √ | ' ' | 参数说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_paramcontrol_pkey |  | fid |
| 2 | index_ssc_paramcontrol |  | fparamname |
