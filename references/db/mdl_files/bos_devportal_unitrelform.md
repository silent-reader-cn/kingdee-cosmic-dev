# 业务单元页面关联-bos_devportal_unitrelform

## 业务单元页面关联-主表 t_meta_bizunitrelform

- **表名称：** 业务单元页面关联-主表
- **表名：** t_meta_bizunitrelform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizunitid | 业务单元 | varchar | 36 |  | √ | ' ' | 业务单元 |
| 3 | fformid | 业务页面 | varchar | 36 |  | √ | ' ' | 业务页面 |
| 4 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizunitrelform_fformid_key |  | fformid |
| 2 | t_meta_bizunitrelform_pkey |  | fid |
