# 例外用户组-实体-perm_exceptusrgrp

## 例外用户组-实体-主表 t_perm_oprexusrgrp

- **表名称：** 例外用户组-实体-主表
- **表名：** t_perm_oprexusrgrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fusergroupid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 bos_usergroup |
| 3 | foperationruleobjid | 特殊操作权限分配对象 | varchar | 18 |  | √ | ' ' | 特殊操作权限分配对象 perm_operationruleobj |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_oprexusrgrp_pkey |  | fid |
| 2 | idx_perm_oprexusrgrp |  | foperationruleobjid |
