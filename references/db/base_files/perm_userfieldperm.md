# 用户字段权限-perm_userfieldperm

## 用户字段权限-主表 t_perm_userfieldperm

- **表名称：** 用户字段权限-主表
- **表名：** t_perm_userfieldperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdimtype | 隔离维度 | varchar | 30 |  | √ | ' ' | 隔离维度 |
| 5 | ffieldpermid | 字段权限 | varchar | 18 |  | √ | ' ' | [字段权限 perm_fieldperm](../base_files/perm_fieldperm.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000004 |  | fuserid |
| 2 | t_perm_userfieldperm_pkey |  | fid |
