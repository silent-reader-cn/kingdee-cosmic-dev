# 同步的维度数据-didc_sync_dim_data

## 同步的维度数据-主表 t_didc_sync_dim_data

- **表名称：** 同步的维度数据-主表
- **表名：** t_didc_sync_dim_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimensionfield | 维度标识 | varchar | 255 |  | √ | ' ' | 维度标识 |
| 3 | fdimensionvalue | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 4 | findexid | 指标id | int8 | 64 |  | √ | 0 | 指标id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_sync_dim_data |  | fid |
| 2 | idx_didc_sync_dim_data |  | findexid |
