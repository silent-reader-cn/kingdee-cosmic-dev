# 用户语言-mai_userlang

## 用户语言-主表 t_mai_userlang

- **表名称：** 用户语言-主表
- **表名：** t_mai_userlang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 语言名称 | varchar | 50 |  | √ | ' ' | 语言名称 |
| 3 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fnumber | 语言编码 | varchar | 50 |  | √ | ' ' | 语言编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_userlang_fuser |  | fuser |
| 2 | pk_t_mai_userlang |  | fid |
