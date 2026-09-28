# 权限禁止生效表-plm_plmsm_denypermission

## 权限禁止生效表-主表 t_plmsm_denypermission

- **表名称：** 权限禁止生效表-主表
- **表名：** t_plmsm_denypermission

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbeginmodelid | 起始业务模型 | int8 | 64 |  | √ | 0 | 起始业务模型 |
| 3 | fdomainid | 域 | int8 | 64 |  | √ | 0 | 域 |
| 4 | flcstatusid | 状态 | int8 | 64 |  | √ | 0 | 状态 |
| 5 | froleid | 角色 | int8 | 64 |  | √ | 0 | 角色 |
| 6 | fendmodelid | 结束业务模型 | int8 | 64 |  | √ | 0 | 结束业务模型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_denypermission |  | fbeginmodelid,fendmodelid,froleid,fdomainid,flcstatusid |
| 2 | pk_plmsm_denypermission |  | fid |
