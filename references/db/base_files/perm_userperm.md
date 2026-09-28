# 用户功能权限-perm_userperm

## 用户功能权限-主表 t_perm_userperm

- **表名称：** 用户功能权限-主表
- **表名：** t_perm_userperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 19 |  | √ | ' ' | id |
| 2 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdimtype | 权限维度类型 | varchar | 30 |  | √ | ' ' | 权限维度类型,枚举: DIM_ORG :业务单元 DIM_BCM_MODEL :合并报表的体系 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000018 |  | fuserid,forgid,fdimtype,fisincludesuborg |
| 2 | t_perm_userperm_pkey |  | fid |

---

## 用户功能权限-子表 t_perm_userpermdetail

- **表名称：** 用户功能权限-子表
- **表名：** t_perm_userpermdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 19 |  | √ | ' ' |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 4 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisincludesub | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 8 | fcontrolmode | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 10 :有权 20 :禁止权 |
| 9 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 10 | fsource | 来源 | varchar | 10 |  | √ | '1' | 来源,枚举: 1 :直接分配 2 :通用角色 3 :业务角色 |
| 11 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型,枚举: bos_org :业务单元 |
| 15 | fentryid | fentryid | varchar | 19 |  | √ | ' ' | id |
| 16 | fdimid | 隔离维度id | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | ffromtypedesc | ffromtypedesc | varchar | 255 |  |  | ' ' |  |
| 18 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | [业务角色（废弃） perm_bizrole](../base_files/perm_bizrole.md) |

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
