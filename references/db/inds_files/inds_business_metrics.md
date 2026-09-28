# 业务服务指标-inds_business_metrics

## 业务服务指标-主表 t_inds_business

- **表名称：** 业务服务指标-主表
- **表名：** t_inds_business

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 指标名称 | varchar | 50 |  | √ | ' ' | 指标名称 |
| 3 | fdomain | 领域 | varchar | 50 |  | √ | ' ' | 领域 |
| 4 | fmethod | 接口名 | varchar | 50 |  | √ | ' ' | 接口名 |
| 5 | findextype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: 0 :通用指标 1 :业务指标 |
| 6 | fcode | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_inds_business |  | fid |
| 2 | index_inds_business |  | fcode |
