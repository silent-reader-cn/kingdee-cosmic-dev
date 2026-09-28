# 角色功能权限-perm_roleperm

## 功能权限-子表 t_perm_rolepermdetial

- **表名称：** 功能权限-子表
- **表名：** t_perm_rolepermdetial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | froleid | 通用角色id | varchar | 18 |  | √ | ' ' | 通用角色id |
| 3 | fpermitemid | 权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 4 | finheritmode | 权限继承策略 | varchar | 10 |  | √ | ' ' | 权限继承策略 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcontrolmode | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 10 :有权 20 :禁用 |
| 7 | fentitytypeid | 业务对象编码 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fentryid | fentryid | varchar | 18 |  | √ | ' ' | id |
| 9 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000017 |  | fid |
| 2 | t_perm_rolepermdetial_pkey |  | fentryid |
| 3 | idx_roleperm_roleid |  | froleid |
| 4 | idx_perm_rolepermdetial_item |  | fbizappid,fentitytypeid,fpermitemid |

---

## 角色功能权限-多语言表 t_perm_roleperm_l

- **表名称：** 角色功能权限-多语言表
- **表名：** t_perm_roleperm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_roleperm_l_pkey |  | fpkid |
| 2 | idx_perm_roleperm_l |  | fid,flocaleid |

---

## 角色功能权限-主表 t_perm_roleperm

- **表名称：** 角色功能权限-主表
- **表名：** t_perm_roleperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | varchar | 18 |  | √ | ' ' | 主数据内码 |
| 6 | froleid | 角色编码 | varchar | 18 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_00000016 |  | froleid |
| 2 | t_perm_roleperm_pkey |  | fid |
