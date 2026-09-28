# 合同管理后台参数-conm_dbparams

## 合同管理后台参数-主表 t_conm_dbparams

- **表名称：** 合同管理后台参数-主表
- **表名：** t_conm_dbparams

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
| 1 | pk_conm_dbparams |  | fid |
| 2 | idx_conm_params_m0 |  | fkey |
