# 用户组用户差异-perm_log_usrgrpuser

## 用户组用户差异-主表 t_perm_log_diff_usrgrpu

- **表名称：** 用户组用户差异-主表
- **表名：** t_perm_log_diff_usrgrpu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键ID | int8 | 64 |  | √ | 0 | 主键ID |
| 2 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 3 | fusrgrp_name | 用户组名 | varchar | 255 |  | √ | ' ' | 用户组名 |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fuser_name | 用户姓名 | varchar | 255 |  | √ | ' ' | 用户姓名 |
| 6 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 7 | fusrgrp_number | 用户组编码 | varchar | 80 |  | √ | ' ' | 用户组编码 |
| 8 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 9 | fuser_number | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |
| 10 | fuser_username | 用户用户名 | varchar | 255 |  | √ | ' ' | 用户用户名 |
| 11 | fusrgrp_id | 用户组id | int8 | 64 |  | √ | 0 | 用户组id |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 14 | fuser_id | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 15 | ffrom_type | 用户组-用户关系来源类型 | varchar | 1 |  | √ | '0' | 用户组-用户关系来源类型 |
| 16 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 17 | ffrom_type_desc | 用户组-用户关系来源类型描述 | varchar | 50 |  | √ | ' ' | 用户组-用户关系来源类型描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_usrgrpu |  | fid |
| 2 | idx_logid_usrgrpu |  | fperm_logid |
