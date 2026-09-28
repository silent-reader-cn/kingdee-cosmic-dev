# 权限配置-plm_ipdsm_permcfg

## 权限配置-主表 t_plm_ipdsm_permcfg

- **表名称：** 权限配置-主表
- **表名：** t_plm_ipdsm_permcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftable | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 3 | fbizobjid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdsm_permcfg_m0 |  | fbizobjid |
| 2 | pk_plm_ipdsm_permcfg |  | fid |
