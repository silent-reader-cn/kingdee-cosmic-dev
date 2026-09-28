# 用户数据权限-perm_userdataperm

## 用户数据权限-主表 t_perm_userdataperm

- **表名称：** 用户数据权限-主表
- **表名：** t_perm_userdataperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 3 | fisupdate | fisupdate | bpchar | 1 |  | √ | '0' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | fdimtype | 隔离维度 | varchar | 30 |  | √ | ' ' | 隔离维度 |
| 6 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户 |
| 8 | fupdatorid | fupdatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fdatapermid | 数据权限 | varchar | 18 |  | √ | ' ' | 数据权限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_userdataperm_pkey |  | fid |
| 2 | ix_perm_00000003 |  | fuserid |
