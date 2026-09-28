# 角色数据规则迁移-xkperm_roledr_migration

## 角色数据规则迁移-主表 t_xkperm_roledr_migration

- **表名称：** 角色数据规则迁移-主表
- **表名：** t_xkperm_roledr_migration

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | froleid | 角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpermitemid | 权限项 | varchar | 36 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 4 | fbdobjecttypeid | 基础资料业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fdataruleid | 数据规则方案 | int8 | 64 |  | √ | 0 | [数据规则方案 perm_datarule](../base_files/perm_datarule.md) |
| 6 | fobjecttypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_roledr_migration |  | fid |
| 2 | idx_xkperm_roledr_migration |  | fdataruleid,froleid |
