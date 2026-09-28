# 通用角色-管理员组关系差异-perm_log_diff_roleadmgr

## 通用角色-管理员组关系差异-主表 t_perm_log_diff_roleadmgr

- **表名称：** 通用角色-管理员组关系差异-主表
- **表名：** t_perm_log_diff_roleadmgr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fmodifiable_desc | 允许修改通用角色描述 | varchar | 20 |  | √ | ' ' | 允许修改通用角色描述 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | frole_name | 角色名 | varchar | 255 |  | √ | ' ' | 角色名 |
| 6 | fadmingroup_name | 管理员组名称 | varchar | 255 |  | √ | ' ' | 管理员组名称 |
| 7 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | frole_id | 角色id | varchar | 18 |  | √ | ' ' | 角色id |
| 9 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 10 | frole_number | 角色编码 | varchar | 30 |  | √ | ' ' | 角色编码 |
| 11 | fadmingroup_num | 管理员组编码 | varchar | 80 |  | √ | ' ' | 管理员组编码 |
| 12 | fadmingroup_id | 管理员组id | int8 | 64 |  | √ | 0 | 管理员组id |
| 13 | fmodifiable | 允许修改通用角色 | bpchar | 1 |  | √ | '0' | 允许修改通用角色 |
| 14 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_roleadmgrp |  | fperm_logid |
| 2 | pk_perm_log_diff_roleadmgrp |  | fid |
