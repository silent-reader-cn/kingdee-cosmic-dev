# 结账配置-fi_closeperiodconf

## 结账配置-主表 t_bd_closeperiodconf

- **表名称：** 结账配置-主表
- **表名：** t_bd_closeperiodconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizapp | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用 |
| 3 | fbooktype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 4 | fcloseoperiod | 结账 | varchar | 50 |  | √ | ' ' | 结账 |
| 5 | fbiztypeid | 业务类型 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 6 | forg | 组织 | varchar | 50 |  | √ | ' ' | 组织 |
| 7 | funcloseoperiod | 反结账 | varchar | 50 |  | √ | ' ' | 反结账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_closeperiodconf_pkey |  | fid |
| 2 | idx_bd_closeperiodconf |  | fbizapp |
