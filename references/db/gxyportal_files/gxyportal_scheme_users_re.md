# 方案与人员关系-gxyportal_scheme_users_re

## 方案与人员关系-主表 t_bas_usersmainpage

- **表名称：** 方案与人员关系-主表
- **表名：** t_bas_usersmainpage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemeid | 方案 | int8 | 64 |  | √ | 0 | [首页方案 gxyportal_scheme](../gxyportal_files/gxyportal_scheme.md) |
| 3 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_usersmainpage |  | fid |
| 2 | idx_users_fuserid |  | fuserid |
| 3 | idx_users_fschemeid |  | fschemeid |
