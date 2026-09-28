# 应用-许可分组关系-lic_appgroup

## 应用-许可分组关系-主表 t_lic_appgroup

- **表名称：** 应用-许可分组关系-主表
- **表名：** t_lic_appgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | 许可分组 lic_group |
| 3 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_appgroup |  | fid |
| 2 | idx_t_lic_appgroup_group |  | fgroupid |
