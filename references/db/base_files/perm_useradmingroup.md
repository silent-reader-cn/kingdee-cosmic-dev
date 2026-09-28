# 用户管理员组关系-perm_useradmingroup

## 用户管理员组关系-主表 t_perm_useradmingroup

- **表名称：** 用户管理员组关系-主表
- **表名：** t_perm_useradmingroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fadmingroupid | 管理员分组 | int8 | 64 |  | √ | 0 | [管理员分组 perm_admingroup](../base_files/perm_admingroup.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_useradmingroup |  | fid |
| 2 | idx_perm_useradmingroup |  | fadmingroupid |
