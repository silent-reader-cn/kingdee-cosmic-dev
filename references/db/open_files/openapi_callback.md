# API回调-openapi_callback

## API回调-主表 t_openapi_callback

- **表名称：** API回调-主表
- **表名：** t_openapi_callback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fthirdid | 第三方应用 | int8 | 64 |  | √ | 0 | [第三方应用 third_app](../open_files/third_app.md) |
| 3 | fapiid | API | int8 | 64 |  | √ | 0 | [API服务 openapi_apilist](../open_files/openapi_apilist.md) |
| 4 | fagentuserid | 代理用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_openapi_callback_api |  | fapiid |
| 2 | pk_t_openapi_callback |  | fid |
