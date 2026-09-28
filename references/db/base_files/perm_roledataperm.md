# 角色数据规则-perm_roledataperm

## 角色数据规则-主表 t_perm_roledataperm

- **表名称：** 角色数据规则-主表
- **表名：** t_perm_roledataperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | froleid | 角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fisupdate | 是否升级成功 | bpchar | 1 |  | √ | '0' | 是否升级成功 |
| 4 | fupdatetime | 升级时间 | timestamp | 0 |  |  | null | 升级时间 |
| 5 | fupdatorid | 升级人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdatapermid | 数据权限id | varchar | 18 |  | √ | ' ' | [数据权限 perm_dataperm](../base_files/perm_dataperm.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000002 |  | froleid |
| 2 | t_perm_roledataperm_pkey |  | fid |
