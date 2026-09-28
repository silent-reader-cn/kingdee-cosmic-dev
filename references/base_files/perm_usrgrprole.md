# 用户组角色关系-多类别-perm_usrgrprole

## 用户组角色关系-多类别-主表 t_perm_usrgrprole

- **表名称：** 用户组角色关系-多类别-主表
- **表名：** t_perm_usrgrprole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusrgrpid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 bos_usrgrp |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | froleid | 角色 | varchar | 19 |  | √ | ' ' | 通用角色 perm_role |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdimtype | 隔离维度类型 | varchar | 30 |  | √ | ' ' | 隔离维度类型,枚举: bos_org :业务单元 |
| 8 | fendtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fdimid | 隔离维度 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fincludesub | 包含下级隔离维度 | bpchar | 1 |  | √ | '0' | 包含下级隔离维度 |
| 11 | fstarttime | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_usrgrpr |  | fusrgrpid,fdimid,froleid |
| 2 | pk_t_perm_usrgrprole |  | fid |
