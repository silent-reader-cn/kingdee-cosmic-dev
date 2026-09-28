# 角色配置用户-plm_plmsm_roleusers

## 角色配置用户-主表 t_plmsm_roleuser

- **表名称：** 角色配置用户-主表
- **表名：** t_plmsm_roleuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 角色 | int8 | 64 |  | √ | 0 | [PLM角色 plm_plmsm_role](../plmsm_files/plm_plmsm_role.md) |
| 2 | frelationid | 关联上下文标识 | int8 | 64 |  | √ | 0 | 关联上下文标识 |
| 3 | fuserorgroup | 用户或用户组 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fusergrouptype | 用户或用户组类型 | varchar | 50 |  | √ | ' ' | 用户或用户组类型,枚举: bos_user :人员 bos_usergroup :用户组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_roleuser |  | fentryid |
| 2 | idx_plmsm_roleuser_userrel |  | frelationid,fuserorgroup |
