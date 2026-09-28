# 全功能用户-perm_superuser

## 全功能用户-主表 t_perm_superuser

- **表名称：** 全功能用户-主表
- **表名：** t_perm_superuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fnumber1 | fnumber1 | varchar | 50 |  | √ | ' ' |  |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fadminid | fadminid | varchar | 18 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_superuser |  | fuserid,fadminid |
| 2 | t_perm_superuser_pkey |  | fid |
| 3 | idx_perm_superuser_user |  | fuserid |
