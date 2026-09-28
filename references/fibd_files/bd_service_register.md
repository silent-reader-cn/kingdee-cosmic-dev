# 启用服务注册-bd_service_register

## 启用服务注册-主表 t_bd_service_register

- **表名称：** 启用服务注册-主表
- **表名：** t_bd_service_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizcloud | 业务云编码 | varchar | 10 |  | √ | ' ' | 业务云编码 |
| 3 | fbizapp | 应用编码 | varchar | 10 |  | √ | ' ' | 应用编码 |
| 4 | fservice | 服务名 | varchar | 255 |  | √ | ' ' | 服务名 |
| 5 | fisconsistent | 是否事务一致 | bpchar | 1 |  | √ | '0' | 是否事务一致 |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_service_register |  | fid |
| 2 | idx_bd_service_register |  | fbizcloud,fbizapp |
