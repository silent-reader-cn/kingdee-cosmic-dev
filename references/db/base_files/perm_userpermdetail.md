# 用户功能权限明细-perm_userpermdetail

## 用户功能权限明细-主表 t_perm_userpermdetail

- **表名称：** 用户功能权限明细-主表
- **表名：** t_perm_userpermdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 用户授权方案 | varchar | 19 |  | √ | ' ' | [用户功能权限 perm_userperm](../base_files/perm_userperm.md) |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisincludesub | 分配组织及下级 | bpchar | 1 |  | √ | '0' | 分配组织及下级 |
| 8 | fcontrolmode | fcontrolmode | varchar | 10 |  | √ | ' ' |  |
| 9 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 10 | fsource | fsource | varchar | 10 |  | √ | '1' |  |
| 11 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型,枚举: bos_org :组织 |
| 15 | fentryid | fentryid | varchar | 19 |  | √ | ' ' | id |
| 16 | fdimid | 权限控制对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | ffromtypedesc | 来源描述 | varchar | 255 |  |  | ' ' | 来源描述 |
| 18 | fbizroleid | fbizroleid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_upd_appid |  | fbizappid |
| 2 | idx_upd |  | fuserid,fbizappid,fentitytypeid,fpermitemid,fdimid |
| 3 | t_perm_userpermdetail_pkey |  | fentryid |
| 4 | idx_userpermdfid |  | fid |
| 5 | idx_userpermdetail_entperm |  | fentitytypeid,fpermitemid |
