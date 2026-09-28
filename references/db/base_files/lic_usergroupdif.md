# 用户许可分组变更-lic_usergroupdif

## 用户许可分组变更-主表 t_lic_userlicensegroupdif

- **表名称：** 用户许可分组变更-主表
- **表名：** t_lic_userlicensegroupdif

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fuid | 云之家ID | int8 | 64 |  | √ | 0 | 云之家ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_userlicensegroupdif_u |  | fuserid |
| 2 | t_lic_userlicensegroupdif_pkey |  | fid |
