# 用户功能权限-多类别-perm_userperm_multype

## 用户功能权限-多类别-主表 t_perm_userperm

- **表名称：** 用户功能权限-多类别-主表
- **表名：** t_perm_userperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 19 |  | √ | ' ' | id |
| 2 | fisincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |
| 3 | forgid | 隔离维度id | int8 | 64 |  | √ | 0 | 隔离维度id |
| 4 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型,枚举: DIM_ORG :业务单元 DIM_BCM_MODEL :合并报表的体系 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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

## 单据体-子表 t_perm_userpermdetail

- **表名称：** 单据体-子表
- **表名：** t_perm_userpermdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 19 |  | √ | ' ' |  |
| 2 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | 权限项 perm_permitem |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fuserid | fuserid | int8 | 64 |  | √ | 0 |  |
| 5 | fisincludesub | fisincludesub | bpchar | 1 |  | √ | '0' |  |
| 6 | fcontrolmode | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: |
| 7 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 8 | fsource | 来源 | varchar | 10 |  | √ | '1' | 来源,枚举: |
| 9 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fdimtype | fdimtype | varchar | 30 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | varchar | 19 |  | √ | ' ' | id |
| 12 | fdimid | fdimid | int8 | 64 |  | √ | 0 |  |
| 13 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色（废弃） perm_bizrole |

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
