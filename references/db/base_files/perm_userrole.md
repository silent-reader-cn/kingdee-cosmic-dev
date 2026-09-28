# 用户和通用角色关系-perm_userrole

## 用户和通用角色关系-主表 t_perm_userrole

- **表名称：** 用户和通用角色关系-主表
- **表名：** t_perm_userrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | froleid | 角色 | varchar | 18 |  | √ | ' ' | 通用角色 perm_role |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatedatefield | fcreatedatefield | timestamp | 0 |  |  | null |  |
| 6 | fsource | 来源 | varchar | 10 |  | √ | '2' | 来源,枚举: 1 :直接分配 2 :通用角色 3 :业务角色 |
| 7 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 8 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 10 | fcreaterfield | fcreaterfield | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 12 | fdimtype | 权限维度类型 | varchar | 30 |  | √ | ' ' | 权限维度类型 |
| 13 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 14 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色（废弃） perm_bizrole |

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
