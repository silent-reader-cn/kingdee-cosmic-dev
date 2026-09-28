# 用户组和业务角色的关系-perm_usrgrpbusirole

## 用户组和业务角色的关系-主表 t_perm_usrgrpbizrole

- **表名称：** 用户组和业务角色的关系-主表
- **表名：** t_perm_usrgrpbizrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusrgrpid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 bos_usergroup |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 perm_busirole |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_usrgrpbizrole |  | fid |
| 2 | idx_perm_usrgrpbr |  | fusrgrpid |
