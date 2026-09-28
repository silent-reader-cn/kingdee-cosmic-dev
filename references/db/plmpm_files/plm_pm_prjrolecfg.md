# 关联角色配置-plm_pm_prjrolecfg

## 关联角色配置-主表 t_plm_pm_prjrolecfg

- **表名称：** 关联角色配置-主表
- **表名：** t_plm_pm_prjrolecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | froleid | 角色 | int8 | 64 |  | √ | 0 | [项目权限模板 plm_pm_prjrole](../plmpm_files/plm_pm_prjrole.md) |
| 3 | fbizobj | 关联ID（项目ID、项目角色ID） | int8 | 64 |  | √ | 0 | 关联ID（项目ID、项目角色ID） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_prjrolecfg_m0 |  | fbizobj |
| 2 | i_plm_pm_prjcfg_bizobj |  | fbizobj,froleid |
| 3 | pk_plm_pm_prjrolecfg |  | fid |
