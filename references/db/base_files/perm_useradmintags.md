# 超级管理员身份映射关系-perm_useradmintags

## 超级管理员身份映射关系-主表 t_perm_useradmintag

- **表名称：** 超级管理员身份映射关系-主表
- **表名：** t_perm_useradmintag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadmintag | 超级管理员身份 | varchar | 20 |  | √ | ' ' | 超级管理员身份,枚举: 1 :administrator 2 :auditor 3 :security 10 :cosmic |
| 3 | ftransfertime | 移交时间 | timestamp | 0 |  |  | null | 移交时间 |
| 4 | ftransferorid | 移交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_useradmintag |  | fadmintag |
| 2 | t_perm_useradmintag_pkey |  | fid |
