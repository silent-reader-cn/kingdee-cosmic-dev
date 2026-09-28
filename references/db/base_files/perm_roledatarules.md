# 角色数据规则（废弃）-perm_roledatarules

## 角色数据规则（废弃）-主表 t_perm_roledatarules

- **表名称：** 角色数据规则（废弃）-主表
- **表名：** t_perm_roledatarules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | froleid | 角色 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisupdate | fisupdate | bpchar | 1 |  | √ | '0' |  |
| 7 | fdatarulesid | 数据规则方案集合 | int8 | 64 |  | √ | 0 | [数据规则方案集合 perm_datarules](../base_files/perm_datarules.md) |
| 8 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 9 | fupdatorid | fupdatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_roledatarules_pkey |  | fid |
| 2 | idx_perm_roledatarules |  | froleid |
