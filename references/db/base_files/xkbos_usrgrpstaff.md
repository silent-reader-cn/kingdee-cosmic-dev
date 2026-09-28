# 用户组职员关系-xkbos_usrgrpstaff

## 用户组职员关系-主表 t_sec_usergroupstaff

- **表名称：** 用户组职员关系-主表
- **表名：** t_sec_usergroupstaff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | fusergroupid | 人员分组 | int8 | 64 |  | √ | 0 | [用户组 bos_usrgrp](../base_files/bos_usrgrp.md) |
| 6 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fusertype | fusertype | varchar | 10 |  | √ | ' ' |  |
| 8 | ffrom_type | 来源类型 | varchar | 1 |  | √ | '0' | 来源类型,枚举: 0 :手动添加 1 :用户组同步 |
| 9 | ffromtypedesc | ffromtypedesc | varchar | 255 |  |  | ' ' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sec_usergroupstaff |  | fuserid,fusergroupid |
| 2 | t_sec_usergroupstaff_pkey |  | fid |
