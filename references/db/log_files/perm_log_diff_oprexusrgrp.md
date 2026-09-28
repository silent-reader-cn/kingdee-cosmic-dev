# 特殊数据权限例外用户组差异表-perm_log_diff_oprexusrgrp

## 特殊数据权限例外用户组差异表-主表 t_perm_log_diff_oprexusgr

- **表名称：** 特殊数据权限例外用户组差异表-主表
- **表名：** t_perm_log_diff_oprexusgr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fusrgrp_name | 用户组名称 | varchar | 255 |  | √ | ' ' | 用户组名称 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fusrgrp_desc | 用户组描述 | varchar | 255 |  | √ | ' ' | 用户组描述 |
| 5 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 6 | fusrgrp_id | 用户组ID | int8 | 64 |  | √ | 0 | 用户组ID |
| 7 | fusrgrp_number | 用户组编码 | varchar | 80 |  | √ | ' ' | 用户组编码 |
| 8 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 10 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_oprexusgr |  | fperm_logid |
| 2 | pk_perm_log_diff_oprexusgr |  | fid |
