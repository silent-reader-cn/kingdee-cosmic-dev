# 访问控制权限条目-plm_plmsm_aclentry

## 访问控制权限条目-主表 t_plmsm_aclentry

- **表名称：** 访问控制权限条目-主表
- **表名：** t_plmsm_aclentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主表ID | int8 | 64 |  | √ | 0 | 主表ID |
| 2 | flcstatusid | 状态 | int8 | 64 |  | √ | 0 | [流程状态 plm_lc_status](../plmsm_files/plm_lc_status.md) |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fpermissiontype | 权限类型 | varchar | 50 |  | √ | ' ' | 权限类型,枚举: A :授权 B :拒绝 |
| 5 | fpdmmodelid | 类型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 6 | fdomainid | fdomainid | int8 | 64 |  | √ | 0 |  |
| 7 | fapplyto | 应用于 | varchar | 50 |  | √ | ' ' | 应用于,枚举: A :参与者 B :全部（选定参与者除外） |
| 8 | fparticipanttype | 参与者类型 | varchar | 50 |  | √ | ' ' | 参与者类型,枚举: bos_user :人员 bos_usergroup :用户组 plm_plmsm_role :PLM角色 |
| 9 | fparticipantid | 参与者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 11 | fdomainofbelongid | 所属域 | int8 | 64 |  | √ | 0 | [域 plm_plmsm_domain](../plmsm_files/plm_plmsm_domain.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fpermissionmask | 授予权限 | int8 | 64 |  | √ | 0 | 授予权限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_aclentry_fid |  | fid |
| 2 | pk_plmsm_aclentry |  | fentryid |
| 3 | idx_plmsm_aclentry_peid |  | fparententryid |
