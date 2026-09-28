# 角色字段权限-perm_rolefieldperm

## 角色字段权限-主表 t_perm_rolefieldperm

- **表名称：** 角色字段权限-主表
- **表名：** t_perm_rolefieldperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | froleid | 角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | ffieldpermid | 字段权限 | varchar | 18 |  | √ | ' ' | [字段权限 perm_fieldperm](../base_files/perm_fieldperm.md) |
| 4 | finheritmode | 角色权限继承策略 | varchar | 10 |  | √ | '10' | 角色权限继承策略,枚举: 10 :私有 20 :公有 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_rolefieldperm_pkey |  | fid |
| 2 | ix_perm_00000005 |  | froleid |
