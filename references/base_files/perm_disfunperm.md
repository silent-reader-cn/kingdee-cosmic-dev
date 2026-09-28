# 禁用功能权限-perm_disfunperm

## 禁用功能权限-主表 t_perm_disfunperm

- **表名称：** 禁用功能权限-主表
- **表名：** t_perm_disfunperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdimtype | 权限维度类型 | varchar | 30 |  | √ | ' ' | 权限维度类型 |
| 5 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | 权限项 perm_permitem |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 8 | fentryid | 分录 | varchar | 18 |  | √ | ' ' | 分录 |
| 9 | ffrom | 来源 | int8 | 64 |  | √ | 0 | 来源 |
| 10 | fsource | 来源 | varchar | 10 |  | √ | '1' | 来源,枚举: 1 :直接分配 2 :通用角色 3 :业务角色 |
| 11 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色（废弃） perm_bizrole |
| 12 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_disfunperm_pkey |  | fid |
| 2 | idx_perm_disfunperm |  | fuserid,forgid,fbizappid,fentitytypeid,fpermitemid |
