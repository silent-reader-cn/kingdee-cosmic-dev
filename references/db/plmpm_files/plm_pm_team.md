# 团队-plm_pm_team

## 团队-主表 t_plm_pm_team

- **表名称：** 团队-主表
- **表名：** t_plm_pm_team

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprjrolecfgid | 关联角色配置 | int8 | 64 |  | √ | 0 | [关联角色配置 plm_pm_prjrolecfg](../plmpm_files/plm_pm_prjrolecfg.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftaskgroupid | 任务组 | int8 | 64 |  | √ | 0 | 任务组 |
| 6 | fprjrolegroupid | 项目角色分组 | int8 | 64 |  | √ | 0 | [项目权限模板 plm_pm_prjrole](../plmpm_files/plm_pm_prjrole.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_team_m0 |  | forgid |
| 2 | pk_plm_pm_team |  | fid |
