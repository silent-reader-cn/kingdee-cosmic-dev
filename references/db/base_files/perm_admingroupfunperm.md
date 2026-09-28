# 管理员组功能权限-perm_admingroupfunperm

## 管理员组功能权限-主表 t_perm_admingroupfunperm

- **表名称：** 管理员组功能权限-主表
- **表名：** t_perm_admingroupfunperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitynum | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fusergroupid | 管理员分组 | int8 | 64 |  | √ | 0 | [管理员分组 perm_admingroup](../base_files/perm_admingroup.md) |
| 4 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 5 | fappid | 应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_admingrpfunperm |  | fappid,fentitynum,fpermitemid |
| 2 | pk_t_perm_admingroupfunperm |  | fid |
| 3 | idx_perm_admingrpfunperm_grp |  | fusergroupid |
