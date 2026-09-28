# 管理员用户组额外管辖用户-perm_admingroupadduser

## 管理员用户组额外管辖用户-主表 t_perm_admingroupadduser

- **表名称：** 管理员用户组额外管辖用户-主表
- **表名：** t_perm_admingroupadduser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusergroupid | 管理员分组 | int8 | 64 |  | √ | 0 | [管理员分组 perm_admingroup](../base_files/perm_admingroup.md) |
| 3 | fuserid | 额外用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_admingroupadduser |  | fid |
| 2 | idx_perm_admingrpadduser |  | fuserid,fusergroupid |
