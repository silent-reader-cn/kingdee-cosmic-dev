# 业务对象应用关系-perm_bizobjapp

## 业务对象应用关系-主表 t_perm_bizobjapp

- **表名称：** 业务对象应用关系-主表
- **表名：** t_perm_bizobjapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fbizobjid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_bizobjapp_pkey |  | fid |
| 2 | ix_perm_bizobjapp_bizobjid |  | fbizobjid,fbizappid |
