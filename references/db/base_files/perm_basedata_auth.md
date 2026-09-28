# 基础资料联动控制-perm_basedata_auth

## 应用用户-多选基础资料表 t_xkperm_bd_auth_users

- **表名称：** 应用用户-多选基础资料表
- **表名：** t_xkperm_bd_auth_users

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bd_auth_users |  | fpkid |
| 2 | idx_xkperm_bd_auth_users_fk |  | fentryid |

---

## 通用角色-多选基础资料表 t_xkperm_bdauth_comrole

- **表名称：** 通用角色-多选基础资料表
- **表名：** t_xkperm_bdauth_comrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bdauth_comrole |  | fpkid |
| 2 | idx_xkperm_bdauth_comrole_id |  | fid,fbasedataid |

---

## 例外用户-多选基础资料表 t_xkperm_bd_auth_excusers

- **表名称：** 例外用户-多选基础资料表
- **表名：** t_xkperm_bd_auth_excusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_bd_auth_excusers_fk |  | fentryid |
| 2 | pk_xkperm_bd_auth_excusers |  | fpkid |

---

## 受控字段-多选基础资料表 t_xkperm_bd_auth_fields

- **表名称：** 受控字段-多选基础资料表
- **表名：** t_xkperm_bd_auth_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | null | [业务单据关联基础资字段 perm_bdauth_field](../xkbase_files/perm_bdauth_field.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bd_auth_fields |  | fpkid |
| 2 | idx_xkperm_bd_auth_fields_fk |  | fentryid |

---

## 例外角色-多选基础资料表 t_xkperm_bd_auth_excroles

- **表名称：** 例外角色-多选基础资料表
- **表名：** t_xkperm_bd_auth_excroles

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | [通用角色 perm_role](../base_files/perm_role.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_bd_auth_excroles_fk |  | fentryid |
| 2 | pk_xkperm_bd_auth_excroles |  | fpkid |

---

## 通用用户-多选基础资料表 t_xkperm_bdauth_comuser

- **表名称：** 通用用户-多选基础资料表
- **表名：** t_xkperm_bdauth_comuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_bdauth_comuse_id |  | fid,fbasedataid |
| 2 | pk_xkperm_bdauth_comuser |  | fpkid |

---

## 单据体-子表 t_xkperm_bd_auth_entry

- **表名称：** 单据体-子表
- **表名：** t_xkperm_bd_auth_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbizobjecttypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbizappid | 应用 | varchar | 36 |  |  | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bd_auth_entry |  | fentryid |
| 2 | idx_xkperm_bd_auth_entry_fid |  | fid,fentryid |

---

## 应用角色-多选基础资料表 t_xkperm_bd_auth_roles

- **表名称：** 应用角色-多选基础资料表
- **表名：** t_xkperm_bd_auth_roles

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | [通用角色 perm_role](../base_files/perm_role.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bd_auth_roles |  | fpkid |
| 2 | idx_xkperm_bd_auth_roles_fk |  | fentryid |

---

## 通用例外角色-多选基础资料表 t_xkperm_bdauth_excomrole

- **表名称：** 通用例外角色-多选基础资料表
- **表名：** t_xkperm_bdauth_excomrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bdauth_excomrole |  | fpkid |
| 2 | idx_xkperm_bdauth_excomrole_id |  | fid,fbasedataid |

---

## 通用例外用户-多选基础资料表 t_xkperm_bdauth_excomuser

- **表名称：** 通用例外用户-多选基础资料表
- **表名：** t_xkperm_bdauth_excomuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bdauth_excomuser |  | fpkid |
| 2 | idx_xkperm_bdauth_excomuse_id |  | fid,fbasedataid |

---

## 受控权限项-多选基础资料表 t_xkperm_bd_auth_perms

- **表名称：** 受控权限项-多选基础资料表
- **表名：** t_xkperm_bd_auth_perms

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | null | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkperm_bd_auth_perms |  | fpkid |
| 2 | idx_xkperm_bd_auth_perms_fk |  | fentryid |

---

## 基础资料联动控制-主表 t_xkperm_bd_auth

- **表名称：** 基础资料联动控制-主表
- **表名：** t_xkperm_bd_auth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcontroltype | 联动控制方式 | bpchar | 1 |  | √ | ' ' | 联动控制方式,枚举: 0 :控制所有业务对象数据范围 1 :选择性控制业务对象数据范围 |
| 5 | fbdobjecttypeid | 基础资料 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 14 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用,枚举: 0 :否 1 :是 |
| 15 | fbdcloudid | 领域 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_bd_auth_bdtypeid |  | fbdobjecttypeid,fcontroltype |
| 2 | pk_xkperm_bd_auth |  | fid |

---

## 通用权限-多选基础资料表 t_xkperm_bd_auth_comperms

- **表名称：** 通用权限-多选基础资料表
- **表名：** t_xkperm_bd_auth_comperms

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkperm_bd_auth_cperms_fbdi |  | fbasedataid |
| 2 | pk_xkperm_bd_auth_comperms |  | fpkid |
