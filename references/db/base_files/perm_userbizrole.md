# 用户业务角色关系-perm_userbizrole

## 用户业务角色关系-主表 t_perm_userbizrole

- **表名称：** 用户业务角色关系-主表
- **表名：** t_perm_userbizrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ffromtypedesc | 来源描述 | varchar | 255 |  |  | ' ' | 来源描述 |
| 9 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色 perm_busirole](../base_files/perm_busirole.md) |
| 10 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_userbizrole_pkey |  | fid |
| 2 | idx_bizroleid_userid |  | fbizroleid,fuserid |
