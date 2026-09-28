# 用户业务角色关系-perm_userbizrole

## 用户业务角色关系-主表 t_perm_userbizrole

- **表名称：** 用户业务角色关系-主表
- **表名：** t_perm_userbizrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | fcreaterfield | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatedatefield | fcreatedatefield | timestamp | 0 |  |  | null |  |
| 6 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 8 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 perm_busirole |
| 9 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_userbizrole_pkey |  | fid |
| 2 | idx_perm_userbizrole_ur |  | fuserid,fbizroleid |
| 3 | idx_bizroleid_userid |  | fbizroleid,fuserid |
