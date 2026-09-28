# 例外角色-实体-perm_exceptrole

## 例外角色-实体-主表 t_perm_oprexrole

- **表名称：** 例外角色-实体-主表
- **表名：** t_perm_oprexrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | froleid | 角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | foperationruleobjid | 特殊操作权限分配对象 | varchar | 18 |  | √ | ' ' | [特殊操作权限分配对象 perm_operationruleobj](../base_files/perm_operationruleobj.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_oprexrole_pkey |  | fid |
| 2 | idx_perm_oprexrole |  | foperationruleobjid |
