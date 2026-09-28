# 网关API服务参数-openapi_gatewayparm

## 网关API服务参数-主表 t_open_gatewayparm

- **表名称：** 网关API服务参数-主表
- **表名：** t_open_gatewayparm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparmvalue | 参数值 | varchar | 512 |  | √ | ' ' | 参数值 |
| 3 | fnumber | 参数编码 | varchar | 255 |  | √ | ' ' | 参数编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_gatewayparm |  | fid |
| 2 | idx_fname |  | fnumber |
