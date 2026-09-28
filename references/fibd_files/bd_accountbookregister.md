# 账簿注册-bd_accountbookregister

## 账簿注册-主表 t_bd_accountbookregister

- **表名称：** 账簿注册-主表
- **表名：** t_bd_accountbookregister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizapp | 应用 | varchar | 30 |  | √ | ' ' | 应用 |
| 3 | fbooktypefieldid | 账簿类型字段标识 | varchar | 30 |  | √ | ' ' | 账簿类型字段标识 |
| 4 | fformid | 账簿表单标识 | varchar | 30 |  | √ | ' ' | 账簿表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbookregister_pkey |  | fid |
| 2 | idx_bd_accountbookregister |  | fbizapp |
