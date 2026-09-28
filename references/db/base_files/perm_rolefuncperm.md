# 通用角色功能权限-perm_rolefuncperm

## 通用角色功能权限-主表 t_perm_rolepermdetial

- **表名称：** 通用角色功能权限-主表
- **表名：** t_perm_rolepermdetial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | froleid | 通用角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 4 | finheritmode | finheritmode | varchar | 10 |  | √ | ' ' |  |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fcontrolmode | fcontrolmode | varchar | 10 |  | √ | ' ' |  |
| 7 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fentryid | fentryid | varchar | 18 |  | √ | ' ' | id |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000017 |  | fid |
| 2 | t_perm_rolepermdetial_pkey |  | fentryid |
| 3 | idx_roleperm_roleid |  | froleid |
| 4 | idx_perm_rolepermdetial_item |  | fbizappid,fentitytypeid,fpermitemid |
