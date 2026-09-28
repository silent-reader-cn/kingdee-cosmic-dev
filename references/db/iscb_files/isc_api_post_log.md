# API调试记录-isc_api_post_log

## API调试记录-主表 t_isc_api_post_log

- **表名称：** API调试记录-主表
- **表名：** t_isc_api_post_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 状态码 | varchar | 50 |  | √ | ' ' | 状态码 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmethod | 请求方式 | varchar | 50 |  | √ | ' ' | 请求方式 |
| 6 | furl | 地址 | varchar | 2000 |  | √ | ' ' | 地址 |
| 7 | fapi_model | 模型数据 | varchar | 500 |  | √ | ' ' | 模型数据 |
| 8 | fapi_model_tag | 模型数据_详情 | text | 0 |  |  | null | 模型数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_api_post_log |  | fid |
| 2 | index_t_isc_api_post_log |  | fcreatetime |
