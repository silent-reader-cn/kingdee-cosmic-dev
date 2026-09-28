# 应用模型关联关系-wf_appmodelrelation

## 应用模型关联关系-主表 t_wf_appmodelrelation

- **表名称：** 应用模型关联关系-主表
- **表名：** t_wf_appmodelrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fmodelid | 模型标识 | int8 | 64 |  | √ | 0 | 模型标识 |
| 4 | fappid | 应用标识 | varchar | 36 |  | √ | ' ' | 应用标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_appmodelrelation_pkey |  | fid |
| 2 | idx_wf_appmodelrelation_fappid |  | fappid |
