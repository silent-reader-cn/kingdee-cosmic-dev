# 禁用功能权限_多类别-perm_disfunperm_multype

## 禁用功能权限_多类别-主表 t_perm_disfunperm

- **表名称：** 禁用功能权限_多类别-主表
- **表名：** t_perm_disfunperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 4 | forgid | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 5 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fsource | 来源 | varchar | 10 |  | √ | '1' | 来源,枚举: 1 :直接分配 2 :通用角色 3 :业务角色 |
| 9 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fdimtype | 权限维度类型 | varchar | 30 |  | √ | ' ' | 权限维度类型 |
| 14 | fentryid | 分录 | varchar | 18 |  | √ | ' ' | 分录 |
| 15 | ffrom | 来源 | int8 | 64 |  | √ | 0 | 来源 |
| 16 | ffromtypedesc | ffromtypedesc | varchar | 255 |  |  | ' ' |  |
| 17 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色（废弃） perm_bizrole](../base_files/perm_bizrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_disfunperm_pkey |  | fid |
| 2 | idx_perm_disfunperm |  | fuserid,forgid,fbizappid,fentitytypeid,fpermitemid |
