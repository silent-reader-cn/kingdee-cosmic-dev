# 优化参数-ocdbd_optimize_params

## 优化参数-主表 t_ocdbd_optimize_params

- **表名称：** 优化参数-主表
- **表名：** t_ocdbd_optimize_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablebalanceservicelog | 开启资金池服务日志 | bpchar | 1 |  | √ | '1' | 开启资金池服务日志 |
| 3 | fenablerecordsubscription | 使用事件订阅 | bpchar | 1 |  | √ | '1' | 使用事件订阅 |
| 4 | fbalancebatchcount | 资金池批量更新 | int4 | 32 |  | √ | 50 | 资金池批量更新 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_optimizeparams |  | fenablebalanceservicelog |
| 2 | pk_ocdbd_optimize_params |  | fid |
