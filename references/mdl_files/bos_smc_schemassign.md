# 方案分配实体-bos_smc_schemassign

## 方案分配实体-主表 t_meta_schemeassign

- **表名称：** 方案分配实体-主表
- **表名：** t_meta_schemeassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | frangetype | 范围类型 | varchar | 1 |  | √ | ' ' | 范围类型,枚举: 0 :管理员 1 :全体人员 2 :特定角色 3 :特定人员 |
| 3 | fschemeid | 方案ID | varchar | 36 |  | √ | ' ' | 方案ID |
| 4 | froleidoruserid | 角色ID或用户ID | varchar | 50 |  | √ | ' ' | 角色ID或用户ID |
| 5 | fschemetype | 方案类型 | varchar | 1 |  | √ | ' ' | 方案类型,枚举: 0 :首页 1 :应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_schemeassign_num |  | fschemeid |
| 2 | idx_kdp_schemeassign_all |  | fschemetype,frangetype,froleidoruserid |
| 3 | t_meta_schemeassign_pkey |  | fid |
