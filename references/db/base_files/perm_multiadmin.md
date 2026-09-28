# 三员管理实体-perm_multiadmin

## 三员管理实体-主表 t_perm_multiadmin

- **表名称：** 三员管理实体-主表
- **表名：** t_perm_multiadmin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadminschemeid | 管理员权限控制策略id | int8 | 64 |  | √ | 0 | 管理员权限控制策略id |
| 3 | fadmintypeid | 虚拟管理员类型 | int8 | 64 |  | √ | 0 | [虚拟管理员类型 perm_admintype](../base_files/perm_admintype.md) |
| 4 | fenablepswstrategy | 密码策略维护 | bpchar | 1 |  | √ | ' ' | 密码策略维护 |
| 5 | fresetpswscopeid | 重置密码范围 | varchar | 50 |  | √ | ' ' | 重置密码范围 |
| 6 | funlockscopeid | 解锁范围 | varchar | 50 |  | √ | ' ' | 解锁范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_multiadmin |  | fadminschemeid |
| 2 | pk_t_perm_multiadmin |  | fid |
