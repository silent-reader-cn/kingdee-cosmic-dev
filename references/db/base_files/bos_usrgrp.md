# 用户组-bos_usrgrp

## 用户组-主表 t_sec_usergroup

- **表名称：** 用户组-主表
- **表名：** t_sec_usergroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | fisleaf | bpchar | 1 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffullname | ffullname | varchar | 500 |  | √ | ' ' |  |
| 8 | flongnumber | flongnumber | varchar | 255 |  | √ | ' ' |  |
| 9 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 10 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 11 | fusrgrpstdid | 用户组分类 | int8 | 64 |  | √ | '1404221671421785088' | [用户组分类 perm_usergroupstandard](../base_files/perm_usergroupstandard.md) |
| 12 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fusergrouptypeid | 用户组类型 | int8 | 64 |  | √ | 0 | [用户组类型 bos_usergrouptype](../base_files/bos_usergrouptype.md) |
| 15 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 16 | fstatus | fstatus | varchar | 50 |  | √ | 'C' |  |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fseted_usrsycrule | 是否设置用户同步规则 | bpchar | 1 |  | √ | '0' | 是否设置用户同步规则 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_usergroup_pkey |  | fid |
| 2 | idx_t_sec_usergroup_num |  | fnumber |

---

## 用户组-多语言表 t_sec_usergroup_l

- **表名称：** 用户组-多语言表
- **表名：** t_sec_usergroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 500 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sec_usergroup_l_pkey |  | fpkid |
| 2 | idx_t_sec_usergroup_l_fid |  | fid |
