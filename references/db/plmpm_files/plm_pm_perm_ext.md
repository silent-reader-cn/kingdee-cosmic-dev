# 项目特权表-plm_pm_perm_ext

## 项目特权表-主表 t_plm_pm_perm_ext

- **表名称：** 项目特权表-主表
- **表名：** t_plm_pm_perm_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fextpermid | 特权设置 | int8 | 64 |  | √ | 0 | [项目特权设置 plm_pm_extperm](../plmpm_files/plm_pm_extperm.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fprjstatusid | 项目状态 | int8 | 64 |  | √ | 0 | [项目状态 plm_pm_projectstatus](../plmpm_files/plm_pm_projectstatus.md) |
| 4 | fbizobjid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fpermid | 权限项 | varchar | 36 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_perm_ext_m0 |  | fbizobjid |
| 2 | pk_plm_pm_perm_ext |  | fid |
