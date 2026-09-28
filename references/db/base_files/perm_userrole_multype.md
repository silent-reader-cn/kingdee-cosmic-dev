# 用户角色关系-多类别-perm_userrole_multype

## 用户角色关系-多类别-主表 t_perm_userrole

- **表名称：** 用户角色关系-多类别-主表
- **表名：** t_perm_userrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | froleid | 通用角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | forgid | 权限控制对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource | 来源 | varchar | 10 |  | √ | '2' | 来源,枚举: 1 :直接分配 2 :通用角色 3 :业务角色 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 9 | fisincludesuborg | 分配组织及下级 | bpchar | 1 |  | √ | '0' | 分配组织及下级 |
| 10 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型,枚举: bos_org :组织 |
| 13 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 14 | ffromtypedesc | 来源描述 | varchar | 255 |  |  | ' ' | 来源描述 |
| 15 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色（废弃） perm_bizrole](../base_files/perm_bizrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_userrole |  | fuserid,froleid |
| 2 | idx_perm_ur |  | froleid,fdimtype,fisincludesuborg,fuserid,forgid |
| 3 | pk_perm_userrole |  | fid |
