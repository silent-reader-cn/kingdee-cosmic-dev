# Schema权限-bos_flydb_schema_perm

## Schema权限-主表 t_flydb_schema_perm

- **表名称：** Schema权限-主表
- **表名：** t_flydb_schema_perm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fschemaid | 模式 | int8 | 64 |  | √ | 0 | [Schema管理 bos_flydb_schema](../superquery_files/bos_flydb_schema.md) |
| 4 | fauthitem | 权限项 | int8 | 64 |  | √ | 0 | 权限项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_flydb_schema_perm_fuid |  | fuserid |
| 2 | idx_flydb_schema_perm_fsid |  | fschemaid |
| 3 | pk_t_flydb_schema_perm |  | fid |
