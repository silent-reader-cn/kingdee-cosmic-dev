# Eas网址-task_easurl

## Eas网址-主表 t_tk_easurl

- **表名称：** Eas网址-主表
- **表名：** t_tk_easurl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feassystermip | eas系统IP | varchar | 255 |  |  | ' ' | eas系统IP |
| 3 | fltpatoken | LtpaToken | varchar | 255 |  |  | ' ' | LtpaToken |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_easurl_pkey |  | fid |
