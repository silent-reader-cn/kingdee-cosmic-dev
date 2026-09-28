# RESTful API日志-open_rest_api_log_new

## RESTful API日志-主表 t_open_rest_api_log

- **表名称：** RESTful API日志-主表
- **表名：** t_open_rest_api_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | frequest_params_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 4 | fhttp_method | 请求方法 | varchar | 50 |  | √ | ' ' | 请求方法 |
| 5 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fthirdappname | 第三方应用 | int8 | 64 |  | √ | 0 | [第三方应用 third_app](../open_files/third_app.md) |
| 8 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fstart_time | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 10 | fuserid | 调用者id | varchar | 50 |  | √ | ' ' | 调用者id |
| 11 | fip | 调用客户端IP | varchar | 50 |  | √ | ' ' | 调用客户端IP |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | frequest_params | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |
| 14 | fstatus | 调用状态 | varchar | 50 |  | √ | ' ' | 调用状态,枚举: true :成功 false :失败 |
| 15 | fusername | 调用者 | varchar | 50 |  | √ | ' ' | 调用者 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fapi_number | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 18 | fhttp_status | HTTP状态码 | int8 | 64 |  | √ | 0 | HTTP状态码 |
| 19 | frest_api | RESTful API | int8 | 64 |  | √ | 0 | RESTful API（基础模型） open_rest_api |
| 20 | ftimecost | API耗时(ms) | int8 | 64 |  | √ | 0 | API耗时(ms) |
| 21 | furl | URL | varchar | 300 |  | √ | ' ' | URL |
| 22 | fresponse_body | 响应参数 | varchar | 255 |  | √ | ' ' | 响应参数 |
| 23 | fapi_name | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 24 | fresponse_body_tag | 响应参数_详情 | text | 0 |  |  | null | 响应参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_api_log |  | fid |
| 2 | idx_open_rest_log_reqd |  | frequest_params |
| 3 | idx_open_rest_log_respd |  | fresponse_body |
| 4 | idx_open_rest_log_st |  | fstart_time |
| 5 | idx_open_rest_log_url |  | furl |
