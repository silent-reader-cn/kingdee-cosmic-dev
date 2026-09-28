# 用户-字段权限方案关系-perm_userfieldscheme

## 用户-字段权限方案关系-主表 t_perm_userfieldscheme

- **表名称：** 用户-字段权限方案关系-主表
- **表名：** t_perm_userfieldscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | [权限控制类型 perm_ctrltype](../base_files/perm_ctrltype.md) |
| 6 | fentnum | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ffieldpermschemeid | 字段权限方案 | int8 | 64 |  | √ | 0 | [属性/明细字段权限方案 perm_fieldscheme](../base_files/perm_fieldscheme.md) |
| 9 | fdimid | 权限控制类型记录id | int8 | 64 |  | √ | 0 | 权限控制类型记录id |
| 10 | fincludesub | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 11 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pufs_userappent |  | fuserid,fappid,fentnum |
| 2 | pk_t_perm_userfieldscheme |  | fid |
