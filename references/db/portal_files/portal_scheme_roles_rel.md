# 方案与角色关系-portal_scheme_roles_rel

## 方案与角色关系-主表 t_bas_rolesmainpage

- **表名称：** 方案与角色关系-主表
- **表名：** t_bas_rolesmainpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | froleid | 角色 | varchar | 250 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | [首页方案 portal_scheme](../portal_files/portal_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_roles_froleid |  | froleid |
| 2 | idx_roles_fschemeid |  | fschemeid |
| 3 | pk_bas_rolesmainpage |  | fid |
