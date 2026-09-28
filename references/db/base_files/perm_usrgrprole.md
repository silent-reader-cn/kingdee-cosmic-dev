# 用户组角色关系-多类别-perm_usrgrprole

## 用户组角色关系-多类别-主表 t_perm_usrgrprole

- **表名称：** 用户组角色关系-多类别-主表
- **表名：** t_perm_usrgrprole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | froleid | 通用角色 | varchar | 19 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fincludesub | 分配组织及下级 | bpchar | 1 |  | √ | '0' | 分配组织及下级 |
| 6 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fusrgrpid | 用户组 | int8 | 64 |  | √ | 0 | [用户组 bos_usrgrp](../base_files/bos_usrgrp.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdimtype | 权限控制类型 | varchar | 30 |  | √ | ' ' | 权限控制类型,枚举: bos_org :业务单元 |
| 11 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 12 | fdimid | 权限控制对象 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | ffromtypedesc | 来源描述 | varchar | 255 |  |  | ' ' | 来源描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_usrgrpr |  | fusrgrpid,fdimid,froleid |
| 2 | pk_t_perm_usrgrprole |  | fid |
