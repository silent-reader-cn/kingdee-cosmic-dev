# 销售管理后台参数-sm_params

## 销售管理后台参数-主表 t_sm_params

- **表名称：** 销售管理后台参数-主表
- **表名：** t_sm_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 参数值 | varchar | 100 |  | √ | ' ' | 参数值 |
| 3 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fkey | 参数标识 | varchar | 100 |  | √ | ' ' | 参数标识 |
| 6 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_params_m0 |  | fkey |
| 2 | pk_sm_params |  | fid |
