# 模板用户权限-bos_nocode_tpl_user

## 模板用户权限-主表 t_nocode_tpl_userauth

- **表名称：** 模板用户权限-主表
- **表名：** t_nocode_tpl_userauth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplateid | 模板ID | int8 | 64 |  | √ | 0 | 模板ID |
| 3 | fuserid | 被授权用户 | int8 | 64 |  | √ | 0 | 被授权用户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_tu_tmpid |  | ftemplateid |
| 2 | pk_nocode_tpl_userauth |  | fid |
