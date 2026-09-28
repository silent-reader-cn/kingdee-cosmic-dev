# 用户直接禁权-perm_direct_disperm

## 用户直接禁权-主表 t_perm_disfunperm

- **表名称：** 用户直接禁权-主表
- **表名：** t_perm_disfunperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 权限控制对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fsource | fsource | varchar | 10 |  | √ | '1' |  |
| 9 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fisincludesuborg | 分配组织及下级 | bpchar | 1 |  | √ | '0' | 分配组织及下级 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型,枚举: bos_org :组织 |
| 14 | fentryid | fentryid | varchar | 18 |  | √ | ' ' |  |
| 15 | ffrom | ffrom | int8 | 64 |  | √ | 0 |  |
| 16 | ffromtypedesc | 来源描述 | varchar | 255 |  |  | ' ' | 来源描述 |
| 17 | fbizroleid | fbizroleid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_disfunperm_pkey |  | fid |
| 2 | idx_perm_disfunperm |  | fuserid,forgid,fbizappid,fentitytypeid,fpermitemid |
