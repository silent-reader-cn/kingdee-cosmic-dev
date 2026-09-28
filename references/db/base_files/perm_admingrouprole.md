# 管理员组通用角色范围-perm_admingrouprole

## 管理员组通用角色范围-主表 t_perm_admingrouprole

- **表名称：** 管理员组通用角色范围-主表
- **表名：** t_perm_admingrouprole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fismodifiable | 是否可修改 | bpchar | 1 |  | √ | '0' | 是否可修改 |
| 3 | froleid | 通用角色 | varchar | 19 |  | √ | ' ' | 通用角色 perm_role |
| 4 | fadmingroupid | 管理员分组 | int8 | 64 |  | √ | 0 | 管理员分组 perm_admingroup |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_admingrouprole |  | fid |
| 2 | idx_perm_admgrprole_grpid |  | fadmingroupid |
| 3 | idx_perm_admgrprole_roleid |  | froleid |
