# API服务拆分表-xkopen_apisplit

## API服务拆分表-主表 t_open_apiservice_x

- **表名称：** API服务拆分表-主表
- **表名：** t_open_apiservice_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisgalaxy | 是否星空 | bpchar | 1 |  | √ | '0' | 是否星空 |
| 3 | fgatewayid | fgatewayid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_t_open_apiservice_x |  | fisgalaxy |
| 2 | pk_t_open_apiservice_x |  | fid |
